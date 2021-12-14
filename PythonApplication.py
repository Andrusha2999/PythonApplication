from random import *
from module1 import*
s=[]
def arvud_loendis():
    """
    :param arv n:int
    :param arv mini:int
    :param arv maxi:int
    :rtype int
    """
    
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
        vahetus(mini,maxi)#min=100 maxi=5 miNI=5 maxi=100
        mini,maxi=vahetus(mini,maxi)
        generator(n,loend,a,b)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    jagamine(s,pos,neg,nol)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",null)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    print(s)

def vahetus(a:int,b:int):
    """Kui min suurem kui max,siis vahetame neid omavahel
    :param int a: minimalne arv mis, mis on suurem kui max
    :param int b:maximaalne arv,mis on suurem kui max
    :rtype: int,int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generator(n:int,loend:list,a:int,b:int):
    """
    Genereerib juhusliku arvu vahemikus a ja b ning lisab ta/need loendisse
    """
    for i in range (n):
        loend.append(randint(a,b))
def jagamine(loend:list,p:list,n:list,nol:list):
    """Sorteerib loendite järgi, kui see on suurem kui null, siis ühte, kui vähem, siis teise
    """
    for el in loend:
        if el>0:
            p(append(el))
        elif el<0:
            n(append(el))
        else:
            nol(append(el))

def keskmine(loend,n):
    """
    Näitab keskmisi positiivseid ja keskmisi negatiivseid numbreid
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend,el):
    """
    :param arv el: int and float
    Programm lisab algsele massiivile negatiivse keskmise või positiivse keskmise
    """

    loend(append(el))
    loend(sort())

arvud_loendis()
