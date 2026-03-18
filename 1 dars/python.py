# sonlar = list(range(10,100,))
# print(sonlar)

# for x in range(1,101):
#     print(x)

# ism1 = input("Ismingizni kiriting: ")
# while ism1 != (ism1):
#     ism2 = input("Ismingizni kiriting: ")
# while ism2 != (ism1):
#     ism  = input("Ismingizni kiritig")
#     print("To'gri")


    # Foydalanuvchidan 2 ta ism soraladi yani (input) 1 ism 2 ismga teng bolmaguncha foydalanuvchidan ism qayta qayta so'ralaveradi


# haqiyqiy_ism = input("Ismingizni kiriting: ")

# random_ism = input("Ismingizni kiriting: ")
# while random_ism != haqiyqiy_ism:
#     random_ism = input("Ismingizni kiriting: ")

# print("To‘g‘ri")

# MinimalYosh = 16
# FoyYosh = int(input("Yoshingizni yozing: "))
# if MinimalYosh <= FoyYosh:  
#     print("ovoz berishingiz mumkin !")
# if MinimalYosh > FoyYosh:
#     print("Hali yosh ekansiz")



# haqiyqiy_ism = input("Ismingizni kiriting: ")

# random_ism = input("Ismingizni kiriting: ")
# if haqiyqiy_ism == random_ism:
#     print("Bu mening ismim")
# else:
#     random_ism = input("Bu ism meniki emas!")


# gb = input("qiymat kiriting :")
# if gb.isdigit():
#     gb = float(gb)
#     mb = gb * 1024
#     print(f"{gb} gegabeyt {mb} megabaytga teng")


# tanlov = input("1 - GB ni MB ga o'tkazish, 2 - MB ni GB ga o'tkazish. Tanlang (1 yoki 2): ")

# if tanlov == "1":
#     gb = input("Gigabayt qiymatini kiriting: ")
#     if gb.isdigit():
#         gb = float(gb)
#         mb = gb * 1024
#         print(f"{gb} gigabayt {mb} megabaytga teng.")
#     else:
#         print("Iltimos, to'g'ri raqam kiriting!")

# elif tanlov == "2":
#     mb = input("Megabayt qiymatini kiriting: ")
#     if mb.isdigit():
#         mb = float(mb)
#         gb = mb / 1024
#         print(f"{mb} megabayt {gb} gigabaytga teng.")
#     else:
#         print("Iltimos, to'g'ri raqam kiriting!")

# else:
#     print("Noto'g'ri tanlov! Faqat 1 yoki 2 ni tanlang.")


# # oziga yuklatilgan vazifani qayta qayta bajaruvchi element

# son1 = int(input("sin 1 ni kiriting : "))
# son2 = int(input("sin 2 ni kiriting : "))
# print(son1 + son2)

# # keyword, syntaxsys
# def UY():
#     son1 = int(input("son 1 :"))
#     son2 = int(input("son 2 :"))
#     print(son1 + son2)
# def UYy(son1, son2, son3, son4, son5):
#     print(son1+son2+son3+son4+son5)

# UYy(1,2,3,4,5)
# UYy(6,7,8,9,10)

# None

# # ayirma
# def ayirma(a,b):
#     return(a-b)
    
# javob = ayirma(100,85)
# print(javob)


# # yigindi
# def yigindi(a,b):
#     return(a+b)

# javob = yigindi(10,8)
# print(javob)

# # kopaytma
# def kopaytma(a,b):
#     return(a**b)
    
# javob = kopaytma(10,3)
# print(javob)


# # bolinma
# def bolinma(a,b):
#     return(a/b)

# javob = bolinma(100,2)
# print(javob)


# def unliHarflar(text):
#     unlilar = ["a","e","i","o","u","o'"]

#     for unli in unlilar:
#         print(f"{text} ning ichida {text.lower().count(unli)} unli {unli} harfi bor")

# unliHarflar("Assalom")





# def unliHarflar(text):
#     unlilar = ["q","w","r","t","y","p","l","k","j","h","g","f","d","s","z","x","c","v","b","n","m"]

