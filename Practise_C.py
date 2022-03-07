# phone_num = input('Enter your phone number: ')
# str1=''
# for i in range(0,len(phone_num)):
#     # str1 = str1 + phone_num[i]
#     if len(str1)==3:
#         str1 = str1 + '-' + phone_num[i]
#     elif len(str1)==7:
#         str1 = str1 + '-' + phone_num[i]
#     else:
#         str1 = str1+phone_num[i]

# print(str1)

# Program to extract digits from string
# str1 = input('Enter a String: ') 
# str2 = ''
# digit = ''
# sum = 0
# for i in str1:
#     if i.isdigit() == False:
#         str2 = str2+i
#     elif i.isdigit() == True:
#         digit += i
#         sum += int(i)
# if len(digit) == 0:
#     print(f'The original string is {str1} and it has no digit')
# else:
#     print(f'The original string is {str1}, alphabet are {str2}, digits are {digit} and its sum {sum}')

# Program to print original sentence and stats 
# str1 = input('Enter a sentence: ')
# words = [w for w in str1.split()]
# words_len = len(words)
# no_of_alnum = 0

# for i in str1:
#     if i.isalnum():
#         no_of_alnum += 1

# alnum_percent = (no_of_alnum/len(str1)) * 100

# print('Number of words: ',words_len)
# print('No of characters: ',(len(str1)+1))
# print('Alphanumeric Percentage: ',alnum_percent)

# Program to print string
# while True:
#     str1 = input('Enter a sentence or (q/Q) to quit: ')
#     str2 = ''
#     if (str1 == 'q') or (str1 == 'Q'):
#         print('Byee')
#         break
#     for s in str1:
#         if s.isupper():
#             str2 = str2 + s.lower()
#         elif s.islower():
#             str2 = str2 + s.upper()
#         else:
#             str2 = str2 + s
#     print(f'Orignal Sentence is: {str1}')
#     print(f'Converted Sentence is: {str2}')

# Program to extract digit and print sum of input integer and extracted integer
# str1 = input('Enter a string: ') 
# int1 = int(input('Enter an integer: '))
# ext_digit = ''
# sum = 0
# if str1.isalnum == False:
#     ext_digit = 0
#     sum = int1 + int(ext_digit)
#     print(f'For input {int1}, {str1} -> {int1} + {ext_digit} = {sum}')
# else:
#     for s in str1:
#         if s.isdigit():
#             ext_digit += s
    
#     sum = int1 + int(ext_digit)
#     print(f'For input {int1}, {str1} -> {int1} + {ext_digit} = {sum}')

# Program to print in following format
# from os import sep
# str1 = input('Enter first string: ')
# str2 = input('Enter second string: ')

# small = str1
# large = str2
# if len(small) > len(large):
#     small = str2
#     large = str1
#     print(small)
# else:
#     print('Both has same length')

# for i in range((len(large)//2)):
#     print(' '*i,large[i],' '*(len(large)-2*i),large[len(large)-i-1],sep='')
from os import sep


n=6

# for i in range(n):
#     atoz=65
#     for j in range(i):
#         print(chr(atoz),end='')
#         atoz += 1
#     print()

# Program to convert integer into roman number
# n = int(input("Enter the number: "))
# num = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
# rom = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')

# result = ''

# for i in range(len(num)) :
#     count = int(n / num[i])
#     result += str(rom[i] * count)
#     n -= num[i] * count

# print(result)

