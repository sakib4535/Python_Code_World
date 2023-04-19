#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sympy as sym
from IPython.display import display, Math

q = sym.symbols('q')
f = sym.cos(q)

for i in range(0,8):
    f_diff = sym.diff(f)
    display(Math(r'\frac{d}{dq}(%s) = %s' % (sym.latex(f), sym.latex(f_diff))))
    f = f_diff


# In[3]:


import sympy.plotting.plot as symplot

f = sym.cos(q)

for i in range(0,4):
    
    if i == 0:
        p = symplot(f, show=False, label=sym.latex(f), line_color =(i/5,i/5,i/5))
        
    else:
        p.extend(symplot(f,show=False, label=sym.latex(f), line_color =(i/5,i/5,i/5)))
    # Redefine the f to be the derivatives    
    f = sym.diff(f)
    
p.legend = True
p.xlim = [-3,3]
p.show()


# In[4]:


import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

def computetangent(f, xa, bnds):
    # Defining the derivatives and values at point xa
    df = sym.diff(f)  # Define derivatives and values at point x
    fa = f.subs(x, xa) # Value of the function at the point f, assuming symbolic variable in function f is called x
    dfa = df.subs(x, xa) # Value of the derivative of the function at point x equals xa
    
    # Evaluate Tangent line
    xx = np.linspace(bnds[0], bnds[-1], 200)  # Assumption: input is list
    return dfa * (xx - xa) + fa

x = sym.symbols('x')
f = x**2
xx = np.linspace(-2, 2, 200)
ffun = sym.lambdify(x, f)(xx)

tanline = computetangent(f, 1, xx[[0,-1]])

plt.plot(xx, ffun)
plt.plot(xx, tanline)
plt.show()


# In[ ]:




