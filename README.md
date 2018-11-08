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

## Get started
#### Clone the repository
```
git clone https://github.com/j40903272/MalConv-keras
```
#### Prepare data
Prepare a csv file with filenames(absolute or relative path) and labels in the  **<filename**, **label>**  format
```
0778a070b283d5f4057aeb3b42d58b82ed20e4eb_f205bd9628ff8dd7d99771f13422a665a70bb916, 0
fbd1a4b23eff620c1a36f7c9d48590d2fccda4c2_cc82281bc576f716d9a0271d206beb81ad078b53, 0
```
see more in [example.csv](https://github.com/j40903272/MalConv-keras/blob/master/example.csv) (1:benign, 0:malicious)
#### Training
```
python3 train.py example.csv
python3 train.py example.csv --resume
```
#### Predict
```
python3 predict.py example.csv
python3 predict.py example.csv --result_path saved/result.csv
```

#### Preprocess
If you require the preprocessed data, run the following
```
python3 preprocess.py example.csv
python3 preprocess.py example.csv --save_path saved/preprocess_data.pkl
```
