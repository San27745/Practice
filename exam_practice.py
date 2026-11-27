# def greeting(name):
#     def hello():
#         return "Hello, " + name + "!"
#     return hello
# greet = greeting("Students")
# print(greet())

# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1
# for num in count_up_to(5):
#     print(num)

# import math as m
# print(m.sqrt(16))
# l=[1,45,3,56,90,0]
# print(min(l))
# print(max(l))
# print(m.pow(4,2))
# print(abs(-56)) #it converts the value in positive
# print(m.factorial(4))
# print(m.ceil(10.89))
# print(m.floor(10.89))
# print(m.pi)

# import random as r
# l=[1,45,3,56,90,0]
# print(r.random())
# print(r.randint(10,20))
# print(r.choice(l))
# r1=r.shuffle(l)
# print(l) #using shuffle the value in list are shuffled

# import datetime as d
# print(d.date.today())
# print(d.datetime.now(),)
# twenty=d.datetime.now()+d.timedelta(minutes=20) #display time of next 20 minute 
# ten=d.date.today()+d.timedelta(days=10)     #display 10 days date from now
# print(ten)
# print(twenty)
