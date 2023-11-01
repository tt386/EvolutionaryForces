from Params import *

import sys

import time 

import random
import numpy as np
import matplotlib.pyplot as plt


random.seed(RandomSeed)


def Data(W0,M0,F,Mu,G,N,T):
    #LIst of timesteps
    Wt = [W0]
    Mt = [M0]

    #Theory Results
    M_Theory = 1
    if F < 1:
        M_Theory = min(1,(Mu + G*F)/(1-F))

    for t in range(T-1):
        w = Wt[-1]
        m = Mt[-1]


        #POst Migration
        wg = 1*w
        mg = m+G

        #Post Selection
        ws = 1*wg
        ms = F*mg


        #Post Breeding
        wb = ws/(ws+ms)
        mb = ms/(ws+ms)

        #Add noise
        n=0
        if wb >0 and mb > 0:
            n = random.uniform(-N, N)

        wn = max(0,wb+n)
        mn = max(0,mb-n)

        #Post Mutation
        wm = wn*(1-Mu)
        mm = mn + Mu*wn

        #Append to list
        Wt.append(wm)
        Mt.append(mm)


    ###########################################################################

    #PLOTTING
    # Set the figure size in millimeters
    fig_width_mm = 45
    fig_height_mm = 45
    fig_size = (fig_width_mm / 25.4, fig_height_mm / 25.4)  # Convert mm to inches (25.4 mm in an inch)
    
    
    fig = plt.figure(figsize=fig_size)
    ax = fig.add_subplot(111)
    
    plt.plot(np.arange(T),Wt,color='cyan',linewidth=3)
    plt.plot(np.arange(T),Mt,color='red',linewidth=3)
    
    plt.plot([0,T],[M_Theory,M_Theory],'--k',linewidth=3)
    
    plt.ylim(0,1)
    plt.xlim(0,T)
    
    xticks = [0,T/2,T]
    yticks = [0,0.5,1]
    
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    
    plt.xticks(fontsize=15,fontname = "Arial")
    plt.yticks(fontsize=15,fontname = "Arial")
    
    text = r"$M^* = \frac{\mu + GF}{1-F}$"
    
    if Mu<=0 and G>0:
        text = r"$M^* = \frac{GF}{1-F}$"
    
    elif Mu>0 and G<=0:
        text = r"$M^* = \frac{\mu}{1-F}$"
        
    elif Mu <= 0 and G<=0:
        text = r"$M^* = 0$"
        
    plt.text(600, M_Theory, text,horizontalalignment='center',
         verticalalignment='bottom',fontsize=15)# fontdict=None, **kwargs)


    plt.savefig(SaveDirName + "/T_%d"%(T) +
        "_W0_%0.1f_M0_%0.1f"%(W0,M0) +
        "_F_%0.2f"%(F) +
        "_Mu_" + f"{Mu:.{1}e}" +
        "_G_" + f"{G:.{1}e}" +
        "_N_" + f"{N:.{1}e}" +
        ".pdf",bbox_inches='tight',dpi=300)

###############################################################################
#Create Data

Data(W0,M0,F,0,0,0,T)

Data(W0,M0,F,Mu,0,0,T)

Data(W0,M0,F,0,G,0,T)

Data(W0,M0,F,0,0,N,T)

Data(W0,M0,F,Mu,G,N,T)


