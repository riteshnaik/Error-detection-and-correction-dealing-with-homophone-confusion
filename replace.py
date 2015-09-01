import sys
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer

def main(argv):
    output = open(argv[1], 'w')
    predict_file = open(argv[2],'r')
    predict = predict_file.readlines()
    f = open(argv[0], 'r')
    s_class1_count = 0
    C_class1_count = 0
    s_class2_count = 0
    C_class2_count = 0
    for line in f:
        list = line.split()
        #tokenizer = RegexpTokenizer('\w+\'*\w+|\w+|[^\w]+')
        #list = tokenizer.tokenize(line)
        #print list
        #sys.exit()
        for i in range(len(list)):
            if list[i] == 'its':
                list[i] = predict[i].strip()
            if list[i] == 'Its':
                list[i] = predict[i].strip().capitalize()
            if list[i] == 'it\'s':
                list[i] = predict[i].strip()
            if list[i] == 'It\'s':
                list[i] = predict[i].strip().capitalize()
        output.write(' '.join(list)+'\n')
    #print 'to: '+str(s_class1_count)
    #print 'To: '+str(C_class1_count)
    #print 'too: '+str(s_class2_count)
    #print 'Too: '+str(C_class2_count)
    #print 'Total: '+str(s_class1_count+C_class1_count+s_class2_count+C_class2_count)
if __name__ =="__main__":
    main(sys.argv[1:])
