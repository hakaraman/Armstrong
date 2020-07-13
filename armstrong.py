num = (input("Lütfen bir sayý giriniz: "))
length =(len(num))
tup = (num,)
amst = (0)
ams = (0)
if not num.isdigit() == True:
    print(num, ": It is an invalid entry. Don't use non-numeric, float, or negative values!")
elif (int(num) < 0):
    print(num, ": It is an invalid entry. Don't use non-numeric, float, or negative values!")
else:
    for i in range(length):  #print(int(tup[0][i])**length)
        amst += (ams + (int(tup[0][i])**length))
    if amst == int(num):
        print(amst, 'is an Armstrong number')
    else:
        print(amst, "is not an Armstrong number")
