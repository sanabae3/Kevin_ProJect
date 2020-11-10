from math import floor
#import matplotlib
""" This function caculatess the 'Poids sec avant lavage'
    it takes 2 values which are measured  poids_initiale_humide_avant_avage and teneur_en_eau_nat
    and calculates it 

 """

poids_initiale_humide_avant_lavage= int(input("poids_initiale_humide_avant_avage:"))
teneur_en_eau_nat=int(input("teneur_en_eau_nat:"))
tamis_mm=[50,20,10,5,1,0.4,0.2,0.08]
def poids_sec_avant_lavage(poids_initiale_humide_avant_lavage,teneur_en_eau_nat):
    return floor((poids_initiale_humide_avant_lavage*100)/(100+teneur_en_eau_nat))
    # from excel sheet =(D20*100)/(100+D21)

def refus_cumule_pourcentage(poins_cumle,psala):
    refu=[]
    for i in poins_cumle:
        tepm=round((i/psala)*100,1)
        refu.append(tepm)
    return refu


        #(B26/D22)*100

def tamisat_Cumulé_pourcentage(refus_result):
    tamisat=[]
    for i in refus_result:
        tamisat.append(100-i)
    return tamisat
psala=poids_sec_avant_lavage(poids_initiale_humide_avant_lavage,teneur_en_eau_nat)
poids_cumle=[0,228,504,870,1334,1390,1390,1452]

poids_sec_avant_lavage(poids_initiale_humide_avant_lavage,teneur_en_eau_nat)
refus_result=refus_cumule_pourcentage(poids_cumle,psala)
tamisat_result=tamisat_Cumulé_pourcentage(refus_result)

print ('Refus cumule % : ',refus_result)
print('Tamisat Cumule % : ',tamisat_result)
print('this is the end for now planing to build a class')
