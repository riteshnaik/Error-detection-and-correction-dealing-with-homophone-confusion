import sys
import pickle
from collections import Counter

def main(argv):
    if len(argv) != 1 :
        print("Usage: python3 percepclassify.py MODELFILE")
        sys.exit()
    model_file = open(argv[0], 'rb')
    model = pickle.load(model_file)
    model_file.close()
    feature_list = model['features']
    class_list = model['class']
    weight = model['weight']
    prod = [0] *len(class_list)
    for line in sys.stdin:
        list = line.split()
        count = Counter(list)
        for key,  value in count.items():
            if key in feature_list:
                for i in range(0, len(weight)):
                     prod[i] = prod[i] + value * weight[i][feature_list[key]]
        z = prod.index(max(prod))
        prod = [0] *len(class_list)
        for key,  value in class_list.items():
            if value == z:
                cls = key
        print(cls+'\n')
if __name__=='__main__':
    main(sys.argv[1:])
