# # function ga list yuborish 

# def yigindi(*list):
#     yigindi = 0
#     for son in list:
#         yigindi+=son
#     return yigindi

# print(yigindi(2,4,4,5,8,9,12,100,36,68))

# def yigindi(*sonlar):
#     yigindi = 0
#     for i in sonlar:
#         yigindi = yigindi + i
#     return f"{sonlar} royhat elementlarining yigindisi = {yigindi}"
# print(yigindi(2,4,4))

# def yigindi(a,b,c,d):
#     return f"{a}, {b}, {c}, {d} sonlarining yigindisi = {a + b + c + d}"
# print(yigindi(2,4,4,5))

# def arfimetik(*sonlar):
#     yigindi = 0
#     soni = len(sonlar)
#     for i in sonlar:
#         yigindi = yigindi  i
#     return f"{sonlar} royhat elementlarining orta arfimetiki  = {yigindi/soni}"


# print(arfimetik(2,4,4,120,-98))

# def geometrik(*sonlar):
#     kopaytma = 1
#     daraja = len(sonlar)
#     for i in sonlar:
#         kopaytma = kopaytma * i
#     return f"{sonlar} royhat elementlarining orta geometriki  = {kopaytma**(1/daraja)}"


# print(geometrik(27,1,1))




# def kub(*son):
#     return son ** 3

# natija = kub(12,21,43)
# print(f"Natija : {natija}")


# davlatlar = {
#     'UZB': 'Toshkent',
#     'TJ' : 'Dushanbe',
#     'KG' : 'Beshkek',
#     'Rus': 'Maskva',
#     'TM': 'Oshqabod'
# }

# davlatlar['AQSH'] = 'Washington'
# davlatlar['TR'] = 'Anqara'
# davlatlar['DE'] = 'Berlin'

# print(davlatlar)


# # Functionga lugat berish

# def talaba_baxosi(**talabalar):
        
#         baxo = talabalar['baxo']
#         ism = talabalar['ism']
#         return f" Hurmatli {ism} sizning baxoyingiz {baxo} ekan "

# print(talaba_baxosi(ism = 'Bobur', baxo = 4))


# def print_board(board):
#     for row in board:
#         print(" | ".join(row))
#         print("-" * 9)

# def check_winner(board):
#     # Gorizontal va vertikal tekshirish
#     for i in range(3):
#         if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
#             return board[i][0]
#         if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
#             return board[0][i]
#     # Diagonal tekshirish
#     if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
#         return board[0][0]
#     if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
#         return board[0][2]
#     return None

# def is_full(board):
#     for row in board:
#         if " " in row:
#             return False
#     return True

# def tic_tac_toe():
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     current_player = "X"

#     while True:
#         print_board(board)
#         print(f"O'yinchi {current_player} navbati!")
#         try:
#             row = int(input("Qatorni tanlang (0, 1, 2): "))
#             col = int(input("Ustunni tanlang (0, 1, 2): "))
#             if board[row][col] != " ":
#                 print("Bu joy band! Boshqa joy tanlang.")
#                 continue
#         except (ValueError, IndexError):
#             print("Noto'g'ri kiritish! Qator va ustun 0, 1 yoki 2 bo'lishi kerak.")
#             continue

#         board[row][col] = current_player
#         winner = check_winner(board)
#         if winner:
#             print_board(board)
#             print(f"Tabriklaymiz! O'yinchi {winner} g'olib bo'ldi!")
#             break
#         if is_full(board):
#             print_board(board)
#             print("Durang! Barcha joylar to'ldi.")
#             break

#         current_player = "O" if current_player == "X" else "X"

# tic_tac_toe()


# import math

# def kalkulyator():
#     print("Oddiy kalkulyatorga xush kelibsiz!")
#     print("Quyidagi amallarni bajarishingiz mumkin:")
#     print("1. Qo'shish (+)")
#     print("2. Ayirish (-)")
#     print("3. Ko'paytirish (*)")
#     print("4. Bo'lish (/)")
#     print("5. Darajaga ko'tarish (^)")
#     print("6. Kvadrat ildiz (sqrt)")
#     print("7. Chiqish (exit)")

#     while True:
#         amal = input("\nAmalni tanlang (+, -, *, /, ^, sqrt, exit): ").lower()

#         if amal == "exit":
#             print("Kalkulyatordan foydalanganingiz uchun rahmat!")
#             break

#         if amal == "sqrt":
#             try:
#                 son = float(input("Sonni kiriting: "))
#                 if son < 0:
#                     print("Manfiy sonning kvadrat ildizi mavjud emas!")
#                 else:
#                     print(f"√{son} = {math.sqrt(son)}")
#             except ValueError:
#                 print("Iltimos, to'g'ri son kiriting!")
#             continue

#         try:
#             son1 = float(input("Birinchi sonni kiriting: "))
#             son2 = float(input("Ikkinchi sonni kiriting: "))

#             if amal == "+":
#                 print(f"{son1} + {son2} = {son1 + son2}")
#             elif amal == "-":
#                 print(f"{son1} - {son2} = {son1 - son2}")
#             elif amal == "*":
#                 print(f"{son1} * {son2} = {son1 * son2}")
#             elif amal == "/":
#                 if son2 == 0:
#                     print("0 ga bo'lish mumkin emas!")
#                 else:
#                     print(f"{son1} / {son2} = {son1 / son2}")
#             elif amal == "^":
#                 print(f"{son1} ^ {son2} = {son1 ** son2}")
#             else:
#                 print("Noto'g'ri amal tanlandi!")
#         except ValueError:
#             print("Iltimos, to'g'ri son kiriting!")

# kalkulyator()




# import random

# def raqam_topish_oyini():
#     print("1 dan 100 gacha bo'lgan sonni toping!")
#     tasodifiy_son = random.randint(1, 100)  # Kompyuter tasodifiy son tanlaydi
#     urinishlar = 0

#     while True:
#         try:
#             foydalanuvchi_soni = int(input("Son kiriting: "))
#             urinishlar += 1

#             if foydalanuvchi_soni < tasodifiy_son:
#                 print("Xato! Siz kiritgan son kichik.")
#             elif foydalanuvchi_soni > tasodifiy_son:
#                 print("Xato! Siz kiritgan son katta.")
#             else:
#                 print(f"Tabriklaymiz! Siz {urinishlar} urinishda to'g'ri topdingiz!")
#                 break
#         except ValueError:
#             print("Iltimos, faqat son kiriting!")

# # O'yinni boshlash
# raqam_topish_oyini()





# import random

# def raqam_topish_oyini():
#     print("1 dan 100 gacha bo'lgan sonni toping!")
#     tasodifiy_son = random.randint(1, 100)  # Kompyuter tasodifiy son tanlaydi
#     urinishlar = 0

#     while True:
#         try:
#             foydalanuvchi_soni = int(input("Son kiriting: "))
#             urinishlar += 1

#             if foydalanuvchi_soni < tasodifiy_son:
#                 print("Xato! Siz kiritgan son kichik.")
#             elif foydalanuvchi_soni > tasodifiy_son:
#                 print("Xato! Siz kiritgan son katta.")
#             else:
#                 print(f"Tabriklaymiz! Siz {urinishlar} urinishda to'g'ri topdingiz!")
#                 break
#         except ValueError:
#             print("Iltimos, faqat son kiriting!")

# # O'yinni boshlash
# raqam_topish_oyini()


# masala yechish ishlari
# def sonlar_yigindisi(*sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return f"{sonlar} royhat elementlarining yigindisi = {yigindi}"
# print(sonlar_yigindisi(2, 4, 4, 5, 8, 9, 12, 100, 36, 68))


