import os,io,re,csv
from tkinter import *
from tkinter import filedialog
import tkinter.scrolledtext as tkst

window = Tk()
window.title("Rockband Song List")

file_path = ""
var = IntVar()
var.set(0)


def listsongs():
    messages.config(state=NORMAL)
    messages.delete(1.0,END)
    pattern_meta = re.compile(".{3}_.{8}_.*_meta")
    for i,filename in enumerate(os.listdir(file_path)):
        for match in re.finditer(pattern_meta,filename):
            regex = r"(name|artist)\s*'?\n?\s*(\"[^dlc].*\")"
            with open(file_path + filename + "\content\songs\songs.dta","r") as f:
                data = f.read().strip()
                matches = re.findall(regex, data, re.MULTILINE)
                title = str(matches[0])[10:-2]
                title = title.replace("\\\'","'")
                artist = str(matches[1])[12:-2]
                artist = artist.replace("\\\'","'")
                messages.insert(INSERT,title + " by " + artist + "\n")
                if var.get() == 1:
                    with open('rockband_songs.csv', mode='a', newline='') as output_file:
                        rockband_songs = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        rockband_songs.writerow([artist, title])
    messages.config(state=DISABLED)


def selectfolder():
    global file_path
    file_path = filedialog.askdirectory()+"/"
    btn.configure(text=file_path)


# Parent widget for buttons
btn = Button(window, text="Select a folder", command=selectfolder)
btn.grid(column=0, row=0)

btn2 = Button(window, text="List songs", command=listsongs)
btn2.grid(column=1, row=0)

box = Checkbutton(window, text="Export to CSV", variable=var)
box.grid(column=2, row=0, padx=10, pady=10)

#Group1 Frame
window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)


# Textbox
messages = tkst.ScrolledText(window, width=60, height=30)
messages.grid(row=1,column=0, sticky = E+W+N+S, columnspan=3)

mainloop()
