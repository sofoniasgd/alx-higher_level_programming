#!/usr/bin/python3
"""Text Indentation module."""


def text_indentation(text=""):
    """Prints new lines when it encounters specific characters.

    Delimiting characters: ".", "?", ":"
    Args:
        text (str): input string
    raises:
        TypeError: when text is not a string
    """

    if text == "" or (not isinstance(text, str)):
        raise TypeError('text must be a string')
    # split text into separate strings and store in a list
    i, start = 0, 0
    textlist = []
    while i < len(text):
        # find occurence of characters, skip if end of string reached
        if text[i] in ".?:":
            textlist.append(text[start:(i+1)])
            start = i + 1
        # end of text and no delimiter at end
        elif i == (len(text) - 1):
            textlist.append(text[start:])
        i += 1
    # print("number of sentences=> {}".format(len(textlist)))
    # remove white space from front of segment
    index = 0
    for sentence in textlist:
        i, rem = 0, 0
        while i < len(sentence):
            if sentence[i] == " ":
                rem += 1
            else:
                break
            i += 1
        if rem > 0:
            textlist[index] = sentence[rem:]
        index += 1
    # Remove white space before text
    for i in textlist:
        if i[-1:] == "\n":
            print(i)
        else:
            print(i, end="")
