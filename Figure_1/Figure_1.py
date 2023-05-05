
import itertools
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import math, numpy #, wx, random
import matplotlib.gridspec as gridspec
import matplotlib.cbook as cbook
import matplotlib.image as mpimg
from matplotlib.patches import FancyBboxPatch
import matplotlib.patches as patches

from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox


fig = plt.figure(figsize=(11, 11))



ax1 = plt.subplot2grid((4, 4), (0, 0),rowspan=1,colspan=3)
ax11 = plt.subplot2grid((4, 4), (0, 3),rowspan=1,colspan=1)
ax2 = plt.subplot2grid((4 ,4), (1, 0),rowspan=1,colspan=3)
ax22 = plt.subplot2grid((4 ,4), (1, 3),rowspan=1,colspan=1)

ax3 = plt.subplot2grid((4, 4), (2, 0),rowspan=1,colspan=3)
ax33 = plt.subplot2grid((4, 4), (2, 3),rowspan=1,colspan=1)
ax4 = plt.subplot2grid((4 ,4), (3, 0),rowspan=1,colspan=3)
ax44 = plt.subplot2grid((4 ,4), (3, 3),rowspan=1,colspan=1)



"""
ax1 = plt.subplot2grid((2, 1), (0, 0),rowspan=1,colspan=1)

ax2 = plt.subplot2grid((2 ,1), (1, 0),rowspan=1,colspan=1)
"""


couleur = '#2d4030'

ax1.set_xlim(0,1.0)
ax1.set_ylim(0,1.0)

ax1.plot((0.05,0.092),(0.65,0.65), color='grey')
ax1.plot((0.903,0.95),(0.65,0.65), color='grey')
ax1.plot((0.188,0.227),(0.65,0.65), color='grey')
ax1.plot((0.552,0.607),(0.65,0.65), color='grey')
p_fancy = FancyBboxPatch((0.1, 0.6), 0.08, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5 )
ax1.add_patch(p_fancy)
p_fancy = FancyBboxPatch((0.1 + 0.1347, 0.6), abs(0.31), 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5 )
ax1.add_patch(p_fancy)
p_fancy = FancyBboxPatch((0.1 + 0.5151, 0.6), abs(0.28), 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5 )
ax1.add_patch(p_fancy)

ax1.text(-0.1,0.99,'A',fontsize = 17)
ax2.text(-0.1,0.99,'B',fontsize = 17)
ax3.text(-0.1,0.99,'C',fontsize = 17)
ax4.text(-0.1,0.99,'D',fontsize = 17)
ax1.plot((0.09,0.129),(0.35,0.35), color='grey')
ax1.plot((0.852,0.891),(0.35,0.35), color='grey')
p_fancy = FancyBboxPatch((0.136, 0.3), 0.088, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5 )
ax1.add_patch(p_fancy)
p_fancy = FancyBboxPatch((0.15 + 0.0852, 0.3), abs(0.31), 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5 )
ax1.add_patch(p_fancy)
p_fancy = FancyBboxPatch((0.156 + 0.40, 0.3), abs(0.2882), 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5 )
ax1.add_patch(p_fancy)

ax11.set_ylim(0,1)
ax11.set_xlim(0,1)

ax11.text(-0.2,0.9,'Primers/probe | PCR product size',fontsize= 10)
ax11.plot((-0.2,1.5),(0.87,0.87), 'k', clip_on=False,linewidth = 0.75)

