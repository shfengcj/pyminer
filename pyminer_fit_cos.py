# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 06:36:02 2015

@author: chaojun
"""
import copy
import numpy as np

from agpy.mpfit       import mpfit
from pyminer_setting  import *

clear_env()


# Parameter setting
# ==========================
# JLA nuiance parameters 
    # ==========================
    # p[0]:alpha
    # p[1]:beta
    # p[2]:M
    # p[3]:DeltaM
    #
    # Cosmological parameters
    # ==========================
    # p[4]:H0
    # p[5]:Omega_bh2
    # p[6]:Omega_m
    # p[7]:Omega_r
    # p[8]:Omega_k
    # p[9]... other Cosmological parameters


# initial conditions

print 'Prepare and reading data ...'
p0  = np.array([0.141 ,3.099 ,-19.10 ,-0.07 , 68.34 , 0.0221, 0.305,ogh2, 0],dtype='float64')
n   = len(p0)

parbase={'value':0., 'fixed':0, 'limited':[0,0], 'limits':[0.,0.]}
parinfo=[]


for i in range(n):
    parinfo.append(copy.deepcopy(parbase))
for i in range(n): 
    parinfo[i]['value']=p0[i]
    


m = mpfit(residual, p0, parinfo=parinfo)

if (m.status <= 0): 
    print 'error message = ', m.errmsg

chisq=(residual(m.params)[1]**2).sum()

print m.params
print m.perror

