#!/usr/bin/python3
"""Text Indentation module."""


def text_indentation(text):
    """Prints new lines when it encounters specific characters.
    
    Delimiting characters: ".", "?", ":"
    Args:
        text (str): input string
    raises:

    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    # split text into separate strings and store in a list
    i, start = 0, 0
    textlist = []
    while i < len(text):
        #find occurence of characters
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            textlist.append(text[start:(i+1)])
            start = i + 1
        #end of text and no delimiter at end
        if i == (len(text) - 1):
            textlist.append(text[start:])
        i += 1
    print("number of sentences=> {}".format(len(textlist)))
    # Remove white space before text
    for i in textlist:

        print("{}".format(i))
        print()
