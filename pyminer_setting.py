# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 06:53:32 2015

@author: chaojun
"""

from pyminer_cos_model import lcdm
from pyminer_residual  import JLAresiCal, CMBresiCal, BAOresiCal

# Genearl setting 
divMax = 15  # for romberg integral
ogh2     = 2.469e-5
JLA_DIR = '/Users/chaojun/Documents/Research/2015/grb/pycode/data/jla'



# Cosmological model 
model = lcdm(divmax = divMax)  

# Data setting
use_sn_data     = True  
use_cmb_data    = True
use_bao_data    = True


resobj=[] 
  
if use_sn_data : resobj.append( JLAresiCal(cosModel = model, DATA_DIR_JLA = JLA_DIR) )
if use_cmb_data: resobj.append( CMBresiCal(cosModel = model) )
if use_bao_data: resobj.append( BAOresiCal(cosModel = model) )
  

# Residual function
def residual(p, resobj = resobj, fjac=None):
        
    import numpy as np
    
    res = np.array([]) 
    
    for obj in resobj:
        tmp = obj.residual(p)
        res = np.append(res, tmp)
        
    status = 0
    return [status, res]    



# some other functions

def clear_env():
    for key in globals().keys():
        if not key.startswith("__"):
            globals().pop(key)
            


