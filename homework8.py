import os
# import os.path
from os import path
'''
HOMEWORK #8:
Create a note-taking program. When a user starts it up, it should prompt them for a filename.
If they enter a file name that doesn't exist, it should prompt them to enter the text they want to write to the file.
After they enter the text, it should save the file and exit.
If they enter a file name that already exists, it should ask the user if they want:

A) Read the file

B) Delete the file and start over

C) Append the file
'''


# Notebook as existing file. For testing code
with open("Notebook.txt", "w") as existingFile:
    for i in range(5):
        notes = "This is a note for existing filename\n"
        existingFile.write(notes)


def Notes():
    Filename = input("Please enter the filename: ")
    if path.exists("{}.txt".format(Filename)):  # Do if filename already exists
        print("The filename already exists. What what you like to do with this file?")
        option = input(
            "Enter 'r' to read, 'd' to delete, 'a' to append to file \n or 's' to replace a line in the file: ")
        if option == "r":  # if user wants to read from existing file
            with open("{}.txt".format(Filename), "r") as NoteFile:
                print(NoteFile.read())
        elif option == "a":  # If user wants to append new notes
            with open("{}.txt".format(Filename), "a") as NoteFile:
                notesTaken = input(
                    "Type your notes and hit enter when done: \n")
                NoteFile.write("\n" + notesTaken)
            with open("{}.txt".format(Filename), "r") as NoteFile:
                print(NoteFile.read())
        elif option == "s":  # replacing a single line
            with open("{}.txt".format(Filename), "r") as NoteFile:
                lineNum = int(
                    input("Please enter line number you want to replace: "))
                notesTaken = input(
                    "Type your notes and hit enter when done: \n")
                NoteFileList = NoteFile.readlines()
                NoteFileList[lineNum] = notesTaken + "\n"
            with open("{}.txt".format(Filename), "w") as NoteFile:
                for List in NoteFileList:
                    NoteFile.write(List)
            with open("{}.txt".format(Filename), "r") as NoteFile:
                print(NoteFile.read())
        elif option == "d":  # if user wants to delete existing file
            os.remove("{}.txt".format(Filename))
            Notes()
    else:  # Do if filename does not exist
        with open("{}.txt".format(Filename), "w") as NoteFile:
            notesTaken = input("Type your notes and hit enter when done: \n")
            NoteFile.write(notesTaken)
        with open("{}.txt".format(Filename), "r") as NoteFile:
            print(NoteFile.read())


Notes()
