#!/usr/bin/env python
# coding: utf-8

# # print number of  vowel in a string

# In[1]:


a=input("enter a string:")
vowel=0
for i in a:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowel+=1
print("number of vowels:",vowel)        
    


# # swap two number without using third variable

# In[2]:


a= int(input("enter a number1:"))
b= int(input("enter a number2:"))
a=a+b
b=a-b
a=a-b
print("a is:",a,"b is:",b)


# # reverse a number

# In[3]:


a=int(input("enter a number:"))
rev=0
while(a>0):
    dig=a%10
    rev=rev*10+dig
    a=a//10
    print("reverse the number:",rev)


# # palindrome

# In[8]:


number = int(input("enter a number:"))
temp=number
rev=0
while(number>0):
    dig=number%10
    rev=rev*10+dig
    number=number//10
if temp==rev:
    print("number is palindrome:")
else:
    print("not a palindrome:")


# # reverse a string

# In[11]:


string=input("enter a string:")[::-1]
print(string)

#txt = "Hello World" [::-1]
#print(txt)


# # star pattern right angel
# 
# 

# In[12]:


n=5
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()    


# In[14]:


n=5
for i in range(n):
    for j in range(i+1): 
        print('*',end=' ')
    print()    


# In[16]:


n=5
for i in range(n):
    for j in range(i,n): 
        print('*',end=' ')
    print()


# In[18]:


n=5
for i in range(n):
    for j in range(i,n): 
        print(' ',end=' ')#hwew we give 'space'
    for j in range(i): 
        print('*',end=' ')
    for j in range(i+1): 
        print('*',end=' ')
    print()
    


# In[21]:


n=5
for i in range(n):
    for j in range(i+1): # done i+1
        print(' ',end=' ')
    for j in range(i,n-1): # i -1
        print('*',end=' ')
    for j in range(i,n): #i,n
        print('*',end=' ')
    print()


# # lambda function

# In[25]:


x = lambda a:a*a
print(x(8))


# # find dublicate value from a list

# In[36]:


numbers = [1,2,3,4,5,6,6,1,2]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]==numbers[j]:
            print(numbers[i]+"is a dublicate")
            break


# In[39]:


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
    
x = Person("vaibhav", "upadhyay")
x.printname()


# In[42]:


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
    
  class Student(Person):
    pass


# In[46]:


x=Person("vaibhav","singh")
x.printname()


# In[ ]:




