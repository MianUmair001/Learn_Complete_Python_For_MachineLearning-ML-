#!/usr/bin/env python
# coding: utf-8

# # Day_01 Datatypes(Variables & Operator)

# # Variables

# # Definition

# ### A characteristic, number, or quantity that increases or decreases over time, or takes different values in different situations.
# ### Two basic types
# ### Independent variable: that can take different values and can cause corresponding changes in other variables. 
# ### Dependent variable: that can take different values only in response to an independent variable.

# # Purpose

# ### Variables are used to store information to be referenced and manipulated in a computer program. They also provide a way of labeling data with a descriptive name, so our programs can be understood more clearly by the reader and ourselves. It is helpful to think of variables as containers that hold information.

# # Importance

# ### Variables play an important role in computer programming because they enable programmers to write flexible programs. Rather than entering data directly into a program, a programmer can use variables to represent the data. The opposite of a variable is a constant. Constants are values that never change.

# # Application

# ### Variables are used in any computer program they are very usefull as they help to store many of the information such as names,list even the complete functions. 
# ### They are used in all of the Systems such as "Library Management Sytem","Database Management Sytem

# # Strengths

# ### The greatest advantage of the variables is that they enable one and the same program to execute various sets of data. In the light of the afore-stated, a variable refers to a symbol for a varying value, which is stored in the system's memory.
# ### They helps us in stoping the code repeation
# ### They helps us better manage our code
# ### If you use variables, you can make your code more clean and simple to you and others understand. Also, it's good practice.
# ### I think you can add the variables you declare inside multiple functions. Whereas yours is a one time use scenario. I could be wrong though... Variables are used for storing data though, and then you can carry that variable over from one function to another.

# # Weakness 

# ### The Biggest weakness of using hte variables in the python is that if a variable of string type is defined in a program and and you mistankkenly or forget taht you have already initalize that variable and you save the integer datatype in the variable the variable property will change and it will become the integer variable instead of string type. 

# # Example 01 :
# # Task:
#    ## Create a Variable of String Type and save your Name inside it and print the Name and show that The datatype of the variables in the Python can be changed just by assigning value of different datatype to the variable

# In[1]:


# Code
Name="Muhammad Umair"
print(Name)
print(type(Name))
Name=5
print(Name)
print(type(Name))
#Output


# # Example 02 :
# # Task:
#    ## Save your personal information into the four variables and print there value

# In[2]:


# Code 
age=20
weight=65.2
name="Muhammad Umair"
fatherName="Muhammad Akram"


# In[3]:


# OutPut
print(name)
print(age)
print(fatherName)
print(weight)


# # Operator

# # Definition

# ### An operator in a programming language is a symbol that tells the compiler or interpreter to perform specific mathematical, relational or logical operation and produce final result.

# # Purpose

# ### They are used to do many of the basic mathematical Computaion 

# # Importance

# ### Operators are very usefull in the programming language as they help us perform so many mathematical computaion and also the logival operators such as AND OR NOT they help us make the decisions onthe basis of certian condition

# # Application

# ### There are numbers of applications of the opertors such as calculator program,computer program used in the banks to do computing on the money to calculate all the ups and downs in the money

# # Strengths

# ### They helps us by reducing so much of our work as we cannot image how much of asembly language code we will have to write to simply add two numbers and it would be so difficult to do a AND,OR,NOT function

# # Weaknesses

# As they are simple math functions there are not any waekness of them. The only weakness of the them is how we use them if our own math or computation is wrong then they will perform wrong

# # Suitable to Use

# ### They are suitable to use in any senario where you want to use the mathematical computaion or logical computation

# # Example 03 :
# # Task:
#    ## Take four variables of integer type and apply math operations on them

# In[4]:


# Code
numberOne=10
numberTwo=20
numberThree=30.5
numberFour=6.7


# In[5]:


numberOne+numberTwo #Adding or subtracting two integer variables will return Integer


# In[6]:


numberOne-numberTwo 


# In[7]:


numberOne+numberThree #Adding One Integer and one float type variables will return the float 


# In[8]:


numberThree*numberFour #Multipling two variables of same datatype will return same Datatype


# In[9]:


numberOne**2 #for exponent use baseNumber**exponent will return the exponent of base number to the power 
#for example 10^2=100


