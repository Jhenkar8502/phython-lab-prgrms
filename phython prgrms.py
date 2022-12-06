#!/usr/bin/env python
# coding: utf-8

# In[1]:


radius=int(input('enter the value'))
Area=3.14*radius*radius
Perimeter=2*3.14*radius
print(Area)
print(Perimeter)


# In[2]:


sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
print(avg)


# In[3]:


n=int(input("Enter the number: "))
c=0
a=1
b=1
if n==0 or n==1:
    print("Yes")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("Yes")
    else:
        print("no")


# ser_input = input("What's your favourite language? ")
# print("My favourite language is ", user_input.upper())

# In[4]:


print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Your height is : %d cm." % h_cm)


# In[5]:


rows = 6
for i in range(1, rows + 1):
    for j in range(1, i - 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()


# In[6]:


string='abcde'
replacestring=''
for letter in string:
    code=ord(letter)
    next_letter=chr(code+1)
    replacestring=replacestring+ next_letter

print(replacestring)


# In[ ]:




