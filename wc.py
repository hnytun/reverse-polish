import sys
import math

#script to print number of lines, number of words, number of characters + filename
#in this task i assume that the "nice word count" to be printed for the extension of
#the task includes the linecount etc as it is printed in my program at this moment




for i in range(1,len(sys.argv)):


        filename = sys.argv[i]
        inputFile=open(filename)

        numLines=0;
        numWords=0;
        numCharacters=0;


        for line in inputFile:
            numLines = numLines + 1
            for w in line.split(" "):
                numWords = numWords + 1
                for c in list(w):
                    numCharacters = numCharacters + 1

        infoList = [str(numLines),str(numWords),str(numCharacters),filename]
        print(infoList[0] + " "
        + infoList[1] + " "
        + infoList[2] + " "
        + infoList[3])
