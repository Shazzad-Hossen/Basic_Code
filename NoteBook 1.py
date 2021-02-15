# NoteBook 1
# SHAZZAD  HOSSEN
# ID: 191-15-2420
#_________________________________





print("Hello World")

x=7
y=3
print(x+y)
total = x+y
print(total)




name = "Adam"
name2 = "Eva"
print(name , name2)



x =10
type(x)



type(10.5)

type(name)



multiplication = 7*4
 print(multiplication)

add = 10+15
print(add)



sub = 40-8
print(sub)



Exponentiation = 2**10
print(Exponentiation)



True_Division = 7/4
print(True_Division)



Floor_Division = 7//4
print(Floor_Division)



remainder = 15%7
print(remainder)




x =105
y = 100

x>y



x<y

x==y



x!=y

x>=y



x<=y

x = 3
y = 10

1 <= x <= 5

1 <= y <= 5




print('Welcome', 'to', 'Python!')



print('Welcome\nto\n\nPython!')



print('this is a longer string, so we \
 split it over two lines')



print('Sum is', 7 + 3)



print('int(5.2)', 'truncates 5.2 to', int(5.2))

print('Display "hi" in quotes')

print('Display \'hi\' in quotes')

print("Display the name O'Brien")

print("Display \"hi\" in quotes")

print("""Display "hi" and 'bye' in quotes""")

triple_quoted_string = """This is a triple-quoted
string that spans two lines"""

print(triple_quoted_string)



triple_quoted_string



print("""This is a lengthy
multiline string containing
a few lines \
of text""")



a = 3.4536475856



# using "%" to print value till 2 decimal places  
print ("The value of number till 2 decimal place(using %) is : ",end="") 
print ('%.2f' %a)

# using "%" to print value till 4 decimal places  
print ("The value of number till 2 decimal place(using %) is : ",end="") 
print ('%.4f' %a)

name = input("What's your name? ")

print(name)

value1 = input('Enter first number: ')
value2 = input('Enter second number: ')

total = value1 + value2
print(total)

type(total) #python takes input as a string we have to type cast the input

total = int(value1) + int(value2) #type casting to int format
print(total)

"""Getting an Integer from the User by casting the input format"""

another_value = int(input('Enter another integer: '))

print(another_value)

a, b = input().split()

print(a , b)

print(type(a))




number1 = int(input('Enter first integer: '))
number2 = int(input('Enter second integer: '))
number3 = int(input('Enter third integer: '))

min(number1,number2,number3)

max(number1,number2,number3)

"""## **Exercise Solutions :**"""

x=2
y=3
print('x =', x)
print('Value of', x, '+', x, 'is', (x + x))
print('x =')
print((x + y), '=', (y + x))