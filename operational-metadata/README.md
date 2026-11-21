# Operational Metadata for the Digital Typhoon Dataset V3

Machine-readable descriptions of **how to use** the [Digital Typhoon Dataset V3](https://agora.ex.nii.ac.jp/digital-typhoon/dataset/V3/)
and its loader library [pyphoon3](https://github.com/kitamoto-lab/pyphoon3): file layout, column types and units,
label codes, missing values, known issues and working code examples.

Classic metadata says *what* a dataset is and *why* it was made. Operational metadata says *how* to handle it,
so that people and AI coding assistants can write correct code for it the first time.

**Covers:** dataset release V3-2025.R2 · pyphoon3 3.0.0 · see [CHANGELOG.md](CHANGELOG.md)

## Contents

| Path | What it is |
| --- | --- |
| [`skills/digital-typhoon/dataset.yaml`](skills/digital-typhoon/dataset.yaml) | The dataset: release, citation, basins, channels and wavelengths, satellites, image geometry, downloads and checksums, caveats |
| [`skills/digital-typhoon/library.yaml`](skills/digital-typhoon/library.yaml) | pyphoon3 and the data files: installation, constructor arguments, label names, usage examples; HDF5 images, track CSV columns, `metadata.json`, `substituted_conversion.csv`; ML tasks; caveats |
| [`skills/digital-typhoon/known_issues/`](skills/digital-typhoon/known_issues/) | `mask_over_30pct_V3-2025.R2.csv`: 174 images over the 30% missing-area limit in V3-2025.R2 |
| [`skills/digital-typhoon/SKILL.md`](skills/digital-typhoon/SKILL.md) | Claude Code skill that uses the files above |
| [`examples/plot_typhoon_tracks.py`](examples/plot_typhoon_tracks.py) | Track plotting script written from the metadata |

The two YAML files follow the Operational Metadata schema 0.1.0 and can be read by any tool.

## Get the files

```sh
git clone https://github.com/kitamoto-lab/digital-typhoon
cd digital-typhoon/operational-metadata
```

The commands below run from this folder.

## Use with Claude Code

Copy the skill folder into your personal skills, or into a project's `.claude/skills/`:

```sh
cp -r skills/digital-typhoon ~/.claude/skills/
```

Then ask in plain language, for example:

- "Write a PyTorch dataloader for Digital Typhoon WP channel 1 with pressure labels and a season split."
- "Plot the tracks of the 2024 AU season."
- "Which images should I exclude before training a wind-speed model?"

Claude loads the skill when the task concerns the Digital Typhoon Dataset, reads the YAML files, and follows their caveats
(split by cyclone, how missing labels are coded, known issues). You can also call it directly with `/digital-typhoon`.

## Use with other assistants

Attach `dataset.yaml` and `library.yaml` to the conversation, or paste them, and ask the assistant to follow them.
The rules in [`SKILL.md`](skills/digital-typhoon/SKILL.md) under "Rules that code must follow" make a good instruction text.

## Quick start with the sample data

The 37 MB sample has the same layout as the full dataset (channel 1, 4 cyclones per basin):

```sh
wget https://github.com/kitamoto-lab/pyphoon3/releases/download/sample-V3-2025/pyphoon3-sample-V3-2025.zip
unzip pyphoon3-sample-V3-2025.zip
uv pip install git+https://github.com/kitamoto-lab/pyphoon3 pandas matplotlib
python examples/plot_typhoon_tracks.py --root pyphoon3-sample-V3-2025 --basin WP --season 2024 -o wp2024.png
```

The full dataset (231.3 GB) is available from the [dataset page](https://agora.ex.nii.ac.jp/digital-typhoon/dataset/V3/).

## Things to know before training

The caveats in the YAML files cover these in detail:

- Split by cyclone (`split_by='sequence'`) or by season; pyphoon3's default image split leaks.
- `wind = 0` means "no value" and is not skipped by pyphoon3; AU grade 0 means the original wind speed is missing.
- `intp` flags only interpolated positions; in AU, wind and pressure can be interpolated where `intp = 0`.
- Longitude is 0-360 °E; AU seasons run July-June.
- V3-2025.R2 contains 174 images over the 30% missing-area limit, listed in `known_issues/`, and 1,477 images
  converted with substituted coefficients, listed in the dataset's `substituted_conversion.csv`.

Some details are not documented by the dataset, for example the pixel spacing. The metadata says so instead of guessing.

## License and citation

The files in this directory are licensed under [CC BY 4.0](LICENSE). pyphoon3 itself is MIT-licensed.

When you use the dataset, cite it as:

```
Digital Typhoon Dataset V3 (National Institute of Informatics), doi:10.20783/DIAS.664
```

and the V3 paper: Asanobu Kitamoto, Victor Le Louarn, Noelia Falczuk, Ngoc Anh Tong, Anja Veleva,
"Digital Typhoon Dataset V3: Benchmarking for Multi-spectral Extension and Analyzing Systematic Bias in Intensity Regression",
arXiv:2610.21654, 2026.
