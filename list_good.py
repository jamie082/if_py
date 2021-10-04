#!/usr/bin/python3

names = [] # list
outF = open("myOutFile.txt", "w")

total = 0
p = '\n'
char_count = "Char count: "
lines_of_text = 1

def findLength (str): # total characters of word
    counter = 0
    counter_total = 0
    for p in str:
        counter += 1 # each word
    return counter

def strTotal (str): # total characters in 3 words
    counter = 0
    counter_total = 0
    for p in str: 
        counter = findLength(str)
        counter_total += counter
    return counter_total

for number in range (1, 4):
    scan_input = input ("Enter line: ")
    names.append(f"name: {scan_input}")
    outF.write (p)
    outF.write(scan_input)
    outF.write(p)
    outF.write ("Char count: ")
    lines_of_text += 1
    print (" ", scan_input, findLength (scan_input))

print ("How many lines of text: ", lines_of_text - 1)
print ("How many characters of text (total chars): ", strTotal (scan_input)) # total characters
