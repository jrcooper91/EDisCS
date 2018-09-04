import pyfits 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import astropy 
from astropy import cosmology 
import math as mt




def c1301(f_Ha,rf_J,rf_U,rf_V,rf_VJ,rf_UV):
    plt.figure(figsize=(18, 16), dpi= 80, facecolor='w', edgecolor='k')
    plt.subplot(2,2,1)
    f = open('/Users/jennifercooper/Documents/Gal_Ev/EDisCS/G102/clusters/1301-1139/cluster_z_match.txt', 'r')
    lines = f.readlines()[1:]
    f.close()
    
    #create arrays 
    f_Ha    = [] 
    rf_J    = []
    rf_U    = []
    rf_V    = []
    rf_VJ   = []
    rf_UV   = []
    
    #pull array column 
    for line in lines: 
        a = line.split()
        f_Ha.append(float(a[4]))
        rf_J.append(float(a[7]))
        rf_U.append(float(a[8]))
        rf_V.append(float(a[9]))
        rf_VJ.append(float(a[10]))
        rf_UV.append(float(a[11]))
        
    f_Ha = np.array(f_Ha)
    f_Ha_log = np.log10(f_Ha)
    rf_J = np.array(rf_J)
    rf_U = np.array(rf_U)
    rf_V = np.array(rf_V)
    rf_VJ = np.array(rf_VJ)
    rf_UV = np.array(rf_UV)
    
    plt.scatter(rf_VJ,rf_UV,c=f_Ha_log,alpha=0.7)
    cbar = plt.colorbar()
    cbar.set_label("log(Halpha)")
    plt.xlabel('VJ')
    plt.ylabel('UV')
    plt.title('Cluster UVJ z+/- 0.02')
    plt.xlim(-2,2)
    plt.ylim(-2,3)
    
    plt.subplot(2,2,2)
    plt.scatter(rf_V,rf_UV,c=f_Ha_log,alpha=0.7)
    cbar = plt.colorbar()
    cbar.set_label("log(Halpha)")
    plt.xlabel('V')
    plt.ylabel('UV')
    plt.title('Cluster z+/- 0.02')
    plt.xlim(0,20)
    plt.ylim(-2,3)
    
    plt.subplot(2,2,3)
    plt.scatter(rf_VJ[np.where(f_Ha>0)],rf_UV[np.where(f_Ha>0)],c='red',alpha=0.2)
    plt.scatter(rf_VJ[np.where(f_Ha<1E-21)],rf_UV[np.where(f_Ha<1E-21)],c='blue',alpha=0.2)
    plt.xlim(-4,3)
    plt.ylim(-1,3)
    plt.xlabel('V-J')
    plt.ylabel('U-V')
    #plt.title('All pointings matched with LPD Halpha>0')
    red_patch = mpatches.Patch(color='purple', label='H alpha Detection', alpha = 0.5)
    blue_patch = mpatches.Patch(color='blue', label='No detection', alpha = 0.5)
    plt.legend(handles=[red_patch,blue_patch])
    
    plt.show()



def c1227(f_Ha,rf_J,rf_U,rf_V,rf_VJ,rf_UV):
    plt.figure(figsize=(18, 16), dpi= 80, facecolor='w', edgecolor='k')
    plt.subplot(2,2,1)
    f = open('/Users/jennifercooper/Documents/Gal_Ev/EDisCS/G102/clusters/1227-1138/cluster_z_match.txt', 'r')
    lines = f.readlines()[1:]
    f.close()
    
    #create arrays 
    f_Ha    = [] 
    rf_J    = []
    rf_U    = []
    rf_V    = []
    rf_VJ   = []
    rf_UV   = []
    
    #pull array column 
    for line in lines: 
        a = line.split()
        f_Ha.append(float(a[4]))
        rf_J.append(float(a[7]))
        rf_U.append(float(a[8]))
        rf_V.append(float(a[9]))
        rf_VJ.append(float(a[10]))
        rf_UV.append(float(a[11]))
        
    f_Ha = np.array(f_Ha)
    f_Ha_log = np.log10(f_Ha)
    rf_J = np.array(rf_J)
    rf_U = np.array(rf_U)
    rf_V = np.array(rf_V)
    rf_VJ = np.array(rf_VJ)
    rf_UV = np.array(rf_UV)
    
    plt.scatter(rf_VJ,rf_UV,c=f_Ha_log,alpha=0.7)
    cbar = plt.colorbar()
    cbar.set_label("log(Halpha)")
    plt.xlabel('VJ')
    plt.ylabel('UV')
    plt.title('Cluster UVJ z+/- 0.02')
    plt.xlim(-2,2)
    plt.ylim(-2,3)
    
    plt.subplot(2,2,2)
    plt.scatter(rf_V,rf_UV,c=f_Ha_log,alpha=0.7)
    cbar = plt.colorbar()
    cbar.set_label("log(Halpha)")
    plt.xlabel('V')
    plt.ylabel('UV')
    plt.title('Cluster z+/- 0.02')
    plt.xlim(0,20)
    plt.ylim(-2,3)
    
    plt.subplot(2,2,3)
    plt.scatter(rf_VJ[np.where(f_Ha>0)],rf_UV[np.where(f_Ha>0)],c='red',alpha=0.2)
    plt.scatter(rf_VJ[np.where(f_Ha<1E-21)],rf_UV[np.where(f_Ha<1E-21)],c='blue',alpha=0.2)
    plt.xlim(-4,3)
    plt.ylim(-1,3)
    plt.xlabel('V-J')
    plt.ylabel('U-V')
    #plt.title('All pointings matched with LPD Halpha>0')
    red_patch = mpatches.Patch(color='purple', label='H alpha Detection', alpha = 0.5)
    blue_patch = mpatches.Patch(color='blue', label='No detection', alpha = 0.5)
    plt.legend(handles=[red_patch,blue_patch])
    
    plt.show()



def c1138(f_Ha,rf_J,rf_U,rf_V,rf_VJ,rf_UV):
    plt.figure(figsize=(18, 16), dpi= 80, facecolor='w', edgecolor='k')
    plt.subplot(2,2,1)
    f = open('/Users/jennifercooper/Documents/Gal_Ev/EDisCS/G102/clusters/1138_1133/cluster_z_match.txt', 'r')
    lines = f.readlines()[1:]
    f.close()
    
    #create arrays 
    f_Ha    = [] 
    rf_J    = []
    rf_U    = []
    rf_V    = []
    rf_VJ   = []
    rf_UV   = []
    
    #pull array column 
    for line in lines: 
        a = line.split()
        f_Ha.append(float(a[4]))
        rf_J.append(float(a[7]))
        rf_U.append(float(a[8]))
        rf_V.append(float(a[9]))
        rf_VJ.append(float(a[10]))
        rf_UV.append(float(a[11]))
        
    f_Ha = np.array(f_Ha)
    f_Ha_log = np.log10(f_Ha)
    rf_J = np.array(rf_J)
    rf_U = np.array(rf_U)
    rf_V = np.array(rf_V)
    rf_VJ = np.array(rf_VJ)
    rf_UV = np.array(rf_UV)
    
    plt.scatter(rf_VJ,rf_UV,c=f_Ha_log,alpha=0.7)
    cbar = plt.colorbar()
    cbar.set_label("log(Halpha)")
    plt.xlabel('VJ')
    plt.ylabel('UV')
    plt.title('Cluster UVJ z+/- 0.02')
    plt.xlim(-2,2)
    plt.ylim(-2,3)
    
    plt.subplot(2,2,2)
    plt.scatter(rf_V,rf_UV,c=f_Ha_log,alpha=0.7)
    cbar = plt.colorbar()
    cbar.set_label("log(Halpha)")
    plt.xlabel('V')
    plt.ylabel('UV')
    plt.title('Cluster z+/- 0.02')
    plt.xlim(0,20)
    plt.ylim(-2,3)
    
    plt.subplot(2,2,3)
    plt.scatter(rf_VJ[np.where(f_Ha>0)],rf_UV[np.where(f_Ha>0)],c='red',alpha=0.2)
    plt.scatter(rf_VJ[np.where(f_Ha<1E-21)],rf_UV[np.where(f_Ha<1E-21)],c='blue',alpha=0.2)
    plt.xlim(-4,3)
    plt.ylim(-1,3)
    plt.xlabel('V-J')
    plt.ylabel('U-V')
    #plt.title('All pointings matched with LPD Halpha>0')
    red_patch = mpatches.Patch(color='purple', label='H alpha Detection', alpha = 0.5)
    blue_patch = mpatches.Patch(color='blue', label='No detection', alpha = 0.5)
    plt.legend(handles=[red_patch,blue_patch])
    
    plt.show()


