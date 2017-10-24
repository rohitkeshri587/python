import datetime
from operator import itemgetter

last5temps=[]

def celsius2kelvin(celsius):
    res1=celsius+273.15
    res1=float(res1)
    return(float(format(res1,'.2f')))

def celsius2fahrenheit(celsius):
    res1=1.8*celsius+32
    res1=float(res1)
    return(float(format(res1,'.2f')))

def kelvin2celsius(kelvin):
    res1=kelvin-273.15
    res1=float(res1)
    return(float(format(res1,'.2f')))

def kelvin2fahrenheit(kelvin):
    res1=1.8*(kelvin-273.15)+32
    res1=float(res1)
    return(float(format(res1,'.2f')))

def fahrenheit2celsius(F):
    res1=(F-32)*5/9
    res1=float(res1)
    return(float(format(res1,'.2f')))

def fahrenheit2kelvin(F):
    res1=((F-32)*5/9)+273.15
    res1=float(res1)
    return(float(format(res1,'.2f')))

def display(L):
    print("-------------- LAST FIVE ENTRIES -------------- ")
    L1=[('FROM VALUE','FROM UNIT','TO VALUE','TO UNIT','DATE')]
    L1+=L
    width=0
    for i in L1:
        for j in i:
            if len(str(j))>width:
                width=len(str(j))
    for item in L1:
        print("{}| {}| {}| {}| {}".format(str(item[0]).ljust(width),str(item[1]).ljust(width),str(item[2]).ljust(width),str(item[3]).ljust(width),str(item[4]).ljust(width)))

while(True):
    print("-----------Temperature Converter------------")
    print("1. Enter new value")
    print("2. View last 5 entries")
    print("Any other key to exit the converter")
    choice=input("\nEnter Choice: ")
    if(choice=='1'):
        print("Enter the new temperature in the following format:")
        print("TEMPERATURE_VALUE(space)UNIT, eg: 21 C")
        print("Supported Units are K(kelvin), F(fahrenheit), and C(celsius)")
        flag=True
        while(flag):
            tempin=input("Enter the temperature value: ")
            L=tempin.split()
            #print(L)
            if len(L)!=2:
                print("INCORRECT ENTRY!")
                print("Enter the new temperature in the following format:")
                print("TEMPERATURE_VALUE(space)UNIT, eg: 21 C")
                print("Supported Units are K(kelvin), F(fahrenheit), and C(celsius)")
                continue
            try:
                res1=float(L[0])
            except ValueError:
                print("INCORRECT ENTRY!")
                print("Enter the new temperature in the following format:")
                print("TEMPERATURE_VALUE(space)UNIT, eg: 21 C")
                print("Supported Units are K(kelvin), F(fahrenheit), and C(celsius)")
                continue
            if L[1] not in ['C','K','F']:
                print("INCORRECT ENTRY!")
                print("Enter the new temperature in the following format:")
                print("TEMPERATURE_VALUE(space)UNIT, eg: 21 C")
                print("Supported Units are K(kelvin), F(fahrenheit), and C(celsius)")
                continue
            print("Choose appropriate option")
            res=float(format(res1,'.2f'))
            while(True):
                if(L[1]=='K'):
                    print("1. Convert to Fahrenheit")
                    print("2. Convert to Celsius")
                    choice=input("Enter choice: ")
                    if choice=='1':
                        res1=kelvin2fahrenheit(res)
                        tovalue='F'
                        now=datetime.datetime.now()
                        time1=now.strftime("%Y-%m-%d %H:%M")
                    elif choice=='2':
                        res1=kelvin2celsius(res)
                        tovalue='C'
                        now=datetime.datetime.now()
                        time1=now.strftime("%Y-%m-%d %H:%M")
                    else:
                        print("INCORRECT INPUT")
                        continue    
                elif(L[1]=='C'):
                    print("1. Convert to Fahrenheit")
                    print("2. Convert to Kelvin")
                    choice=input("Enter choice: ")
                    if choice=='1':
                        res1=celsius2fahrenheit(res)
                        tovalue='F'
                        now=datetime.datetime.now()
                        time1=now.strftime("%Y-%m-%d %H:%M")
                    elif choice=='2':
                        res1=celsius2kelvin(res)
                        tovalue='K'
                        now=datetime.datetime.now()
                        time1=now.strftime("%Y-%m-%d %H:%M")
                    else:
                        print("INCORRECT INPUT")
                        continue
                elif(L[1]=="F"):
                    print("1. Convert to Celsius")
                    print("2. Convert to Kelvin")
                    choice=input("Enter choice: ")
                    if choice=='1':
                        res1=fahrenheit2celsius(res)
                        tovalue='C'
                        now=datetime.datetime.now()
                        time1=now.strftime("%Y-%m-%d %H:%M")
                    elif choice=='2':
                        res1=fahrenheit2kelvin(res)
                        tovalue='K'
                        now=datetime.datetime.now()
                        time1=now.strftime("%Y-%m-%d %H:%M")
                    else:
                        print("INCORRECT INPUT")
                        continue
                row=()
                row=(res,L[1],res1,tovalue,time1)
                if len(last5temps)==5:
                    del(last5temps[0])
                last5temps.append(row)
                #print(last5temps)
                flag=False
                break
    elif choice=='2':
        while(True):
            print("Enter appropriate option to sort results")
            print("1. ASC Order - FROM VALUE")
            print("2. DESC Order - FROM VALUE")
            print("3. ASC Order - TO VALUE")
            print("4. DESC Order - TO VALUE")
            print("5. ASC Order - DATE")
            print("6. DESC Order - DATE")
            print("Any other key to return to main menu")
            choice=input("Enter choice: ")
            if choice=='1':
                temparr=sorted(last5temps,key=itemgetter(0))
                display(temparr)
            elif choice=='2':
                temparr=sorted(last5temps,key=itemgetter(0))[::-1]
                display(temparr)
            elif choice=='3':
                temparr=sorted(last5temps,key=itemgetter(2))
                display(temparr)
            elif choice=='4':
                temparr=sorted(last5temps,key=itemgetter(2))[::-1]
                display(temparr)
            elif choice=='5':
                temparr=sorted(last5temps,key=itemgetter(4))
                display(temparr)
            elif choice=='6':
                temparr=sorted(last5temps,key=itemgetter(4))[::-1]
                display(temparr)
            else:
                break
            
    else:
        print("Thank You")
        break
