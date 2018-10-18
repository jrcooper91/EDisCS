import pyfits 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import astropy 
from astropy import cosmology 
import math as mt
import os, sys
import matplotlib.lines as mlines




def c1301(f_Ha,rf_J,rf_U,rf_V,rf_VJ,rf_UV,rf_m,logLHa,SFR,z,q,c):
    plt.figure(figsize=(18, 16), dpi= 80, facecolor='w', edgecolor='k')
    f = open('/Users/jennifercooper/Documents/Gal_Ev/EDisCS/G102/test/1301_sn_bic>5.txt', 'r')
    lines = f.readlines()[1:]
    f.close()
    
    #create arrays 
    f_Ha    = [] 
    rf_J    = []
    rf_U    = []
    rf_V    = []
    rf_VJ   = []
    rf_UV   = []
    rf_m    = []
    logLHa  = []
    SFR     = []
    z       = []
    q       = [] 
    c       = []
  
    
    #pull array column 
    for line in lines: 
        a = line.split()
        f_Ha.append(float(a[3]))
        rf_J.append(float(a[8]))
        rf_U.append(float(a[9]))
        rf_V.append(float(a[10]))
        rf_VJ.append(float(a[11]))
        rf_UV.append(float(a[12]))
        rf_m.append(float(a[13]))
        logLHa.append(float(a[18]))
        SFR.append(float(a[19]))
        z.append(float(a[14]))
        q.append(float(a[16]))
        c.append(float(a[20]))
        
    f_Ha = np.array(f_Ha)
    f_Ha_log = np.log10(f_Ha)
    rf_J = np.array(rf_J)
    rf_U = np.array(rf_U)
    rf_V = np.array(rf_V)
    rf_VJ = np.array(rf_VJ)
    rf_UV = np.array(rf_UV)
    rf_m  = np.array(rf_m)
    logLHa= np.array(logLHa)
    SFR   = np.array(SFR)
    z     = np.array(z)
    q     = np.array(q)
    c     = np.array(c)
    
    x1 = [-5,0.85]
    x2 = [0.85,1.6]
    x3 = [1.6,1.6]
    y1 = [1.3,1.3]
    y2 = [1.3,2]
    y3 = [2,5]
    
    plt.subplot(3,2,1)
    plt.scatter(rf_VJ[np.where(np.logical_and(z>0.4628,z<0.5028))],rf_UV[np.where(np.logical_and(z>0.4628,z<0.5028))],c=SFR[np.where(np.logical_and(z>0.4628,z<0.5028))])
    cbar = plt.colorbar()
    cbar.set_label("log(SFR)")
    plt.xlabel('V-J')
    plt.ylabel('U-V')
    plt.title('Cluster UVJ z+/- 0.02')
    plt.plot(x1,y1,color='black')
    plt.plot(x2,y2,color='black')
    plt.plot(x3,y3,color='black')
    plt.xlim(-0.5,2)
    plt.ylim(0,3)
    
    plt.subplot(3,2,2)
    #plt.scatter(rf_VJ[np.where(np.logical_and(z<0.4628,z>0.5028))],rf_UV[np.where(np.logical_and(z<0.4628,z>0.5028))],c=SFR[np.where(np.logical_and(z<0.4628,z>0.5028))])
    plt.scatter(rf_VJ[np.where(z<0.4628)],rf_UV[np.where(z<0.4628)],c=SFR[np.where(z<0.4628)])
    plt.scatter(rf_VJ[np.where(z>0.5028)],rf_UV[np.where(z>0.5028)],c=SFR[np.where(z>0.5028)])
    cbar = plt.colorbar()
    cbar.set_label("log(SFR)")
    cbar.set_clim(-0.2,0.8)
    plt.xlabel('V-J')
    plt.ylabel('U-V')
    plt.title('Field UVJ')
    plt.plot(x1,y1,color='black')
    plt.plot(x2,y2,color='black')
    plt.plot(x3,y3,color='black')
    plt.xlim(-0.5,2)
    plt.ylim(0,3)
    
    plt.subplot(3,2,3)
    plt.scatter(rf_V[np.where(np.logical_and(z>0.4628,z<0.5028))],rf_UV[np.where(np.logical_and(z>0.4628,z<0.5028))],c=SFR[np.where(np.logical_and(z>0.4628,z<0.5028))],alpha=0.7)
    cbar = plt.colorbar()
    cbar.set_label("log(SFR)")
    plt.xlabel('V')
    plt.ylabel('U-V')    
    plt.title('Cluster z+/- 0.02')
    plt.xlim(0,20)
    plt.ylim(-2,3)
    
    plt.subplot(3,2,4)
    plt.scatter(rf_VJ[np.where(z<0.4628)],rf_UV[np.where(z<0.4628)],c=SFR[np.where(z<0.4628)])
    plt.scatter(rf_VJ[np.where(z>0.5028)],rf_UV[np.where(z>0.5028)],c=SFR[np.where(z>0.5028)])    
    cbar = plt.colorbar()
    cbar.set_clim(-0.2,0.8)
    cbar.set_label("log(SFR)")
    plt.xlabel('V')
    plt.ylabel('U-V')    
    plt.title('Field')
    plt.xlim(-5,5)
    plt.ylim(-2,3)
    
    plt.subplot(3,2,5)
    plt.scatter(rf_m[np.where((z>0.4628)&(z<0.5028)&(c>0.))],SFR[np.where((z>0.4628)&(z<0.5028)&(c>0.))],color='blue',alpha=0.7,marker = 'o')
    plt.scatter(rf_m[np.where((z>0.4628)&(z<0.5028)&(c<1.))],SFR[np.where((z>0.4628)&(z<0.5028)&(c<1.))],color='blue',alpha=0.5,marker = 'x')
    plt.scatter(rf_m[np.where(z<0.4628)],SFR[np.where(z<0.4628)],c='red',alpha=0.5)
    plt.scatter(rf_m[np.where(z>0.5028)],SFR[np.where(z>0.5028)],c='red',alpha=0.5)   
    plt.xlim(6.8,11)
    #plt.ylim(-1,3)
    plt.xlabel('logM')
    plt.ylabel('logSFR')
    #plt.title('All pointings matched with LPD Halpha>0')
    red_patch = mpatches.Patch(color='red', label='Field', alpha = 0.5)
    blue_patch = mpatches.Patch(color='blue', label='Outside R200', alpha = 0.5)
    blue_star = mlines.Line2D([], [], color='blue', marker='x', linestyle='None',
                          markersize=10, label='Within R200')
    plt.legend(handles=[red_patch,blue_patch,blue_star],loc=2)
    
    plt.subplot(3,2,6)
    
    zc       = z[np.where((z>0.4628)&(z<0.5028))]
    
    zf1       = z[np.where(z<0.4628)]   
    zf2       = z[np.where((z>0.5028))]

    x1 = zc
    x2 = zf1
    x3 = zf2
    
    
    kwargs1 = dict(histtype='stepfilled', alpha=0.3, normed=False, bins=2)
    kwargs2 = dict(histtype='stepfilled', alpha=0.3, normed=False, bins=5)
    kwargs3 = dict(histtype='stepfilled', alpha=0.3, normed=False, bins=5)



    
    plt.hist(x1,color='blue', **kwargs1)
    plt.hist(x2,color='red', **kwargs2)
    plt.hist(x3,color='red', **kwargs3);
    plt.xlabel('z')


    plt.show()
    