def c1059(f_Ha,rf_J,rf_U,rf_V,rf_VJ,rf_UV):
    plt.figure(figsize=(18, 16), dpi= 80, facecolor='w', edgecolor='k')
    plt.subplot(2,2,1)
    f = open('/Users/jennifercooper/Documents/Gal_Ev/EDisCS/G102/clusters/1059-1253/cluster_z_match.txt', 'r')
    lines = f.readlines()[1:]
    f.close()
    
    #create arrays 
    f_Ha    = [] 
    rf_J    = []
    rf_U    = []
    rf_V    = []
    rf_VJ   = []
    rf_UV   = []
    
    #pull array column 
    for line in lines: 
        a = line.split()
        f_Ha.append(float(a[4]))
        rf_J.append(float(a[7]))
        rf_U.append(float(a[8]))
        rf_V.append(float(a[9]))
        rf_VJ.append(float(a[10]))
        rf_UV.append(float(a[11]))
        
    f_Ha = np.array(f_Ha)
    f_Ha_log = np.log10(f_Ha)
    rf_J = np.array(rf_J)
    rf_U = np.array(rf_U)
    rf_V = np.array(rf_V)
    rf_VJ = np.array(rf_VJ)
    rf_UV = np.array(rf_UV)
    
    plt.scatter(rf_VJ,rf_UV,c=f_Ha_log,alpha=0.7)
    cbar = plt.colorbar()
    cbar.set_label("log(Halpha)")
    plt.xlabel('VJ')
    plt.ylabel('UV')
    plt.title('Cluster UVJ z+/- 0.02')
    plt.xlim(-2,2)
    plt.ylim(-2,3)
    
    plt.subplot(2,2,2)
    plt.scatter(rf_V,rf_UV,c=f_Ha_log,alpha=0.7)
    cbar = plt.colorbar()
    cbar.set_label("log(Halpha)")
    plt.xlabel('V')
    plt.ylabel('UV')
    plt.title('Cluster z+/- 0.02')
    plt.xlim(0,20)
    plt.ylim(-2,3)
    
    plt.subplot(2,2,3)
    plt.scatter(rf_VJ[np.where(f_Ha>0)],rf_UV[np.where(f_Ha>0)],c='red',alpha=0.2)
    plt.scatter(rf_VJ[np.where(f_Ha<1E-21)],rf_UV[np.where(f_Ha<1E-21)],c='blue',alpha=0.2)
    plt.xlim(-4,3)
    plt.ylim(-1,3)
    plt.xlabel('V-J')
    plt.ylabel('U-V')
    #plt.title('All pointings matched with LPD Halpha>0')
    red_patch = mpatches.Patch(color='purple', label='H alpha Detection', alpha = 0.5)
    blue_patch = mpatches.Patch(color='blue', label='No detection', alpha = 0.5)
    plt.legend(handles=[red_patch,blue_patch])
    
    plt.show()





