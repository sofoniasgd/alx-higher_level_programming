#!/usr/bin/python3
"""Advanced Task 13 module"""


def append_after(filename="", search_string="", new_string=""):
    """Defines a method that inserts aline of text to a file,
    after each line containing  a keyword
    Args:
        filename (str)
        search_string (str) string to be searched
        new_string (str) string to be inserted
    """

    lines_list = list()
    line = ""
    # open file for reading
    with open(filename, mode='r', encoding='utf-8') as f:
        # read line by line till end
        line = f.readline()
        while line != "":
            # append read line to lines_list and
            # find search-string in current line
            lines_list.append(line)
            if line.find(search_string) != -1:
                lines_list.append(new_string)
            # read next line
            line = f.readline()
        # end of file, write to file and exit
    with open(filename, mode='w', encoding='utf-8') as file_wr:
        file_wr.writelines(lines_list)