def c1138(f_Ha,rf_J,rf_U,rf_V,rf_VJ,rf_UV,rf_m,logLHa,SFR,z,q,c):
    plt.figure(figsize=(18, 16), dpi= 80, facecolor='w', edgecolor='k')
    f = open('/Users/jennifercooper/Documents/Gal_Ev/EDisCS/G102/test/1138_sn_bic>5_no_st.txt', 'r')
    lines = f.readlines()[1:]
    f.close()
    
    #create arrays 
    f_Ha    = [] 
    rf_J    = []
    rf_U    = []
    rf_V    = []
    rf_VJ   = []
    rf_UV   = []
    rf_m    = []
    logLHa  = []
    SFR     = []
    z       = []
    q       = [] 
    c       = []
  
    
    #pull array column 
    for line in lines: 
        a = line.split()
        f_Ha.append(float(a[3]))
        rf_J.append(float(a[8]))
        rf_U.append(float(a[9]))
        rf_V.append(float(a[10]))
        rf_VJ.append(float(a[11]))
        rf_UV.append(float(a[12]))
        rf_m.append(float(a[13]))
        logLHa.append(float(a[18]))
        SFR.append(float(a[19]))
        z.append(float(a[14]))
        q.append(float(a[16]))
        c.append(float(a[20]))
        
    f_Ha = np.array(f_Ha)
    f_Ha_log = np.log10(f_Ha)
    rf_J = np.array(rf_J)
    rf_U = np.array(rf_U)
    rf_V = np.array(rf_V)
    rf_VJ = np.array(rf_VJ)
    rf_UV = np.array(rf_UV)
    rf_m  = np.array(rf_m)
    logLHa= np.array(logLHa)
    SFR   = np.array(SFR)
    z     = np.array(z)
    q     = np.array(q)
    c     = np.array(c)
    
    x1 = [-5,0.85]
    x2 = [0.85,1.6]
    x3 = [1.6,1.6]
    y1 = [1.3,1.3]
    y2 = [1.3,2]
    y3 = [2,5]
    
    plt.subplot(3,2,1)
    plt.scatter(rf_VJ[np.where(np.logical_and(z<0.4996,z>0.4596))],rf_UV[np.where(np.logical_and(z<0.4996,z>0.4596))],c=SFR[np.where(np.logical_and(z<0.4996,z>0.4596))])
    cbar = plt.colorbar()
    cbar.set_label("log(SFR)")
    plt.xlabel('V-J')
    plt.ylabel('U-V')
    plt.title('Cluster UVJ z+/- 0.02')
    plt.plot(x1,y1,color='black')
    plt.plot(x2,y2,color='black')
    plt.plot(x3,y3,color='black')
    plt.xlim(-0.5,2)
    plt.ylim(0,3)
    
    plt.subplot(3,2,2)
    #plt.scatter(rf_VJ[np.where(np.logical_and(z<0.4628,z>0.5028))],rf_UV[np.where(np.logical_and(z<0.4628,z>0.5028))],c=SFR[np.where(np.logical_and(z<0.4628,z>0.5028))])
    plt.scatter(rf_VJ[np.where(z<0.4596)],rf_UV[np.where(z<0.4628)],c=SFR[np.where(z<0.4596)])
    plt.scatter(rf_VJ[np.where(z>0.4996)],rf_UV[np.where(z>0.4996)],c=SFR[np.where(z>0.4996)])
    cbar = plt.colorbar()
    cbar.set_clim(0,1)
    cbar.set_label("log(SFR)")
    plt.xlabel('V-J')
    plt.ylabel('U-V')
    plt.title('Field UVJ')
    plt.plot(x1,y1,color='black')
    plt.plot(x2,y2,color='black')
    plt.plot(x3,y3,color='black')
    plt.xlim(-0.5,2)
    plt.ylim(0,3)
    
    plt.subplot(3,2,3)
    plt.scatter(rf_V[np.where(np.logical_and(z<0.4996,z>0.4596))],rf_UV[np.where(np.logical_and(z<0.4996,z>0.4596))],c=SFR[np.where(np.logical_and(z<0.4996,z>0.4596))],alpha=0.7)
    cbar = plt.colorbar()
    cbar.set_label("log(SFR)")
    plt.xlabel('V')
    plt.ylabel('U-V')    
    plt.title('Cluster z+/- 0.02')
    plt.xlim(0,20)
    plt.ylim(-2,3)
    
    plt.subplot(3,2,4)
    plt.scatter(rf_VJ[np.where(z<0.4596)],rf_UV[np.where(z<0.4596)],c=SFR[np.where(z<0.4596)])
    plt.scatter(rf_VJ[np.where(z>0.4996)],rf_UV[np.where(z>0.4996)],c=SFR[np.where(z>0.4996)])    
    cbar = plt.colorbar()
    cbar.set_clim(0,1)
    cbar.set_label("log(SFR)")
    plt.xlabel('V')
    plt.ylabel('U-V')    
    plt.title('Field')
    plt.xlim(-5,5)
    plt.ylim(-2,3)
    
    plt.subplot(3,2,5)
    plt.scatter(rf_m[np.where((z>0.4596)&(z<0.4996)&(c>0.))],SFR[np.where((z>0.4596)&(z<0.4996)&(c>0.))],color='blue',alpha=0.7,marker = 'o')
    plt.scatter(rf_m[np.where((z>0.4596)&(z<0.4996)&(c<1.))],SFR[np.where((z>0.4596)&(z<0.4996)&(c<1.))],color='blue',alpha=0.5,marker = 'x')
    plt.scatter(rf_m[np.where(z<0.4596)],SFR[np.where(z<0.4596)],c='red',alpha=0.5)
    plt.scatter(rf_m[np.where(z>0.4996)],SFR[np.where(z>0.4996)],c='red',alpha=0.5)   
    plt.xlim(7.5,11)
    #plt.ylim(-1,3)
    plt.xlabel('logM')
    plt.ylabel('logSFR')
    #plt.title('All pointings matched with LPD Halpha>0')
    red_patch = mpatches.Patch(color='red', label='Field', alpha = 0.5)
    blue_patch = mpatches.Patch(color='blue', label='Outside R200', alpha = 0.5)
    blue_star = mlines.Line2D([], [], color='blue', marker='x', linestyle='None',
                          markersize=10, label='Within R200')
    plt.legend(handles=[red_patch,blue_patch,blue_star],loc=1)

    plt.subplot(3,2,6)
    
    zc       = z[np.where((z>0.4596)&(z<0.4996))]
    
    zf1       = z[np.where(z<0.4596)]   
    zf2       = z[np.where((z>0.4996))]

    x1 = zc
    x2 = zf1
    x3 = zf2
    
    
    kwargs1 = dict(histtype='stepfilled', alpha=0.3, normed=False, bins=2)
    kwargs2 = dict(histtype='stepfilled', alpha=0.3, normed=False, bins=5)
    kwargs3 = dict(histtype='stepfilled', alpha=0.3, normed=False, bins=5)



    
    plt.hist(x1,color='blue', **kwargs1)
    plt.hist(x2,color='red', **kwargs2)
    plt.hist(x3,color='red', **kwargs3);
    plt.xlabel('z')
    
    plt.show()
    
