import os
from raven import Client

# def calculator():
#     num1 = int()
#     flag = False
#
#     while True:
#         if flag is False:
#             a = int(input("숫자를 입력하세요"))
#             num1 = a
#             flag = True
#         else:
#             menu = int(input("1.더한다 2.뺀다 3.곱한다 4.나눈다 5.초기화 6.나간다"))
#             if menu <= 4:
#                 num2 = int(input("숫자를 입력하세요"))
#                 if menu == 1:
#                     num1 += num2
#                     print(num1)
#                 elif menu == 2:
#                     num1 -= num2
#                     print(num1)
#                 elif menu == 3:
#                     num1 *= num2
#                     print(num1)
#                 elif menu == 4:
#                     num1 /= num2
#                     print(num1)
#             elif menu == 5:
#                 flag = False
#                 print("초기화 되었습니다")
#             elif menu == 6:
#                 print("계산기를 끕니다")
#                 break
#             elif menu > 5:
#                 input("잘못 입력하셨습니다, 다시 선택하세요")
#
#
# calculator()

#
# def calculator():
#     background = ["식.", "값.", "★"]
#     back = ["식.", "값.", "★"]
#     calc = ["+", "-", "*", "÷"]
#     num1 = int()
#     flag = False
#     print("계산기가 실행되었습니다. 괄호 사용은 현재 미구현입니다")
#     while True:
#         os.system('cls')
#         for x in range(3):
#             print(background[x], end='\n')
#
#         if flag is False:
#             a = int(input("숫자를 입력하세요"))
#
#             num1 = a
#             background[0] += str(num1)
#             background[1] += str(num1)
#             flag = True
#         else:
#             menu = int(input("1.더한다 2.뺀다 3.곱한다 4.나눈다 5.초기화 6.나간다"))
#             assert menu is not int
#             # menu의 값이 정수가 아닐 경우 에러 발생
#             if menu <= 4:
#                 num2 = int(input("숫자를 입력하세요"))
#                 if menu == 1:
#                     background[0] += calc[0]
#                     background[0] += str(num2)
#                     num1 += num2
#                     background[1] = num1
#                 elif menu == 2:
#
#                     background[0] += calc[1]
#                     background[0] += str(num2)
#                     num1 -= num2
#                     background[1] = num1
#                 elif menu == 3:
#
#                     background[0] += calc[2]
#                     background[0] += str(num2)
#                     num1 *= num2
#                     background[1] = num1
#                 elif menu == 4:
#
#                     background[0] += calc[3]
#                     background[0] += str(num2)
#                     num1 /= num2
#                     background[1] = num1
#             elif menu == 5:
#                 flag = False
#                 background = back
#                 print("초기화 되었습니다")
#             elif menu == 6:
#                 print("계산기를 끕니다")
#                 break
#             elif menu > 6:
#                 input("잘못 입력하셨습니다, 다시 선택하세요")
#
#
# client = Client(
#     'https://65d575d59e1748299f322af362a6b529'
#     ':c4ba94596b824466a1a11631ec50623c@sentry.team504.co.kr//2')
#
# if __name__ == '__main__':
#     # noinspection PyBroadException
#
#     try:
#         calculator()
#     except Exception:
#         client.captureException()

