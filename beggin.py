# # # #print("Sec Name Generation!")
# # # #x = input('Your Name? \n')
# # # #y= input('your SecendName? \n')




# # # #print("your Name is" + " " + x + " " + y)




# # # #print("Body Mass Calculator")

# # # #weight = int(input("type Weight in kg: \n"))

# # # #height = float(input("type height in m: \n"))

# # # #bmi = weight/height ** 2

# # # #print(int(bmi)

# # # #print("days left on your life")
# # # #age = int(input("type your age: \n"))
# # # #month = age * 12
# # # #week = age * 52
# # # #day = 365 * age

# # # #print(f"you have {day} days, {week} week, {month} month")


# # # #print("tip calculator")

# # # #bill = int(input("type total bill: \n"))

# # # #tip = int(input("type how much would u want to give? \n"))

# # # #tip_percent = tip / 100

# # # #bill_plus_tip = bill + tip_percent

# # # #person = int(input("how many peaple to split bill: \n"))

# # # #spited_price = bill_plus_tip / person

# # # #final_result = round(spited_price, 2)
# # # #final_result = "{:.2f}".format(spited_price)
# # # #print(f"each person will pay {final_result}")


# # # #print("is odd or even?")

# # # #num = int(input("input number \n"))

# # # #if num % 2 == 1:
# # #  #   print("number is odd")
# # # #elif num/2 == 0 :
# # #   #  print("number is 0")
# # # #else :
# # #  #   print("number is even")


# # # #print("can or not?")

# # # #height = int(input("input your Height in cm: \n"))

# # # #if height > 120:
# # #  #   age = int(input("input your age: \n"))
# # #   #  photo = input("did u want photo y or n \n")
# # #    # if age <= 12:
# # #     #    if(photo == 'y'): 
# # #      #       print("you may pay $8")
# # #       #  else:
# # #        #      print("you may pay $5")
# # #     #elif (age>12)and(age<=18):
# # #      #   if(photo == 'y'): 
# # #       #      print("you may pay $10")
# # #        # else:
# # #         #     print("you may pay $7")
# # #     #elif age > 18:
# # #      #   if(photo == 'y'): 
# # #       #      print("you may pay $15")
# # #        # else:
# # #         #     print("you may pay $12")
# # # #else:
# # #  #   print("you cant ride")


# # # #print("leap or not")
# # # #year = int(input("input year"))

# # # #if (year%4 == 0):
# # # #    if(year%100 != 0):
# # #  #       print("leap")
# # #   #  else:
# # #    #     if(year%400 == 0):
# # #     #        print("leap")
# # #      #   else: 
# # #       #      print("not leap")
# # # #else:
# # #  #   print("its not leap")


# # # #print("pizza deliver")

# # # #size = input("what size pizza do u want? we can give you s, m, l \n")
# # # #add_peperoni = input("do u want to add peperoni? y or n \n")
# # # #extra_cheese = input("do you want extra chees? y or n \n")

# # # #bill = 0

# # # #if(size == "s") :
# # #  #   bill += 15
# # # #elif(size == "m"):
# # #  #   bill+=20
# # # #elif(size == "l"):
# # #  #   bill+=25


# # # #if(size == "s") and (add_peperoni == "y"):
# # #  #   bill+=2
# # # #elif((size == "m") or (size == "l"))and (add_peperoni == "y"):
# # #  #   bill+=3


# # # #if extra_cheese == "y":
# # #  #   bill+=1


# # # #print(f"your bill is {bill}")


# # # #print("love calculator")

# # # #name1 = input("input first person name \n")
# # # #name2 = input("input secont person name \n")

# # # #name1_down_case = name1.lower()
# # # #name2_down_case = name2.lower()

# # # #both_name = name1_down_case + name2_down_case

# # # #t = both_name.count("t")
# # # #r = both_name.count("r")
# # # #u = both_name.count("u")
# # # #e = both_name.count("e")

# # # #true_count = t+r+u+e

# # # #l = both_name.count("l")
# # # #o = both_name.count("o")
# # # #v = both_name.count("v")
# # # #e_love = both_name.count("e")

# # # #love_count = l+o+v+e_love

# # # #print(f"{true_count}{love_count}%")



# # # #print("Welcome to Tresure Island")
# # # #print("Your mission is to find the treasure")

# # # #side = input(f"You're at a cross road. where do u want to go? Type 'left' or 'right'").lower()

# # # #if(side == 'left'):
# # #  # choice_door = input(f"we have 3 door choose one 'red' or 'yellow' or 'blue'").lower()
# # #   #if(choice_door == "blue"):
# # #    #     print("congrats u win")
# # #   #else:
# # #    # print("u lose")
# # # #else:
# # #  #   print("u lose")




# # # #print('Random Test')

# # # #import random

# # # #random_first = random.randint(1,100)
# # # #print(random_first)
# # # #random_first_float = random.random()*10
# # # #print(random_first_float)

# # # #print("head or tails")
# # # #import random

# # # #random_side = random.randint(0,1)

# # # #if(random_side == 1):
# # #  # print("head")
# # # #else:
# # #  # print("tails")


# # # #print("რანდომ ნ ამე ფორ ბილლ")
# # # #import random
# # # #names = input(f'input your names (between each one pls write ","')
# # # #split_names = names.split(",")
# # # #name_count = len(split_names)

# # # # random_name = random.randint(0,name_count)

# # # # print(f"hey {split_names[random_name-1]}, pls your car to pay")

# # # # print("x and o")

# # # # row1 = ['0', '0','0']
# # # # row2 = ['0', '0','0']
# # # # row3 = ['0', '0','0']
# # # # map = [row1,row2,row3]

# # # # print(f"{row1}\n{row2}\n{row3}")

# # # # position = input("where do u want to be X? 1 or 2 or 3 \n")
# # # # position1 = str(position)
# # # # map[int(position1[0])-1][int(position1[1])-1] = "X"

# # # # print(f"{row1}\n{row2}\n{row3}")


# # # # print("rock, paper scissors")
# # # # import random

# # # # rock = '''
# # # #     _______
# # # # ---'   ____)
# # # #       (_____)
# # # #       (_____)
# # # #       (____)
# # # # ---.__(___)
# # # # '''

# # # # paper = '''
# # # #     _______
# # # # ---'   ____)____
# # # #           ______)
# # # #           _______)
# # # #          _______)
# # # # ---.__________)
# # # # '''

# # # # scissors = '''
# # # #     _______
# # # # ---'   ____)____
# # # #           ______)
# # # #        __________)
# # # #       (____)
# # # # ---.__(___)
# # # # '''

# # # # game_rule=[rock, paper, scissors]

# # # # player_choice = int(input("write your choice 1-rock, 2- paper, 3- scissors \n"))
# # # # if (player_choice <= 0) or (player_choice >3):
# # # #   print("invaild number")
# # # # ai_choice = random.randint(1,3)

# # # # print(f"\nPlayer-1 \n{game_rule[player_choice - 1]}")
# # # # print(f"\nAI \n{game_rule[ai_choice - 1]}")

# # # # if (player_choice != 1) and (player_choice > ai_choice):
# # # #   if(player_choice == 3) and (ai_choice == 1):
# # # #     print("player_lose")
# # # #   else:
# # # #      print("player_win")
# # # # elif(player_choice == 1) and (ai_choice == 3):
# # # #   print("player_win")
# # # # elif(player_choice == ai_choice):
# # # #   print("its draw")
# # # # else:
# # # #   print("player_lose")

# # # # print("test for loop in python")
# # # # test = 0
# # # # students = input("Students height list")
# # # # split_students = students.split(",")

# # # # for i in split_students:
# # # #   test += int(i)

# # # # print(test)


# # # print("max or min number test with for loop") not finishted need to work much time

# # # score = input("input score list")
# # # score_count = 0
# # # sum_score = 0
# # # split_score_one = []
# # # split_score = score.split(",")

# # # for repeat in range(0, int(len(split_score)/2)):
# # #   for i in range(0, len(split_score)):
# # #     split_score[i] = int(split_score[i])
# # #     score_count += 1

# # #   for n in split_score:
# # #     sum_score+=n

# # #   mean_score = sum_score/score_count

# # #   for j in range(0, score_count-1):
# # #     print(f"{j} test")
# # #     if (j<score_count) and (split_score[j] >= mean_score):
# # #       split_score_one.append(split_score[j])
# # #       print(split_score_one)
# # # # print(f"n{sum_score}")
# # # # print(score_count)


# # # print("highest number")
# # # score = input("input score list")
# # # hight_score = 0
# # # split_score = score.split(",")
# # # for score in split_score:
# # #   int_score = int(score)
# # #   if (hight_score < int_score):
# # #     hight_score = int_score
# # #     print(score)


# # # print("check even numbers")

# # # even_numbers = []
# # # even_numbers_sum = 0
# # # for i in range(2, 101, 2):
# # #   even_numbers.append(i)
# # #   even_numbers_sum += i
# # # print(even_numbers)
# # # print(even_numbers_sum)

# # # print("fizz buzz challange")

# # # for i in range(1, 101):
# # #   if(i%3 == 0) and (i%5 == 0):
# # #     print("FizzBuzz")
# # #   elif i%3 == 0:
# # #     print("Fizz")
# # #   elif i%5 == 0:
# # #     print("Buzz")
# # #   else:
# # #     print(i)



# # # print("Passwored generator")
# # # import random

# # # letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
# # #           'p','q','r','s','t','w','x','y','z']
# # # random_letters = 0
# # # random_letters_let = []
# # # number = [1,2,3,4,5,6,7,8,9,0]
# # # random_numbers = 0
# # # random_numbers_num = []
# # # symbol = ['!','@','#','$','%','^','&','*','(',')']
# # # random_symbols = 0
# # # random_symbols_sym = []

# # # find_sequence = 0
# # # find_lns = 0
# # # password_first_generation = []
# # # test = 0
# # # password = []

