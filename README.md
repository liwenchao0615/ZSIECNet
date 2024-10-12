<!--
 * @Author       : WenChan Li
 * @Date         : 2024-03-19 23:41:45
 * @LastEditors  : WenChan Li
 * @LastEditTime : 2024-10-13 02:18:07
 * @Description  : 
 * Copyright 2024 OBKoro1, All Rights Reserved. 
 * 2024-03-19 23:41:45
-->
# ZSDECNet : A Zero-Shot Deep Learning Framework for Image Exposure Correction

This is the official PyTorch code for our paper :
ZSDECNet: A Zero-Shot Deep Learning Framework for Image Exposure Correction

![Network structure diagram](network_structure.pdf)

*Wenchao Li, Shuyuan Wen,Jinhao Zhua, Qiaofeng Oub, Yanchun Guob, Jiabao Chen and Bangshu Xiong*


Keywords: Exposure correction, Zero-shot, Illumination estimation,
Multi-exposure fusion.



 This repository contains the code and resources for the paper: 

    code: Will be open source after the paper is accepted.

    resources: includes the DSN night street view dataset and test results on all datasets.


## Setup

* Create a new conda environment


        conda create -n ZSDECNet python=3.7
        conda activate ZSDECNet

* Install Pytroch

        # CUDA  
        conda install pytorch==1.8.1 torchvision==0.9.1 torchaudio==0.8.1 cudatoolkit=10.2 -c pytorch

* Install other dependencies

        pip install -r requirements.txt
-----------------------------------------
## Dataset
DSN Night street scene, including underexposure and overexposure. Can be downloaded from 
<u>[Baidu Cloud](https://pan.baidu.com/s/1cy9unkx1brYNx813_i5UrA?pwd=4mqt)</u> and <u>[Google Drive](https://drive.google.com/drive/folders/1Ch3n1qxcr8TJeK3XbBt1ftM_pMb1GdTZ?usp=drive_link)<u>.

## Test results

Contains the visual comparison results of all methods in the paper on 7 datasets.
Can be downloaded from <u>[Baidu Cloud](https://pan.baidu.com/s/1cy9unkx1brYNx813_i5UrA?pwd=4mqt)</u> and and <u>[Google Drive]()<u>.


## Contact
If you have any problem with the released code, please do not hesitate to contact me by email ([wenchaoli@buaa.edu.cn]())

## Citation
    xxx