def c1059(f_Ha,rf_J,rf_U,rf_V,rf_VJ,rf_UV,rf_m,logLHa,SFR,z,q,c):
    plt.figure(figsize=(18, 16), dpi= 80, facecolor='w', edgecolor='k')
    f = open('/Users/jennifercooper/Documents/Gal_Ev/EDisCS/G102/test/1059_sn_bic>5_no_st.txt', 'r')
    lines = f.readlines()[1:]
    f.close()
    
    #create arrays 
    f_Ha    = [] 
    rf_J    = []
    rf_U    = []
    rf_V    = []
    rf_VJ   = []
    rf_UV   = []
    rf_m    = []
    logLHa  = []
    SFR     = []
    z       = []
    q       = [] 
    c       = []
  
    
    #pull array column 
    for line in lines: 
        a = line.split()
        f_Ha.append(float(a[3]))
        rf_J.append(float(a[8]))
        rf_U.append(float(a[9]))
        rf_V.append(float(a[10]))
        rf_VJ.append(float(a[11]))
        rf_UV.append(float(a[12]))
        rf_m.append(float(a[13]))
        logLHa.append(float(a[18]))
        SFR.append(float(a[19]))
        z.append(float(a[14]))
        q.append(float(a[16]))
        c.append(float(a[20]))
        
    f_Ha = np.array(f_Ha)
    f_Ha_log = np.log10(f_Ha)
    rf_J = np.array(rf_J)
    rf_U = np.array(rf_U)
    rf_V = np.array(rf_V)
    rf_VJ = np.array(rf_VJ)
    rf_UV = np.array(rf_UV)
    rf_m  = np.array(rf_m)
    logLHa= np.array(logLHa)
    SFR   = np.array(SFR)
    z     = np.array(z)
    q     = np.array(q)
    c     = np.array(c)
    
    x1 = [-5,0.85]
    x2 = [0.85,1.6]
    x3 = [1.6,1.6]
    y1 = [1.3,1.3]
    y2 = [1.3,2]
    y3 = [2,5]
    
    plt.subplot(3,2,1)
    plt.scatter(rf_VJ[np.where(np.logical_and(z<0.4764,z>0.4364))],rf_UV[np.where(np.logical_and(z<0.4764,z>0.4364))],c=SFR[np.where(np.logical_and(z<0.4764,z>0.4364))])
    cbar = plt.colorbar()
    cbar.set_label("log(SFR)")
    plt.xlabel('V-J')
    plt.ylabel('U-V')
    plt.title('Cluster UVJ z+/- 0.02')
    plt.plot(x1,y1,color='black')
    plt.plot(x2,y2,color='black')
    plt.plot(x3,y3,color='black')
    plt.xlim(-0.5,2)
    plt.ylim(0,3)
    
    plt.subplot(3,2,2)

    plt.scatter(rf_VJ[np.where(z<0.4364)],rf_UV[np.where(z<0.4364)],c=SFR[np.where(z<0.4364)])
    plt.scatter(rf_VJ[np.where(z>0.4764)],rf_UV[np.where(z>0.4764)],c=SFR[np.where(z>0.4764)])
    cbar = plt.colorbar()
    cbar.set_label("log(SFR)")
    cbar.set_clim(-0.5,1.25)
    plt.xlabel('V-J')
    plt.ylabel('U-V')
    plt.title('Field UVJ')
    plt.plot(x1,y1,color='black')
    plt.plot(x2,y2,color='black')
    plt.plot(x3,y3,color='black')
    plt.xlim(-0.5,2)
    plt.ylim(0,3)
    
    plt.subplot(3,2,3)
    plt.scatter(rf_V[np.where(np.logical_and(z<0.4764,z>0.4364))],rf_UV[np.where(np.logical_and(z<0.4764,z>0.4364))],c=SFR[np.where(np.logical_and(z<0.4764,z>0.4364))],alpha=0.7)
    cbar = plt.colorbar()
    cbar.set_label("log(SFR)")
    plt.xlabel('V')
    plt.ylabel('U-V')    
    plt.title('Cluster z+/- 0.02')
    plt.xlim(0,20)
    plt.ylim(-2,3)
    
    plt.subplot(3,2,4)
    plt.scatter(rf_VJ[np.where(z<0.4364)],rf_UV[np.where(z<0.4364)],c=SFR[np.where(z<0.4364)])
    plt.scatter(rf_VJ[np.where(z>0.4764)],rf_UV[np.where(z>0.4764)],c=SFR[np.where(z>0.4764)])    
    cbar = plt.colorbar()
    cbar.set_label("log(SFR)")
    plt.xlabel('V')
    plt.ylabel('U-V')    
    plt.title('Field')
    plt.xlim(-5,5)
    plt.ylim(-2,3)
    
    plt.subplot(3,2,5)
    plt.scatter(rf_m[np.where((z>0.4364)&(z<0.4764)&(c>0.))],SFR[np.where((z>0.4364)&(z<0.4764)&(c>0.))],color='blue',alpha=0.7,marker = 'o')
    plt.scatter(rf_m[np.where((z>0.4364)&(z<0.4764)&(c<1.))],SFR[np.where((z>0.4364)&(z<0.4764)&(c<1.))],color='blue',alpha=0.5,marker = 'x')
    plt.scatter(rf_m[np.where(z<0.4364)],SFR[np.where(z<0.4364)],c='red',alpha=0.5)
    plt.scatter(rf_m[np.where(z>0.4764)],SFR[np.where(z>0.4764)],c='red',alpha=0.5)   
    plt.xlim(7.5,11.5)
    #plt.ylim(-1,3)
    plt.xlabel('logM')
    plt.ylabel('logSFR')
    #plt.title('All pointings matched with LPD Halpha>0')
    red_patch = mpatches.Patch(color='red', label='Field', alpha = 0.5)
    blue_patch = mpatches.Patch(color='blue', label='Outside R200', alpha = 0.5)
    blue_star = mlines.Line2D([], [], color='blue', marker='x', linestyle='None',
                          markersize=10, label='Within R200')
    plt.legend(handles=[red_patch,blue_patch,blue_star],loc=2)

    plt.subplot(3,2,6)
    
    h = open('/Users/jennifercooper/Documents/Gal_Ev/EDisCS/G102/clusters/1059-1253/abcd_LDP_c.txt', 'r')
    lines = h.readlines()[1:]
    h.close()   
    zc       = []   
    for line in lines: 
        a = line.split()     
        zc.append(float(a[14]))
    zc     = np.array(zc)
    g = open('/Users/jennifercooper/Documents/Gal_Ev/EDisCS/G102/clusters/1059-1253/abcd_LDP_f.txt', 'r')
    lines = g.readlines()[1:]
    g.close()   
    zf       = []   
    for line in lines: 
        a = line.split()     
        zf.append(float(a[14]))
    zf     = np.array(zf)

    x1 = zc
    x2 = zf
    
    kwargs1 = dict(histtype='stepfilled', alpha=0.3, normed=False, bins=2)
    kwargs2 = dict(histtype='stepfilled', alpha=0.3, normed=False, bins=20)


    
    plt.hist(x1,color='blue', **kwargs1)
    plt.hist(x2,color='red', **kwargs2);
    
    plt.show()
    