# # # count_letters = int(input("how many letters do u want to be in your passwored \n"))
# # # count_numbers = int(input("how many numbers do u want to be in your passwored \n"))
# # # count_symbols = int(input("how many symbolss do u want to be in your passwored \n"))

# # # for i in range(0, count_letters):
# # #   random_letters = random.randint(0, len(letters)-1)
# # #   random_letters_let.append(letters[random_letters])

# # # for k in range(0, count_numbers):
# # #   random_numbers = random.randint(0, len(number)-1)
# # #   random_numbers_num.append(str(number[random_numbers]))

# # # for j in range(0, count_symbols):
# # #   random_symbols = random.randint(0, len(symbol)-1)
# # #   random_symbols_sym.append(symbol[random_symbols])

# # # password_first_generation = [random_letters_let, random_numbers_num,random_symbols_sym]


# # # for i in range(0, count_letters+count_numbers+count_symbols):
# # #   find_sequence = random.randint(0,2)
# # #   find_lns = random.randint(0,(len(password_first_generation[find_sequence]))-1)

# # #   password.append(password_first_generation[find_sequence][find_lns])


# # # test2 =''
# # # for pas in range(0, len(password)-1):
# # #   test+=1
# # #   test2 = test2 + password[pas]

# # # print(test2)

# # # print("find Letter")

# # # stages = ['''
# # #   +---+
# # #   |   |
# # #   O   |
# # #  /|\  |
# # #  / \  |
# # #       |
# # # =========
# # # ''', '''
# # #   +---+
# # #   |   |
# # #   O   |
# # #  /|\  |
# # #  /    |
# # #       |
# # # =========
# # # ''', '''
# # #   +---+
# # #   |   |
# # #   O   |
# # #  /|\  |
# # #       |
# # #       |
# # # =========
# # # ''', '''
# # #   +---+
# # #   |   |
# # #   O   |
# # #  /|   |
# # #       |
# # #       |
# # # =========''', '''
# # #   +---+
# # #   |   |
# # #   O   |
# # #   |   |
# # #       |
# # #       |
# # # =========
# # # ''', '''
# # #   +---+
# # #   |   |
# # #   O   |
# # #       |
# # #       |
# # #       |
# # # =========
# # # ''', '''
# # #   +---+
# # #   |   |
# # #       |
# # #       |
# # #       |
# # #       |
# # # =========
# # # ''']


# # # import random
# # # end_messige = "u lose"
# # # word_list = ["home","computer","hand","move"]
# # # live_count = 6
# # # live_count2 = 0
# # # hidde_word = []
# # # live_bool = False

# # # random_word = random.randint(0, len(word_list)-1)
# # # game_word = word_list[random_word]
# # # print(game_word)
# # # for i in range(0, len(game_word)):
# # #     hidde_word.append(" _ ")
# # # while live_count > 0 and live_count2 < len(game_word):
# # #     print(live_count)
# # #     print(' '.join(hidde_word))
# # #     print(stages[live_count])
# # #     player_letter = str(input("input letter \n")).lower()
# # #     for i in range(0, len(game_word)):
# # #         if player_letter == game_word[i]:
# # #             hidde_word[i] = player_letter
# # #             live_bool = True
# # #     if live_bool:
# # #             live_count2+=1
# # #             live_bool = False
# # #     else:
# # #             live_count-=1
    
# # #     if live_count2 == len(game_word):
# # #         end_messige = "U Win"
# # #     elif live_count == 0:
# # #         end_messige = "U lose"
# # #         live_count = 0
# # #         print(stages[live_count])

# # # print(end_messige)

# # # print("check prime numbers")

# # # num = int(input("type number \n"))

# # # def checker(number):
# # #     if number % 2 == 0 and number != 2:
# # #         print("its not prime number")
# # #     elif number % 3 == 0 and number != 3:
# # #         print("its not prime number")
# # #     elif number % 5 == 0 and number != 5:
# # #         print("its not prime number")
# # #     else:
# # #         print("its prime number")

# # # checker(number = num)

# # # print("encrypte decrypted")
# # # alphabet = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

# # # def encrypt_function(text, shift, completed_text):
# # #     for let in text:
# # #         if let in alphabet:
# # #             encryot_text = alphabet.index(let)
# # #             if let != " ":
# # #                 encryot_text += (shift%26)
# # #             else:
# # #                 encryot_text = encryot_text
# # #         completed_text += alphabet[encryot_text]
# # #     print(completed_text)

# # # def decrypted_function(text, shift, completed_text):
# # #     for let in text:
# # #         if let in alphabet:
# # #             encryot_text = alphabet.index(let)
# # #             if let != " ":
# # #                 encryot_text -= (shift%26)
# # #             else:
# # #                 encryot_text = encryot_text
# # #         completed_text += alphabet[encryot_text]
# # #     print(completed_text)

# # # def start_function():
# # #     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
# # #     text = input("Type yout text: \n").lower()
# # #     shift = int(input("type shift number: \n"))
# # #     completed_text = ''
# # #     if direction == "encode":
# # #         encrypt_function(text,shift,completed_text)
        
