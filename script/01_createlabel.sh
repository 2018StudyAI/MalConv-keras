#!/bin/sh

#train set
python ../utils/create_traindataset.py --prefix ~/Downloads/trainset -c ~/Downloads/label/trainset.csv -o ~/train.csv 
#test set
python ../utils/create_traindataset.py --prefix ~/Downloads/testset -c ~/Downloads/label/testset.csv -o ~/test.csv
