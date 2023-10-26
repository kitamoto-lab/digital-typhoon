# Digital Typhoon Dataset

This dataset is created by the [Digital Typhoon](http://agora.ex.nii.ac.jp/digital-typhoon/) project. 

## Overview

This page summarizes information about the Digital Typhoon Dataset, the longest typhoon satellite image dataset for 40+ years, aimed at benchmarking machine learning models for long-term spatio-temporal data. To build the dataset, we developed a workflow to create a typhoon-centered image by cropping the original satellite image using Lambert azimuthal equal-area projection centered at the location of the best track data. We also address data quality issues such as inter-satellite calibration to create a long-term homogeneous dataset. To take advantage of the dataset, we proposed machine learning tasks by the types and targets of inference, with other tasks for meteorological analysis, societal impact, and climate change.

## Paper

The following papers describe the dataset. 

Asanobu Kitamoto, Jared Hwang, Bastien Vuillod, Lucas Gautier, Yingtao Tian, Tarin Clanuwat, "Digital Typhoon: Long-term Satellite Image Dataset for the Spatio-Temporal Modeling of Tropical Cyclones", NeurIPS 2023 Datasets and Benchmarks (Spotlight), 2023.

```
@InProceedings{ neurips23,
      author = {Asanobu Kitamoto and Jared Hwang and Bastien Vuillod and Lucas Gautier and Yingtao Tian and Tarin Clanuwat},
      title = {Digital Typhoon: Long-term Satellite Image Dataset for the Spatio-Temporal Modeling of Tropical Cyclones},
      booktitle = {NeurIPS 2023 Datasets and Benchmarks (Spotlight)},
      year = 2023,
      month = 12,
}
```

## Dataset

[Digital Typhoon Dataset](http://agora.ex.nii.ac.jp/digital-typhoon/dataset/) is a satellite image dataset designed for machine learning research on tropical cyclones. The dataset comprises 1,099 typhoons and 189,364 infrared images from the western North Pacific basin.

The dataset is provided under a CC BY 4.0 international license, with attribution as follows.

Digital Typhoon Dataset (National Institute of Informatics) 
doi: [10.20783/DIAS.664](https://doi.org/10.20783/DIAS.664)

## Software

[pyphoon2](https://github.com/kitamoto-lab/pyphoon2) is a machine-learning library for the Digital Typhoon Dataset. 

## Model

[Hugging Face](https://huggingface.co/kitamoto-lab) provides model weights for machine learning tasks.

## Website

[Digital Typhoon](http://agora.ex.nii.ac.jp/digital-typhoon/) is one of Japan's most popular and largest typhoon information websites. The annual page view is around 20 million, and many people visit the website to check the latest information and study historical data. 

## Data Repository

[Digital Typhoon](https://doi.org/10.20783/DIAS.664) is a dataset page on the DIAS (Data Integration and Analysis System) data repository. DIAS is a Japanese data repository for earth science and environmental datasets and offers the dataset DOI (Digital Object Identifier) 10.20783/DIAS.664 as a persistent identifier. 
