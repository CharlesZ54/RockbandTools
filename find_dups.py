import os

for i,filename in enumerate(os.listdir("./SZFE")):
    name = filename[13:]
    name2 = filename[14:]
    for i,filename2 in enumerate(os.listdir("./SZFE")):
        if filename2[13:] == name:
            print('break '+name)
        if filename2[13:] == name2:
            print('break2 '+name2)
