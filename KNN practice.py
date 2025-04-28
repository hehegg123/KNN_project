import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#import data file
def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLine = len(arrayOLines)
    returnMat = np.zeros((numberOfLine, 3))
    classLabelVector = []
    
    index = 0
    for line in arrayOLines:
        #strip the empty space
        line = line.strip()
        # split based on tab
        listFromLine = line.split('\t')
        # record the first three values on each row into the dataframe
        returnMat[index,:] = listFromLine[0:3]
        # use the last column as data label
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector

datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    maxClassCount = max(classCount, key=classCount.get)
    return maxClassCount


#save max and min and range of each property.
minVals = datingDataMat.min(0)
maxVals = datingDataMat.max(0)
ranges = maxVals - minVals
m = datingDataMat.shape[0]
print(m)
#Normalize: (X-Xmin)/(Xmax-Xmin)
normDataSet = datingDataMat - np.tile(minVals,(m,1))
normDataSet = normDataSet / np.tile(ranges,(m,1))

#set the test ratio
hoRatio = 0.1
#set m as row count of dataset
m = normDataSet.shape[0]
# Set
numTestVecs = int(m*hoRatio)
print('numTestVecs=',numTestVecs)
errorCount = 0.0
for i in range(numTestVecs):
    classifierResult = 




