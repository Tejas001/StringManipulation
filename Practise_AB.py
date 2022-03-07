# Write a Python script that traverses through an input string and prints its characters
# str1 = input('Enter a string: ')
# for i in range(0,len(str1),2):
#     print(str1[i:i+2])

# Program to print
# print(input('..')+' trial'+' ooty'*3,end=' ')

# Program to print
# s = 'CARPE DIEM'
# n = len(s)//2
# print(s[:n])
# print(s[n:])
# print(s[n:n])
# print(s[1:n])
# print(s[n:(len(s)-1)])

# print("Hello World".upper( ).lower( ))
# print("Hello World".lower( ).upper( ))
# print("Hello World".find("Wor", 1, 6))
# print("Hello World".find("Wor"))
# print("Hello World".find("wor"))
# print("Hello World".isalpha( ))
# print("Hello World".isalnum( ))
# print("1234".isdigit( ))
# print("123FGH".isdigit( ))

# print(' Tejas '.strip())

# from curses.ascii import isdigit
# from itertools import count


# 's'.isdigit()
# 's'.find('s')
# 's'.capitalize()
# 's'.upper()
# 's'.isupper()
# 's'.rstrip()
# 's'.lstrip()

# txt = "banana,,,,,ssqqqww....."
# x = txt.rstrip(".wqs,")
# print(x)

# print(""" 
# 1
#     2
#         3""")

# text = "Test.\nNext line."
# print (text)

# y = str(123)
# x = "hello" * 3
# print (x, y)
# x = "hello" + "world"
# y = len(x)
# print (y, x)

# x = "hello" + \
# "to " + \
# "world"
# print(x)
# for char in x :
#     y = char
#     print (y, ' : ', end = ' ')

# theStr = " This is a test "         
# inputStr = input(" Enter integer: ")
# inputlnt = int(inputStr)            
# testStr = theStr
# while inputlnt >= 0 :               
#     testStr = testStr[1:-1]        
#     inputlnt = inputlnt - 1
# testBool = 't' in testStr
# print (theStr)             # Line 1 
# print (testStr)            # Line 2 
# print (inputlnt)           # Line 3 
# print (testBool)

# testStr = "abcdefghi"                    
# inputStr = input ("Enter integer:")      
# inputlnt = int(inputStr)                 
# count = 2                                
# newStr = ''                               
# while count <= inputlnt :                
#     newStr = newStr + testStr[0 : count]
#     testStr = testStr[2:]      #Line 1   
#     count = count + 1                    
# print (newStr)                 # Line 2
# print (testStr)                # Line 3  
# print (count)                  # Line 4  
# print (inputlnt)   

# in1Str = input(" Enter string of digits: ")
# in2Str = input(" Enter string of digits: ")

# if len(in1Str)>len(in2Str):
#     small = in2Str
#     large = in1Str
# else:
#     small = in1Str
#     large = in2Str
# newStr = ''
# for element in small:
#     result = int(element) + int(large[0])
#     newStr = newStr + str(result)
#     large = large[1:]
# print (len(newStr))      # Line 1
# print (newStr)           # Line 2
# print (large)            # Line 3
# print (small)            # Line 4

# s = input('Enter a string: ')
# rs = ' '
# for ch in s:
#     rs = ch+rs
#     # print(rs)
# print(s+rs)

