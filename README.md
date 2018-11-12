# MalConv-keras
A Keras implementation of MalConv and adversarial sample

---
## Desciprtion

This is the implementation of MalConv proposed in [Malware Detection by Eating a Whole EXE](https://arxiv.org/abs/1710.09435) which can be used for any very long sequence classification.

The adversarial samples are crafted by padding some bytes to the input file. It would fail if the origin file length exceeds the model's input size.

Enjoy !

## Requirement
- python3 (3.5.2)

if you have not gpu:
```
pip install -r requirments_cpu.txt
```

if you have gpu
```
pip install -r requirements_gpu.txt
```
