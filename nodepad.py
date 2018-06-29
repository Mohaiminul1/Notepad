from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox, simpledialog
import tkinter.scrolledtext as ScrolledText

root=Tk(className= " Emon's Text Editor")
textArea=ScrolledText.ScrolledText(root,width=100,height=80)

def newFile():
    if len (textArea.get('1.0',END+'-1c')) >0:
        if messagebox.askyesno("Save?", "Do you wish to save?"):
            saveFile()
            
            
        else:
            textArea.delete('1.0',END)

    root.title("TEXT EDITOR")
            
def openFile():
    textArea.delete('1.0',END)
    file= filedialog.askopenfile(parent=root, title='Select a text file', filetype=(("Text file", "*.txt"), ("All files", "*.*")))

    root.title(os.path.basename(file.name) +" - TEXT EDITOR")

    if file != None:
        contents = file.read()
        textArea.insert('1.0',contents)
        file.close()

def saveFile():
    file=filedialog.asksaveasfile(mode='w')

    if file !=None:
        data=textArea.get('1.0',END+'-1c')
        file.write(data)
        file.close()

def findInFile():
    findString= simpledialog.askstring("Find...","Enter text")
    textData=textArea.get('1.0',END)

    occurances= textData.upper().cout(findString.upper())

    if textData.upper().cout(findString.upper()) > 0:
        label=messagebox.showinfo("Results",findString+ "has multiple occurance," + str())

    else:
        label=messagebox.showinfo("Results","Naah sorry mate")
        
    
    #cout= 0

    print(textData.upper().cout(findString.upper()))
    
    if findString.upper() in textData.upper():
        print("True")
    

def about():
    label=messagebox.showinfo("About", "A Python alternative to Notepad!")
    

def exitRoot():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.dedestroy()
menu=Menu(root)
root.config(menu=menu)
fileMenu=Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Find", command=findInFile)
fileMenu.add_command(label="Print")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exitRoot)

helpMenu = Menu(menu)
menu.add_cascade(label="Edit")
menu.add_cascade(label="Format")
menu.add_cascade(label="Help")
menu.add_cascade(label="About", command=about)

textArea.pack()

root.mainloop()
