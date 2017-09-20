import Tkinter as tkinter
import web_parser
import textformat
import os

class Gui:
    def __init__(self):
        self.root = tkinter.Tk()
        self.initColor = self.root['bg']
        self.root.resizable(0,0)
        self.root.title("Harassment-O-Metter")
        self.makeFileSelect()
        self.makeTextEntryDisplay()
        
    def makeTextEntryDisplay(self):
        self.main = tkinter.Frame(self.root)
        self.main.grid(row = 0,column = 1,rowspan = 2)
        self.scroll = tkinter.Scrollbar(self.main)
        self.display = tkinter.Text(self.main,height = 31,width = 50,yscrollcommand = self.scroll.set,bg = "gray",state = tkinter.DISABLED)
       # self.entry = tkinter.Entry(self.main,width = 62,bg = "gray")
       # self.mark = tkinter.Entry(self.main,width = 4,bg = "gray")
        self.display.grid(row = 0,column = 0,columnspan = 2)
        #self.entry.grid(row = 1,column = 1)
        #self.mark.grid(row = 1,column = 0)
        self.scroll.grid(row = 0,column = 2,rowspan = 2,sticky = tkinter.N+tkinter.S)
        self.scroll.config(command=self.display.yview)
        #self.mark.insert("end",">>")
        #self.entry.bind("<Return>",self.enter)
    def makeFileSelect(self):
        self.selectedSource = -1
        self.fileSelectFrame = tkinter.Frame(self.root)
        self.fileSelectFrame.grid(row = 0,column = 0,sticky=tkinter.W+tkinter.E+tkinter.N+tkinter.S)
        self.fileEntryPrompt = tkinter.Label(self.fileSelectFrame,height = 2,width = 50,font = 20)
        self.fileEntry = tkinter.Entry(self.fileSelectFrame,width = 62,bg = "gray", justify = tkinter.CENTER,font = 20)
        self.fileEntryPrompt.grid(row = 0, column = 0,columnspan = 2)
        self.fileEntry.grid(row = 1, column = 0,columnspan = 2)
        self.fileEntryPrompt.config(text = 'Enter source to be analysed')

        self.chooseFileButton = tkinter.Button(self.fileSelectFrame,height = 2, width = 25,text = 'File')
        self.chooseFileButton.grid(row = 2, column = 0)
        self.chooseFileButton.bind('<Enter>',lambda event: self.chooseFileButton.config(bg = self.getButtonHover(0)))
        self.chooseFileButton.bind('<Leave>',lambda event: self.chooseFileButton.config(bg = self.getButtonExit(0)))
        self.chooseFileButton.bind('<Button-1>',lambda event: self.chooseFileButton.config(bg = self.buttonClick(0)))

        self.chooseWebButton = tkinter.Button(self.fileSelectFrame,height = 2,width = 25,text = 'Web')
        self.chooseWebButton.grid(row = 2, column = 1)
        self.chooseWebButton.bind('<Enter>',lambda event: self.chooseWebButton.config(bg = self.getButtonHover(1)))
        self.chooseWebButton.bind('<Leave>',lambda event: self.chooseWebButton.config(bg = self.getButtonExit(1)))
        self.chooseWebButton.bind('<Button-1>',lambda event: self.chooseWebButton.config(bg = self.buttonClick(1)))

        self.runButton = tkinter.Button(self.fileSelectFrame,height = 2, width = 52,anchor = tkinter.CENTER,text = 'Analyse')
        self.runButton.grid(row = 3, column = 0,columnspan = 2)
        self.runButton.bind('<Enter>',lambda event: self.runButton.config(bg = self.getButtonHover(2)))
        self.runButton.bind('<Leave>',lambda event: self.runButton.config(bg = self.getButtonExit(2)))
        self.runButton.bind('<Button-1>',lambda event: self.buttonClick(2))
        
        self.ratioDisp = tkinter.Text(self.fileSelectFrame,bg = self.initColor)
        self.ratioDisp.grid(row = 4, column = 0, columnspan = 2)
    def getButtonHover(self,key):
        if key == 2:
            return 'gray'
        elif key == self.selectedSource:
            return 'red'
        else:
            return 'gray'
    def getButtonExit(self,key):
        if key == 2:
            return self.initColor
        elif key == self.selectedSource:
            return 'red'
        else:
            return self.initColor
    def buttonClick(self,key):
        if key == 2:
            fileName = ''
            if self.selectedSource == -1:
                return -1
            elif self.selectedSource == 0:

                textformat.formatText(self.fileEntry.get())
                self.fileEntry.delete(0,tkinter.END)
                self.fileEntry.insert(0,'Analysis done..')
            elif self.selectedSource == 1:
                try:
                    wp = web_parser.WebFunctions()
                    wp.parseFromWeb(self.fileEntry.get(),'wpoutput.txt')
                    #textformat.formatText('wpoutputsub.txt')
                    self.fileEntry.delete(0,tkinter.END)
                    self.fileEntry.insert(0,'Analysis done..')
                except:
                    print('File analysis is not successful. URL doesn\'t use correct encoding or incorrect url')
            if self.selectedSource != -1:
                os.system("fastText/fasttext predict fastText/model.bin wpoutput.txt 1 > out.txt")
                cnt1, cnt2 = makeComparison("wpoutput.txt", "out.txt")
                f = open('listOffensive.txt','r')
                for line in f:
                    line = line.strip()
                    if line == '':
                        continue
                    self.enter(line.strip())
                f.close()
                ratio = 'Offensive Ratio: ' + str(cnt2) + '/' + str((cnt1 + cnt2))
                self.ratioDisp.delete(1.0,tkinter.END)
                self.ratioDisp.insert(tkinter.END,ratio)
                pass
        else:
            self.selectedSource = key
            if key == 1:
                self.chooseFileButton.config(bg = self.initColor)
            elif key == 0:
                self.chooseWebButton.config(bg = self.initColor)
            return 'red'
    def enter(self,text):
        self.display["state"] = tkinter.NORMAL
        self.display.insert("end",">> " + text + "\n")
        self.display["state"] = tkinter.DISABLED
        #self.entry.delete(0,"end")
        self.display.yview("end")
    def output(self,text):
        self.display["state"] = tkinter.NORMAL
        self.display.insert("end","<< " + text + "\n")
        self.display["state"] = tkinter.DISABLED
        self.display.yview("end")

# each line of these 
def makeComparison(inputFile, resultFile):
    lines1 = open(inputFile,'r').readlines()
    lines2 = open(resultFile,'r').readlines()
    listOK = open('listOkay.txt','w')
    listOF = open('listOffensive.txt','w')
    cnt = 0
    cnt2 = 0
    for i in range(min([len(lines1), len(lines2)])):
        lines2[i] = lines2[i].strip()
        if (lines2[i] == "__label__Okay"):
            cnt += 1
            listOK.write(lines1[i] + '\n')
        elif (lines2[i] == "__label__Offensive"):
            cnt2 += 1
            listOF.write(lines1[i] + '\n')
    listOK.close()
    listOF.close()
    return (cnt,cnt2)



gui = Gui()
tkinter.mainloop()
