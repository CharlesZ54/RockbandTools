import os,shutil

for i,filename in enumerate(os.listdir("E:\Dropbox\Projects\Wii Shit\C2GS Library")):
    name = filename[13:]
    name2 = filename[14:]
    for i,filename2 in enumerate(os.listdir("E:\Dropbox\Projects\Wii Shit\sZFE")):
        if filename2[13:] == name:
            print(filename)
        if filename2[13:] == name2:
            print(filename)