ax11.text(-0.2,0.7,"PH178_F TTTAGTCGGCTCTTATCCGGCATG",fontsize= 7.5)
ax11.text(-0.2,0.625,"PH178_R CAGCAAGTAATAGAACAGGTTCCCCT",fontsize= 7.5)
ax11.text(-0.2,0.55,"PH178_gDNA TCAGCTGGAGGATGGAGTTGACCCATGTT",color = 'r', fontsize= 7.5)
ax11.text(-0.2,0.4,"PH178_F TTTAGTCGGCTCTTATCCGGCATG",fontsize= 7.5)
ax11.text(-0.2,0.325,"PH178_R CAGCAAGTAATAGAACAGGTTCCCCT",fontsize= 7.5)
ax11.text(-0.2,0.25,"PH178_cDNA GCTTCAAGGAGAAAATTGCTCAGAACCA",color = 'r', fontsize= 7.5)
ax11.plot((1.35,1.35),(0.75,0.54), 'k', clip_on=False,linewidth = 0.75)
ax11.plot((1.35,1.35),(0.45,0.24), 'k', clip_on=False,linewidth = 0.75)
ax11.text(1.375,0.625,"157bp",fontsize= 7.5)
ax11.text(1.375,0.325,"84bp",fontsize= 7.5)




ax1.axis('off')
ax11.axis('off')
ax1.text(-0.05,0.95,'$\it{Phytophthora}$ $\it{ramorum}$ - PH178\n(SNARE associated Golgi protein)',fontsize = 10)

ax1.arrow(0.49,0.74,0.03,0., head_width=0.02, head_length=0.01, fc='k', ec='k')
ax1.arrow(0.675,0.56,-0.03,0., head_width=0.02, head_length=0.01, fc='k', ec='k')
ax1.plot((0.565,0.595),(0.675,0.675),'k',color = 'r')
ax1.text(0.42,0.733,'PH178_F',fontsize = 7)
ax1.text(0.679,0.547,'PH178_R',fontsize = 7)
ax1.text(0.61,0.76,'PH178_gDNA',fontsize = 7,color = 'r')
ax1.plot((0.59,0.598),(0.778,0.778),'k',linewidth= 0.4,color = 'r')
ax1.plot((0.59,0.575),(0.778,0.68),'k',linewidth= 0.4,color = 'r')

ax1.text(-0.02,0.63,'gDNA',fontsize = 9)
ax1.text(0.01,0.28,'cDNA\n(mRNA)',multialignment='center',fontsize = 9)


ax1.plot((0.095,0.095),(0.59,0.565),color = 'grey',linewidth = 0.75)
ax1.plot((0.13,0.13),(0.41,0.435),color = 'grey',linewidth = 0.75)
ax1.plot((0.095,0.13),(0.565,0.435),color = 'grey',linestyle = '--',linewidth = 0.75)
ax1.plot((0.185,0.185),(0.59,0.565),color = 'grey',linewidth = 0.75)
ax1.plot((0.23,0.23),(0.41,0.435),color = 'grey',linewidth = 0.75)
ax1.plot((0.185,0.23),(0.565,0.435),color = 'grey',linestyle = '--',linewidth = 0.75)
ax1.plot((0.23,0.23),(0.59,0.565),color = 'grey',linewidth = 0.75)
ax1.plot((0.23,0.23),(0.565,0.435),color = 'grey',linestyle = '--',linewidth = 0.75)
ax1.plot((0.55,0.55),(0.59,0.565),color = 'grey',linewidth = 0.75)
ax1.plot((0.55,0.55),(0.41,0.435),color = 'grey',linewidth = 0.75)
ax1.plot((0.55,0.55),(0.565,0.435),color = 'grey',linestyle = '--',linewidth = 0.75)
ax1.plot((0.61,0.61),(0.59,0.565),color = 'grey',linewidth = 0.75)
ax1.plot((0.61,0.55),(0.565,0.435),color = 'grey',linestyle = '--',linewidth = 0.75)
ax1.plot((0.90,0.90),(0.59,0.565),color = 'grey',linewidth = 0.75)
ax1.plot((0.849,0.849),(0.41,0.435),color = 'grey',linewidth = 0.75)
ax1.plot((0.90,0.849),(0.565,0.435),color = 'grey',linestyle = '--',linewidth = 0.75)

ax1.text(0.11,0.635,'Exon 1',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')
ax1.text(0.36,0.635,'Exon 2',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')
ax1.text(0.725,0.635,'Exon 3',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')

ax1.text(0.155,0.336,'100bp',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')
ax1.text(0.36,0.336,'372bp',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')
ax1.text(0.68,0.336,'334bp',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')





ax1.arrow(0.49,0.44,0.03,0., head_width=0.02, head_length=0.01, fc='k', ec='k')
ax1.arrow(0.615,0.26,-0.03,0., head_width=0.02, head_length=0.01, fc='k', ec='k')



ax1.plot((0.535,0.565),(0.26,0.26),'k',color = 'r')
ax1.text(0.42,0.433,'PH178_F',fontsize = 7)
ax1.text(0.624,0.247,'PH178_R',fontsize = 7)




ax1.plot((0.53,0.538),(0.16,0.16),'k',linewidth= 0.4,color = 'r')
ax1.plot((0.538,0.553),(0.16,0.26),'k',linewidth= 0.4,color = 'r')

ax1.text(0.425,0.14,'PH178_cDNA',fontsize = 7,color = 'r')




################## ax2 #######################

ax2.text(-0.05,0.95,'$\it{Phytophthora}$ $\it{cinnamomi}$ - PH027\n(Transcription initiation factor TFIID)',fontsize = 10)
ax2.text(0.03,0.63,'gDNA',fontsize = 9)
ax2.text(0.06,0.28,'cDNA\n(mRNA)',multialignment='center',fontsize = 9)

ax2.set_xlim(0,1.0)
ax2.set_ylim(0,1.0)
ax2.plot((0.1,0.9),(0.65,0.65), color='grey',zorder=1)
couleur = '#516823'

p_fancy = FancyBboxPatch((0.15, 0.6), 0.14488, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax2.add_patch(p_fancy)
p_fancy = FancyBboxPatch((0.33129, 0.6), 0.02441, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax2.add_patch(p_fancy)
p_fancy = FancyBboxPatch((0.38514, 0.6), 0.1902, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax2.add_patch(p_fancy)
p_fancy = FancyBboxPatch((0.71209, 0.6), 0.13791, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax2.add_patch(p_fancy)

ax2.text(0.20,0.635,'Exon 3',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')
ax2.text(0.335,0.635,'4',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')
ax2.text(0.45,0.635,'Exon 5',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')
ax2.text(0.75,0.635,'Exon 6',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')

ax2.arrow(0.335,0.74,0.012,0., head_width=0.02, head_length=0.01, fc='k', ec='k')
ax2.arrow(0.42,0.56,-0.012,0., head_width=0.02, head_length=0.01, fc='k', ec='k')
ax2.plot((0.365,0.375),(0.675,0.675),'r')

ax2.plot((0.377,0.385),(0.778,0.778),'r',linewidth= 0.4)
ax2.plot((0.377,0.369),(0.778,0.68),'r',linewidth= 0.4)

ax2.text(0.26,0.733,'PH027_F',fontsize = 7)
ax2.text(0.43,0.54,'PH027_R',fontsize = 7)
ax2.text(0.39,0.77,'PH027_gDNA',fontsize = 7,color = 'r')


p_fancy = FancyBboxPatch((0.2, 0.3), 0.164, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax2.add_patch(p_fancy)
p_fancy = FancyBboxPatch((0.3753, 0.3), 0.0201, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax2.add_patch(p_fancy)
p_fancy = FancyBboxPatch((0.4067, 0.3), 0.218, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax2.add_patch(p_fancy)
p_fancy = FancyBboxPatch((0.6358, 0.3), 0.1379, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax2.add_patch(p_fancy)


ax2.plot((0.15,0.82),(0.35,0.35), color='grey',zorder=1)
ax2.arrow(0.373,0.44,0.012,0., head_width=0.02, head_length=0.01, fc='k', ec='k')
ax2.arrow(0.44,0.26,-0.012,0., head_width=0.02, head_length=0.01, fc='k', ec='k')
ax2.plot((0.397,0.406),(0.26,0.26),'k',color = 'r')
ax2.text(0.299,0.433,'PH027_F',fontsize = 7)
ax2.text(0.451,0.24,'PH027_R',fontsize = 7)

ax2.plot((0.38,0.388),(0.16,0.16),'k',linewidth= 0.4,color = 'r')
ax2.plot((0.388,0.403),(0.16,0.26),'k',linewidth= 0.4,color = 'r')
ax2.text(0.27,0.14,'PH027_cDNA',fontsize = 7,color = 'r')



#little grey lines
ax2.plot((0.145,0.145),(0.59,0.565),color = 'grey',linewidth = 0.75)
ax2.plot((0.195,0.195),(0.41,0.435),color = 'grey',linewidth = 0.75)
ax2.plot((0.145,0.195),(0.565,0.435),color = 'grey',linestyle = '--',linewidth = 0.75)

ax2.plot((0.38,0.38),(0.59,0.565),color = 'grey',linewidth = 0.75)
ax2.plot((0.401,0.401),(0.41,0.435),color = 'grey',linewidth = 0.75)
ax2.plot((0.38,0.401),(0.565,0.435),color = 'grey',linestyle = '--',linewidth = 0.75)

ax2.plot((0.58,0.58),(0.59,0.565),color = 'grey',linewidth = 0.75)
ax2.plot((0.63,0.63),(0.41,0.435),color = 'grey',linewidth = 0.75)
ax2.plot((0.58,0.63),(0.565,0.435),color = 'grey',linestyle = '--',linewidth = 0.75)

ax2.plot((0.707,0.707),(0.59,0.565),color = 'grey',linewidth = 0.75)
ax2.plot((0.63,0.63),(0.41,0.435),color = 'grey',linewidth = 0.75)
ax2.plot((0.707,0.63),(0.565,0.435),color = 'grey',linestyle = '--',linewidth = 0.75)

ax2.plot((0.855,0.855),(0.59,0.565),color = 'grey',linewidth = 0.75)
ax2.plot((0.778,0.778),(0.41,0.435),color = 'grey',linewidth = 0.75)
ax2.plot((0.855,0.778),(0.565,0.435),color = 'grey',linestyle = '--',linewidth = 0.75)





ax2.text(0.26,0.335,'374bp',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')
ax2.text(0.376,0.315,'63\nbp',fontsize=5.5,multialignment='center',color= '#ffffff',weight ='bold')
ax2.text(0.49,0.335,'491bp',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')
ax2.text(0.68,0.335,'435bp',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')



ax22.set_ylim(0,1)
ax22.set_xlim(0,1)

ax22.text(-0.2,0.7,"PH027_F ACCGCTCTCAAGTGCTCCGAGTC",fontsize= 7.5)
ax22.text(-0.2,0.625,"PH027_R GCATTCGATAGCTGCTCGTCACGA",fontsize= 7.5)
ax22.text(-0.2,0.55,"PH027_gDNA CCGTGCTGACATTACTGGCTGGTGCTTGCA",color = 'r', fontsize= 7.5)
ax22.text(-0.2,0.4,"PH027_F ACCGCTCTCAAGTGCTCCGAGTC",fontsize= 7.5)
ax22.text(-0.2,0.325,"PH027_R GCATTCGATAGCTGCTCGTCACGA",fontsize= 7.5)
ax22.text(-0.2,0.25,"PH027_cDNA TCAACTCACGCCGTAGATGCTGCCAAGAAA",color = 'r', fontsize= 7.5)
ax22.plot((1.40,1.40),(0.75,0.54), 'k', clip_on=False,linewidth = 0.75)
ax22.plot((1.40,1.40),(0.45,0.24), 'k', clip_on=False,linewidth = 0.75)
ax22.text(1.42,0.625,"176bp",fontsize= 7.5)
ax22.text(1.42,0.325,"102bp",fontsize= 7.5)

ax2.axis('off')
ax22.axis('off')


################## ax3 #######################
ax3.text(-0.05,0.95,'$\it{Phytophthora}$ $\it{alni}$ - PH149\n(TLC domain-containing protein 1)',fontsize = 10)
ax3.set_xlim(0,1.0)
ax3.set_ylim(0,1.0)
ax3.plot((0.1,0.95),(0.65,0.65), color='grey',zorder=1)
ax3.text(0.03,0.63,'gDNA',fontsize = 9)
ax3.text(0.07,0.28,'cDNA\n(mRNA)',multialignment='center',fontsize = 9)
ax3.axis('off')
ax33.axis('off')
couleur = '#dec000'

#top
p_fancy = FancyBboxPatch((0.15, 0.6), 0.1319, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax3.add_patch(p_fancy)
p_fancy = FancyBboxPatch((0.3904, 0.6), 0.0944, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax3.add_patch(p_fancy)
p_fancy = FancyBboxPatch((0.5925, 0.6), 0.30, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax3.add_patch(p_fancy)

ax3.text(0.19,0.635,'Exon 1',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')
ax3.text(0.41,0.635,'Exon 2',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')
ax3.text(0.72,0.635,'Exon 3',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')

ax3.arrow(0.405,0.74,0.024,0., head_width=0.02, head_length=0.01, fc='k', ec='k')
ax3.arrow(0.63,0.56,-0.024,0., head_width=0.02, head_length=0.01, fc='k', ec='k')
ax3.plot((0.53,0.56),(0.675,0.675),'r')

ax3.plot((0.552,0.56),(0.778,0.778),'r',linewidth= 0.4)
ax3.plot((0.552,0.544),(0.778,0.68),'r',linewidth= 0.4)

ax3.text(0.33,0.733,'PH149_F',fontsize = 7)
ax3.text(0.64,0.54,'PH149_R',fontsize = 7)
ax3.text(0.57,0.77,'PH149_gDNA',fontsize = 7,color = 'r')






#bottom
p_fancy = FancyBboxPatch((0.2, 0.3), 0.1489, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax3.add_patch(p_fancy)
p_fancy = FancyBboxPatch((0.36, 0.3), 0.1087, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax3.add_patch(p_fancy)
p_fancy = FancyBboxPatch((0.48, 0.3), 0.3074, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax3.add_patch(p_fancy)


ax3.plot((0.15,0.82),(0.35,0.35), color='grey',zorder=1)
ax3.arrow(0.38,0.44,0.024,0., head_width=0.02, head_length=0.01, fc='k', ec='k')
ax3.arrow(0.525,0.26,-0.024,0., head_width=0.02, head_length=0.01, fc='k', ec='k')
ax3.plot((0.462,0.487),(0.26,0.26),'k',color = 'r')
ax3.text(0.305,0.433,'PH149_F',fontsize = 7)
ax3.text(0.535,0.24,'PH149_R',fontsize = 7)

ax3.plot((0.45,0.458),(0.16,0.16),'k',linewidth= 0.4,color = 'r')
ax3.plot((0.458,0.473),(0.16,0.26),'k',linewidth= 0.4,color = 'r')
ax3.text(0.34,0.14,'PH149_cDNA',fontsize = 7,color = 'r')

ax3.text(0.245,0.335,'109bp',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')
ax3.text(0.39,0.335,'79bp',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')
ax3.text(0.605,0.335,'176bp',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')



#little grey lines ax3
ax3.plot((0.145,0.145),(0.59,0.565),color = 'grey',linewidth = 0.75)
ax3.plot((0.195,0.195),(0.41,0.435),color = 'grey',linewidth = 0.75)
ax3.plot((0.145,0.195),(0.565,0.435),color = 'grey',linestyle = '--',linewidth = 0.75)


ax3.plot((0.49,0.49),(0.59,0.565),color = 'grey',linewidth = 0.75)
ax3.plot((0.475,0.475),(0.41,0.435),color = 'grey',linewidth = 0.75)
ax3.plot((0.49,0.475),(0.565,0.435),color = 'grey',linestyle = '--',linewidth = 0.75)


ax3.plot((0.587,0.587),(0.59,0.565),color = 'grey',linewidth = 0.75)
ax3.plot((0.475,0.475),(0.41,0.435),color = 'grey',linewidth = 0.75)
ax3.plot((0.587,0.475),(0.565,0.435),color = 'grey',linestyle = '--',linewidth = 0.75)


ax3.plot((0.897,0.897),(0.59,0.565),color = 'grey',linewidth = 0.75)
ax3.plot((0.791,0.791),(0.41,0.435),color = 'grey',linewidth = 0.75)
ax3.plot((0.897,0.791),(0.565,0.435),color = 'grey',linestyle = '--',linewidth = 0.75)

ax33.set_ylim(0,1)
ax33.set_xlim(0,1)

ax33.text(-0.3,0.7,"PH149_F AGCTGCGATATGCCATTGTGCTAGT",fontsize= 7.5)
ax33.text(-0.3,0.625,"PH149_R CGCGATCCAGTACAAACTCTCCTTAG",fontsize= 7.5)
ax33.text(-0.3,0.55,"PH149_gDNA AGTCGTTGAAAACCAGAAGCCAAGTTGAAG",color = 'r', fontsize= 7.5)
ax33.text(-0.3,0.4,"PH149_F AGCTGCGATATGCCATTGTGCTAGT",fontsize= 7.5)
ax33.text(-0.3,0.325,"PH149_R CGCGATCCAGTACAAACTCTCCTTAG",fontsize= 7.5)
ax33.text(-0.3,0.25,"PH149_cDNA ATCGGGTTGCTCGAAGATCTGCTGGAACAG",color = 'r', fontsize= 7.5)
ax33.plot((1.32,1.32),(0.75,0.54), 'k', clip_on=False,linewidth = 0.75)
ax33.plot((1.32,1.32),(0.45,0.24), 'k', clip_on=False,linewidth = 0.75)
ax33.text(1.35,0.625,"184bp",fontsize= 7.5)
ax33.text(1.35,0.325,"125bp",fontsize= 7.58)



################## ax4 #######################
ax4.text(-0.05,0.95,'$\it{Phytophthora}$ $\it{lateralis}$ - PH218\n(Chorismate mutase)',fontsize = 10)
ax4.set_xlim(0,1.0)
ax4.set_ylim(0,1.0)
ax4.plot((0.05,0.95),(0.65,0.65), color='grey',zorder=1)
ax4.text(-0.02,0.63,'gDNA',fontsize = 9)
ax4.text(0.07,0.28,'cDNA\n(mRNA)',multialignment='center',fontsize = 9)

couleur = '#677e8e'

p_fancy = FancyBboxPatch((0.1, 0.6), 0.03644, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax4.add_patch(p_fancy)
p_fancy = FancyBboxPatch((0.1759, 0.6), 0.1264, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax4.add_patch(p_fancy)
p_fancy = FancyBboxPatch((0.3660, 0.6), 0.5339, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax4.add_patch(p_fancy)

ax4.text(0.1,0.635,'Ex.8',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')
ax4.text(0.21,0.635,'Exon 9',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')
ax4.text(0.605,0.635,'Exon 10',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')

ax4.arrow(0.24,0.74,0.024,0., head_width=0.02, head_length=0.01, fc='k', ec='k')
ax4.arrow(0.405,0.56,-0.024,0., head_width=0.02, head_length=0.01, fc='k', ec='k')
ax4.plot((0.318,0.348),(0.675,0.675),'r')

ax4.plot((0.335,0.34),(0.778,0.778),'r',linewidth= 0.4)
ax4.plot((0.335,0.331),(0.778,0.68),'r',linewidth= 0.4)

ax4.text(0.163,0.733,'PH218_F',fontsize = 7)
ax4.text(0.415,0.54,'PH218_R',fontsize = 7)
ax4.text(0.348,0.77,'PH218_gDNA',fontsize = 7,color = 'r')





#bottom
ax4.plot((0.15,0.9),(0.35,0.35), color='grey',zorder=1)
p_fancy = FancyBboxPatch((0.2, 0.3), 0.0299, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax4.add_patch(p_fancy)
p_fancy = FancyBboxPatch((0.2415, 0.3), 0.125, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax4.add_patch(p_fancy)
p_fancy = FancyBboxPatch((0.378, 0.3), 0.48, 0.1,boxstyle="round,pad=0.005",facecolor = couleur, edgecolor = '#222222', linewidth=0.5, zorder=2 )
ax4.add_patch(p_fancy)

ax4.text(0.197,0.335,'83bp',fontsize=5.5,multialignment='center',color= '#ffffff',weight ='bold')
ax4.text(0.275,0.335,'288bp',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')
ax4.text(0.605,0.335,'1216bp',fontsize=7,multialignment='center',color= '#ffffff',weight ='bold')

ax4.arrow(0.30,0.44,0.024,0., head_width=0.02, head_length=0.01, fc='k', ec='k')
ax4.arrow(0.421,0.26,-0.024,0., head_width=0.02, head_length=0.01, fc='k', ec='k')
ax4.plot((0.352,0.382),(0.26,0.26),'k',color = 'r')

ax4.text(0.225,0.433,'PH218_F',fontsize = 7)
ax4.text(0.435,0.24,'PH218_R',fontsize = 7)

ax4.plot((0.35,0.358),(0.16,0.16),'k',linewidth= 0.4,color = 'r')
ax4.plot((0.358,0.373),(0.16,0.26),'k',linewidth= 0.4,color = 'r')
ax4.text(0.24,0.14,'PH218_cDNA',fontsize = 7,color = 'r')



ax4.axis('off')
ax44.axis('off')



ax44.set_ylim(0,1)
ax44.set_xlim(0,1)

ax44.text(-0.3,0.7,"PH218_F CGGATCAACATCAACGACCAGATTAT",fontsize= 7.5)
ax44.text(-0.3,0.625,"PH218_R ACTTGCCAAAATGAATACGCTTGCT",fontsize= 7.5)
ax44.text(-0.3,0.55,"PH218_gDNA GTAAACCAATTGGTGGTTGAGTTGCTGC",color = 'r', fontsize= 7.5)
ax44.text(-0.3,0.4,"PH218_F CGGATCAACATCAACGACCAGATTAT",fontsize= 7.5)
ax44.text(-0.3,0.325,"PH218_R ACTTGCCAAAATGAATACGCTTGCT",fontsize= 7.5)
ax44.text(-0.3,0.25,"PH218_cDNA ACGACACCGCGTATGGCTCTACG",color = 'r', fontsize= 7.5)
ax44.plot((1.26,1.26),(0.75,0.54), 'k', clip_on=False,linewidth = 0.75)
ax44.plot((1.26,1.26),(0.45,0.24), 'k', clip_on=False,linewidth = 0.75)
ax44.text(1.285,0.625,"227bp",fontsize= 7.5)
ax44.text(1.285,0.325,"157bp",fontsize= 7.5)


#little grey lines ax3
ax4.plot((0.095,0.095),(0.59,0.565),color = 'grey',linewidth = 0.75)
ax4.plot((0.195,0.195),(0.41,0.435),color = 'grey',linewidth = 0.75)
ax4.plot((0.095,0.195),(0.565,0.435),color = 'grey',linestyle = '--',linewidth = 0.75)

ax4.plot((0.308,0.308),(0.59,0.565),color = 'grey',linewidth = 0.75)
ax4.plot((0.3725,0.3725),(0.41,0.435),color = 'grey',linewidth = 0.75)
ax4.plot((0.308,0.3725),(0.565,0.435),color = 'grey',linestyle = '--',linewidth = 0.75)

ax4.plot((0.36,0.36),(0.59,0.565),color = 'grey',linewidth = 0.75)
ax4.plot((0.3725,0.3725),(0.41,0.435),color = 'grey',linewidth = 0.75)
ax4.plot((0.36,0.3725),(0.565,0.435),color = 'grey',linestyle = '--',linewidth = 0.75)


ax4.plot((0.905,0.905),(0.59,0.565),color = 'grey',linewidth = 0.75)
ax4.plot((0.862,0.862),(0.41,0.435),color = 'grey',linewidth = 0.75)
ax4.plot((0.905,0.862),(0.565,0.435),color = 'grey',linestyle = '--',linewidth = 0.75)


#plt.tight_layout()
plt.savefig('Figure_1.png',dpi=800,  format='png')

