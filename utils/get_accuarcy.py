from sklearn.metrics import confusion_matrix, accuracy_score
import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--csv', type=str, required=True, help='csv file for getting accuracy')
parser.add_argument('-t', '--threshold', type=str, default=0.75, help='threadshold for predicting')
args = parser.parse_args()

def main():
    data = pd.read_csv(args.csv, names=['hash', 'y', 'ypred'])
    #data["ypred"].describe().apply(lambda x: format(x, 'f'))
    
    y = data.y
    ypred = np.where(np.array(data.ypred) > args.threshold, 1, 0)

    #get and print accuracy
    accuracy = accuracy_score(y, ypred)
    print("accuracy : %.0f%%" % (np.round(accuracy, decimals=2)*100))

    #get and print matrix
    mt = confusion_matrix(y, ypred)
    t = mt[0][0]
    mt[0][0] = mt[1][1]
    mt[1][1] = t
    print(mt)

    #print FP, FN
    print("True Postive : %.0f%%" % (round(mt[0][1]/(mt[0][1]+mt[1][1]), 2)*100))
    print("False Postive : %.0f%%" % (round(mt[1][0]/(mt[0][0]+mt[1][0]), 2)*100))

if __name__=='__main__':
    main()
