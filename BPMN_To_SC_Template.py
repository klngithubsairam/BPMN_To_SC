#Python code to illustrate parsing of XML files
#https://towardsdatascience.com/processing-xml-in-python-elementtree-c8992941efd2
#Execution Procedure: D:\>BPMN_To_SC_Template.py inputFile.xml outputFile.sol 

#importing the required modules

import csv
import re
import xml.etree.ElementTree as ET
import sys
inFile = sys.argv[1]
outFile = open(sys.argv[2],'w')

#tree = ET.parse('MoneyTransfer.xml')
tree = ET.parse(inFile)
  
# get root element
root = tree.getroot()
#print(root)

# create empty list for news items
bpmnitems = []
 
# iterate bpmn items
#for elem in root.iter():
#    if('name' in elem.attrib.keys()):
#        print(elem.tag, "--", elem.attrib)
#print("\n")


for ele in root.iter():
    if(re.search('}task',ele.tag)):
        bpmnitems.append(ele.attrib)
        #print(ele.tag,"--",ele.attrib)    //To display only task names
          
    #if(re.search('}sequenceFlow',ele.tag)):   // To display only sequence flow
        #print(ele.attrib)
    #elif('name' in ele.attrib.keys()):    // To display only labels in the sequence
        #print("Label: ",ele.attrib)


#print("Tasks: \n",bpmnitems,"\n")


outFile.write("#***Smart Contract Templat Generated from BPMN file(XML)***\n\n")
outFile.write("#====Precausions to avoid common vulnerabilites:====\n\n")
outFile.write("#=> Use transfer() instead of send() for money transfer operations.\n")
outFile.write("#=> Use msg.sender instead of tx.origin for authentication\n")
outFile.write("#=> Specify visibility (Public/private) explicitly.\n")
outFile.write("#=> Use datatype uint256 in case of loop iterations >256 (instead of uint8, default type). \n")
outFile.write("#=> use bytes[] instead of byte[] for lower gas consumption.\n")
outFile.write("#=> Avoid conditional statements (if/for/while) with function call inside the condition.\n\n")


outFile.write("pragma  solidity  0.4.24;\n")
outFile.write("import safeMath; #To avoid Integer overflow and underflow vulnerabilities.\n")
outFile.write("contract  SolidityContract {\n\n")

for task in bpmnitems:
    for ele in root.iter():
        #print('targetRef=',task['id'])
        if('targetRef' in ele.attrib.keys()):
            if( ele.attrib['targetRef']==task['id']):
                arg=ele.attrib['name']
    str="function  "+task['name']+"(dataType "+ arg+ repr(') payable  public return( ) {')+"\n\t...\n\t...\n}\n"

    outFile.write(str)
print("output File saved in given output file.")
outFile.close()
  
   

