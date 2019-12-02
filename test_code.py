import pytest
from program import *
import os
import shutil

def test_findDuplicates():
    expected = ['Hotel California']
    result = findDuplicates(listSongs("./sZFE/"))
    assert result == expected

def test_display():
    expected = ['Goodbye Blue Sky', 'Hotel California', 'Hotel California', 'Fluttering Romance', 'Born to Run']
    result = display("./sZFE/")
    assert result == expected

def test_listSongs():
    expected = [['Goodbye Blue Sky', 'Pink Floyd', 'The Wall'], ['Hotel California', 'The Eagles', 'Hotel California'], ['Hotel California', 'The Eagles', 'Hotel California'], ['Fluttering Romance', 'Nightmare Lyre', 'The Rainbow Colored Album'], ['Born to Run', 'Bruce Springsteen', 'Born To Run']]
    result = listSongs("./sZFE/")
    assert result == expected

def test_exportCSV():
    exportCSV("./sZFE/")
    result = os.path.isfile(os.getcwd() + "/rockband_songs.csv")
    assert result == TRUE

def test_copySongs():
    copySongs("./sZFE/",os.getcwd())
    assert os.path.isdir("export") == TRUE
    assert os.path.isdir("export/052_00000034_nlfr_meta") == TRUE

def test_rename():
    rename("export/",1)
    assert os.path.isdir("export/056_00000038_nlfr_meta") == TRUE
    f1 = open("export/056_00000038_nlfr_meta/content/songs/songs.dta")
    for i,line in enumerate(f1):
        if i == 15:
            result = line

    assert result == '         "dlc/sZFE/056/content/songs/nlfr/nlfr"\n'
    f1.close()

def test_cleanup():
    shutil.rmtree("export")
    os.remove("rockband_songs.csv")
