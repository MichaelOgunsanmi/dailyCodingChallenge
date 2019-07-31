# # #
# # # def Solution(endvalue):
# # #     for number in range(1,endvalue + 1):
# # #         if number%3 == 0 and number%5 == 0:
# # #             print('FizzBuzz')
# # #         elif number%3 == 0:
# # #             print('Fizz')
# # #         elif number%5 == 0:
# # #             print('Buzz')
# # #         else:
# # #             print(number)
# # #
# # # # Driver code
# # # test = Solution(100)
# # #
# # # print(test)
# #
# #
# # # def solution(value):
# # #     max == 0
# # #     while value != 0:
# # #         new_max = max + value
# # #         if max
# #
# # #
# # # #!/bin/python3
# # #
# # # import math
# # # import os
# # # import random
# # # import re
# # # import sys
# # #
# #
# #
# # # #!/bin/python3
# # #
# # # import math
# # # import os
# # # import random
# # # import re
# # # import sys
# # #
# # #
# # #
# # # # # Complete the charityAllocation function below.
# # # def charityAllocation(profits):
# # #     Charity_A = 0
# # #     Charity_B = 0
# # #     Charity_C = 0
# # #
# # #     for profit in profits:
# # #         print(profit)
# # #         if Charity_A <= Charity_B and Charity_A <= Charity_C:
# # #             Charity_A = Charity_A + profit
# # #             print('A')
# # #
# # #         elif Charity_B <= Charity_C:
# # #             Charity_B = Charity_B + profit
# # #             print('B')
# # #         else:
# # #             Charity_C = Charity_C + profit
# # #             print('C')
# # #
# # # charityAllocation([8,25,8,2,35,15,120,55,42])
# # # # if __name__ == '__main__':
# # # #     fptr = open(os.environ['OUTPUT_PATH'], 'w')
# # # #
# # # #     profits_count = int(input().strip())
# # # #
# # # #     profits = []
# # # #
# # # #     for _ in range(profits_count):
# # # #         profits_item = float(input().strip())
# # # #         profits.append(profits_item)
# # # #
# # # #     res = charityAllocation(profits)
# # # #
# # # #     fptr.write('\n'.join(res))
# # # #     fptr.write('\n')
# # # #
# # # #     fptr.close()
# # # #
# #
# #
# # #!/bin/python3
# #
# # import math
# # import os
# # import random
# # import re
# # import sys
# #
# #
# #
# # # # Complete the charityAllocation function below.
# # def charityAllocation(profits):
# #     Charity_A = 0
# #     Charity_B = 0
# #     Charity_C = 0
# #     output = list()
# #
# #     for profit in profits:
# #         if Charity_A <= Charity_B and Charity_A <= Charity_C:
# #             Charity_A = Charity_A + profit
# #             output.append('A')
# #
# #         elif Charity_B <= Charity_C:
# #             Charity_B = Charity_B + profit
# #             output.append('B')
# #
# #         else:
# #             Charity_C = Charity_C + profit
# #             output.append('C')
# #
# #
# #     return output
# #
# # if __name__ == '__main__':
# #     fptr = open(os.environ['OUTPUT_PATH'], 'w')
# #
# #     profits_count = int(input().strip())
# #
# #     profits = []
# #
# #     for _ in range(profits_count):
# #         profits_item = float(input().strip())
# #         profits.append(profits_item)
# #
# #     res = charityAllocation(profits)
# #
# #     fptr.write('\n'.join(res))
# #     fptr.write('\n')
# #
# #     fptr.close()
#
#
# # def latestStudent(attendanceData):
# #     if attendanceData == []:
# #         return ''
# #     else:
# #         for person in attendanceData:
# #             if person[3] - person[2] < 0:
# #
# #
# #
# #     for line in attendanceData:
# #         if not line.startswith():
# #             continue
# #         else:
# #             words = line.split()
# #
# #
# # if __name__ == '__main__':
# #     fptr = open(os.environ['OUTPUT_PATH'], 'w')
# #
# #     attendanceData_rows = int(input().strip())
# #     attendanceData_columns = int(input().strip())
# #
# #     attendanceData = []
# #
# #     for _ in range(attendanceData_rows):
# #         attendanceData.append(input().rstrip().split())
# #
# #     res = latestStudent(attendanceData)
# #
# #     fptr.write(res + '\n')
# #
# #     fptr.close()
#
#
# # sentence = 'hello words'
# # reverse = sentence[::-1]
# # print(reverse)
#
# # input = 'rrrryye'
# # mega = {}
# #
# # for letter in input:
# #     mega[letter] = mega.get(letter, 0) + 1
# # jab = ''
# # for k,v in mega.items():
# #     jab +=str(v)+k
# #
# # print(jab)
# #
# # def passphraseStrength(passphrase):
# #     words = passphrase.split()
# #     mega = {}
# #     weak = 'weak'
# #     strong = 'strong'
# #
# #     for letter in words:
# #         mega[letter] = mega.get(letter, 0) + 1
# #     for k,v in mega.items():
# #         if v > 1:
# #             return weak
# #         else:
# #             return strong
# #
# #
# #
# # # ja = input
# # # num_of_elements = len(array)
# # # mean = sum(array)/num_of_elements
# # # print(mean)
# #
# # def oddNumbers(l, r):
# #     output = []
# #     for num in range(l, r+1):
# #         if num%2 != 0:
# #             output.append(num)
# #         else:
# #             continue
# #     return output
# #
# # def findNumber(arr, k):
# #     for i in arr:
# #         if i == k:
# #             print('YES')
# #             break
# #         else:
# #             continue
#
#
# # def runLengthEncoding(string):
# #     not_ava = 'n/a'
# #     if string != '':
# #         mega = {}
# #         for letter in string:
# #             mega[letter] = mega.get(letter, 0) + 1
# #         jab = ''
# #         for k,v in mega.items():
# #             jab +=str(v)+k
# #         return jab
# #     else:
# #         return 'n/a'
# #
# # job = runLengthEncoding('a')
# # print(job)
#
# # import fernet
# #
# # key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='
# #
# # # Oh no! The code is going over the edge! What are you going to do?
# # message = b'gAAAAABcNO2QGQGNmhgTPm8YZ_e-hvahPl8UYaQ3Vm1w2s871T_eurtlTJ7_vf_lve-90HMrJBFfhIJZ5SClLWvis98UC35M5S3XXXne46CFWk4-rP23FjRFK_n4z8OEWGpEx9j2Zwpebt_T9FWSkREm-C2AUKYwEJAUU9gSRMhS-69qiMm8YKHvd-LEULPZbx6m46-gckry'
# #
# # def main():
# #     f = Fernet(key)
# #     print(f.decrypt(message))
# #
# #
# # if __name__ == "__main__":
# #     main()
#
# # for i in range(0,11):
# #     if i%2 == 0:
# #         print(i)
# #     else:
# #         continue
#
# # word = 'ABCDEFGHIJK'
# #
# # for letter in word:
# #     print(letter)
#
# # Uber AI Residency Segments
# # arr = [5,12,3,5,5,6]
# # n = len(arr)
# # p = 0
# # l = list()
# # x = 3
# # while(p+x <= n):
# #     d= list()
# #     for i in range(p, p+x):
# #         if (n >= 1 and n <= 1000000) and (arr[i] >= 1 and arr[i] <= 1000000000) and (x >= 1 and x <= 100000):
# #             d.append(arr[i])
# #     l.append(d)
# #     p += 1
# #
# # j = list()
# # for i in l:
# #     j.append(min(i))
# # print(max(j))
# #
#
#
# # if __name__ == '__main__':
# #     fptr = open(os.environ['OUTPUT_PATH'], 'w')
# #
# #     x = int(input().strip())
# #
# #     arr_count = int(input().strip())
# #
# #     arr = []
# #
# #     for _ in range(arr_count):
# #         arr_item = int(input().strip())
# #         arr.append(arr_item)
# #
# #     result = segment(x, arr)
# #
# #     fptr.write(str(result) + '\n')
# #
# #     fptr.close()
#
#
# # arr = [12, 7, 25, 18]
# # ykk = [24, 21, 50, 47]
# # k = list()
# # z = list()
# # w = list()
# # r = list()
# # v = list()
# # for i in arr:
# #     d = list()
# #     for m in range(1, i+1):
# #         if i % m == 0:
# #             d.append(m)
# #     k.append(d)
# # print(k)
# #
# # for i in k:
# #     y = list()
# #     for j in i:
# #         if j> 7:
# #             y.append(j)
# #     z.append(y)
# #
# # print(z)
# #
# # for i in ykk:
# #     d = list()
# #     for m in range(1, i+1): #produced greatest common divisor
# #         if i % m == 0:
# #             d.append(m)
# #     r.append(d)
# # print(r)
# #
# # for i in r:         #checked against
# #     y = list()          #https://www.hackerrank.com/contests/hack-it-to-win-it-paypal/challenges/q4-traveling-is-fun
# #     for j in i:
# #         if j> 7:
# #             y.append(j)
# #     v.append(y)
# #
# # print(v)
# #
# #
# # for i in range(0,len(arr)):
# #     if z[i] == [] or v[i] == []:
# #         w.append(0)
# #     else:
# #         for t, k in map(None, z[i], v[i]):
# #             if z[i][t] == v[i][k]:
# #                 w.append(1)
# #                 #             continue
# #                 # else:
# #                 #     w.append(0)
# #                 #     continue
# #
# # print(w)
#
# # l = ['man', True, 23, 'bannaan']
# #
# # l.remove(23)
# # print(l)
# # l.pop(0)
# # print(l)
# # l.extend('bannaan')
# # print(l)
#
# # GOLDMAN SACHS ARI 2019
# # def newstring(textmessage):
# #     return textmessage.lower()[:len(textmessage) - 3]
# #
# # def symbol(textmessage):
# #     return textmessage[-3:]
# #
# # def return_palindromes(textmessage):
# #     palindromes_string = newstring(textmessage)
# #     palindromes_possibles = []
# #
# #     for initial_position in range(len(palindromes_string)):
# #         for position in range(initial_position+1,len(palindromes_string)):
# #              new_palindrome = palindromes_string[initial_position:position+1]
# #              if len(new_palindrome) >= 3 and new_palindrome == new_palindrome[::-1]:
# #                  palindromes_possibles.append(new_palindrome)
# #     return palindromes_possibles
# #
# # def cardinality(list_of_possibilities):
# #     value = 0
# #     if len(list_of_possibilities) >=2 :
# #         for palindrome in list_of_possibilities:
# #             value += len(palindrome)
# #     return value
# #
# # def checkcardinality(cardinality_value):
# #     if cardinality_value >= 1 and cardinality_value <= 10:
# #         return 'Possible'
# #     elif cardinality_value >= 11 and cardinality_value <= 40:
# #         return 'Probable'
# #     elif cardinality_value >= 41 and cardinality_value <= 150:
# #         return 'Escalate'
# #     else:
# #         return 'Ignore'
# #
# # def Solution(textmessage):
# #     spy_word = symbol(textmessage)
# #     cardinality_type = checkcardinality(cardinality(return_palindromes(textmessage)))
# #     output = spy_word + ' ' + cardinality_type
# #     return output
# #
# #
# def threatDetector(textmessage):
#     output = ''
#     for element in textmessage:
#         spy_word = symbol(element)
#         if len(element) >= 1 and len(element) <=240 and spy_word[0] != element[-4] and element != ' ':
#             cardinality_type = checkcardinality(cardinality(return_palindromes(element)))
#             output += spy_word + ' ' + cardinality_type + '\n'
#         else:
#             continue
#     print(output)
#
#
#
# if __name__ == '__main__':
#     textMessages_count = int(input().strip())
#
#     textMessages = []
#
#     for _ in range(textMessages_count):
#         textMessages_item = input()
#         textMessages.append(textMessages_item)
#
#     threatDetector(textMessages)


# def binaryConversion(num):
#     output = ''
#     while num != 0:
#         output += str(num%2)
#         num = num/2
#
#     output = output[::-1]
#     return output
#
# def octalConversion(num):
#     output = ''
#     while num != 0:
#         output += str(num%8)
#         num = num/8
#
#     output = output[::-1]
#     return output
#
# def hexaConversion(num):
#     output = ''
#     ('A', 'B', 'C', 'D', 'E') = (10, 11, 12, 13, 14, 15)
#     while num != 0:
#         switch num%16:
#
#         if num%16 = 10:
#
#         output += str(num%16)
#         num = num/16
#
#     output = output[::-1]
#     return output
#
#
#
#
#
# octalConversion(16)
#
#
# ('A', 'B', 'C', 'D', 'E') = (10, 11, 12, 13, 14, 15)
#
# print(10)

# def plusMinus(arr):
#     num_pos = 0
#     num_neg  = 0
#     num_zer = 0
#     for i in arr:
#         if i > 0:
#             num_pos += 1
#         elif i < 0:
#             num_neg += 1
#         else:
#             num_zer  += 1

#     positive = num_pos/len(arr)
#     negative = num_neg/len(arr)
#     zero = num_zer/len(arr)

#     print(positive)
#     print(negative)
#     print(zero)

# plusMinus([-4, 3, -9, 0, 4, 1])
c = [1,2,3,4,5]
print(c[::-1])