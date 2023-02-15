#!/usr/bin/python3
import sys
from os.path import exists

"""A markdown to html file
    Args:
        Arg 1: Markdown file
        Arg 2: output file name (HTML)
    """

markdownHeader = {'#': '<h1> </h1>', '##': '<h2> </h2>', '###': '<h3> </h3>',
                  '####': '<h4> </h4>', '#####': '<h5> </h5>', '######': '<h6> </h6>'}

markdownList = {'-': '<li> </li>', '*': '<li> </li>'}

if __name__ == '__main__':

    """Check if number of arguments == 2"""

    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    """Check if input file is a correct markdown file"""
    if "." in sys.argv[1]:
        newArr = sys.argv[1].split('.')
        if len(newArr) != 2:
            sys.stderr.write('Bad Markdown file\n')
            exit(1)
        if newArr[1] != "md":
            sys.stderr.write('First argument must a markdown file\n')

    """Check if markdown file exist"""
    if exists(sys.argv[1]) == False:
        sys.stderr.write('Missing {}\n'.format(sys.argv[1]))
        exit(1)

    """Opening the markdown file for file operations"""
    ulCount = 0
    with open(sys.argv[1]) as markdown:
        line = True

        while line:
            line = markdown.readline()
            if line.startswith('#'):  # Headings operation
                hash = line.split(' ')[0]

                with open(sys.argv[2], 'a') as htmlFile:
                    hashL = len(hash) + 1
                    htmlFile.write('{}{}{}\n'.format(
                        markdownHeader[hash].split(' ')[0], line[hashL: -1], markdownHeader[hash].split(' ')[1]))

            if line.startswith('-'):  # Unordered list operation
                with open(sys.argv[2], 'a') as htmlFile:
                    if ulCount == 0:
                        htmlFile.write('<ul>\n')
                    else:
                        htmlFile.write('\t{}{}{}\n'.format(
                            markdownList['-'].split(' ')[0], line[2: -1], markdownList['-'].split(' ')[1]))
                    ulCount += 1

            else:
                with open(sys.argv[2], 'a') as htmlFile:
                    htmlFile.write(line)

    exit(0)
