# Digital Typhoon Dataset

This dataset is created by the [Digital Typhoon](http://agora.ex.nii.ac.jp/digital-typhoon/) project. 

![Overview of the Digital Typhoon dataset](http://agora.ex.nii.ac.jp/digital-typhoon/dataset/overview.png)

## Overview

This page summarizes information about the Digital Typhoon Dataset, the longest typhoon satellite image dataset for 40+ years, aimed at benchmarking machine learning models for long-term spatio-temporal data. To build the dataset, we developed a workflow to create a typhoon-centered image by cropping the original satellite image using Lambert azimuthal equal-area projection centered at the location of the best track data. We also address data quality issues such as inter-satellite calibration to create a long-term homogeneous dataset. To take advantage of the dataset, we proposed machine learning tasks by the types and targets of inference, with other tasks for meteorological analysis, societal impact, and climate change.

## Paper

The following paper describes the dataset. 

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

[Digital Typhoon Dataset](http://agora.ex.nii.ac.jp/digital-typhoon/dataset/) is a satellite image dataset designed for machine learning research on tropical cyclones. The Dataset V2, released on November 26, 2024, comprises the WP dataset from the northern hemisphere, and the AU dataset from the southern hemisphere. 

| Basin | Western Pacific (WP) | Around Australia (AU) | 
|--|--|--|
| Season | 1978-2023 (1978, 1979, 1980 are not complete) | 1979-2024 (some years are not complete) |
| Tropical cyclones | 1,116 | 480 |
| Images | 192,956 | 70,087 |
| Dataset Size | 56GB | 21GB | 

[image](https://github.com/user-attachments/assets/61f8d9b0-7706-4162-9b9a-aac14fe836f9)

The dataset is provided under a CC BY 4.0 international license, with attribution as follows.

```
Digital Typhoon Dataset (National Institute of Informatics), doi:10.20783/DIAS.664
```

## Software

[pyphoon2](https://github.com/kitamoto-lab/pyphoon2) is a machine-learning library for the Digital Typhoon Dataset. The documentation is available at [pyphoon2’s documentation at readthedocs](https://pyphoon2.readthedocs.io/en/latest/).

## Model

[Hugging Face](https://huggingface.co/kitamoto-lab) provides model weights for machine learning tasks and some codes for using them. 

## Data Repository

[Digital Typhoon Dataset](https://doi.org/10.20783/DIAS.664) is also available from [DIAS (Data Integration and Analysis System)](https://www.diasjp.net/). DIAS is a Japanese data repository for earth science and environmental datasets and offers the [dataset DOI (Digital Object Identifier)](https://dias.ex.nii.ac.jp/doi/) 10.20783/DIAS.664 as a persistent identifier. 

## Website

[Digital Typhoon](http://agora.ex.nii.ac.jp/digital-typhoon/) is one of Japan's most popular and largest typhoon information websites. The annual page view is around 20 million, and many people visit the website to check the latest information and study historical data. 
