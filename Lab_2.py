print("---------------TASK 01---------------")
count=0
while count<=5:
    print("Hi")
    count=count+1
print("---------------TASK 02---------------")
print("List iterration")
l=["hi","bye","hiii"]
for i in l:
    print(i)
print("---------------TASK 03---------------")
l=["hi","bye","hiii"]
for index in range(len(l)):
    print (index)
print("---------------TASK 04---------------")
for letter in'geeksforgeeks':
    if letter=='e' or letter=='s':
        continue
    print('Current letter:',letter)
print("---------------TASK 06---------------")
for letter in'geeksforgeeks':
    if letter=='e' or letter=='s':
        break
    print('Current letter:',letter)
print("---------------TASK 07--------------")
def my_function():
    print("Hello from a function")
my_function()
print("---------------TASK 08--------------")
def my_function(fname):
    print(fname+' Refsnes')
my_function("Ali")
my_function("Ahmad")
my_function("Shahzaib")
print("---------------TASK 09--------------")
def my_function(country='Pakistan'):
    print("i am from "+ country)
my_function()
my_function("Australia")
my_function("UK")
print("---------------TASK 10---------------")
def my_function(food):
    for i in l:
        print(i)
l=["hi","bye","hiii"]
my_function(l)
print("---------------TASK 11---------------")
def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(4))
print(my_function(8))


