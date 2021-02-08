
"""
HOMEWORK #7 Dictionaries and Sets
My Favorite Song's Attributes

"""
# Using a loop to Print the key and value of each item in SongDictionary
SongDictionary = {"Artist Name": "Luther Vandross", "Song Title": "Dance with My Father",
                  "Genre": "R&B", "Lyricists": "Luther Vandross, Richard Marx", "Album Name": "Dance with My Father",
                  "Release Date": "5/30/2003", "Song Duration": "266 seconds", "Album Number": 14, "Record Label": "J Records",
                  "Producers": "Luther Vandross, Nat Adderley Jr."}

for key in SongDictionary:
    print(key, ": ", SongDictionary[key])

print()


# Guessing the value of any key in SongDictionary


def guessKeyValue(key, value):
    Val = SongDictionary[key]
    if value == Val:
        print("Your guessed was correct!")
    else:
        print("Your guess was wrong. Better luck next time!")


for ky in SongDictionary.keys():
    print(ky)
print()
print("You are to choose and guess the value of any of the attributes given above")
x = input("Pick and enter any attribute from the list above: ")
y = input("Guess and enter the value off the attribute you chose: ")

guessKeyValue(x, y)
