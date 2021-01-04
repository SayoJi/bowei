
selectedElements=["Cu","Fe"]

file=open('element.txt','w')
writeStr = ''
for element in selectedElements:
    writeStr = writeStr + str(element) + '\n'
file.write(writeStr); 
file.close()


selectedContent1=[98,2]

file=open('content1.txt','w')
writeContent = ''
for content in selectedContent1:
    writeContent = writeContent + str(content) + '\n'
file.write(writeContent); 
file.close() 
