# 1 (i) Write a python program to read contents of a file (filename as argument) 

import sys
import os
import functools

if(len(sys.argv) != 2):
	print ("Invalid Arguments")
	sys.exit()

if(not(os.path.exists(sys.argv[0]))):
	print ("Invalid File Path")
	sys.exit()

if(sys.argv[1].split('.')[-1] != "txt"):
	print ("Invalid File Format. Only TXT files allowed")
	sys.exit()

escape = open(sys.argv[1])

worddic = { }

# 1 (ii) Store number of occurrences of each word in a dictionary.

for line in escape: #Outer for loop - taking each line in the file 
 #print (line )
 myline = line.split()  #myline is a list containg the words split - space is delimiter 
 #print (myline)

 for word in myline: #Inner for-loop processing each line 
  w = worddic.get(word,0) #'0' is the default value put in the value part, in case the word is encountered for first time 
  #print ("key word %s exists in doctionary with %d value" %(word, w))
  
  worddic[word] = w + 1 #Incrementing the word count, if the word exists 
  #print (worddic[word] )
 
print ("\n Result of storing number of occurances of word in dictionary \n", worddic ,"\n ")

# 1 (iii) Display in descending order.

sortedlist = [ ]

sortedlist = sorted(worddic.items(), key = lambda Y : Y[1], reverse = True)
print ("\n Sorting in Dscending order of Value Occurance - frequency of word occurance \n", sortedlist)

# 1 (iv) Display ONLY the Top 10 sorted words - Descending Order - most frequency to least frequency
# 1 (v) Store the length of the Top 10 words in a list & display this list 

topten = []

print ("\n Top Ten Occuring Words \n")
for i in range(10): #Top 10 in range 
	try:
		wordTuple = sortedlist[i]
		topten.append(len(wordTuple[0]))
		print ("\n ", wordTuple[0], ", Frequency: " , wordTuple[1] , ", Length " , len(wordTuple[0]))
	except IndexError:
		print ("\n File has less than 10 words")
		break

print ("\n Lengths of 10 most frequently occuring words:")
print (topten)

# 1 (vi) Write a one-line reduce function to get the average length of the words in the Top Ten List

mysum = functools.reduce(lambda x, y: x + y, topten)
print ("Average length of Top Ten words: " , mysum/len(topten))

# 1 (Vii) Write a one-line list comprehension to display squares of all odd numbers in the Top Ten List
 
squares = [x**2 for x in topten if x%2 != 0]
print ("\n Squres of odd word lengths: ")
print (squares)
