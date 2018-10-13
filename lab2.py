import xml.etree.ElementTree as etree
import re
from collections import OrderedDict
from itertools import izip, repeat

#2.1
def f(n):
    file = open('a.txt', 'r')
    output = file.readlines()[0:n]
    return output

print f(2)

#2.2
def f1():
    words = []

    with open("a.txt") as f:
        words = [word for line in f for word in line.split()]
    
    b1 = open('b1.txt', 'w')
    b2 = open('b2.txt', 'w')

    for i in range(0, len(words)):
        temp = words[i] + " "
        if i%2:
            b1.write(temp.upper())
        else:
            b2.write(temp.lower())
    return words

#2.3
def f2(wordsArr):
    words = etree.Element("words")
    wordsList = []
    for word in wordsArr:
        if word not in wordsList:
            wordsList.append(word)
            etree.SubElement(words, "word", name = word).text = str(wordsArr.count(word))
    tree = etree.ElementTree(words)
    tree.write("filename.xml")
    return wordsList

f2(f1())

#2.4
def f3():
    with open("a.txt", 'r') as f:
        wordsList = f.read().replace('\n', '')
    endings = []
    words = etree.Element("words")
    temp = re.findall(r'\B\w\w\w\b', wordsList)
    endings = list(OrderedDict(izip(temp, repeat(None))))
    for ending in endings:
        newEnding = etree.SubElement(words, "end", ending = ending)
        reg = "\w{1,}" + str(ending) + "\\b"
        wordsWithSameEnding = re.findall(reg, wordsList)
        for word in wordsWithSameEnding:
            etree.SubElement(newEnding, "word", word = word)
                
    tree = etree.ElementTree(words)
    tree.write("c.xml")

f3()