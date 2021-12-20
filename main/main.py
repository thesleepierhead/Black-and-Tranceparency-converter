from PIL import Image
import tkinter as tk
from tkinter import filedialog as fd 

class BnT:

    def __init__(self, root):
            
        root.title('BnT converter')    
        root.resizable(False, False)

        mnf = tk.Frame(root, borderwidth=10)
        mnf.grid(column=0, row=0, sticky=('N, W, E, S'))
        mnf.columnconfigure(0, weight=1, minsize=75)
        mnf.columnconfigure(1, weight=4, minsize=225)
        mnf.rowconfigure(0, weight=1)      

        #setting global variables
        self.path = tk.StringVar()
        self.status = tk.StringVar()
        self.path_short = tk.StringVar()

        #Info Labels
        tk.Label(mnf, text ='   ').grid(column=0, row=0)
        tk.Label(mnf, text='Black and Transparency converter:', font=('Default', 15)).grid(column=0, row=1, columnspan=2)
        tk.Label(mnf, text = 
            'This application takes an image, converts it to grayscale \n'
            'and then converts it to an image made only of black pixels \n'
            ' of varying opacity.', relief = 'sunken').grid(column = 0, row = 2, columnspan = 2, pady = 10)

        #Pick options for grayscaling
        radbutton = tk.Frame(mnf, borderwidth=10)
        radbutton.grid(column=0, row=3, columnspan=2)
        self.optionpicked = tk.IntVar()
        options = [('Grayscale as seen\n by the human eye', 0),
                   ('Grayscale without \n correcting for the eye', 1)]
        tk.Label(radbutton, text='Pick how the conversion is handled').pack()
        for optname, val in options:
            tk.Radiobutton(radbutton, text=optname, variable=self.optionpicked, value=val).pack(side=tk.LEFT)

        #Open File 
        tk.Button(mnf, text='Open a File',
            command=self.select_file).grid(column=0, row=4, pady = 10, sticky='E')
        
        tk.Label(mnf, textvariable = self.path_short, wraplength=260).grid(column=1, row=4, pady = 10, sticky='W')

        #Save File
        tk.Button(mnf, text='Save', command=self.save).grid(column = 0, row = 5, pady = 10, sticky='E')
        tk.Label(mnf, textvariable = self.status).grid(column=1, row=5, pady = 10, sticky='W')

    def select_file(self):
        filetypes = (
            ('png files', '*.png'),
            ('jpg files', '*.jpg'),
            ('jpeg files', '*.jpeg'), 
            ('gif files', '*.gif'),
            ('All files', '*.*')
        )
        filepath = fd.askopenfilename(
            title='Open a file',            
            filetypes=filetypes)
        self.path.set(filepath)
        self.path_short.set('...' + str(self.path.get())[-35:])
        self.status.set('')
        

    def save(self):

        img_path = self.path.get() #image preprocessing
        print(img_path)
        img = Image.open(img_path)
        img = img.convert("RGB") #flattens the transparency
        img = img.convert('RGBA') #adds it back in


        if self.optionpicked.get() == 0: #depends on the radiobutton
            out = self.greyscale(img)
        elif self.optionpicked.get() == 1:
            out = self.nohue(img)
        out = out.convert('RGBA')

        file = fd.asksaveasfile(mode='wb', defaultextension=".png", filetypes=(("PNG file", "*.png"),("All Files", "*.*") )) #image saving
        if file:
            out.save(file)
            self.status.set("Done!")
    
    def greyscale(self, img): 
        datas = img.getdata()        
        newData = []
        for item in datas:
            newData.append((0, 0, 0, 255-int((item[0] * 299/1000 + item[1] * 587/1000 + item[2] * 114/1000)))) #pixel conversion
        img.putdata(newData)
        return img
    def nohue(self, img):
        datas = img.getdata()        
        newData = []
        for item in datas:
            newData.append((0,0,0,255 - max(item[0], item[1], item[2]))) #pixel conversion, removes the color channels and creates a key 
        img.putdata(newData)
        return img

root = tk.Tk()
BnT(root)
root.mainloop()
