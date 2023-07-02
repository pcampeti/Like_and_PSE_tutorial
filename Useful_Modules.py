#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: paolo
"""
import os.path as op
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle
from scipy.io import FortranFile
import pymaster as nmt
import healpy as hp
import scipy
import scipy.interpolate
from SGWB_Signal import Signal_GW
from numpy.linalg import inv



def binning_definition(nside):	
    ells_full=np.arange(3*nside,dtype='int32')
    ells = np.arange(2,int(np.max(ells_full)), 1)
    #ells = [2, 4, 10, 35, 50, 70, 90, int(np.max(ells_full))]
    weights = np.zeros(len(ells_full))
    l = 0
    bpws=-1+np.zeros_like(ells_full)
    for ell in ells[:-1]:
        b0_ = np.argmin(np.abs(ells_full - ells[l]))
        b1_ = np.argmin(np.abs(ells_full - ells[l+1]))
        nlb = (ells_full[b1_]-ells_full[b0_])*1.0
        weights[int(ells_full[b0_]):int(ells_full[b1_])] = 1.0/nlb
        bpws[int(ells_full[b0_]):int(ells_full[b1_])] = l
        l+=1
    b=nmt.NmtBin(nside, bpws=bpws, ells=ells_full, weights=weights)
    return b


def read_transfer(transferfile):
    h=FortranFile(transferfile, 'r')
    record= h.read_record([('a', '<i4'),('b', '<i4')])
    lmax=(record[0][0])
    q_ix=(record[0][1])
    record= h.read_record([('a', '<f8',(q_ix,lmax))])
    Delta=record[0][0].transpose()
    h.close()
    return Delta

def read_k_file(filetoread):
    dataset = np.genfromtxt(filetoread, names=None)
    ks = dataset[:,0]
    pows = dataset[:,1]
    measures = dataset[:,2]
    return ks, pows, measures

def load_camb_file(filename, lmax, Norm=None):
    if Norm:
        FACTOR = 7.42835025e12
    else:
        FACTOR=1.
    dataset=np.genfromtxt(filename, names=True)
    DlTT = FACTOR * np.array(dataset['TT'])[0:lmax] 
    DlEE = FACTOR * np.array(dataset['EE'])[0:lmax] 
    DlTE = FACTOR * np.array(dataset['TE'])[0:lmax] 
    DlBB = FACTOR * np.array(dataset['BB'])[0:lmax] 
    return DlTT, DlEE, DlTE, DlBB

def load_class_file(filename, lmax):
    dataset = np.genfromtxt(filename, names=None, skip_header=9) #mind the skip_header
    DlTT = dataset[:,1]
    DlEE = dataset[:,2]
    DlBB = dataset[:,3]
    DlTE = dataset[:,4]
    return DlTT[:lmax], DlEE[:lmax], DlTE[:lmax], DlBB[:lmax]


def compute_cls_from_transfer(lmax, pows, Delta3, measures, ell):
    FACTOR = 7.42835025e12
    qmax = len(measures)
    ClBB = [0.0]*lmax
    for j in range(0, len(ClBB)):  
        for q_ix in range(0, qmax): 
            ClBB[j] = ClBB[j] + pows[q_ix]*((Delta3[j][q_ix])**2)*measures[q_ix]
        ClBB[j] = (((ell[j]*(ell[j]+1))/(2*np.pi)*np.pi)/4.0)*ClBB[j]
    ClBB = np.array(ClBB)
    DlBB = FACTOR * ClBB
    return DlBB


def _get_Cl_cmb(Alens=1., r=0.):
    CURRENT_PATH = op.abspath('')
    PATH_TEMPLATE1=CURRENT_PATH+'/ancillary_files/Cls_Planck2018_lensed_scalar.fits'
    PATH_TEMPLATE2=CURRENT_PATH+'/ancillary_files/Cls_Planck2018_unlensed_scalar_and_tensor_r1.fits'
    power_spectrum = hp.read_cl(PATH_TEMPLATE1)[:,:4000]
    if Alens != 1.:
        power_spectrum[2] *= Alens
    if r:
        power_spectrum += r * hp.read_cl(PATH_TEMPLATE2)[:,:4000]
    return power_spectrum


def log_interp1d(xx, yy, kind='linear'):
    '''
    Interpolator used in the code above.
    '''
    logx = np.log10(xx)
    logy = np.log10(yy)
    lin_interp = scipy.interpolate.interp1d(logx, logy, kind=kind)
    log_interp = lambda zz: np.power(10.0, lin_interp(np.log10(zz)))
    return log_interp


def compute_Dl(window, measures, lmax, Delta3, A_S):
    FACTOR = 7.42835025e12
    Delta3 = np.array(Delta3) 
    Delta3 = Delta3[0:lmax] 
    measures = np.array(measures)   
    mult_factor_BB = np.pi/4.0 #multiplicative factor in the formula for DlBB
    Delta3_square = Delta3**2
    DPM3 = A_S * Delta3_square * measures #I multiply preventively these 3 ndarray to make the computation faster
    DlBB = np.einsum("jq,iq->ij", DPM3, window)
    DlBB = mult_factor_BB * DlBB
    return FACTOR*DlBB
    
