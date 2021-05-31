#!/usr/bin/env python
# coding: utf-8

# In[1]:


def hello():
    print ('Hello!')

greet = hello


# In[2]:


greet


# In[3]:


greet()


# In[4]:


def hello(name):
    print ('Hey this is the hello parent function!!')
    
    def greet():
        return '\t Hey this is the greet function inside Hello func!!'
    def welcome():
        return '\t Hey this is the welcome function inside Hello func!!'
    
    if name=='Jit':
        return greet
    else:
        return welcome


# In[5]:


my_func= hello('Jit')


# In[6]:


my_func


# In[7]:


my_func()


# In[ ]:





# In[8]:


#Decorator Creation


# In[9]:


def func_needs_decoration():
    print('I need to be decorated!!')


# In[10]:


def new_decorator(pass_func_that_needs_decoration):
    
    def wrap_func():
        print('Some code that will come before original!')
        pass_func_that_needs_decoration()
        print('Some code that will come after original!')
    return wrap_func


# In[20]:


my_new_func= func_needs_decoration
decorated_func= new_decorator(my_new_func)


# In[21]:


my_new_func()


# In[22]:


decorated_func= new_decorator(func_needs_decoration) 


# In[23]:


decorated_func()


# In[29]:


deco= new_decorator(my_new_func)
deco()


# In[ ]:


#Syntax on how to add new decorator to existing function.


# In[27]:


@new_decorator
def func_needs_decoration(): 
    print('I need to be decorated!!')


# In[28]:


func_needs_decoration()


# In[ ]:




