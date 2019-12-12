#!/usr/bin/env python
# coding: utf-8

# In[38]:


class FizzBuzz:       
    def fb(self,i):
            if i % 3 == 0 and i % 5 ==0:
                print("The number " + str(i) + " is FizzBuzz")
            elif i % 5 == 0:
                print("The number " + str(i) + " is Buzz")
            elif i % 3 == 0:
                print("The number " + str(i) + " is Fizz")
            else:
                print("The number" + str(i) + " is neither Fizz, Buzz nor Fizzbuzz")


# In[39]:


test = FizzBuzz()


# In[40]:


test.fb(10)
test.fb(30)
test.fb(6)
test.fb(7)


# In[ ]:




