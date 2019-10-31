This is a project for EE551: Engineering Programming Python

This project will include a series of tools to be used with RockBand 3 for Wii. (I realize this is a niche application, so I will explain what this will entail.)

Background:
  It is possible to play custom songs on Rockband 3 for Wii, but there are several tedious steps that must be done manually for each song in order to be recognized by the software on the Wii. My goal is to automate the process for a batch of songs, with error checking.
  1. Songs must be contained in folders in the following format: 000_00000000_{song_name}_song

  ![Folder Format](./images/format.png)

  2. Song folders must contain a file in which it contains the full file path of the song, among other information

  ![File Format](./images/file.png)

  3. Songs must be copied to an external drive to be read by the Wii

My goal in this project includes several functions:
  1. It will edit files and file names in order to be read by the Wii's file system
  2. It will check for duplicate songs
  3. It will automatically copy these files to an external USB device
  4. It will automatically convert filetypes to be read by the Wii
  5. It will be able to list all songs installed and sort (by name, artist, track length, etc.)
  6. It will have both a GUI and a CLI to achieve these functions (written either in PyQt or Tkinter)
