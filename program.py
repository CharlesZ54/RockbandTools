import os,io,re,csv
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.scrolledtext as tkst
from shutil import copytree

def rename(file_path,backup=None): #Renames folders and line in song.dta files
    if __name__ == "__main__": #If executed as main program
        result = messagebox.askyesnocancel("Are you sure?", "Do you want to make a backup of your files before editing? Press Yes to backup, No to overwrite.")
        if result == None:
            messagebox.showinfo("Cancelled", "Operation Cancelled")
            return
        elif result == True:
            copytree(file_path,os.path.join(file_path,"old"))
    else: #If executed from another program
        if backup == None:
            result = input("Do you want to create a backup of your files before editing?")
            if result.lower().startswith("n"):
                print("Operation Cancelled")
            elif result.lower().startswith("y"):
                copytree(file_path,os.path.join(file_path,"old"))
            else:
                print("Unknown entry. Please type 'y' or 'n'.")
                return
        else:
            pass

    folder_num = 56 #Initial folder number
    for filename in sorted(os.listdir(file_path)): #Edit folder name
        if filename.endswith("_meta") or filename.endswith("_song"):
            new_filename = str(folder_num).zfill(3) + "_" + hex(folder_num).split('x')[-1].zfill(8) + filename[12:] #Creates new folder name from existing information
            os.rename(file_path + filename, file_path + new_filename)
            text_str = "sZFE/" + str(folder_num).zfill(3)
            folder_num += 1

        if filename.endswith("_meta"): #Edit line in file
            f1 = open(file_path + new_filename + "/content/songs/songs.dta","r")
            f2 = open(file_path + new_filename + "/content/songs/songs_new.dta","w")
            pattern = re.compile(r"sZFE/\d{3}")
            for line in f1:
                f2.write(re.sub(pattern,"sZFE/"+new_filename[:3],line))
            f1.close()
            f2.close()
            os.remove(file_path + new_filename + "/content/songs/songs.dta")
            os.rename(file_path + new_filename + "/content/songs/songs_new.dta",file_path + new_filename + "/content/songs/songs.dta")

def findDuplicates(list): #Find duplicate songs in folder
    names = {}
    duplicates = []
    for song in list:
        if song[0] in names:
            duplicates.append(song[0])
        names[song[0]] = song[1]
    if __name__ == "__main__":
        messages.config(state=NORMAL)
        messages.delete(1.0,END)
        for song in duplicates:
            messages.insert(INSERT,"Found Duplicate of: " + song + "\n")
        messages.config(state=DISABLED)

    return(duplicates)

def display(file_path): #Sends songs and artist names to GUI or CLI
    if __name__ == "__main__":
        messages.config(state=NORMAL)
        messages.delete(1.0,END)
        for song in listSongs(file_path):
            messages.insert(INSERT,song[0] + " by " + song[1] + "\n")
        messages.config(state=DISABLED)
    else:
        lines = []
        for song in listSongs(file_path):
            if __name__ == "__main__":
                print("* " + song[0] + " by " + song[1] + "\n")
            lines.append(song[0])
        return(lines)

def listSongs(file_path): #Creates a list of songs in folder
    song_list = []
    pattern_meta = re.compile(".{3}_.{8}_.*_meta")
    regex = r"(name|artist|album_name)\s*'?\n?\s*(\"[^dlc].*\")"
    for i,filename in enumerate(os.listdir(file_path)):
        for match in re.finditer(pattern_meta,filename):
            with open(os.path.join(file_path + filename) + "/content/songs/songs.dta","r") as f:
                data = f.read().strip()
                matches = re.findall(regex, data, re.MULTILINE)
                song_list.append([matches[0][1][1:-1],matches[1][1][1:-1],matches[2][1][1:-1]])
    return song_list

def selectFolder(): #PRompts user to select a folder
    global file_path
    if __name__ == "__main__":
        file_path = filedialog.askdirectory()+"/"
        btn.configure(text=file_path)
        display(file_path)
    else:
        file_path = input("Enter the folder path: ")
    return file_path


def exportCSV(file_path): #Export song,artist,album into CSV format
    for song in listSongs(file_path):
        with open('rockband_songs.csv', mode='a', newline='') as output_file:
            rockband_songs = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            rockband_songs.writerow([song[0], song[1], song[2]])
    print(os.path.isfile(os.getcwd() + "/rockband_songs.csv"))
    print(os.getcwd())
    if os.path.isfile(os.getcwd() + "/rockband_songs.csv")==True: #Check to make sure operation was successful
        if __name__ == "__main__":
            messagebox.showinfo("Success", "File saved to " + os.getcwd() + "/rockband_songs.csv")
        else:
            print("Success! File saved to" + os.getcwd() + "/rockband_songs.csv")
    else: #If error
        if __name__ == "__main__":
            messagebox.showerror("Error", "Unable to create file")
        else:
            print("Error, unable to create file")

def copySongs(src,dst=None): #Copy songs to a user specified directory
    if __name__ == "__main__":
        export_path = filedialog.askdirectory()+"/"
    elif dst == None:
        export_path = input("Enter the folder path: ")
    else:
        export_path = dst
    copytree(src,os.path.join(export_path,"export"))

if __name__ == "__main__": #Creates GUI if run as its own program
    window = Tk()
    window.title("Rockband Song List")
    var = IntVar()
    var.set(0)
    
    #Parent widget for buttons
    btn = Button(window, text="Select a folder", command=selectFolder)
    btn.grid(column=0, row=0, sticky = E+W+N+S)

    btn2 = Button(window, text="Refresh", command= lambda: display(file_path))
    btn2.grid(column=3, row=0, sticky = E+W+N+S)

    box = Button(window, text="Export to CSV", command= lambda: exportCSV(file_path))
    box.grid(column=3, row=2, sticky = E+W+N+S)

    btn3 = Button(window, text="Rename", command= lambda:rename(file_path))
    btn3.grid(column=3, row=3, sticky = E+W+N+S)

    btn4 = Button(window, text="Copy to folder", command= lambda:copySongs(file_path))
    btn4.grid(column=3,row=4, sticky = E+W+N+S)

    btn5 = Button(window, text="Check for Duplicates", command= lambda:findDuplicates(listSongs(file_path)))
    btn5.grid(column=3,row=5,sticky = E+W+N+S)

    #Group1 Frame
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    # Textbox
    messages = tkst.ScrolledText(window, width=60, height=30)
    messages.grid(row=2,column=0, sticky = E+W+N+S, columnspan=1, rowspan=4)

    mainloop()
