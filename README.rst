************
Introduction
************
:Version: 1.0
:Authors: Chao-Jun Feng
:Copyright: This document has been placed in the public domain.
:License: pyminer is released under the Academic Free License.

.. image:: https://secure.travis-ci.org/pymc-devs/pymc.png 
    :target: http://travis-ci.org/pymc-devs/pymc
.. image:: http://img.shields.io/pypi/v/pymc.svg?style=flat
    :target: https://pypi.python.org/pypi/pymc
.. image:: http://img.shields.io/badge/license-AFL-blue.svg?style=flat
    :target: https://github.com/pymc-devs/pymc/blob/master/LICENSE


Purpose
=======
pyminer is a python module  to do the data fitting by using supernovae, CMB, BAO, etc.

Requirement
==========
  - python2.x 
  - numpy
  - agpy

Files
=======
pyminer_cos_model.py : realize a cosmological model, e.g. LCDM
pyminer_residual.py ： add data, JLA, CMB, BAO
pyminer_setting.py : some global variables, functions, and the most important is the residual function
pyminer_fit_cos.py : show an example for fitting.
