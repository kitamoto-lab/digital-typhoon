#!/usr/bin/env python3
"""
Plot typhoon tracks from the Digital Typhoon Dataset V3.

Written from the operational metadata in skills/digital-typhoon/:
- library.yaml  file_structure: {root}/{channel}/{basin}/metadata/{sequence_id}.csv and metadata.json
- library.yaml  files.track_file.csv_spec: columns lat, lng, grade, intp
- library.yaml  files.metadata_json.json_spec: season and cyclone name
- dataset.yaml  spatial_coverage.basins

Requirements:
    uv pip install pandas matplotlib          # optional: cartopy, for coastlines

Usage:
    python plot_typhoon_tracks.py --root /path/to/V3-2025.R2 --basin WP --season 2025 -o wp2025.png
    python plot_typhoon_tracks.py --root /path/to/V3-2025.R2 --basin AU --sequence 199002 -o felicity.png
    python plot_typhoon_tracks.py --root pyphoon3-sample-V3-2025 --basin WP --season 2024
"""

import argparse
import json
import os
from typing import Any, Dict, List, Optional

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D

# Coastlines with cartopy if installed; otherwise a plain longitude/latitude plot
try:
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    HAS_CARTOPY = True
except ImportError:
    HAS_CARTOPY = False


# =============================================================================
# Constants from the operational metadata
# =============================================================================

# dataset.yaml: spatial_coverage.basins
BASINS = ("WP", "AU")

# Every channel has its own track CSVs. Positions and grades are the same across channels;
# channel 1 covers the longest period (from 1978) (dataset.yaml: channels).
DEFAULT_CHANNEL = 1

# library.yaml: files.track_file, column grade
GRADE_LABELS = {
    0: "Wind speed missing (AU only)",
    2: "Tropical Depression (<34 kt)",
    3: "Tropical Storm (34-47 kt)",
    4: "Severe Tropical Storm (48-63 kt)",
    5: "Typhoon (>=64 kt)",
    6: "Extratropical Cyclone (WP only)",
    7: "Entering JMA area (WP only)",
}

GRADE_COLORS = {
    0: "#7f8c8d",
    2: "#3498db",
    3: "#2ecc71",
    4: "#f39c12",
    5: "#e74c3c",
    6: "#9b59b6",
    7: "#34495e",
}

# library.yaml: column intp, the position interpolation flag (0 = original best-track position)
INTP_ORIGINAL = 0


# =============================================================================
# Reading the data
# =============================================================================

def basin_dir(root: str, channel: int, basin: str) -> str:
    """library.yaml: file_structure -> {root}/{channel}/{basin}/"""
    return os.path.join(root, str(channel), basin)


def load_metadata_json(root: str, channel: int, basin: str) -> Dict[str, Any]:
    """
    Read metadata.json (library.yaml: files.metadata_json):
    {"<sequence_id>": {"id", "number", "season", "name", "start", "end", "images"}, ...}
    AU seasons run from July to June and are labelled by the ending year.
    """
    path = os.path.join(basin_dir(root, channel, basin), "metadata.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} not found: --root must point to a V3 release or the pyphoon3 sample")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_track_csv(root: str, channel: int, basin: str, sequence_id: str) -> pd.DataFrame:
    """
    Read one track CSV (library.yaml: files.track_file): hourly rows, header, comma-separated.
    lng is 0-360 degrees east (values above 180 occur).
    """
    path = os.path.join(basin_dir(root, channel, basin), "metadata", f"{sequence_id}.csv")
    return pd.read_csv(path, delimiter=",")


def sequences_in_season(metadata: Dict[str, Any], season: int) -> List[str]:
    return sorted(seq_id for seq_id, info in metadata.items() if info.get("season") == season)


# =============================================================================
# Plotting
# =============================================================================

def _plot_kwargs() -> Dict[str, Any]:
    return {"transform": ccrs.PlateCarree()} if HAS_CARTOPY else {}


def plot_track(ax, track: pd.DataFrame, label: str, linewidth: float = 1.5) -> None:
    """
    Draw one track: line segments colored by grade, dots only at original best-track positions (intp = 0).
    """
    lngs = track["lng"].to_numpy()
    lats = track["lat"].to_numpy()
    grades = track["grade"].astype(int).to_numpy()
    kw = _plot_kwargs()

    for i in range(len(track) - 1):
        ax.plot(lngs[i:i + 2], lats[i:i + 2], color=GRADE_COLORS.get(grades[i], "#7f8c8d"),
                linewidth=linewidth, **kw)

    original = (track["intp"] == INTP_ORIGINAL).to_numpy()
    for grade, color in GRADE_COLORS.items():
        mask = original & (grades == grade)
        if mask.any():
            ax.scatter(lngs[mask], lats[mask], c=color, s=12, zorder=5, **kw)

    ax.plot(lngs[0], lats[0], "go", markersize=7, zorder=10, **kw)
    ax.plot(lngs[-1], lats[-1], "rx", markersize=7, zorder=10, **kw)
    ax.text(lngs[0], lats[0] + 0.8, label, fontsize=7, **kw)


