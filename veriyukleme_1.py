#Ders-1 - VERİ YÜKLEME(DATA İMPORT)

#kUTUPHANELER
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#kODLAR
#Veri Yükleme

veriler = pd.read_csv('veriler.csv')
print(veriler)




#Veri Ön İşleme
boy = veriler[['boy']]
print(boy)

ulkecins = veriler[['ulke','cinsiyet']]
print(ulkecins)


class insan:
    boy = 180
    def kosmak(self,b):
        return b + 10
    
ali = insan()
print(ali.boy)
print(ali.kosmak(90))
