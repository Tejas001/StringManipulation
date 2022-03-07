# a = 'Friday'
# for i in a:
#     print(i,'-',end='')

# str1=''
# print(str1.join(['a','b','c','d']))

# Program to reverse the string
# str1 = input('Enter string: ')
# length = len(str1)
# print(length)
# # for i in range(-1,(-length-1),-1):
# #     print(str1[i])
# for i in range(length-1,0-1,-1):
#     print(str1[i])

# print(3*'go!')
# print('go!'*3)

# print('a' in 'Tejas')
# print('a' not in 'Tejas')

# print('a' == 'A')
# print('a' == 'a')
# print('a' != 'A')

# str1='Amazon'
# print(str1[-7:])
# print(str1[::-1])
# print(str1[0:1])
# print(str1[:3]+str1[3:6],end='')

# a = '#'
# for i in range(1,5):
#     print(a*i)

# print('tejas'.capitalize())
# print('tejas'.lower())
# print('tejas'.upper())
# print('tejas'.find('jas'))
# print('  tejas '.strip())
# print('  tejas '.lstrip())
# print('  tejas '.rstrip())
# print('   '.isspace())
# print(('  tejas123 '.strip()).isalnum())
# print('tejas'.strip('jas'))
# print('tejas'.lstrip('te'))
# print('tejas'.rstrip('jas'))

# Program for string content check
# string = input('Enter a sentence or string: ')
# uppercase_count = 0
# lowercase_count = 0
# alphabet_count = 0
# digits_count = 0
# for i in string:
#     if i >= 'A' and i <= 'Z':
#         uppercase_count += 1
#     elif i >= 'a' and i <= 'z':
#         lowercase_count += 1
#     elif ord(i) >= 48 and ord(i) <= 57:
#         digits_count += 1
# alphabet_count = uppercase_count + lowercase_count
# for i in string:
#     if i.isupper():
#        uppercase_count += 1
#     elif i.islower():
#        lowercase_count += 1
#     elif i.isdigit():
#        digits_count += 1
#     if i.isalpha():
#        alphabet_count += 1
# print('uppercase_count',uppercase_count)
# print('lowercase_count',lowercase_count)
# print('alphabet_count',alphabet_count)
# print('digits_count',digits_count)

# Program to print no of occurence of substring into string
# string = input('Enter line or string: ')
# substring = input('Enter substring which need to be found: ')
# start =0
# length_string = len(string)
# length_substring = len(substring) 
# frequency_count = 0
# while True:
#     part = string.find(substring,start,length_string)
#     if part > -1:
#         frequency_count += 1
#         start = part+length_substring
#     else:
#         break
#     if start >= length_string:
#         break
# print(f'Substring {substring} occurred in string for {frequency_count} time')

# Program to check string is palindrome or not
# string = input('Enter a string: ')
# mid = len(string)/2
# a = 0
# rev = -1
# for i in range(int(mid)):
#     if string[a] == string[rev]:
#         a += 1
#         rev -= 1
#     else:
#         print('Not Palindrome',string)
#         break
# else:
#     print('Palindrome',string)

# Program print every other letter in string as capital
# string = input('Enter a string: ')
# length = len(string)
# string1 = ''
# for i in range(0,length,2):
#     string1 += string[i].lower()
#     if i < (length-1):
#         string1 += string[i+1].upper()
# print(f'Alternative Capitalized String: {string1}')

# for i in range(0,length):
#     if i%2!=0:
#         string1 += string[i].lower()
#     elif i%2==0:
#         string1 += string[i].upper()
# print(f'Alternative Capitalized String: {string1}')

# email = input('Enter your email address: ')
# substring = '@gmail.com'
# if substring in email:
#     print(f'It is a valid email: {email}')
# else:
#     print(f'This email is from other domain {email}')