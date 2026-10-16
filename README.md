<img width="1226" height="562" alt="overview-v3" src="https://github.com/user-attachments/assets/2bf992ca-a033-4197-922e-87bc3b8e98c1" />

# Digital Typhoon Dataset

The [Digital Typhoon](http://agora.ex.nii.ac.jp/digital-typhoon/) project created this dataset. 

## Overview

This page summarizes the Digital Typhoon Dataset, the longest typhoon satellite image dataset spanning nearly 50 years, designed to benchmark machine learning models for long-term spatio-temporal data. To build the dataset, we developed a workflow to create typhoon-centered images by cropping the original satellite image using azimuthal equidistant projection centered on the best-track location. We also addressed data quality issues, such as inter-satellite calibration, to create a long-term, homogeneous dataset. To leverage the dataset, we propose machine learning tasks by inference type and target, including meteorological analysis, societal impact, and climate change.

## Paper

### Dataset V3

[Asanobu Kitamoto, Victor Le Louarn, Noelia Falczuk, Ngoc Anh Tong, Anja Veleva, "Digital Typhoon Dataset V3: Benchmarking for Multi-spectral Extension and Analyzing Systematic Bias in Intensity Regression", arXiv, doi:arXiv.2610.21654, 2026.](https://arxiv.org/abs/2610.21654)

```
@Article{ arxiv26,
      author = {Asanobu Kitamoto, Victor Le Louarn, Noelia Falczuk, Ngoc Anh Tong, Anja Veleva},
      title = {Digital Typhoon Dataset V3: Benchmarking for Multi-spectral Extension and Analyzing Systematic Bias in Intensity Regression},
      journal = {arXiv},
      year = 2026,
      month = 10,
      doi = {https://doi.org/10.48550/arXiv.2610.21654},
}
```

### Dataset V2

[Asanobu KITAMOTO, Erwan Dzik, Gaspar Faure, "Machine Learning for the Digital Typhoon Dataset: Extensions to Multiple Basins and New Developments in Representations and Tasks", arXiv, doi:arXiv.2411.16421, 2024.](https://arxiv.org/abs/2411.16421)

```
@Article{ arxiv24,
      author = {Asanobu KITAMOTO and Erwan Dzik and Gaspar Faure},
      title = {Machine Learning for the Digital Typhoon Dataset: Extensions to Multiple Basins and New Developments in Representations and Tasks},
      journal = {arXiv},
      year = 2024,
      month = 11,
      doi = {https://doi.org/10.48550/arXiv.2411.16421},
}
```

### Dataset V1

[Asanobu Kitamoto, Jared Hwang, Bastien Vuillod, Lucas Gautier, Yingtao Tian, Tarin Clanuwat, "Digital Typhoon: Long-term Satellite Image Dataset for the Spatio-Temporal Modeling of Tropical Cyclones", NeurIPS 2023 Datasets and Benchmarks (Spotlight), 2023.](https://neurips.cc/virtual/2023/poster/73675)

```
@InProceedings{ neurips23,
      author = {Asanobu Kitamoto and Jared Hwang and Bastien Vuillod and Lucas Gautier and Yingtao Tian and Tarin Clanuwat},
      title = {Digital Typhoon: Long-term Satellite Image Dataset for the Spatio-Temporal Modeling of Tropical Cyclones},
      booktitle = {{NeurIPS} 2023 Datasets and Benchmarks (Spotlight)},
      year = 2023,
      month = 12,
}
```
You can also find the paper on arXiv [Asanobu Kitamoto, Jared Hwang, Bastien Vuillod, Lucas Gautier, Yingtao Tian, Tarin Clanuwat, "Digital Typhoon: Long-term Satellite Image Dataset for the Spatio-Temporal Modeling of Tropical Cyclones", arXiv:2311.02665, 2023.](https://arxiv.org/abs/2311.02665)

## Dataset

[Digital Typhoon Dataset](http://agora.ex.nii.ac.jp/digital-typhoon/dataset/) is a satellite image dataset designed for machine learning research on tropical cyclones. Dataset V3, released on October 16, 2026, includes the WP dataset for the Northern Hemisphere and the AU dataset for the Southern Hemisphere. 

The dataset is provided under a CC BY 4.0 international license, with attribution as follows.

```
Digital Typhoon Dataset V3 (National Institute of Informatics), doi:10.20783/DIAS.664
```

## Software

[pyphoon3](https://github.com/kitamoto-lab/pyphoon3) is a machine-learning library for the Digital Typhoon Dataset. 

## Model

[Hugging Face](https://huggingface.co/kitamoto-lab) provides model weights for machine learning tasks and some code for Dataset V1 (obsolete version).

## Data Repository

[Digital Typhoon Dataset](https://doi.org/10.20783/DIAS.664) is also available from [DIAS (Data Integration and Analysis System)](https://www.diasjp.net/). DIAS is a Japanese data repository for earth science and environmental datasets and offers the [dataset DOI (Digital Object Identifier)](https://dias.ex.nii.ac.jp/doi/) 10.20783/DIAS.664 as a persistent identifier. 

## Website

[Digital Typhoon](http://agora.ex.nii.ac.jp/digital-typhoon/) is one of Japan's most popular and largest typhoon information websites. The site gets around 20 million page views annually, and many people visit it to check the latest information and study historical data. 
