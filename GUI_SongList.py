import os,io,re,csv
from tkinter import *
from tkinter import filedialog
import tkinter.scrolledtext as tkst

window = Tk()
window.title("Rockband Song List")

var = IntVar()
var.set(0)

def rename(file_path):
    folder_num = 56
    for filename in sorted(os.listdir(file_path)):
        if filename.endswith("_meta") or filename.endswith("_song"):
            new_filename = str(folder_num).zfill(3) + "_" + hex(folder_num).split('x')[-1].zfill(8) + filename[12:]
            os.rename(file_path + filename, file_path + new_filename)
            text_str = "sZFE/" + str(folder_num).zfill(3)
            folder_num += 1

        if filename.endswith("_meta"):
            f1 = open(file_path + new_filename + "/content/songs/songs.dta","r")
            f2 = open(file_path + new_filename + "/content/songs/songs_new.dta","w")
            pattern = re.compile(r"sZFE/\d{3}")
            for line in f1:
                f2.write(re.sub(pattern,"sZFE/"+new_filename[:3],line))
            f1.close()
            f2.close()
            os.remove(file_path + new_filename + "/content/songs/songs.dta")
            os.rename(file_path + new_filename + "/content/songs/songs_new.dta",file_path + new_filename + "/content/songs/songs.dta")

def findDuplicates(list):
    names = {}
    for song in list:
        if song[0] in names:
            print("Found Duplicate of: " + song[0])
        names[song[0]] = song[1]

def display(file_path):
    list = listSongs(file_path)
    messages.config(state=NORMAL)
    messages.delete(1.0,END)
    for song in list:
        messages.insert(INSERT,song[0] + " by " + song[1] + "\n")
        # if var.get() == 1:
        #     with open('rockband_songs.csv', mode='a', newline='') as output_file:
        #         rockband_songs = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #         rockband_songs.writerow([song[0], song[1], song[2]])

    messages.config(state=DISABLED)

def listSongs(file_path):
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
    display(file_path)

def exportCSV(file_path):
    for song in listSongs(file_path):
        with open('rockband_songs.csv', mode='a', newline='') as output_file:
            rockband_songs = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            rockband_songs.writerow([song[0], song[1], song[2]])

# file_path='/home/charles/Documents/RockbandTools/SZFE/'
# findDuplicates(listSongs())

#Parent widget for buttons
btn = Button(window, text="Select a folder", command=selectfolder)
btn.grid(column=0, row=0)

btn2 = Button(window, text="Refresh", command= lambda: display(file_path))
btn2.grid(column=1, row=0)

box = Button(window, text="Export to CSV", command= lambda: exportCSV(file_path))
box.grid(column=2, row=0, padx=10, pady=10)

btn3 = Button(window, text="Rename", command= lambda:rename(file_path))
btn3.grid(column=0, row=1)

#Group1 Frame
window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

# Textbox
messages = tkst.ScrolledText(window, width=60, height=30)
messages.grid(row=2,column=0, sticky = E+W+N+S, columnspan=3)

mainloop()