# # #     elif direction == "decode":
# # #         decrypted_function(text,shift,completed_text)
# # #     repeat_function()
# # # def repeat_function():
# # #     repeat = input("Type 'yes' if u want to repeat function, Type 'No' if u dont want to repeat Function \n").lower()
# # #     if repeat == 'yes':
# # #         start_function()
# # #     else:
# # #         print("We completed Task <3")

# # # start_function()
# # # from turtle import st


# # # print("Score for students")

# # # students_scores = {
# # #     "Harry": 81,
# # #     "Ron": 78,
# # #     "Hermione": 99,
# # #     "Draco": 74,
# # #     "Neville": 62,
# # # }

# # # students_grades = {}

# # # for key in students_scores:
# # #     if(students_scores[key] > 90):
# # #         students_grades[key] = "Outstanding"
# # #     elif(students_scores[key] > 80 and students_scores[key] < 91):
# # #         students_grades[key] = "Exceeds Expectations"
# # #     elif(students_scores[key] < 80 and students_scores[key] > 71):
# # #         students_grades[key] = "Acceptable"
# # #     elif(students_scores[key] < 71):
# # #         students_grades[key] = "Fail"
# # # print(students_grades)

# # # travel_log = [
# # # {
# # #   "country": "France",
# # #   "visits": 12,
# # #   "cities": ["Paris", "Lille", "Dijon"]
# # # },
# # # {
# # #   "country": "Germany",
# # #   "visits": 5,
# # #   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# # # },
# # # ]


# # # def add_new_country(country, count, cities):
# # #     new_dict = {
# # #         "country": country,
# # #         "visits": count,
# # #         "cities": cities
# # #     }

# # #     travel_log.append(new_dict)

# # # add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# # # print(travel_log)

# # # import os
# # # from art import logo
# # # def clear_console():
# # #     os.system('clear')
# # # auction_dictionary = []
# # # print(logo)
# # # action =  True

# # # while action:
# # #     name = input("Please Write your Name \n")
# # #     bid = int(input("Your bid? \n$"))
# # #     auc_dic = {
# # #         "name" : name,
# # #         "bid": bid
# # #     }

# # #     auction_dictionary.append(auc_dic)
# # #     act = input("are other bids 'yes' or 'no' \n")
# # #     if(act == "no"):
# # #         action = False
# # #     elif(act == "yes"):
# # #         clear_console()
# # #         action = True
# # #     else: 
# # #         print("write correct world")
# # #         act = input("are other bids 'yes' or 'no' \n")
# # # max_bid = {
# # #     "name": '',
# # #     "bid": 0
# # # }
# # # for i in auction_dictionary:
# # #     if(i['bid'] >= max_bid['bid']):
# # #          max_bid['name'] = i['name']
# # #          max_bid['bid'] = i['bid']
# # # print(f"Winner is {max_bid['name']} with {max_bid['bid']}$ bid")

# # # def is_leap(year):
# # #   if year % 4 == 0:
# # #     if year % 100 == 0:
# # #       if year % 400 == 0:
# # #         print("Leap year.")
# # #         return True
# # #       else:
# # #         print("Not leap year.")
# # #         return False
# # #     else:
# # #       print("Leap year.")
# # #       return True
# # #   else:
# # #     print("Not leap year.")
# # #     return False
# # # def days_in_month(year, month):
# # #   if(is_leap(year)):
# # #     month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# # #   else:
# # #     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# # #   return month_days[month-1]
# # # year = int(input("Enter a year: "))
# # # month = int(input("Enter a month: "))
# # # days = days_in_month(year, month)
# # # print(days)

# # # print("Calculator")

# # # def add(n1,n2):
# # #     return n1+n2

# # # def minus(n1,n2):
# # #     return n1-n2

# # # def multiple(n1,n2):
# # #     return n1*n2

# # # def devide(n1,n2):
# # #     return n1/n2

# # # operators = {
# # #     "+": add,
# # #     "-": minus,
# # #     "*":multiple,
# # #     "/":devide
# # # }

# # # n1 = float(input("First Number \n"))
# # # next = True
# # # for sym in operators:
# # #     print(sym)

# # # while next:
# # #     n2 = float(input("write new second number\n"))
# # #     oper_symb = str(input("Write operator: "))
# # #     start_calculation = operators[oper_symb]
# # #     answer = start_calculation(n1,n2)
# # #     print(f"{n1} {oper_symb} {n2} = {answer}")
# # #     next_input = input("do u want to calculate with previus answer? 'y' or 'n' or 'e' to exit: ")
# # #     if(next_input == 'y'):
# # #         n1 = answer 
# # #     elif next_input == 'n':
# # #         n1 = float(input("First Number \n"))
# # #     else:
# # #         next = False

# # # from art import logo2

# # # print(logo2)
# # # print("bj")
# # # import random
# # # import os
# # # def clear_console():
# # #     os.system('clear')

# # # start_function = True
# # # player_point = 0
# # # ai_point = 0
# # # cards = [2,3,4,5,6,7,8,9,10,'j','d','k','A']

