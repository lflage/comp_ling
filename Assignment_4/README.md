# Intro

This repository contains files related to Assignment 4 from the Computational Linguistics lecture.


# Dependencies

Python             3.7.4  
pytorch            1.10.1  cuda 10.2  
torchtext          0.11.1  
comet_ml           3.2.0  
  

# Tree Structure

```
.
├── corpus
│   ├── de_gsd-ud-dev.conllu
│   ├── de_gsd-ud-test.conllu
│   └── de_gsd-ud-train.conllu
├── images
│   ├── Mean Accuracy per Epoch - DevData 1.svg
│   ├── Mean Accuracy per Epoch - DevData2.svg
│   ├── Mean Accuracy per Epoch - DevData3.svg
│   ├── Mean Accuracy per Epoch - DevData4.svg
│   ├── Mean Accuracy per Epoch - DevData5.svg
│   ├── Mean Accuracy per Epoch - TrainData.svg
│   ├── Mean Loss per Epoch - DevData1.svg
│   ├── Mean Loss per Epoch - DevData2.svg
│   ├── Mean Loss per Epoch - DevData3.svg
│   ├── Mean Loss per Epoch - DevData4.svg
│   ├── Mean Loss per Epoch - DevData5.svg
│   └── Mean Loss per Epoch - TrainData.svg
├── models
│   ├── LSTM_PosTagger_DEV - DevData1.pt
│   ├── LSTM_PosTagger_DEV - DevData2.pt
│   ├── LSTM_PosTagger_DEV - DevData3.pt
│   ├── LSTM_PosTagger_DEV - DevData4.pt
│   ├── LSTM_PosTagger_DEV - DevData5.pt
│   └── LSTM_PosTagger_Train - TrainData1.pt
├── data.py
├── LSTM_PosTagger.ipynb
└── README.md
```

# How to run

* The corpus folder should contain the .conllu files from the Universal Depencencies German GSD [repo](https://github.com/UniversalDependencies/UD_German-GSD).

* The images folder contains the exported plots created with comet.

* The LSTM_PosTagger.ipynb is the main file.


## Observations

* Only the ```LSTM_PosTagger_Train - TrainData1.pt``` model is provided in the zip file. The other models can be downloaded from my personal repo. By doing this you can reproduce the results of the Accuracy of the Dev Models on the Test Data. [lflage](https://github.com/lflage/comp_ling/tree/master/Assignment_4)