import re
import string


exampleLinesToGet = 2

example = open('GenomeStudio_Example_DataFormat.txt','r')
i = 0
for line in example:
    if i < exampleLinesToGet:
        print(line)
        line = line.replace("\n","")
        splitLine = line.split('\t')
        if i is 0:
            j = 0
            sampleIndex ={}
            for item in splitLine:
                if item == "Name":
                    nameIndex = j
                elif re.search('GType',item):
                    print(item)
                    sampleIndex.update({j:item})
                j=j+1
        elif i > 0:
            print(splitLine[nameIndex])
            for index in sampleIndex:
                #filtered_string = filter(lambda x: x in string.printable, splitLine[index])
                print(sampleIndex[index]+":"+splitLine[index])
        
        i = i+1
        
