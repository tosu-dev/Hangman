

# _____VAR_____
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

listWords = []
with open('mots.txt', 'r') as wordFile:
    for mot in wordFile.readlines():
        if mot[-1] == '\n':
            mot = mot[:-1]
        listWords.append(mot)




trashLetter =  []

maxLives = 6
lives = maxLives

draws = [
    """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """
        ,
    """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """
]
