import pandas as pd
import argparse
import os
import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--prefix', required=True, help='add prefix path')
parser.add_argument('-c', '--csv', required=True, help='label')
parser.add_argument('-o', '--output', default='dataset.csv', help='output')
args = parser.parse_args()

def main():
	if not os.path.exists(args.csv):
		parser.error("csv does not exist".format(args.csv))
	data = pd.read_csv(args.csv, names=['hash', 'y'])
	new_name = []
	
	for _hash in data.hash:
		path = os.path.join(args.prefix, _hash)
		new_name.append(path)
	
	new_data = pd.DataFrame({'hash': new_name, 'y': data.y})
	new_data.to_csv(args.output, index=False, header=None)

if __name__=='__main__':
	main()
	print('Done')
