'''
THIS IS A COMMON INTERVIEW QUESTION

KEY TAKE AWAY:
  be careful about the order you place your conditionals
    the more specific it is the sooner it needs to be called!

  
So we're going to write a program that prints the numbers from 1 to 100 but for multiples of 3 it prints Fizz. So it prints a string of fizz instead of the number and for the multiples of five it prints Buzz for the numbers which are multiples of both 5 and 3 then you're going to print out fizz buzz. 
'''

def fizz_buzz (num):
  for i in range(1,num+1):
    if i %3 == 0 and i %5 == 0:
      print('FizzBuzz')
    elif i %3 == 0:
      print('Fizz')
    elif i %5 == 0:
      print ('Buzz')
    else:
      print(i)
  

fizz_buzz(50)

'''
JORDAN'S PERSONAL SOLUTION

def fizz_buzz(max_num):
  for num in range(1, max_num + 1):
    if num % 3 == 0 and num % 5 == 0:
      print('FizzBuzz')
    elif num % 5 == 0:
      print('Buzz')
    elif num % 3 == 0:
      print('Fizz')
    else:
      print(num)


fizz_buzz(100)
'''