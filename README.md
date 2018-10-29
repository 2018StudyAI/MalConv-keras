# MalConv-keras
A Keras implementation of MalConv and adversarial sample

---
## Desciprtion

This is the implementation of MalConv proposed in [Malware Detection by Eating a Whole EXE](https://arxiv.org/abs/1710.09435) which can be used for any very long sequence classification.

The adversarial samples are crafted by padding some bytes to the input file. It would fail if the origin file length exceeds the model's input size.

Enjoy !

## Requirement
- python3 (3.5.2)
- numpy (1.13.1)
- pandas (0.22.0)
- pickle (0.7.4)
- keras (2.1.5)
- tensorflow (1.6.0)
- sklearn

## 요약
지도기반 딥러닝 악성코드 탐지

## train
```
python src/train.py -c [훈련 데이터셋 csv파일]
```

## predict
```
python src/predict.py -c [테스트 데이터셋 csv파일]
```

## 소스원본
https://github.com/j40903272/MalConv-keras
