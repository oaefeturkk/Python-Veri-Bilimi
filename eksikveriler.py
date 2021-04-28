#Ders-1 - VERİ YÜKLEME(DATA İMPORT)

#kUTUPHANELER
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#kODLAR
#Veri Yükleme

veriler = pd.read_csv('eksikveriler.csv')
print(veriler)




#Veri Ön İşleme
# boy = veriler[['boy']]
# print(boy)

# ulkecins = veriler[['ulke','cinsiyet']]
# print(ulkecins)


# class insan:
#     boy = 180
#     def kosmak(self,b):
#         return b + 10
#     # y=f(x)
#     # f(x) = x+10
    
# ali = insan()
# print(ali.boy)
# print(ali.kosmak(90))



#Eksik Veriler

#sci-kit learn
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

Yas = veriler.iloc[:,1:4].values
print(Yas)

imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)
























