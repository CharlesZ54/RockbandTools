import os,io,re,csv
from tkinter import *
from tkinter import filedialog
import tkinter.scrolledtext as tkst

window = Tk()
window.title("Rockband Song List")

file_path = ""
var = IntVar()
var.set(0)

def display():
    list = listsongs()
    messages.config(state=NORMAL)
    messages.delete(1.0,END)
    for song in list:
        messages.insert(INSERT,song[0] + " by " + song[1] + "\n")
        if var.get() == 1:
            with open('rockband_songs.csv', mode='a', newline='') as output_file:
                rockband_songs = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                rockband_songs.writerow([song[0], song[1], song[2]])

    messages.config(state=DISABLED)

def listsongs():
    song_list = []
    pattern_meta = re.compile(".{3}_.{8}_.*_meta")
    for i,filename in enumerate(os.listdir(file_path)):
        for match in re.finditer(pattern_meta,filename):
            regex = r"(name|artist|album_name)\s*'?\n?\s*(\"[^dlc].*\")"
            with open(file_path + filename + "/content/songs/songs.dta","r") as f:
                data = f.read().strip()
                matches = re.findall(regex, data, re.MULTILINE)
                song_list.append([matches[0][1][1:-1],matches[1][1][1:-1],matches[2][1][1:-1]])
    return song_list

def selectfolder():
    global file_path
    file_path = filedialog.askdirectory()+"/"
    btn.configure(text=file_path)

#Parent widget for buttons
btn = Button(window, text="Select a folder", command=selectfolder)
btn.grid(column=0, row=0)

btn2 = Button(window, text="List songs", command=display)
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