def create_map(title: str, extent: List[float]):
    """extent: [lon_min, lon_max, lat_min, lat_max] in degrees east, 0-360"""
    fig = plt.figure(figsize=(12, 9))
    if HAS_CARTOPY:
        # Centered on 180 degrees so tracks crossing the date line (WP up to 188, AU up to 212 degrees east) stay whole
        ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=180))
        ax.set_extent(extent, crs=ccrs.PlateCarree())
        ax.add_feature(cfeature.LAND, facecolor="lightgray")
        ax.add_feature(cfeature.OCEAN, facecolor="lightblue")
        ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
        ax.gridlines(draw_labels=True, linewidth=0.5, alpha=0.5)
    else:
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlim(extent[0], extent[1])
        ax.set_ylim(extent[2], extent[3])
        ax.set_xlabel("Longitude (°E, 0-360)")
        ax.set_ylabel("Latitude (°N)")
        ax.grid(True, alpha=0.3)
        ax.set_aspect("equal")
    ax.set_title(title, fontsize=13)
    return fig, ax


def add_legend(ax, grades_present: set) -> None:
    handles = [Line2D([0], [0], color=GRADE_COLORS[g], linewidth=2, label=f"Grade {g}: {GRADE_LABELS[g]}")
               for g in sorted(grades_present) if g in GRADE_COLORS]
    handles += [
        Line2D([0], [0], marker="o", color="w", markerfacecolor="gray", markersize=5, label="Original position (intp=0)"),
        Line2D([0], [0], marker="o", color="w", markerfacecolor="g", markersize=7, label="Start"),
        Line2D([0], [0], marker="x", color="r", linestyle="", markersize=7, label="End"),
    ]
    ax.legend(handles=handles, loc="lower left", fontsize=7)


def extent_of(tracks: List[pd.DataFrame], margin: float = 5.0) -> List[float]:
    allt = pd.concat(tracks)
    return [allt["lng"].min() - margin, allt["lng"].max() + margin,
            allt["lat"].min() - margin, allt["lat"].max() + margin]


def finish(fig, output: Optional[str]) -> None:
    if output:
        fig.savefig(output, dpi=150, bbox_inches="tight")
        print(f"Saved to {output}")
    else:
        plt.show()
    plt.close(fig)


# =============================================================================
# Main
# =============================================================================

def plot_season(root: str, channel: int, basin: str, season: int, output: Optional[str]) -> None:
    metadata = load_metadata_json(root, channel, basin)
    seq_ids = sequences_in_season(metadata, season)
    if not seq_ids:
        print(f"No sequences found for {basin} season {season} (channel {channel})")
        return
    print(f"Found {len(seq_ids)} sequences for {basin} season {season}")

    tracks = [load_track_csv(root, channel, basin, s) for s in seq_ids]
    fig, ax = create_map(f"Digital Typhoon V3 - {basin} season {season}", extent_of(tracks))
    for seq_id, track in zip(seq_ids, tracks):
        plot_track(ax, track, f"{metadata[seq_id].get('name', '')} ({seq_id})")
    add_legend(ax, set(pd.concat(tracks)["grade"].astype(int)))
    finish(fig, output)


def plot_sequence(root: str, channel: int, basin: str, sequence_id: str, output: Optional[str]) -> None:
    metadata = load_metadata_json(root, channel, basin)
    if sequence_id not in metadata:
        print(f"Sequence {sequence_id} not found in {basin} channel {channel}")
        return
    info = metadata[sequence_id]
    track = load_track_csv(root, channel, basin, sequence_id)

    title = (f"{info.get('name', '')} ({sequence_id}, {basin}, season {info.get('season')})\n"
             f"{info.get('start', '')} - {info.get('end', '')}, {info.get('images')} images")
    fig, ax = create_map(title, extent_of([track]))
    plot_track(ax, track, info.get("name", ""), linewidth=2.5)
    add_legend(ax, set(track["grade"].astype(int)))
    finish(fig, output)


def main() -> None:
    parser = argparse.ArgumentParser(description="Plot typhoon tracks from the Digital Typhoon Dataset V3")
    parser.add_argument("--root", "-r", required=True,
                        help="Dataset root: an unpacked V3 release (e.g. V3-2025.R2) or the pyphoon3 sample")
    parser.add_argument("--basin", "-b", choices=BASINS, default="WP", help="Basin (default: WP)")
    parser.add_argument("--channel", "-c", type=int, choices=[1, 2, 3, 4], default=DEFAULT_CHANNEL,
                        help="Channel whose track CSVs are read (default: 1, the longest coverage)")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--season", "-y", type=int, help="Plot all sequences of this season")
    group.add_argument("--sequence", "-s", help="Plot one sequence (e.g. 202527)")
    parser.add_argument("--output", "-o", help="Output image path (default: show interactively)")
    args = parser.parse_args()

    if not HAS_CARTOPY:
        print("Note: cartopy is not installed; plotting without coastlines.")
    if args.season is not None:
        plot_season(args.root, args.channel, args.basin, args.season, args.output)
    else:
        plot_sequence(args.root, args.channel, args.basin, args.sequence, args.output)


if __name__ == "__main__":
    main()
