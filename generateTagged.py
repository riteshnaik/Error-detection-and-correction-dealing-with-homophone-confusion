import glob
import sys
import os
def main(argv):
    output = open(argv[1], 'w')
    class_list = ['it\'s', 'its']
    feature = {}
    feature[0] = 'L1_'
    feature[1] = 'L2_'
    feature[2] = 'L3_'
    feature[3] = 'R1_'
    feature[4] = 'R2_'
    feature[5] = 'R3_'
    feature[6] = 'L1_TAG_'
    feature[7] = 'L2_TAG_'
    feature[8] = 'L3_TAG_'
    feature[9] = 'R1_TAG_'
    feature[10] = 'R2_TAG_'
    feature[11] = 'R3_TAG_'
    for file in sorted(glob.glob(os.path.join(argv[0], "*.txt"))):
             f = open(file, 'r')
             print(file)
             for line in f:
                 list = line.split()
                 for i in range(len(list)):
                     word = list[i].split('/')[0]
                     if word.lower() in class_list:
                         current = 'CURR_'+list[i]
                         if i == 1:
                             feature[2] = 'L3_'+list[i-1].split('/')[0]
                             feature[8] = 'L3_TAG_'+list[i-1].split('/')[-1]
                         if i == 2:
                            feature[2] = 'L3_'+list[i-1].split('/')[0]
                            feature[8] = 'L3_TAG_'+list[i-1].split('/')[-1]
                            feature[1] = 'L2_'+list[i-2].split('/')[0]
                            feature[7] = 'L2_TAG_'+list[i-2].split('/')[-1]
                         if i >= 3:
                            feature[2] = 'L3_'+list[i-1].split('/')[0]
                            feature[8] = 'L3_TAG_'+list[i-1].split('/')[-1]
                            feature[1] = 'L2_'+list[i-2].split('/')[0]
                            feature[7] = 'L2_TAG_'+list[i-2].split('/')[-1]
                            feature[0] = 'L1_'+list[i-3].split('/')[0]
                            feature[6] = 'L1_TAG_'+list[i-3].split('/')[-1]
                         if i == len(list) - 2:
                            feature[3] = 'R1_'+list[i+1].split('/')[0]
                            feature[9] = 'R1_TAG_'+list[i+1].split('/')[-1] 
                         if i == len(list) - 3:
                            feature[3] = 'R1_'+list[i+1].split('/')[0]
                            feature[9] = 'R1_TAG_'+list[i+1].split('/')[-1]
                            feature[4] = 'R2_'+list[i+2].split('/')[0]
                            feature[10] = 'R2_TAG_'+list[i+2].split('/')[-1]
                         if i <= len(list) - 4:
                            feature[3] = 'R1_'+list[i+1].split('/')[0]
                            feature[9] = 'R1_TAG_'+list[i+1].split('/')[-1]
                            feature[4] = 'R2_'+list[i+2].split('/')[0]
                            feature[10] = 'R2_TAG_'+list[i+2].split('/')[-1]
                            feature[5] = 'R3_'+list[i+3].split('/')[0]
                            feature[11] = 'R2_TAG_'+list[i+3].split('/')[-1]
                         output.write(list[i].split('/')[0].lower()+' '+feature[0]+' '+feature[6]+' '+feature[1]+' '+feature[7]+' '+feature[2]+' '+feature[8]+' '+feature[3]+' '+feature[9]+' '+feature[4]+' '+feature[10]+' '+feature[5]+' '+feature[11]+'\n')
    output.close()

if __name__ =="__main__":
    main(sys.argv[1:])
