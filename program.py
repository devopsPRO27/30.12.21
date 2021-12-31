'''this
is
 a
 comment
  section
  '''
#this is a comment line

#print('33 st')

numb1=7
numb2=9
ans=numb1/numb2
print('before error')
print(anr)
print('after error')

number1=input('please enter a number :')
print(number1)
print(type(number1))
number1=int(number1)
print(number1)
print(type(number1))


number1=int(input('please enter a number :\n '))
number2=int(input('please enter the second number : '))
#answer=number1+number2
print('{}+{}={}'.format(number1,number2,number1+number2))
print(number1,'+',number2,'=',number1+number2)


x=int(input())
if x==9 :
    print('equal')
else :
    print('not equal')
print('thank you')'''
'''n1=int(input('please enter a number : '))
n2=int(input('please enter the second number : '))
if n2==0:
    print("machane is zero")
else:
    ans=n1/n2
    print(ans)

'''
תכתבו תוכנית שתקלוט מהמשתמש את הגיל שלו ותבדוק 
אם הגיל מתחת ל 12 תדיפס ילד 
אחרת תדפיס מבוגר 
'''

age=int(input("please enter your age "))
if age >0:
    if age<5:
        print('baby')
    elif age < 12:
            print('hi kid')
    else:
            print('hii adult')
else :
    print("wrong input")

x=int(input())

if x>0 and x<=17 :
    print('hii boss')
else:
    print("hii worker")
    s='sadasdas'
    print(s)
