#!/usr/bin/python3

names = [] # list
outF = open("myOutFile.txt", "w")

total = 0
p = '\n'
lines_of_text = 1

def findLength_2 (word:str) -> int:
    return len(word)
'''
def findLength (word): # total characters of word
    counter = 0
    counter_total = 0
    for p in word:
        counter += 1 # each word
    return counter

def strTotal (word): # total characters in 3 words
    counter = 0
    counter_total = 0
    for p in word: 
        counter_total += findLength ()
    return counter_total
    '''

for number in range (1, 4):
    scan_input = input ("Enter line: ")
    names.append(f"name: {scan_input}")
    outF.write (p)
    outF.write(scan_input)
    outF.write(p)
    outF.write ("Char count: ")
    lines_of_text += 1
    print (" ", scan_input, findLength_2 (scan_input))
outF.close () # close buffer

print ("How many lines of text: ", lines_of_text - 1)
print ("How many characters of text (total chars): ", findLength_2 (scan_input)) # total characters
