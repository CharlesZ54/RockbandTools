import os,io

file_path = os.getcwd()
#num_folders = len(os.walk(file_path).next()[1])
#folder_num = raw_input("What number should I start with? ")
folder_num = 56

for i,filename in enumerate(os.listdir(file_path)):
   if filename.startswith("000_"):
      new_filename = str(folder_num).zfill(3) + "_" + hex(folder_num).split('x')[-1].zfill(8) + filename[12:]
      os.rename(filename, new_filename)
      text_str = "sZFE/" + str(folder_num).zfill(3)
      folder_num += 1

   if filename.endswith("_meta"):
      f1 = open(new_filename + "/content/songs/songs.dta","r")
      f2 = open(new_filename + "/content/songs/songs_new.dta","w")
      for line in f1:
         f2.write(line.replace("sZAE/000",text_str))
      f1.close()
      f2.close()
      os.remove(new_filename + "/content/songs/songs.dta")
      os.rename(new_filename + "/content/songs/songs_new.dta",new_filename + "/content/songs/songs.dta")