def c1227(f_Ha,rf_J,rf_U,rf_V,rf_VJ,rf_UV,rf_m,logLHa,SFR,z,q,c):
    plt.figure(figsize=(18, 16), dpi= 80, facecolor='w', edgecolor='k')
    f = open('/Users/jennifercooper/Documents/Gal_Ev/EDisCS/G102/test/1227_sn_bic>5.txt', 'r')
    lines = f.readlines()[1:]
    f.close()
    
    #create arrays 
    f_Ha    = [] 
    rf_J    = []
    rf_U    = []
    rf_V    = []
    rf_VJ   = []
    rf_UV   = []
    rf_m    = []
    logLHa  = []
    SFR     = []
    z       = []
    q       = [] 
    c       = []
  
    
    #pull array column 
    for line in lines: 
        a = line.split()
        f_Ha.append(float(a[3]))
        rf_J.append(float(a[8]))
        rf_U.append(float(a[9]))
        rf_V.append(float(a[10]))
        rf_VJ.append(float(a[11]))
        rf_UV.append(float(a[12]))
        rf_m.append(float(a[13]))
        logLHa.append(float(a[18]))
        SFR.append(float(a[19]))
        z.append(float(a[14]))
        q.append(float(a[16]))
        c.append(float(a[20]))
        
    f_Ha = np.array(f_Ha)
    f_Ha_log = np.log10(f_Ha)
    rf_J = np.array(rf_J)
    rf_U = np.array(rf_U)
    rf_V = np.array(rf_V)
    rf_VJ = np.array(rf_VJ)
    rf_UV = np.array(rf_UV)
    rf_m  = np.array(rf_m)
    logLHa= np.array(logLHa)
    SFR   = np.array(SFR)
    z     = np.array(z)
    q     = np.array(q)
    c     = np.array(c)
    
    x1 = [-5,0.85]
    x2 = [0.85,1.6]
    x3 = [1.6,1.6]
    y1 = [1.3,1.3]
    y2 = [1.3,2]
    y3 = [2,5]
    
    plt.subplot(3,2,1)
    plt.scatter(rf_VJ[np.where(np.logical_and(z<0.6557,z>0.6157))],rf_UV[np.where(np.logical_and(z<0.6557,z>0.6157))],c=SFR[np.where(np.logical_and(z<0.6557,z>0.6157))])
    cbar = plt.colorbar()
    cbar.set_label("log(SFR)")
    plt.xlabel('V-J')
    plt.ylabel('U-V')
    plt.title('Cluster UVJ z+/- 0.02')
    plt.plot(x1,y1,color='black')
    plt.plot(x2,y2,color='black')
    plt.plot(x3,y3,color='black')
    plt.xlim(-0.5,2)
    plt.ylim(0,3)
    
    plt.subplot(3,2,2)
    #plt.scatter(rf_VJ[np.where(np.logical_and(z<0.4628,z>0.5028))],rf_UV[np.where(np.logical_and(z<0.4628,z>0.5028))],c=SFR[np.where(np.logical_and(z<0.4628,z>0.5028))])
    plt.scatter(rf_VJ[np.where(z<0.6157)],rf_UV[np.where(z<0.6157)],c=SFR[np.where(z<0.6157)])
    plt.scatter(rf_VJ[np.where(z>0.6557)],rf_UV[np.where(z>0.6557)],c=SFR[np.where(z>0.6557)])
    cbar = plt.colorbar()
    cbar.set_clim(0,0.5)
    cbar.set_label("log(SFR)")
    plt.xlabel('V-J')
    plt.ylabel('U-V')
    plt.title('Field UVJ')
    plt.plot(x1,y1,color='black')
    plt.plot(x2,y2,color='black')
    plt.plot(x3,y3,color='black')
    plt.xlim(-0.5,2)
    plt.ylim(0,3)
    
    plt.subplot(3,2,3)
    plt.scatter(rf_V[np.where(np.logical_and(z<0.6557,z>0.6157))],rf_UV[np.where(np.logical_and(z<0.6557,z>0.6157))],c=SFR[np.where(np.logical_and(z<0.6557,z>0.6157))],alpha=0.7)
    cbar = plt.colorbar()
    cbar.set_label("log(SFR)")
    plt.xlabel('V')
    plt.ylabel('U-V')    
    plt.title('Cluster z+/- 0.02')
    plt.xlim(0,20)
    plt.ylim(-2,3)
    
    plt.subplot(3,2,4)
    plt.scatter(rf_VJ[np.where(z<0.6157)],rf_UV[np.where(z<0.6157)],c=SFR[np.where(z<0.6157)])
    plt.scatter(rf_VJ[np.where(z>0.6557)],rf_UV[np.where(z>0.6557)],c=SFR[np.where(z>0.6557)])    
    cbar = plt.colorbar()
    cbar.set_clim(0,0.5)
    cbar.set_label("log(SFR)")
    plt.xlabel('V')
    plt.ylabel('U-V')    
    plt.title('Field')
    plt.xlim(-5,5)
    plt.ylim(-2,3)
    
    plt.subplot(3,2,5)
    plt.scatter(rf_m[np.where((z>0.6157)&(z<0.6557)&(c>0.))],SFR[np.where((z>0.6157)&(z<0.6557)&(c>0.))],color='blue',alpha=0.7,marker = 'o')
    plt.scatter(rf_m[np.where((z>0.6157)&(z<0.6557)&(c<1.))],SFR[np.where((z>0.6157)&(z<0.6557)&(c<1.))],color='blue',alpha=0.5,marker = 'x')
    plt.scatter(rf_m[np.where(z<0.6157)],SFR[np.where(z<0.6157)],c='red',alpha=0.5)
    plt.scatter(rf_m[np.where(z>0.6557)],SFR[np.where(z>0.6557)],c='red',alpha=0.5)   
    plt.xlim(7.5,11)
    #plt.ylim(-1,3)
    plt.xlabel('logM')
    plt.ylabel('logSFR')
    #plt.title('All pointings matched with LPD Halpha>0')
    red_patch = mpatches.Patch(color='red', label='Field', alpha = 0.5)
    blue_patch = mpatches.Patch(color='blue', label='Outside R200', alpha = 0.5)
    blue_star = mlines.Line2D([], [], color='blue', marker='x', linestyle='None',
                          markersize=10, label='Within R200')
    plt.legend(handles=[red_patch,blue_patch,blue_star],loc=2)

    plt.subplot(3,2,6)
    
    zc       = z[np.where((z>0.6157)&(z<0.6557))]  
    
    zf1       = z[np.where(z<0.6157)]   
    zf2       = z[np.where((z>0.6557))]

    x1 = zc
    x2 = zf1
    x3 = zf2
    
    
    kwargs1 = dict(histtype='stepfilled', alpha=0.3, normed=False, bins=2)
    kwargs2 = dict(histtype='stepfilled', alpha=0.3, normed=False, bins=12)
    kwargs3 = dict(histtype='stepfilled', alpha=0.3, normed=False, bins=3)



    
    plt.hist(x1,color='blue', **kwargs1)
    plt.hist(x2,color='red', **kwargs2)
    plt.hist(x3,color='red', **kwargs3);
    plt.xlabel('z')


    plt.show()
    





