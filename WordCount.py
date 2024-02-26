# Andrew Pham
# 2765261

import sys
from collections import Counter

def wordCounter(file):
    wordArray = Counter()
    with open(file, 'r', encoding = 'utf-8') as file:
        #https://www.geeksforgeeks.org/python-program-to-read-file-word-by-word/#
        for line in file: # go through each line
            for word in line.split(): # go through each word, ignoring spoces and tabs
        #geeksforgeeks
                word = word.lower() # if word is uppercase, make it lowercase
                if word in wordArray: # if word is in array add 1
                    wordArray[word] += 1
                else: # if word isn't in array set to 1
                    wordArray[word] = 1
    return wordArray

def printCount(wordCount):
    sortedCount = sorted(wordCount.items(), key=lambda x: x[1], reverse=True)
    # sorts by second element of each tuple, reverse= true ensures descending order in list
    for word, count in sortedCount:  # connects each word with their count
        print(word + ": " + str(count))

def main():
    file = sys.argv[1]
    wordCount = wordCounter(file)
    printCount(wordCount)

if __name__ == "__main__":
    main()