# # # def player1():
# # #     add_card = False
# # #     player_card = []
# # #     for i in range(0,2):
# # #         player_card.append(cards[random.randint(0, len(cards) - 1)])
# # #     print(f"{player_card} - Player Cards")
# # #     calculate_point(player_card)
# # #     while not add_card:
# # #         if calculate_point(player_card) <= 21:
# # #             cont = input("add cards? 'y' or 'n' \n")

# # #             if(cont == "y"):
# # #                 player_card.append(cards[random.randint(0, len(cards) - 1)])
# # #                 clear_console()
# # #                 print(f"{player_card} - Player Cards")
# # #             elif (cont == "n"): 
# # #                 print(calculate_point(player_card))
# # #                 add_card = True
# # #         else: 
# # #             add_card = True
# # #     return calculate_point(player_card)
    

# # # def ai():
# # #     add_card = False
# # #     ai_card = []
# # #     for i in range(0,2):
# # #         ai_card.append(cards[random.randint(0, len(cards) - 1)])
# # #     print(f"{ai_card} - Dealer Cards")
# # #     calculate_point(ai_card)
# # #     while not add_card:
       
# # #         if calculate_point(ai_card) <= 21:
# # #             if calculate_point(ai_card) <= 15:
# # #                 ai_card.append(cards[random.randint(0,len(cards)-1)])
# # #                 print(f"{ai_card} - Dealer Cards")
# # #             else:
# # #                 add_card = True
# # #         else:
# # #             add_card = True
# # #     return calculate_point(ai_card)

# # # def calculate_point(n):
# # #     """calculate player point in bj"""
# # #     full_point = 0
# # #     for i in n:
# # #         if type(i) == str:
# # #             if i == "A":
# # #                 if full_point >= 11:
# # #                     full_point += 1
# # #                 else:
# # #                     full_point += 11
# # #             else:
# # #                 full_point += 10
# # #         else:
# # #             full_point += i
# # #     return full_point

# # # def check_winner(n1,n2):
# # #     print(n1)
# # #     if int(n1) > 21:
# # #         print("Dealer Win")
# # #     elif n2 > 21:
# # #         print("Player Win")
# # #     elif n1 > n2 and n1 < 22:
# # #         print("player win")
# # #     elif n2 >= n1 and n2 < 22:
# # #         print("dealer win")


# # # check_winner(player1(), ai())

# # # import random
# # # print("guess number")

# # # print("I'm thinking of a number between 1 and 100")

# # # DIF = input("Choose a difficulty. easy or hard \n")
# # # ATTEMPT= 0
# # # NUM = random.randint(1,100)

# # # def game():
# # #     global ATTEMPT
# # #     if DIF == "easy":
# # #         ATTEMPT = 9
# # #     elif DIF == "hard":
# # #         ATTEMPT = 4

# # #     def start_game():
# # #         game_start = True
# # #         global ATTEMPT
# # #         print(f"u have {ATTEMPT + 1} try")
# # #         print(f"asdasdasdasdasd{NUM}")
# # #         while game_start:
# # #             num = int(input("type Number \n"))
# # #             if ATTEMPT != 0 and NUM < num:
# # #                 ATTEMPT -= 1
# # #                 print("to Hight")
# # #                 print(f"u have {ATTEMPT + 1} try")
# # #             elif ATTEMPT != 0 and NUM > num:
# # #                 ATTEMPT -= 1
# # #                 print("to Low")
# # #                 print(f"u have {ATTEMPT + 1} try")
# # #             elif ATTEMPT != 0 and NUM == num:
# # #                 print("U win")
# # #                 game_start = False
# # #             elif ATTEMPT <= 1:
# # #                 print("Game Over")
# # #                 game_start = False
# # #     start_game()
# # # game()

# # # print("High Low")

# # # from game_data import data

# # # import random



# # # def random_first():
# # #     return random.randint(0,len(data)-1)

# # # def random_second():
# # #     return random.randint(0,len(data)-1)

# # # def start_game():
# # #     game = True
# # #     point = 0
# # #     while game:
# # #         high_or_low = 0
        
# # #         first_name = data[random_first()]['name']
# # #         first_count = data[random_first()]['follower_count']

# # #         second_name = data[random_second()]['name']
# # #         second_count = data[random_second()]['follower_count']

# # #         print(f"First Instagramer is {first_name} with {first_count}")
# # #         print(f"Second Instagramer is {second_name} with {second_count}")
# # #         choice = input("write, a or b \n")

# # #         if int(first_count) < int(second_count):
# # #             high_or_low = 2
# # #         elif int(first_count) > int(second_count):
# # #             high_or_low = 1
# # #         else:
# # #             high_or_low = 0

# # #         if choice == 'a' and high_or_low ==1:
# # #             print(f"winner {first_name} with {first_count}")
# # #             point+=1
# # #         elif choice == 'b' and high_or_low ==2:
# # #             print(f"winner {second_name} with {second_count}")
# # #             point+=1
# # #         else:
# # #             game = False
# # #             print(f"game Over, your point is {point}")

