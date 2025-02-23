#ELEVENTH

#create dict and search name

"""a=eval(input("enter the no. of customers:"))
b={}
for i in range(a):
    c=input("enter the customer name:")
    d=input("enter the items bought:")
    f=input("enter cost")
    g=input("enter phone number")
    b[c]=d,f,g
print("\ncustomer name \t\titems bought \t\tcost \tphone number")
for j in b:
    print(j,"\t",b[j])
e=input("enter the customer name to be searched:")
for k in b:
    if k==e:
        print("customer name",k,"\t","details",b[k])"""

#count frequency

'''c=()
a=()
b=tuple(eval(input("enter comma separated values:")))
for i in b:
    if i not in a:
        a+=(i,)
        c=b.count(i)
        print(i,"occurs",c,"times")  '''
'''have to check again'''

#create dict and delete name

"""d=dict()
a=eval(input("enter no of students:"))
for i in range(a):
    b=input("enter students name:")
    c=eval(input("enter percentage:"))
    d[b]=c
print(d)
e=input("enter student name to be deleted:")
for j in d:
    if j==e:
        del d[j]
print(d)"""

#    palindrome

'''a=int(input("enter"))
b=a%100
c=str(a//100)
d=str(b//10)
f=str(a%10)
print(f+d+c)
if str(a)==f+d+c :
    print("no.is palindrome")
else:
    print("no.is not palindrome")'''

#create the pattern

'''*
**
***
****
*****
for i in range(0,5):
    for j in range(1,i+1):
        print("*",end='')
    print("")'''


'''5
54
543
5432
54321
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
            print(j,end='')
    print("")'''


'''1
12
123
1234
12345
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print("")'''

#armstrong number

'''a=int(input("enter"))
b=a%100
c=(a//100)
d=(b//10)
f=(a%10)
sum=c**3+d**3+f**3
if sum==a:
    print("yes")
else:
    print("no")'''

#animation
"""from turtle import *
import colorsys
bgcolor("black")
tracer(1000)
def draw():
    h=0
    for i in range (100):
        c=colorsys.hsv_to_rgb(h,1,1)
        h+=0.5
        up()
        goto(0,0)
        down()
        color("black")
        fillcolor(c)
        begin_fill()
        rt(98)
        circle(i,12)
        fd(290)
        fd(i)
        lt(29)
        for j in range(129):
            fd(i)
            circle(j,299,steps=2)
        end_fill()
draw()
done()"""

#ME
"""a=input("how's ur life going on")
b=input("what's hurting u the most?")
print("dnt feel sad dear U r very special for urself noone else cares not even ur family so dnt cry and be happy for someone who only wants to see u happy Have faith in god everything will be fine darling If today noone cares for u or trust u just wait for some years get successful for urself not for others Return the each and every ruppe to ur parents that they have invested on u by tripling the amount Dnt be sad sweetheart)"""

#TWELFTH

#2.74,ques49
"""def LeftShift(lst,x):
    a=[]
    for i in range(len(lst)):
        if i>=x:
           a.append(lst[i])
    for j in range(len(lst)):
        if j<x:
           a.append(lst[j])
    return a
lst=list(eval(input("enter elements separated by commas")))
x=int(input("enter place value where list to be shifted"))
b=LeftShift(lst,x)
print(b) """   

#2.74,ques46
'''def tue(t):
    a=0
    for i in range(len(t)):
        a+=t[i]
    print(a/len(t))
t=tuple(eval(input("enter tuple:")))
tue(t)'''

#2.74,ques43          
"""def prime_no(N):
    
    for i in range(2,N+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
a=int(input("enter no. of prime numbers:"))
prime_no(a)"""

#ch-4 data file handling


'''f=open("gurasees.txt","w")
f.write("beleive in yourself girl!!!!!\n")
f.write("you can do it\n")
f.write("if you can't then nobody can't\n")
f.write("believe in god and do hardwork\n")
f.close()'''

#ques 26
'''f=open("asees.txt","w")
a=''
while a!="END":
    a=input("enter line or END to end ")
    f.write(a)
    f.write("\n")
f.close()
f1=open("asees.txt","r")
l=f1.readline()
while l:
    for i in l:
        if i=="#":
            print(l)
    l=f1.readline()
f1.close()'''

'''f=open("gurasees.txt","r")
print(f.read(2))
print(f.readlines())
print(f.read(3))
print("remaining data")
print(f.read())'''

#1
"""countvowel=0
countconsonant=0
countupper=0
countlower=0
f=open("asees.txt","r")
f1=f.read()
print(f1)
for i in f1:
    if i in ('a','e','i','o','u','A','E','I','O','U'):
        countvowel+=1
    elif i not in("a","e","i","o","u","A","E","I","O","U"," ","\n"):
        countconsonant+=1
for j in f1:
    if j.isupper():
        countupper+=1
    elif j.islower():
        countlower+=1
print("no.of vowels are",countvowel)
print("no. of consonant are",countconsonant)
print("no.of uppercase letters are",countupper)
print("no.of lowercase letters are",countlower)"""

'''s="Racecar Car Radar"
l=s.split()
for w in l:
    x=w.upper()
    if x==x[::-1]:
        for i in x:
            print(i,end="*")
    else:
        for i in w:
            print(i,end="#")
    print()'''



"""def computepay(hours,rate):
    print("in computepay",hours,rate)
    if hours>40:
        reg=rate+hours
        otp=(hours-40.0)+(rate*0.5)
        pay=reg+otp
    else:
        pay=hours*rateprint("returning",pay)
        return pay
sh=input("enter hours:")
sr=input("enter rate:")
fh=float(sh)
fr=float(sr)
xp=computepay(fh,fr)
print("pay:",xp)"""

#1
n=int(input())
b=[]
for i in range(n):
    a=int(input())
    b.append(a)
c=max(b)-min(b)
print(c)
#1
a=int(input())
if a<=2:
    print("0")
elif a>2 and a<11:
    fee=0
    for i in range(a-2):
        fee+=10
    print(fee)
else:
    print("100")
#2
a=int(input())
b=[]
for i in range(a):
    c=list(map(int,input().split(" ")))
    b.append(c)
value=[]
for j in b:
    s=sum(j)
    value.append(s)
print(max(value))
#matrix
def sum_of_borders(matrix, N, M):
    total_sum = 0
    total_sum += sum(matrix[0])
    if N > 1:
        total_sum += sum(matrix[N-1])
    for i in range(1, N-1):
        total_sum += matrix[i][0]  
        total_sum += matrix[i][M-1]    
    return total_sum
N,M = map(int, input().split())  
matrix = [list(map(int, input().split())) for _ in range(N)]  
print(sum_of_borders(matrix, N, M))
#armstrong
a=int(input("enter"))
b=a%100
c=(a//100)
d=(b//10)
f=(a%10)
sum=c**3+d**3+f**3
if sum==a:
    print("yes")
else:
    print("no")
#palindrome
a=int(input("enter"))
b=a%100
c=str(a//100)
d=str(b//10)
f=str(a%10)
print(f+d+c)
if str(a)==f+d+c :
    print("no.is palindrome")
else:
    print("no.is not palindrome")
#reverse a number
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10 
        reversed_num = reversed_num * 10 + digit  
        num = num // 10 
    return reversed_num
number = int(input())
reversed_number = reverse_number(number)
print(f"Reversed number: {reversed_number}")
#fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
a = int(input())
print(a * fibonacci(a - 1))