#     for unli in unlilar:
#         print(f"{text} ning ichida {text.lower().count(unli)} unli {unli} harfi bor")

# unliHarflar("Assalom")



# def PowerA3(a,b):
#     return(a**b)
    
# javob = PowerA3(10,3)
# print(javob)



# son = -34.89

# if son > 0:
#     print("Siz kiritgan son musbat")
# else:
#     print("Siz kiritgan son manfiy")


# son = float(input("Ixtiyoriy son kiriting men uni sizga - yoki + ekanini aniqlab beraman"))
# if son > 0:
#     print("Siz kiritgan son musbat")
# else:
#     print("Siz kiritgan son manfiy")


# 1
# son = int(input("Ihtiyoriy son kiriting : "))
# if son < 0:
#     print(f"Siz kiritgan son manfiy {son+0}")
# else:
    
#     print(f"Siz kiritgan son musbat {son+1}")



# 2
# son = int(input("Ihtiyoriy son kiriting : "))
# if son < 0:
#     print(f"Siz kiritgan son manfiy {son-2}")
# else:
    
#     print(f"Siz kiritgan son musbat {son+1}")



# 3
# son = int(input("Ihtiyoriy son kiriting : "))
# if son < 0:
#     print(f"Siz kiritgan son manfiy {son-2}")
# elif son == 0:
#     print(f"Siz kiritgan son 0 ga teng {son+10}")
# else:
#     print(f"Siz kiritgan son musbat {son+1}")



# # 4
# son1 = int(input("1 sonni kiriting : "))
# son2 = int(input("2 sonni kiriting : "))
# son3 = int(input("3 sonni kiriting : "))
# if son1 > 0:
#     print(f"{son1} musbat son")
# elif son1 < 0:
#     print(f"{son1} manfiy son")
# elif son2 > 0:
#     print(f"{son2} musbat son")
# elif son2 < 0:
#     print(f"{son2} manfiy son")
# elif son3 > 0:
#     print(f"{son3} musbat son")
# elif son3 < 0:
#     print(f"{son3} manfiy son")
# else:
#     print(f"hech qaysi son musbat emas")

# son = son1,son2,son3        
# print(son)



# ism = input("Ismingizni kiriting : ")
# mashinalarqiymati = int(input("Necha mln pulingiz bor : "))
# if mashinalarqiymati <= 10:
#     print(f"{ism} siz TICO olishingiz mumkin")
# elif mashinalarqiymati <= 40:
#     print(f"{ism} siz Maskvich olishingiz mumkin")
# elif mashinalarqiymati <= 120:
#     print(f"{ism} siz Nexia olishingiz mumkin")
# elif mashinalarqiymati <= 210:
#     print(f"{ism} siz Malibu olishingiz mumkin")
# elif mashinalarqiymati <= 350:
#     print(f"{ism} siz BYD olishingiz mumkin")
# else:
#     print("Pulingizni menga berishingiz mumkin")



# ism = input("Ismingizni kiriting : ")
# mashinalarqiymati = int(input("Necha mln pulingiz bor : "))
# if mashinalarqiymati <= 10:
#     print(f"{ism} siz TICO olishingiz mumkin")
# elif mashinalarqiymati <= 40:
#     print(f"{ism} siz Maskvich olishingiz mumkin")
# elif mashinalarqiymati <= 120:
#     print(f"{ism} siz Nexia olishingiz mumkin")
# elif mashinalarqiymati <= 210:
#     print(f"{ism} siz Malibu olishingiz mumkin")
# elif mashinalarqiymati <= 350:
#     print(f"{ism} siz BYD olishingiz mumkin")
# else:
#     print("Pulingizni menga berishingiz mumkin")




# kitoblar = []

# while True:
#     kitob = input("Yaxshi ko'rgan kitobingizni kiriting : ")
#     if kitob.lower() == "stop":
#         break
#     else:
#         kitoblar.append(kitob)
# print("Dastur tugadi")





