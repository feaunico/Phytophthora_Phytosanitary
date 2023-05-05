

import numpy as np
import matplotlib.pyplot as plt



fx = open('CqValues.txt')
cq = fx.readlines()
fx.close()


gDNAh = {'Pcin':[],'Pram':[],'Plat':[],'Paln':[]}
gDNAc = {'Pcin':[],'Pram':[],'Plat':[],'Paln':[]}

cDNAh = {'Pcin':[],'Pram':[],'Plat':[],'Paln':[]}
cDNAc = {'Pcin':[],'Pram':[],'Plat':[],'Paln':[]}

for x in cq[1:]:
    if x.split('\t')[1] == 'gDNA':
        if x.split('\t')[0] == 'Palni':
            if x.split('\t')[2] == 'Treated':
                gDNAh['Paln'].append(float(x.split('\t')[-1].replace(',','.').replace('\n','')))
            else:
                gDNAc['Paln'].append(float(x.split('\t')[-1].replace(',','.').replace('\n','')))
        elif x.split('\t')[0] == 'Plateralis':
            if x.split('\t')[2] == 'Treated':
                gDNAh['Plat'].append(float(x.split('\t')[-1].replace(',','.').replace('\n','')))
            else:
                gDNAc['Plat'].append(float(x.split('\t')[-1].replace(',','.').replace('\n','')))
        elif x.split('\t')[0] == 'Pramorum':
            if x.split('\t')[2] == 'Treated':
                gDNAh['Pram'].append(float(x.split('\t')[-1].replace(',','.').replace('\n','')))
            else:
                gDNAc['Pram'].append(float(x.split('\t')[-1].replace(',','.').replace('\n','')))
        else :
            if x.split('\t')[2] == 'Treated':
                gDNAh['Pcin'].append(float(x.split('\t')[-1].replace(',','.').replace('\n','')))
            else:
                gDNAc['Pcin'].append(float(x.split('\t')[-1].replace(',','.').replace('\n','')))
    else:
        if x.split('\t')[0] == 'Palni':
            if x.split('\t')[2] == 'Treated':
                cDNAh['Paln'].append(float(x.split('\t')[-1].replace(',','.').replace('\n','')))
            else:
                cDNAc['Paln'].append(float(x.split('\t')[-1].replace(',','.').replace('\n','')))
        elif x.split('\t')[0] == 'Plateralis':
            if x.split('\t')[2] == 'Treated':
                cDNAh['Plat'].append(float(x.split('\t')[-1].replace(',','.').replace('\n','')))
            else:
                cDNAc['Plat'].append(float(x.split('\t')[-1].replace(',','.').replace('\n','')))
        elif x.split('\t')[0] == 'Pramorum':
            if x.split('\t')[2] == 'Treated':
                cDNAh['Pram'].append(float(x.split('\t')[-1].replace(',','.').replace('\n','')))
            else:
                cDNAc['Pram'].append(float(x.split('\t')[-1].replace(',','.').replace('\n','')))
        else :
            if x.split('\t')[2] == 'Treated':
                cDNAh['Pcin'].append(float(x.split('\t')[-1].replace(',','.').replace('\n','')))
            else:
                cDNAc['Pcin'].append(float(x.split('\t')[-1].replace(',','.').replace('\n','')))

print gDNAc
print gDNAh
print cDNAc
print cDNAh



fig = plt.figure(figsize=(8, 7))   #figsize=(10, 14)
ax1 = plt.subplot2grid((2,2), (1, 0),)
ax2 = plt.subplot2grid((2, 2), (0, 1),)
ax3 = plt.subplot2grid((2, 2), (1, 1),)
ax4 = plt.subplot2grid((2, 2), (0, 0),)






bp = ax1.boxplot([gDNAc['Paln'], gDNAh['Paln'], cDNAc['Paln'], cDNAh['Paln']], [0,1,3,4],patch_artist=True,  widths = [0.6, 0.6, 0.6,0.6],showfliers=True)
#bp = ax1.boxplot([pi1, pi3], patch_artist=True, widths = [0.5, 0.5])

colors = ['#dec000', '#dec000','#dec000','#dec000']
n = 1
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    if n%2==0:
            patch.set_hatch('....')
            patch.set_alpha(0.6)
    n = n + 1


for median in bp['medians']:
    median.set(color='w', linewidth=2)
bp['medians'][3].set(color='k', linewidth=2)

bp = ax2.boxplot([gDNAc['Pcin'], gDNAh['Pcin'], cDNAc['Pcin'], cDNAh['Pcin']], [0, 1, 3, 4], patch_artist=True,
        widths=[0.6, 0.6, 0.6, 0.6], showfliers=True)
# bp = ax1.boxplot([pi1, pi3], patch_artist=True, widths = [0.5, 0.5])

colors = ['#516823', '#516823', '#516823', '#516823']
n=1
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    #patch.set_edgecolor('w')
    if n%2==0:
            patch.set_hatch('....')
            patch.set_alpha(0.6)

    n = n + 1



for median in bp['medians']:
    median.set(color='w', linewidth=2)
bp['medians'][3].set(color='k', linewidth=2)

bp = ax3.boxplot([gDNAc['Plat'], gDNAh['Plat'], cDNAc['Plat'], cDNAh['Plat']], [0, 1, 3, 4], patch_artist=True,
        widths=[0.6, 0.6, 0.6, 0.6], showfliers=True)
# bp = ax1.boxplot([pi1, pi3], patch_artist=True, widths = [0.5, 0.5])

colors = ['#677e8e', '#677e8e', '#677e8e', '#677e8e']
n = 1
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    if n%2==0:
            patch.set_hatch('....')
            patch.set_alpha(0.6)
    n = n + 1


