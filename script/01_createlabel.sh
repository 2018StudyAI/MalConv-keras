#!/bin/sh

#train set
python ../utils/create_traindataset.py --prefix /home/abc/train -c ~/label/sample.csv -o ~/sample.csv 
#test set
python ../utils/create_traindataset.py --prefix /home/abc/test -c ~/label/sample.csv -o ~/test.csv 
