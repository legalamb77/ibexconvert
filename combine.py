#PLAN: take two input files, and an output name(3 args). The first input is the original experiment file, the second is
#the experiment results.
#First, match until end of line on the first file, and place it in the new file. Then put a tab, and grab the trial data

#each time a patient is reached, add new break column, and then possibly put labels again?
import sys
import re
import json

originalExperiment=sys.argv[1]
trialDataFile=sys.argv[2]
outputFileName=sys.argv[3]

f=open(originalExperiment)

experimentData=re.split(r"(?:\r\n)|(?:\n)|(?:\r)",f.read())

f.close()

f2=open(trialDataFile)
trialDataList=re.split(r"(?:\r\n)|(?:\n)|(?:\r)",f2.read())

f2.close()
nonHeadersString=''.join(experimentData[1:len(experimentData)])

trialDataListWithNonHeaders=[]
for i in xrange(len(trialDataList)):
    if len(trialDataList[i])>0 and not trialDataList[i][0]=="#":
        trialDataList[i]=nonHeadersString + "\t" + trialDataList[i].replace(",", "\t")

out=open(outputFileName, 'w')
out.write(experimentData[0]+"\n")
for line2 in trialDataList:
    if len(line2)>0 and not line2[0]=="#":
        out.write(line2+"\n")
out.close()
