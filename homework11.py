'''
HOMEWORK #11: Error Handling
Creating a note-taking program that prompts for a filename at startup and
performs error handling when a user enters a filename that already exist,
by prompting them to enter a different filename
After they enter the text, it should save the file and exit.
If they enter a file name that already exists, it should ask the user if they want:
'''
import os


def Notes(File):
    global Filename
    try:
        with open("{}.txt".format(File), "x") as NoteFile:
            notesTaken = input("Type your notes and hit enter when done: \n")
            NoteFile.write(notesTaken)
        with open("{}.txt".format(File), "r") as NoteFile:
            print(NoteFile.read())
    except FileExistsError as fne:
        print(fne, "\n", f"A file with filename {Filename} already exists")
        option = input(
            "Enter 'r' to read from existing file,\nEnter 'd' to delete the file,\nEnter 'a' to append to the file \nEnter 's' to replace a line in the file:\n ")
        if option == "r":  # if user wants to read from existing file
            with open("{}.txt".format(File), "r") as NoteFile:
                print(NoteFile.read())
        elif option == "a":  # If user wants to append new notes
            with open("{}.txt".format(File), "a") as NoteFile:
                notesTaken = input(
                    "Type your notes and hit enter when done: \n")
                NoteFile.write("\n" + notesTaken)
            with open("{}.txt".format(File), "r") as NoteFile:
                print(NoteFile.read())
        elif option == "s":  # replacing a single line
            with open("{}.txt".format(File), "r") as NoteFile:
                lineNum = int(
                    input("Please enter line number you want to replace: "))
                notesTaken = input(
                    "Type your notes and hit enter when done: \n")
                NoteFileList = NoteFile.readlines()
                NoteFileList[lineNum] = notesTaken + "\n"
            with open("{}.txt".format(File), "w") as NoteFile:
                for List in NoteFileList:
                    NoteFile.write(List)
        elif option == "d":  # if user wants to delete existing file
            os.remove("{}.txt".format(File))
            Filename = input("Please enter the filename: ")
            if len(Filename) > 0:
                Notes(Filename)
    except FileNotFoundError as fne:
        print(fne, "\n", "Please avoid using special characters in filename")
        Filename = input("Please enter the filename: ")
        if len(Filename) > 0:
            Notes(Filename)
    except OSError as ose:
        print("Something is wrong with the filename you entered \n", ose)
        Filename = input("Please enter the filename: ")
        if len(Filename) > 0:
            Notes(Filename)
    except NameError as ne:
        print(ne, "Please enter correct file extension")
        Filename = input("Please enter the filename: ")
        if len(Filename) > 0:
            Notes(Filename)
    finally:
        Filename.close()


Filename = input("Please enter the filename: ")
Notes(Filename)