for median in bp['medians']:
    median.set(color='w', linewidth=2)
bp['medians'][3].set(color='k', linewidth=2)

bp = ax4.boxplot([gDNAc['Pram'], gDNAh['Pram'], cDNAc['Pram'], cDNAh['Pram']], [0, 1, 3, 4], patch_artist=True,
        widths=[0.6, 0.6, 0.6, 0.6], showfliers=True)
# bp = ax1.boxplot([pi1, pi3], patch_artist=True, widths = [0.5, 0.5])

colors = ['#2d4030', '#2d4030', '#2d4030', '#2d4030']
n = 1
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    if n%2==0:
            patch.set_hatch('....')
            patch.set_alpha(0.6)
    n = n + 1

for median in bp['medians']:
    median.set(color='w', linewidth=2)
bp['medians'][3].set(color='k', linewidth=2)

ax1.set_ylim(18,44)
ax2.set_ylim(18,44)
ax3.set_ylim(18,44)
ax4.set_ylim(18,44)

ax1.set_yticks([20,25,30,35,40])
ax1.set_yticklabels(["20","25","30","35","40"],fontsize=9)
ax2.set_yticks([20,25,30,35,40])
ax2.set_yticklabels(["20","25","30","35","40"],fontsize=9)
ax3.set_yticks([20,25,30,35,40])
ax3.set_yticklabels(["20","25","30","35","40"],fontsize=9)
ax4.set_yticks([20,25,30,35,40])
ax4.set_yticklabels(["20","25","30","35","40"],fontsize=9)

ax1.set_ylabel('Cq value')
ax3.set_ylabel('Cq value')

ax1.set_title('$P. alni$ - PH149',fontsize=10)
ax2.set_title('$P. cinnamomi$ - PH027',fontsize=10)
ax3.set_title('$P. lateralis$ - PH218',fontsize=10)
ax4.set_title('$P. ramorum$ - PH178',fontsize=10)

ax4.set_xticklabels(["","","",""])
ax2.set_xticklabels(["","","",""])

ax3.set_xticklabels(['Ctl','Heat','Ctl','Heat'])
ax1.set_xticklabels(['Ctl','Heat','Ctl','Heat'])

ax3.plot((0.9,2.2),(15,15),'k-',clip_on = False,linewidth = 0.85)
ax3.text(1.2,13,'gDNA',clip_on= False)
ax1.plot((0.9,2.2),(15,15),'k-',clip_on = False,linewidth = 0.85)
ax1.text(1.2,13,'gDNA',clip_on= False)

ax3.plot((2.9,4.2),(15,15),'k-',clip_on = False,linewidth = 0.85)
ax3.text(3.2,13,'cDNA',clip_on= False)
ax1.plot((2.9,4.2),(15,15),'k-',clip_on = False,linewidth = 0.85)
ax1.text(3.2,13,'cDNA',clip_on= False)

ax1.plot((1,1),(29,29.5),'k-',linewidth=0.75)
ax1.plot((2,2),(29,29.5),'k-',linewidth=0.75)
ax1.plot((1,2),(29.5,29.5),'k-',linewidth=0.75)
ax1.text(0.9,30.5,'$F$=14.71, $p$<0.01',fontsize=8)
ax1.plot((3,3),(41,41.5),'k-',linewidth=0.75)
ax1.plot((4,4),(41,41.5),'k-',linewidth=0.75)
ax1.plot((3,4),(41.5,41.5),'k-',linewidth=0.75)
ax1.text(2.8,42.25,'$H$=9.46, $p$<0.01',fontsize=8)

ax2.plot((1,1),(32,32.5),'k-',linewidth=0.75)
ax2.plot((2,2),(32,32.5),'k-',linewidth=0.75)
ax2.plot((1,2),(32.5,32.5),'k-',linewidth=0.75)
ax2.text(1.4,33.25,'ns',fontsize=8)
ax2.plot((3,3),(41,41.5),'k-',linewidth=0.75)
ax2.plot((4,4),(41,41.5),'k-',linewidth=0.75)
ax2.plot((3,4),(41.5,41.5),'k-',linewidth=0.75)
ax2.text(2.7,42.25,'$H$=14.59, $p$<0.001',fontsize=8)

ax3.plot((1,1),(31.5,32),'k-',linewidth=0.75)
ax3.plot((2,2),(31.5,32),'k-',linewidth=0.75)
ax3.plot((1,2),(32,32),'k-',linewidth=0.75)
ax3.text(0.75,33,'$F$=46.96, $p$<0.0001',fontsize=8)
ax3.plot((3,3),(41,41.5),'k-',linewidth=0.75)
ax3.plot((4,4),(41,41.5),'k-',linewidth=0.75)
ax3.plot((3,4),(41.5,41.5),'k-',linewidth=0.75)
ax3.text(2.7,42.25,'$H$=14.59, $p$<0.001',fontsize=8)


ax4.plot((1,1),(28.5,29),'k-',linewidth=0.75)
ax4.plot((2,2),(28.5,29),'k-',linewidth=0.75)
ax4.plot((1,2),(29,29),'k-',linewidth=0.75)
ax4.text(0.9,30.,'$F$=7.75, $p$<0.05',fontsize=8)
ax4.plot((3,3),(41,41.5),'k-',linewidth=0.75)
ax4.plot((4,4),(41,41.5),'k-',linewidth=0.75)
ax4.plot((3,4),(41.5,41.5),'k-',linewidth=0.75)
ax4.text(2.7,42.25,'$H$=13.40, $p$<0.001',fontsize=8)

plt.savefig('Figure_3.pdf',dpi=800,  format='pdf')

