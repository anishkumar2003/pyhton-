import random
s=random.random()*200#the random.random()method return a random flot between 0.0 to 1.0. the function does not need any arguments. we can change the value by multiplythe module by any number
print(s)
"""generate random integer"""
c=random.randint(0,100)
print(c)
"""generate random number with in range"""
d=random.randrange(1,10)
print(d)
e=random.randrange(1,10,2)
print(e)
"""shuffle elements randomly"""
numbers=[12,13,14,15,16,17]
random.shuffle(numbers)
print(numbers)
