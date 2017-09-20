
def formatText(fileName):
    file = open(fileName, 'r')
    newFile = open('wpoutput.txt', 'w')
    for line in file:
        line = line.strip()
        line = line.split('.')
        for sentence in line:            
           newFile.write(sentence+'\n')
    file.close()
    newFile.close()

def getFileName():
    return input("Enter file name")