# # # start_game()

# # # print("Coffe Machine")
# # # import os

# # # coffe_bool = True

# # # resource = [
# # #     {"water" : 500},
# # #     {"milk" : 200},
# # #     {"coffe" : 100},
# # #     {"money" : 0}
# # # ]

# # # espresso_res = [
# # #     {"water" : 50},
# # #     {"milk" : 0},
# # #     {"coffe" : 18},
# # #     {"money" : 1.5}
# # # ]
# # # latte_res = [
# # #     {"water" : 200},
# # #     {"milk" : 150},
# # #     {"coffe" : 24},
# # #     {"money" : 2.5}
# # # ]
# # # cappuccino_res = [
# # #     {"water" : 250},
# # #     {"milk" : 100},
# # #     {"coffe" : 24},
# # #     {"money" : 3}
# # # ]

# # # def coffe():
# # #     while coffe_bool:
# # #         coffe_type = input("What would u like ? (write key for key words)(espresso/late/cappuccino):")
        
# # #         if coffe_type == "key":
# # #             key_function()
# # #         else:
# # #             coffe_type_fun(coffe_type)

# # # def key_function():
# # #     global coffe_bool
   
# # #     key_word = input("write 'report' to check resources or 'off' to turn off machine")
# # #     if key_word == "report":
# # #         clear_console()
# # #         print(f"Water : {resource[0]['water']}ml")
# # #         print(f"Milk : {resource[1]['milk']}ml")
# # #         print(f"Coffe : {resource[2]['coffe']}g")
# # #         print(f"Money : ${resource[3]['money']}")
# # #     elif key_word == "off":
# # #         clear_console()
# # #         coffe_bool = False

# # # def coffe_type_fun(n):
# # #     global espresso_res
# # #     if n == "espresso":
# # #         if check_res(espresso_res):
# # #             espresso_fun()
# # #         else:
# # #             print("Sorry we dont have enough resources")
# # #     elif n == "late":
# # #         if check_res(latte_res):
# # #             latte_fun()
# # #         else:
# # #             print("Sorry we dont have enough resources")

# # #     elif n == "cappuccino":
# # #         if check_res(cappuccino_res):
# # #             cappuccino_fun()
# # #         else:
# # #             print("Sorry we dont have enough resources")


# # # def espresso_fun():
# # #     print (f"Please Pay {espresso_res[3]['money']}")
# # #     quaters = int(input("How many quarters?: \n"))
# # #     dimes = int(input("How many dimes?: \n"))
# # #     nickles = int(input("How many nickles?: \n"))
# # #     pennies = int(input("How many pennies?: \n"))

# # #     total = (quaters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    
# # #     if total < espresso_res[3]['money']:
# # #         print("Uppss Not enough Money, Please Add more")
# # #         quaters = int(input("How many quarters?: \n"))
# # #         dimes = int(input("How many dimes?: \n"))
# # #         nickles = int(input("How many nickles?: \n"))
# # #         pennies = int(input("How many pennies?: \n"))
# # #     else:
# # #         cash_out = total - espresso_res[3]['money']
# # #         clear_console()
# # #         print(f"here is {round(cash_out,2)} in change")
# # #         print("Here is Your espresso, Enjoy")
# # #         resource[0]['water'] -= espresso_res[0]['water']
# # #         resource[1]['milk'] -= espresso_res[1]['milk']
# # #         resource[2]['coffe'] -= espresso_res[2]['coffe']
# # #         resource[3]['money'] += espresso_res[3]['money']

# # # def latte_fun():
# # #     print (f"Please Pay {latte_res[3]['money']}")
# # #     quaters = int(input("How many quarters?: \n"))
# # #     dimes = int(input("How many dimes?: \n"))
# # #     nickles = int(input("How many nickles?: \n"))
# # #     pennies = int(input("How many pennies?: \n"))

# # #     total = (quaters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    
# # #     if total < latte_res[3]['money']:
# # #         print("Uppss Not enough Money, Please Add more")
# # #         quaters = int(input("How many quarters?: \n"))
# # #         dimes = int(input("How many dimes?: \n"))
# # #         nickles = int(input("How many nickles?: \n"))
# # #         pennies = int(input("How many pennies?: \n"))
# # #     else:
# # #         cash_out = total - latte_res[3]['money']
# # #         clear_console()
# # #         print("Here is Your Latte, Enjoy")
# # #         print(f"here is {round(cash_out,2)} in change")
# # #         resource[0]['water'] -= latte_res[0]['water']
# # #         resource[1]['milk'] -= latte_res[1]['milk']
# # #         resource[2]['coffe'] -= latte_res[2]['coffe']
# # #         resource[3]['money'] += latte_res[3]['money']
# # #         print(resource[0]['water'])


# # # def cappuccino_fun():
# # #     print (f"Please Pay {cappuccino_res[3]['money']}")
# # #     quaters = int(input("How many quarters?: \n"))
# # #     dimes = int(input("How many dimes?: \n"))
# # #     nickles = int(input("How many nickles?: \n"))
# # #     pennies = int(input("How many pennies?: \n"))

