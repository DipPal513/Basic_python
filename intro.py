# get output...
# print("hello world");

# this is condition
# if 5>2:
    # print("five is greater than two...")
# if 200>199:
    # print("its a huge amount...")

    # this is comment

# Python variable

x = 3; 
name = 'Pritom Paul Dip'

# number cannot be the first letter of a variable name
# converter
y = str(4)
f = int(4)
z = float(44)

u = 4.34;
# print(type(u))
# class float


# single Quote and Double Quote are same


w = 'wick';
W = 33;
# w will not replace W

m,n,z = "hola",'hola','yo';

sakib=rakib=Nagib = 'Simp';

# unpack a collection/list

fruits = ['apple','bananna','cherry']
l,a,k = fruits


# this is a global variable that can be used by everyone
d = 'awesome'

def myfunc():
    print('it is '+ d)


myfunc();

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)