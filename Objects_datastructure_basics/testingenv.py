#Testing for all modules under Objects and data structure basic

#indexing
x = "testing"
#Grabbing the first letter indexing the first letter
print(x[0])
#Grabbing the last letter in the string without knowing how long the length of the string is
print(x[-1])
#Indexing the 3rd element of the string which should output the t
print(x[3])

#SLICING 
#slicing from the 3rd element to the end
print(x[3:])
#slicing from the start to the 5th elements but not including the 5th element
print(x[:5])
#slicing a range 
print(x[2:5])

#STEP SIZE
#we can choose how many elements we want to step by 
#this is slicing through all elements 
#Output would be TSIG with our string being "testing"
print(x[::2])
#Python trick to reverse a string instead of creating a loop
#output: gnitset
print(x[::-1])

print(x.upper())

y = "This is a test string"

print(y.split())