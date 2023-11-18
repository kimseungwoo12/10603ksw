# number = 0
#
# while number < 10:
#      print(number)
#      number = number + 1
#
# print("=====메뉴======")
# print("1. 시작하기")
# print("2. 종료하기")
# print("==============")
#
# user_input = -1
# #
# # while user_input != 2:
# #     user_input = int(input("값을 입력하세요 >>"))
#
#
# while True:
#      print("=====메뉴======")
#      print("1. 시작하기")
#      print("2. 종료하기")
#      print("==============")
#
#      user_imput = int(input("값을 입력하세요"))
#      if user_input ==  2:
#          break

# import random
# answer = random.randrange(0, 10)
# user_input = -1
#
# while True:
#     user_input = int(input("값을 입력하세요 >>"))
#
#     if user_input == answer:
#         print("정답입니다!")
#         break
import random
answer = random.randrange(0, 10)
user_input = -1
while True:
    user_input = int(input())
    if answer == user_input:
        print('correct')
        break
    else:
        print('try again')
        if user_input < answer:
            print('up')
        else:
            print('down')