# def calculator():
#     num1 = int()
#     flag = False
#
#     while True:
#         if flag is False:
#             a = int(input("숫자를 입력하세요"))
#             num1 = a
#             flag = True
#         else:
#             menu = int(input("1.더한다 2.뺀다 3.곱한다 4.나눈다 5.초기화 6.나간다"))
#             if menu <= 4:
#                 num2 = int(input("숫자를 입력하세요"))
#                 if menu == 1:
#                     num1 += num2
#                     print(num1)
#                 elif menu == 2:
#                     num1 -= num2
#                     print(num1)
#                 elif menu == 3:
#                     num1 *= num2
#                     print(num1)
#                 elif menu == 4:
#                     num1 /= num2
#                     print(num1)
#             elif menu == 5:
#                 flag = False
#                 print("초기화 되었습니다")
#             elif menu == 6:
#                 print("계산기를 끕니다")
#                 break
#             elif menu > 5:
#                 input("잘못 입력하셨습니다, 다시 선택하세요")
#
#
# calculator()
# if '+' in value2:
#     x = value2.index('+')
#     result = int(value2[x - 1]) + int(value[x + 1])
#     assert result is int, '정수가 아니므로 에러 처리합니다'
#     print(result)
#
# elif '-' in value2:
#     x = value2.index('-')
#     result = int(value2[x - 1]) + int(value[x + 1])
#     print(result)
#
# elif '*' in value2:
#     x = value2.index('*')
#     result = int(value2[x - 1]) * int(value[x + 1])
#     print(result)
#
# elif '/' in value2:
#     x = value2.index('/')
#     result = int(value2[x - 1]) / int(value[x + 1])
#     print(result)
#
# else:
#     print("올바른 계산이 아닙니다")


# def calculator():
#     while True:
#
#         value = input("게산을 입력하세요 예) a+b, a-b, a*b, a/b")
#         value2 = list(value)
#         y = None
#
#         if '+' in value2:
#             y = '+'
#         if '-' in value2:
#             y = '-'
#         if '*' in value2:
#             y = '*'
#         if '/' in value2:
#             y = '/'
#         if y is None:
#             print("올바른 연산자 또는 숫자를 입력하세요")
#             continue
#
#         location = value2.index(y)
#         a = ''.join(value2[0:location])
#         b = ''.join(value2[location+1:])
#         # a = (value2[location - 1])
#         # b = (value2[location + 1])
#         if a.isdigit() and b.isdigit():
#             a = int(a)
#             b = int(b)
#
#             if y is '+':
#                 print(a + b)
#
#             elif y is '-':
#                 print(a - b)
#
#             elif y is '*':
#                 print(a * b)
#
#             elif y is '/':
#                 print(a / b)
#         else:
#             print("숫자를 입력하세요")
#
# client = Client(
#     'https://65d575d59e1748299f322af362a6b529'
#     ':c4ba94596b824466a1a11631ec50623c@sentry.team504.co.kr//2')
#
# if __name__ == '__main__':
#     # noinspection PyBroadException
#
#     try:
#         calculator()
#     except Exception:
#         client.captureException()
#
# def calculator():
#     while True:
#         Menu = input("계산을 입력하세요. 단 더하기, 빼기, 곱하기, 나누기가 사용 "
#                      "가능하고 숫자와 연산자 사이를 띄어쓰기(공백)으로 구분합니다")
#         value = Menu.split(' ')
#         for x in ['*', '/', '+', '-']:
#             if x in value:
#                 location = value.index(x)
#                 a = int(value[location - 1])
#                 b = int(value[location + 1])
#                 if x is '*':
#                     result = a * b
#                     print(result)
#                 elif x is '/':
#                     result = a / b
#                     print(result)
#                 elif x is '+':
#                     result = a + b
#                     print(result)
#                 elif x is '-':
#                     result = a - b
#                     print(result)
#             else:
#                 pass
#
#
# client = Client(
#     'https://65d575d59e1748299f322af362a6b529'
#     ':c4ba94596b824466a1a11631ec50623c@sentry.team504.co.kr//2')
#
# if __name__ == '__main__':
#     # noinspection PyBroadException
#
#     try:
#         calculator()
#     except Exception:
#         client.captureException()
import re
def calculator():

    while True:
        Menu = input("계산을 입력하세요")
        Menu = Menu.replace(" ", "")
        value = list(Menu)
        data = None

        while True:
            flag = True
            if data is None:
                data = value
                box: list = []
            else:
                for y in ['*', '/', '+', '-']:

                    if flag is False:
                        break

                    elif y in data:
                        location = data.index(y)
                        a = ' '
                        data.insert(location, a)
                        data.insert(location + 2, a)
                        box.extend((data[:location + 2]))
                        data = data[location + 2:]

                    elif len(data) < 3:
                        flag = False
                    # 괄호 미구현
                if flag is True:
                    continue

                box.extend(data)


                result = ''.join(box)
                break

        print(result)

calculator()