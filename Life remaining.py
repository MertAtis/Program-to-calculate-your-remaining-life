# (TR) 90 yaşına kadar yaşayacağınızı düşünerek. Şimdiki yaşınızı yazdığınızda kalan ömrünüzü gün hafta ve ay olarak hesaplayacak bir program yazıyoruz. 
# 1 Yıl = 365 gün ve 52 hafta ve 12 ay olarak hesaplanacaktır.
#(ENG) Thinking you've lived to the age of ninety. We write a program that will calculate your remaining lifespan as a day week and month when you write down your current age.
age = input("How old are you?\n")
age1=int(age)
day = 32850- age1*365
week= 4680- age1*52
month=1080- age1*12
print(f"Your remaining life is {day} day , {week} week , {month} month")