# ism = input("Ismingizni kiriting : ")
# narx = 2000
# narx1 = 3000
# narx2 = 10000
# yosh = int(input(f"{ism} yoshingizni kiriting : "))
# if yosh <= 7:
#     print(f"{ism} siz yosh ekansiz siz uchun chipta narxi {narx} som")
# elif yosh > 7 and yosh <= 18:
#     print(f"{ism} siz uchun chipta narxi {narx1} som")
# elif yosh > 18 and yosh <= 50:
#     print(f"{ism} siz uchun chipta narxi {narx2} som")
# else:
#     yosh > 50
#     print(f"{ism} siz ancha katta ekansiz sizga chipta bepul")
    

# # telefonlar = []

# # while True:
# #     telefonlar = input("Yaxshi ko'rgan telefoningizni kiriting : ")
# #     if telefonlar.lower() == "stop":
# #         print("dastur toxtatildi")
# #     elif telefonlar == ("Iphone 17 pro"):
# #      print("Iphone 17 pro yaxshi telefon lekin zaryadi kop vaqtga yetmaydi")
# #     break
# # else:
# #         telefonlar.append(telefonlar)
# # # print("Dastur tugadi")



# telefonlar = []
# print("Telefonlar nomini kiriting : (malumot kiritishni xoxlamasangiz yoq deb yozing) ")
# son = 1
# while True:
#     telefon = input(f"{son} - telefonni kiriting : ")
#     if telefon == 'yoq':
#         break
#     telefonlar.append(telefon)
#     son += 1
# print(telefonlar)

# uzunlik = len(telefonlar)
# son2 = 1


# while son2 <= uzunlik:
#     savol = telefonlar.pop()
#     print(f"{savol.title()} zo'r telefon amma ko'pchilikga yoqmaydi")
#     son2 += 1


# #          Birinchi vazifa
# def kopaytma(a,b,c,d):
#     kopaytma = a * b * c * d
#     print(kopaytma)
# kopaytma(10,25,8,2)



# #          Ikkinchi vazifa
# def darajaga_oshirish(a,b):
#     darajaga_oshirish = a ** b
#     print(darajaga_oshirish)
# darajaga_oshirish(45,24)



# def kopaytma(a, b, c, d):
#     "a,b,c,d qiymatlarni ko'paytma ko'rinishida chiqaruvchi function"
#     natija = a * b * c * d
#     return natija
# print(kopaytma(10, 25, 8, 2))


# def darajaga_oshirish(a, b):
#     "a sonini b inchi darajasini aniqlovchi function"
#     return a ** b
# print(darajaga_oshirish(45, 24))


# def maksimum(a, b):
#     "a va b sonlaridan kattasini aniqlovchi function"
#     if a > b:
#         return a
#     else:
#         return b
# print(maksimum(10, 25))


# def ishorani_aniqlash(a):
#     "a sonini manfiy yoki musbat yoki nolga teng ekanini aniqlovchi function"
#     if a > 0:
#         return "Musbat"
#     elif a < 0:
#         return "Manfiy"
#     else:
#         return "Nol"
# print(ishorani_aniqlash(-34.89))


# def salom_ber(ism):
#     "Foydalanuvchidan ismni qabul qilib, unga salom beruvchi function"
#     return f"Salom, {ism}!"
# print(salom_ber("Ali"))


# def oliy_talimga_kirish(kirish_bali, ozingizning_balingiz):
#     "Oliy talimga kirishni aniqlash (sirtqi, kontrakt, grant)"
#     if ozingizning_balingiz >= kirish_bali + 30:
#         return "Siz grant asosida o‘qishga kirdingiz "
#     elif ozingizning_balingiz >= kirish_bali:
#         return "Siz kontrakt asosida o‘qishga kirdingiz "
#     else:
#         return "Siz o‘qishga kira olmadingiz "
# print(oliy_talimga_kirish(100, 130))


# def yoshni(yosh):
#     "Foydalanuvchidan yoshni qabul qilib, uning yosh toifasini aniqlovchi function"
#     if yosh < 0:
#         return "Yosh manfiy bo'lishi mumkin emas"
#     elif yosh <= 12:
#         return "Siz bolaliksiz"
#     elif yosh <= 19:
#         return "Siz o'smirlikdasiz"
#     elif yosh <= 59:
#         return "Siz kattaliksiz"
#     else:
#         return "Siz qariyapsiz"


# def qoshish_ayirish_bolish_kopaytirish(a, b, c):
#     qoshish = a + b + c
#     ayirish = a - b - c
#     bolish = a / b / c
#     kopaytirish = a * b * c
#     return qoshish, ayirish, bolish, kopaytirish
# natijalar = qoshish_ayirish_bolish_kopaytirish(10, 5, 15)
# print(natijalar)


# def orta_geometrik(a,b,c,d):
#     geometrik = (a * b * c * d) ** (1/4)
#     return geometrik
# natija = orta_geometrik(10, 25, 8, 2)
# print(natija)


# def orta_arifmetik(a,b,c,d,e,f,g):
#     arifmetik = (a + b + c + d + e + f + g) / 7
#     return arifmetik
# natija = orta_arifmetik(10, 25, 8, 2, 15, 20, 30)
# print(natija)



# maxsulotlar = ["olma", "xoddog", "pecheniya", "cola", "ruchka", "daftar"]
# print(f"Hush kelibsiz bizda {maxsulotlar} mahsulotlari bor")
# def savdogarlik(maxsulot):
#     if maxsulot == "olma":
#         print(f"Olma 5000 so'm")
#     elif maxsulot == "xoddog":
#         print(f"Olma 5000 so'm")
#     elif maxsulot == "pecheniya":
#         print(f"Olma 5000 so'm")
#     elif maxsulot == "cola":
#         print(f"Olma 5000 so'm")
#     elif maxsulot == "ruchka":
#         print(f"Olma 5000 so'm")
#     elif maxsulot == "daftar":
#         print(f"Olma 5000 so'm")
# print(savdogarlik("olma"))






# mashinalar = {
#     "malibu": 35000, 
#     "nexia": 10000,
#     "cobalt": 15000,
#     "gentra": 18000,
#     "spark": 8000,
#     "captiva": 40000,
#     "tracker": 25000
# }

# print(f"Hush kelibsiz! Bizda quyidagi mashinalar mavjud: {', '.join(mashinalar.keys())}")

# def mashina_narxi(mashina):
#     if mashina.lower() in mashinalar:
#         narx = mashinalar[mashina.lower()]
#         print(f"{mashina.capitalize()} narxi {narx} $")
#     else:
#         print("Kechirasiz, bizda bunday mashina haqida ma'lumot yo'q.")


# mashina_narxi("Malibu")  
# mashina_narxi("Nexia")   
# mashina_narxi("Tesla")   

# def qoshish(a, b):
#     return f"{a}+{b} = {a + b}"

# natija = qoshish(5, 7)
# print(f"Natija: {natija}")  

# def ayirma(a, b):
#     return a - b

# natija = ayirma(10, 3)
# print(f"Natija: {natija}")

# def kopaytirish(a, b):
#     return a * b

# natija = kopaytirish(4, 6)
# print(f"Natija: {natija}")


# def bolish(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Nolga bo'lish mumkin emas"
# natija = bolish(20, 0)
# print(f"Natija: {natija}")


# def kvadrat(a, b):
#     return a ** b

# natija = kvadrat(12,5)
# print(f"Natija : {natija}")


# def kvadrat(a):
#     return a ** 3

# natija = kvadrat(12)
# print(f"Natija : {natija}")




# def arifmetik(a,b,c):
#     return (a + b + c) / 3

# natija = arifmetik(12,158,6)
# print(f"Natija : {natija}")


# def maksimal(a, b):
#     if a > b :
#         return print(f"{a} soni {b} sonidan katta")
#     elif b > a :
#         return  print(f"{b} soni {a} sonidan katta")
#     elif a == b :
#         print(f"{a} soni {b} soniga teng")
#     else:
#         return "Ikkala son ham teng"

# maksimal(45,8)



# def minimal(a, b):
#     if a < b :
#         return print(f"{a} soni {b} sonidan kichik")
#     elif b < a :
#         return  print(f"{b} soni {a} sonidan kichik")
#     elif a == b :
#         print(f"{a} soni {b} soniga teng")
#     else:
#         return "Ikkala son ham teng"

# minimal(45,8)





# def True_False(a):
#     if a > 0:
#         return "True"
#     elif a < 0:
#         return "False"
#     else:
#         return "Nol"
# print(True_False(34))




# def ishorani_aniqlash(a):
#     if a > 0:
#         return "Musbat"
#     elif a < 0:
#         return "Manfiy"
#     else:
#         return "Nol"
# print(ishorani_aniqlash(15))




# def baholash(a):
#     if a > 0 and a < 30:
#         return print(f"Siz {a} ball oldingiz. Sizning bahoyingiz 2 !! O'z ustingizda ko'proq ishlang")
#     elif a > 30 and a <= 60:
#         return print(f"Siz {a} ball oldingiz. Sizning bahoyingiz 3")
#     elif a > 61 and a <= 86:
#         return print(f"Siz {a} ball oldingiz. Sizning bahoyingiz 4")
#     elif a > 87 and a <= 100:
#         return print(f"Siz {a} ball oldingiz. Sizning bahoyingiz 5")
    
# print(baholash(15))




# def parol(password):
#     return len(password) > 8

# parol1 = input("Parolni kiriting: ")
# if parol(parol1):
#     print("Parol qabul qilindi!")
# else:
#     print("Parol juda qisqa, kamida 8 ta belgidan iborat bo'lishi kerak.")






# def factorial(n):
#     if n == 0 or n == 1:  
#         return 1
#     else:
#         return n * factorial(n - 1)  

# son = int(input("Faktorialini hisoblash uchun son kiriting: "))
# print(f"{son} = {factorial(son)}")






# def sonni_topish(n):
#     return len(str(abs(n)))  

# son = int(input("Sonni kiriting: "))
# print(f"{son} soni {sonni_topish(son)} xonali.")






# def list_sum(numbers):
#     return sum(numbers) 

# raqamlar = [1, 2, 3, 4, 5]
# print(f"Ro'yxat elementlari yig'indisi: {list_sum(raqamlar)}")



def menyu():
    print("\nHisob-kitoblar menyusi:")
    print("1. Qo'shish")
    print("2. Ayirish")
    print("3. Ko'paytirish")
    print("4. Bo'lish")
    print("5. Darajaga ko'tarish")
    print("6. Kvadrat ildiz")
    print("7. Chiqish")

def hisoblash():
    import math

    while True:
        menyu()
        tanlov = input("\nAmalni tanlang (1-7): ")

        if tanlov == "7":
            print("Dasturdan chiqildi. Xayr!")
            break

        try:
            if tanlov in ["1", "2", "3", "4", "5"]:
                son1 = float(input("Birinchi sonni kiriting: "))
                son2 = float(input("Ikkinchi sonni kiriting: "))

                if tanlov == "1":
                    print(f"Natija: {son1} + {son2} = {son1 + son2}")
                elif tanlov == "2":
                    print(f"Natija: {son1} - {son2} = {son1 - son2}")
                elif tanlov == "3":
                    print(f"Natija: {son1} * {son2} = {son1 * son2}")
                elif tanlov == "4":
                    if son2 == 0:
                        print("Xatolik: 0 ga bo'lish mumkin emas!")
                    else:
                        print(f"Natija: {son1} / {son2} = {son1 / son2}")
                elif tanlov == "5":
                    print(f"Natija: {son1} ^ {son2} = {son1 ** son2}")

            elif tanlov == "6":
                son = float(input("Sonni kiriting: "))
                if son < 0:
                    print("Xatolik: Manfiy sonning kvadrat ildizi mavjud emas!")
                else:
                    print(f"Natija: √{son} = {math.sqrt(son)}")

            else:
                print("Noto'g'ri tanlov! Iltimos, 1 dan 7 gacha bo'lgan raqamni tanlang.")

        except ValueError:
            print("Xatolik: Iltimos, faqat son kiriting!")

# Dastur ishga tushiriladi
hisoblash()
print("f")