# # #     total = (quaters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    
# # #     if total < cappuccino_res[3]['money']:
# # #         print("Uppss Not enough Money, Please Add more")
# # #         quaters = int(input("How many quarters?: \n"))
# # #         dimes = int(input("How many dimes?: \n"))
# # #         nickles = int(input("How many nickles?: \n"))
# # #         pennies = int(input("How many pennies?: \n"))
# # #     else:
# # #         clear_console()
# # #         cash_out = total - cappuccino_res[3]['money']
# # #         print(f"here is {round(cash_out,2)} in change")
# # #         print("Here is Your cappuccino, Enjoy")
# # #         resource[0]['water'] -= cappuccino_res[0]['water']
# # #         resource[1]['milk'] -= cappuccino_res[1]['milk']
# # #         resource[2]['coffe'] -= cappuccino_res[2]['coffe']
# # #         resource[3]['money'] += cappuccino_res[3]['money']
# # #         print(resource[0]['water'])



# # # def check_res(n):
# # #     if(n[0]['water'] <= resource[0]['water']):
# # #         if(n[1]['milk'] <= resource[1]['milk']):
# # #             if(n[2]['coffe'] <= resource[2]['coffe']):
# # #                 return True
# # #             else:
# # #                 return False
# # #         else:
# # #             return False
# # #     else:
# # #         return False


# # # def clear_console():
# # #     os.system('clear')
# # # coffe()

# # # print("Turte Challange")

# # # from turtle import Turtle, Screen

# # # timmy = Turtle()
# # # timmy.shape("turtle")
# # # timmy.color("red")
# # # timmy.forward(100)
# # # timmy.left(90)
# # # timmy.forward(100)
# # # timmy.left(90)
# # # timmy.forward(100)
# # # timmy.left(90)
# # # timmy.forward(100)


# # # my_screen = Screen()

# # # my_screen.exitonclick()
# # # print(timmy)

# # # from turtle import Turtle, Screen

# # # tom = Turtle()
# # # screen = Screen()


# # # def forward():
# # #     tom.forward(10)
# # # def backward():
# # #     tom.backward(10)
# # # def left():
# # #     heading = tom.heading()+10
# # #     tom.setheading(heading)
# # # def right():
# # #     heading = tom.heading()-10
# # #     tom.setheading(heading)
# # # def clear():
# # #     tom.clear()
# # # screen.listen()

# # # screen.onkeypress(fun=forward, key="w")
# # # screen.onkeypress(fun=backward, key="s")
# # # screen.onkeypress(fun=left, key="a")
# # # screen.onkeypress(fun=right, key="d")
# # # screen.onkey(fun=clear, key="c")

# # # screen.exitonclick()



# # # from turtle import Turtle, Screen
# # # import random
# # # screen = Screen()
# # # screen.setup(500,400)
# # # color = ['red','green','yellow','blue','gray','black']
# # # y_pos = [40,100,160,-10,-60,-120]
# # # turtle_count = []
# # # winner = screen.textinput("winner", "Select Winner color")
# # # game = True

# # # for i in range (0,6):
# # #     tom = Turtle()
# # #     tom.shape("turtle")
# # #     tom.penup()
# # #     tom.color(color[i])
# # #     tom.goto(-230, y_pos[i])
# # #     turtle_count.append(tom)

# # # while game:
# # #     for j in turtle_count:
# # #         j.forward(random.random()*5)
        
# # #         if j.xcor()>=220:
# # #             game = False
# # #             if winner == color[turtle_count.index(j)]:
# # #                 print(f"Winner is {color[turtle_count.index(j)]}, You win ")
# # #             else:
# # #                 print(f"Winner is {color[turtle_count.index(j)]}, You lose ")


# # # screen.exitonclick()

# # # from turtle import Screen,Turtle
# # # import time
# # # import random

# # # lenght = 3
# # # snake_count = []
# # # game = True
# # # ball = None
# # # point = 0

# # # screen = Screen()

# # # def screen_setup():
# # #     screen.setup(600,600)
# # #     screen.bgcolor('black')
# # #     screen.title("Snake")
# # #     screen.listen()
# # #     screen.tracer(0)


# # # def draw_snake():
# # #     for i in range (0,lenght):
# # #         snake = Turtle()
# # #         snake.penup()
# # #         snake.color('white')
# # #         snake.shape('square')
# # #         snake.setx(5*(-i))
# # #         snake.width(20)
# # #         snake_count.append(snake)

# # # def draw_ball():
# # #     global ball
# # #     ball = Turtle()
# # #     ball.shape('circle')
# # #     ball.shapesize(0.5)
# # #     ball.goto(random.randint(-250,250),random.randint(-250,250))
# # #     ball.color("blue")

