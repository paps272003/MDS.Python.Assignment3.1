
# coding: utf-8

# In[1]:

def myreduce(fnc, seq):
    tally = seq[0]
    for next in seq[1:]:
        tally = fnc(tally, next)
    return tally


# In[ ]:



