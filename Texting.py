#!/usr/bin/env python
# coding: utf-8

# In[34]:


#Some of my friends react via text by saying "asda kjldjsflk;a", with a bunch of random letters. I've always wondered their reaction if I made a longer reaction text; one of a few hundred/thousand letters. Now that's a possiblity :)

#Importing the relevant packages
import string #allows me to import the alphabet
import random #allows me to choose random letters of the alphabet


# In[35]:


#Importing the alphabet, lower-case, upper-case, and combined
alphabet= string.ascii_letters
lower_case_alphabet = string.ascii_lowercase
uppper_case_alphabet = string.ascii_uppercase
print(alphabet)


# In[36]:


#The alphabet is a string
type(alphabet)


# In[37]:


#How many letters do I want following the inital asD 
#For the random selection, I'm ensuring that the number (num) is an int
num = int(input("How many letters do you want your message to be? "))


# In[38]:


#confirming the type of the variable, should be int 
type(num)


# In[40]:


check = 52
'''
#Allows the user to input another number if they want a shorter string 
def checker(num):
    while num>check:
        x= int(input("Try again, Type a number less than 52! "))
        num=x
    return num
print("There will be " + str(checker(num)) + " letters in the message")'''


# In[41]:


#function to make the problem work if the inital input is more than 52 
if num > 52:
    num2 = num/52
    num2 = int(num2)
    alphabet= alphabet * num2
    num3 = num2 *52
else:
    num3 = num


# In[42]:


#The beginning of any text
beginning = "asD"


# In[43]:


#Selection of the random letters, num is representating how many letters follow asD
ending=(random.sample(alphabet,num3))
#Below are the random letters selected 
print(ending)


# In[44]:


#Changing the list of random numbers to a string 
str1 = ""
# traverse in the string 
for i in ending:
    str1 += i 
print(str1)


# In[45]:


#changing the variable to a string, to make it compartible to the beginning 
str1 = str(str1)
print(str1)


# In[46]:


#FInal Product 
texting = beginning + str1
print(texting)


# In[ ]:




