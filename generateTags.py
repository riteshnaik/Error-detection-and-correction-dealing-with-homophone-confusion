import sys
import nltk
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
import codecs

def main(argv):
    output = open(argv[1], 'w')
    f = open(argv[0], 'r')
    for line in f:
        #text = word_tokenize(line.decode('utf8','ignore'))
        #tokenizer = RegexpTokenizer('\w+\'*\w+|\$[\d\.]+|[.,]+')
        #text = tokenizer.tokenize(line.decode('utf8','ignore'))
        text = line.split()
        #tokenizer = RegexpTokenizer('\w+\'*\w+|\w+|[^\w]+')
        #text = tokenizer.tokenize(line)
        tagged_text = nltk.pos_tag(text)
	for word in tagged_text:
            output.write('/'.join(word).encode('utf8','ignore') + ' ')
        output.write('\n')
if __name__ =="__main__":
    main(sys.argv[1:])
