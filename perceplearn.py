import sys
import os
import operator
import random
import pickle
from collections import Counter

def getDevAccuracy(weight, feature_list, class_list, dev_file):
    correct = 0
    line_count = 0
    prod = [0] *len(class_list)
    dev = open(dev_file, 'r')
    for line in dev:
        line_count = line_count + 1
        list = line.split()
        count = Counter(list[1:])
        for key,  value in count.items():
            if key in feature_list:
                for i in range(0, len(weight)):
                     prod[i] = prod[i] + value * weight[i][feature_list[key]]
        z = prod.index(max(prod))
        prod = [0] *len(class_list)
        if list[0] == "rs":
            print(line_count)
            sys.exit()
        if z == class_list[list[0]]:
            correct = correct + 1
    return correct/line_count

def main(argv):
    if len(argv) != 2 and len(argv) != 4 and argv[2]  != '-h' :
        print("Usage: python3 perceplearn.py TRAININGFILE MODELFILE -h DEVFILE")
        sys.exit()
    if not os.path.exists(argv[0]) :
        print('File does not exist')
        sys.exit()
    if not os.path.isfile(argv[0]):
        print('Not a file')
        sys.exits()
    if len(argv) == 4:
        if not os.path.exists(argv[3]) :
            print(argv[3] + ' does not exist')
            sys.exit()
        if not os.path.isfile(argv[3]):
            print(argv[3] + ' not a file')
            sys.exit()
    
    input = open(argv[0], 'r', errors='ignore')
    output = open(argv[1],  'wb')
    class_list = {}
    feature_list = {}
    model = {}
    class_n = 0
    feature_n = 0
    for line in input:
        list = line.split()
        if list[0] not in class_list:
            class_list[list[0]] = class_n
            class_n = class_n + 1
        for feature in list:
            if feature not in feature_list:
                feature_list[feature] = feature_n
                feature_n =  feature_n + 1
    prod = [0] *len(class_list)
    weight = [[0 for x in range(len(feature_list))] for x in range(len(class_list))] 
    avg_weight = [[0 for x in range(len(feature_list))] for x in range(len(class_list))] 
    update = [[0 for x in range(len(feature_list))] for x in range(len(class_list))]
    icount = 0
    model['features'] = feature_list
    model['class'] = class_list
    
    for iter in range(1, 20):
        input = open(argv[0], 'r', errors='ignore')
        line_count = 0
        incorrect = 0
        data = [ (random.random(), line) for line in input ]
        data.sort()
        for _, line in data:
            line_count += 1
            icount = icount + 1
            list = line.split()
            true_class = class_list[list[0]]
            count = Counter(list[1:])
            for key,  value in count.items():
                for cls in range(0, len(weight)):
                    prod[cls] = prod[cls] + value * weight[cls][feature_list[key]]
            z = prod.index(max(prod))
            prod = [0] *len(class_list)

            if z != class_list[list[0]]:
                 incorrect = incorrect + 1
                 for key,  value in count.items():
                     weight[true_class][feature_list[key]] = weight[true_class][feature_list[key]] + value
                     update[true_class][feature_list[key]] = update[true_class][feature_list[key]] + icount * value
                    
                 for key,  value in count.items():
                     weight[z][feature_list[key]] = weight[z][feature_list[key]] - value
                     update[z][feature_list[key]] = update[z][feature_list[key]] - icount * value  
                       
        accuracy = (line_count - incorrect)/line_count
        if len(argv) == 4:
            temp =[[update[i][j]/icount for j in range(len(update[i]))] for i in range(len(update))]
            for i in range(len(weight)):
                avg_weight[i][:] = map(operator.sub, weight[i], temp[i])
            accuracy = getDevAccuracy(avg_weight,feature_list,class_list,   argv[3])
            print('Iteration: ' + str(iter) + ' Accuracy on development set: '+ str(accuracy))
        if len(argv) == 2:
            print('Iteration: ' + str(iter) + ' Accuracy on training set: '+ str(accuracy))
        
    if len(argv) == 2:
        temp = [[0 for x in range(len(feature_list))] for x in range(len(class_list))]
        temp =[[update[i][j]/icount for j in range(len(update[i]))] for i in range(len(update))]
        for i in range(len(weight)):
            weight[i][:] = map(operator.sub, weight[i], temp[i])
            
    model['weight'] = weight
    pickle.dump(model, output)
    output.close()
    
if __name__ == "__main__":
    main(sys.argv[1:])
