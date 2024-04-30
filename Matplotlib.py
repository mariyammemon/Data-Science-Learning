#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


import numpy as np
x=np.linspace(0,5,11)
y=x**2
x


# In[5]:


y


# In[6]:


plt.plot(x,y,'b>')#b is for blue colour and > is for linestyle
plt.xlabel('x axis title')
plt.ylabel('y axis title')
plt.title('chart')
plt.xlim(-5,100)#sets limit for the x axis
plt.ylim(-5,100)#sets limit for the y axis
plt.show()


# In[ ]:


''attributes for chart in plt.show()
y axis
x-axis
color
linestyle
marker
''


# In[ ]:


TYPE OF MARKER
marker='0'
marker='.'
marker='x'
marker='y'
marker='^'
marker='*'
marker='s'
marker='d'


# In[14]:


import matplotlib.pyplot as plt
#plt.subplot() is used for plotting multple charts in a single plot area
plt.subplot(1,2,1)# parameters for tijs will be rows,columns and chart no
plt.plot(x,y,'b')
plt.subplot(1,2,2)# targets the second chart of the single plot
plt.plot(x,y,'r')
plt.show()


# In[15]:


get_ipython().run_line_magic('pinfo', 'plt.plot')


# In[16]:


plt.subplot(1,3,1)
plt.plot(x,y,'m.')
plt.xlabel('x axis of subplot1')
plt.ylabel('y axis of subplot1')
plt.xlim(-5,10)
plt.ylim(-5,20)
 
plt.subplot(1,3,2)
plt.plot(x,y,'m.')
plt.xlabel('x axis of subplot2')
plt.ylabel('y axis of subplot2')
plt.xlim(-10,20)
plt.ylim(-10,20)
plt.subplot(1,3,3)
plt.plot(x,y,'k^')
plt.show()


# In[17]:


#Creates a figure(empty canvas)
fig=plt.figure()
#to add axes
axes=fig.add_axes([0.1,0.1,0.9,0.9])#left,bottom,width,height
axes2=fig.add_axes([0.2,0.5,0.4,0.3])
axes3=fig.add_axes([0.7,0.1,0.3,0.3])
#plot on that set of axes
axes.plot(x,y,'r')
axes.set_xlabel('x axis label')
axes.set_ylabel('y axis label')
axes.set_title('set title')
#second chart
axes2.plot(x,y,'g-.')
axes2.set_xlabel('x axis label')
axes2.set_ylabel('y axis label')
axes2.set_title('set title')


# In[21]:


#Scatter Plot
a=np.arange(10)
b=a**2
c1=np.random.randint(0,100,10)#to make all markers of different colors
plt.scatter(a,b,c=c1,s=100,edgecolor='white',marker='p',linewidth=1.75,cmap='brg',alpha=0.7)# s for size
plt.colorbar()#to show colorbar at on sid


# In[23]:


#histogram data
plt.hist(x,y)


# In[24]:


from random import sample
data=sample(range(1,1000),100)
plt.hist(data,linewidth=0.6,edgecolor='y')


# In[25]:


# stem plot
plt.stem(data)


# In[26]:


plt.stairs(data)


# In[27]:


x=np.arange(0,100,10)
y=np.random.randint(0,100,10)
z=x*2
plt.stackplot(x,y,z)


# In[28]:


x=[1,2,3,4]
e=(0.4,0,0,0)
plt.pie(x,explode=e,radius=3,center=(4,4),frame=True)


# In[29]:


d=np.random.normal(0,100,60)
#print d
plt.boxplot(d)


# In[30]:


data=[np.random.normal(0,std,100) for std in range(1,4)]
data1=np.random.normal(0,1,100)
data2=np.random.normal(0,2,100)
data3=np.random.normal(0,3,100)
dataf=[data1,data2,data3]
plt.boxplot(dataf,vert=False,patch_artist=True);


# In[ ]:





# In[ ]:





# In[ ]:




