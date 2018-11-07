import pandas as pd
import os
import argparse
import numpy as np
import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dataset', required=True, help='upx directory')
parser.add_argument('-c', '--csv', required=True, help='upx label')
parser.add_argument('-o', '--output', default='upx.csv', help='output name')
args = parser.parse_args()

if not os.path.exists(args.dataset):
	parser.error("{} does not exists".format(args.dataset))
if not os.path.exists(args.csv):
	parser.error("{} does not exists".format(args.csv))

label = pd.read_csv(args.csv, names=['hash', 'y'])
names = []
y = []

#get directory names
for name in tqdm.tqdm(os.listdir(args.dataset)):
	path = os.path.join(args.dataset, name)
	names.append(path)
	y.append(label[label.hash==name].values[0][1])	

np_names = np.array(names)
np_y = np.array(y)

data = pd.DataFrame({'hash': np_names, 'y': np_y})
data.to_csv(args.output, header=None, index=False)