# # # def move_snake():
# # #     screen.update()
# # #     time.sleep(1)
# # #     for i in range(0,len(snake_count), 1):
# # #         snake_count[0].forward(0)
# # #         x = snake_count[0].xcor()
# # #         y = snake_count[0].ycor()
# # #         snake_count[0].forward(10)
# # #         snake_count[i].goto(x,y)
# # #         screen.onkeypress(left,'a')
# # #         screen.onkeypress(right,'d')
# # #         snake_count[i].penup()
# # #         snake_x = snake_count[0].ycor()
# # #         snake_y = snake_count[0].ycor()
# # #         ball_x = ball.ycor()

# # #         print(f"snake`{snake_x}")
        
# # #         print(f"ball{ball_x}")

# # # def check_point():
# # #     global point, lenght
# # #     snake_x = snake_count[0].xcor()
# # #     snake_y = snake_count[0].ycor()
# # #     ball_x = ball.xcor()
# # #     ball_y = ball.ycor()
# # #     if snake_x+20>=ball_x and snake_y>=ball_y and snake_y-10<=ball_y:
# # #         point += 1
# # #         lenght += 1
# # #         ball.goto(random.randint(-250,250),random.randint(-250,250))
# # #         snake = Turtle()
# # #         snake.shape('square')
# # #         snake.color('white')
# # #         gotox = snake_count[len(snake_count)-1].xcor()
# # #         gotoy = snake_count[len(snake_count)-1].ycor()
# # #         snake.goto(gotox,gotoy)
# # #         snake_count.append(snake)
# # #         move_snake()
# # #         print(point)

# # # # def right():
# # # #     for j in snake_count:
# # # #         heading = j.heading()+90
# # # #         j.setheading(heading)

# # # # def left():
# # # #     for j in snake_count:
# # # #         heading = j.heading()-90
# # # #         j.setheading(heading)

# # # # while True:
# # # #     for i in snake_count:
# # # #         i.forward(5)
       
# # #         # screen.onkey(right, 'd')
# # #         # screen.onkey(left, 'a')


# # # def left():
# # #     head = snake_count[0].heading()
# # #     snake_count[0].setheading(head-90)

# # # def right():
# # #     snake_count[0].right(90)

# # # screen_setup()
# # # draw_snake()
# # # draw_ball()

# # # while game:
# # #     move_snake()
# # #     check_point()
        




# # # screen.exitonclick()

# # from turtle import Screen
# # from snake import Snake
# # import time
# # import random
# # from food import Food
# # from scoreboard import Score

# # game = True
# # lenght = 3
# # screen = Screen()
# # screen.bgcolor('black')

# # obj_count = []

# # snake = Snake()
# # food = Food()
# # score = Score()

# # screen.listen()
# # screen.onkey(snake.up, "w")
# # screen.onkey(snake.down, "s")
# # screen.onkey(snake.left, "a")
# # screen.onkey(snake.right, "d")

# # while game:

# #     screen.update()
# #     time.sleep(0.05)
# #     snake.move()
# #     if snake.head.distance(food)< 15:
# #         food.refresh()
# #         score.scoreUp()
# #         snake.extend()

# #     if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
# #         score.game_over()
# #         game = False

# #     for i in snake.count[1:]:
# #         if snake.head.distance(i)<10:
# #             score.game_over()
# #             game = False


# # screen.exitonclick()

# from turtle import Turtle, Screen
# from paddle import Paddle
# from ball import Ball
# from scoreboard import ScorePong
# import time


# # paddle = Turtle()

# # paddle.shape('square')
# # paddle.shapesize(5,1)

# # def moveUp():
# #     x = paddle.xcor()
# #     y = paddle.ycor() + 15

# #     paddle.goto(x,y)

# screen = Screen()
# screen.listen()

# screen.bgcolor("white")
# screen.setup(width=700,height=500)
# screen.title("Pong")
# screen.tracer(0)

# padd = Paddle((-325,0))
# padd1 = Paddle((325,0))

# ball = Ball()

# score = ScorePong()

# screen.onkeypress(padd.moveUpFirst,"w")
# screen.onkeypress(padd.moveDownFirst,"s")

# screen.onkeypress(padd1.moveUpSecond,"Up")
# screen.onkeypress(padd1.moveDownSecond,"Down")



# game_on = True

# while game_on:

#     ball.move_ball()
#     ball.detect_wall()
#     ball.lose_ball()
#     if ball.ball_x() < -300 and ball.ball_y() < padd.paddle_y()+50 and ball.ball_y() > padd.paddle_y() - 50:
#         ball.x_move *= -1
#     if ball.ball_x() > 300 and ball.ball_y() < padd1.paddle_y()+50 and ball.ball_y() > padd1.paddle_y() - 50:
#         ball.x_move *= -1
    
#     screen.update()

# screen.exitonclick()

# # need to add speed for ball

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreCar

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()

car = CarManager()

level = ScoreCar()
over = ScoreCar()
game_is_on = True
screen.listen()
screen.onkey(player.go_up,"w")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    level.create_level()
    for i in car.all_car:
        if i.distance(player) < 25:
            over.game_over()
            game_is_on = False


    if player.is_finish_true():
        level.clear_old()
        level.level_up_counter()
        car.speed_up()


screen.exitonclick()

































