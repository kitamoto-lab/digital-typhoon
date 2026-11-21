---
name: digital-typhoon
description: Write correct code for the Digital Typhoon Dataset V3 (typhoon satellite images + best-track data, release V3-2025.R2) and its loader library pyphoon3. Use when the user wants to load, explore, validate, visualize or train on Digital Typhoon data — a PyTorch/TensorFlow dataloader, a train/eval split, a track plot, label statistics — or asks how its files, columns, units, channels or known issues work.
---

# Digital Typhoon Dataset V3

This skill carries the operational metadata of the Digital Typhoon Dataset V3: how the data is laid out
and how to read it correctly. Use it instead of guessing file formats, units or label meanings.

## Files in this skill

Read them from this skill's directory before writing code:

| File | What it holds |
| --- | --- |
| `dataset.yaml` | Release, citation, licence, basins, channels and wavelengths, satellites, image geometry, download files and checksums, dataset-level caveats |
| `library.yaml` | pyphoon3 3.0.0: installation, constructor arguments, label names, usage examples; file formats (HDF5 images, track CSV columns with types, units, codes and missing values, metadata.json, substituted_conversion.csv); ML tasks; caveats |
| `known_issues/mask_over_30pct_V3-2025.R2.csv` | 174 images over the 30% missing-area limit in V3-2025.R2, to pass to `ignore_list` |

Read `library.yaml` for any code that loads data, and `dataset.yaml` for questions about coverage,
channels, downloads or citation. Quote values from these files; do not rely on memory.

## Rules that code must follow

These come from the caveats in the metadata. Generated code must respect them and say so in comments:

1. **Split by cyclone, not by image.** pyphoon3's default `split_dataset_by='image'` leaks images of the
   same cyclone into training and evaluation. Use `split_by='sequence'`, or the season split of the V3
   benchmarks (SS-L2: seasons 2024-2025 for evaluation, earlier seasons for training).
2. **Missing labels are not all skipped.** pyphoon3 skips a label only when it is -1 (AU `pressure`).
   `wind = 0` means "no value" and is kept. For wind tasks use
   `filter_func=lambda img: img.wind() > 0 and img.grade() != 0`.
3. **AU grade 0** means the original wind speed is missing; some of these rows carry interpolated wind.
   Grades 6 and 7 (WP) and 0 (AU) are not intensity classes.
4. **`intp` flags only the position** (lat/lng). In AU, wind and pressure can be interpolated where `intp = 0`.
5. **Longitude is 0-360 °E** (values above 180 occur). **AU seasons run July-June**, labelled by the ending year.
6. **Images are brightness temperature in K**, float32 from pyphoon3, shape (512, 512) or (C, 512, 512).
   The benchmark preprocessing clips to [170, 300] K and scales to [0, 1].
7. **Channels have different start years:** 1 from 1978, 2 and 3 from 1995, 4 from 2005. Multi-channel
   loading keeps only times where every channel exists.
8. **Known issues in V3-2025.R2:** offer to exclude the 174 images in `known_issues/` and, if accuracy
   matters, the 1,477 images in the dataset's own `substituted_conversion.csv`. Both go into `ignore_list`
   (for several channels, file names without the channel suffix).
9. **Record the release** (V3-2025.R2) in generated code or configs; seasonal updates can change past data.

## Writing code

1. **Ask before generating** (one question round): framework (PyTorch, TensorFlow, JAX, NumPy only);
   wrap pyphoon3 (recommended) or read the files directly; basin(s), channel(s) and label(s); where to
   write the files; extras such as augmentation, caching or multi-process loading.
2. **Prefer pyphoon3.** Start from `library.usage_examples` in `library.yaml`. Read files directly only when
   the user asks or the framework is not PyTorch; then follow `files` in `library.yaml` exactly
   (HDF5 key `Data`, CSV columns by position, `file_N` empty for hours without an image).
3. **Dependencies:** pyphoon3 is not on PyPI. Install it from GitHub
   (`uv pip install git+https://github.com/kitamoto-lab/pyphoon3`) and do not list it as a plain
   `pyproject.toml` dependency. Use `uv` in instructions. If `h5py` fails to build, the system HDF5 library
   is too old (h5py needs HDF5 >= 1.10.7).
4. **Data path:** never hard-code a path. Take the dataset root as a parameter or argument, and point users
   to the 37 MB sample (`dataset.yaml`: `distribution.sample`) for a first run.
5. **Quality:** type hints, docstrings, clear errors for a wrong root path, and the relevant caveats as
   comments where they apply.
6. **Check it runs** on the sample when it is available: one batch, shapes and label values.

## Answering questions

Answer from the YAML files and name the field you used (for example `library.yaml: files.track_file.csv_spec`,
column `wind`). If the metadata does not cover something (for example pixel spacing), say it is not
documented rather than guessing.

## Citation

Data from the dataset must be attributed as:
`Digital Typhoon Dataset V3 (National Institute of Informatics), doi:10.20783/DIAS.664` (CC BY 4.0).
Add this to READMEs of generated projects.
