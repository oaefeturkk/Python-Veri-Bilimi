#Ders-1 - VERİ YÜKLEME(DATA İMPORT) ********

#kUTUPHANELER ********
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#kODLAR ********
#Veri Yükleme ********

eksikveriler = pd.read_csv('eksikveriler.csv')
print(eksikveriler)




#Veri Ön İşleme ********
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



#Eksik Veriler ********

#sci-kit learn ********
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

Yas = eksikveriler.iloc[:,1:4].values
# print(Yas)

imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
# print(Yas)

ulke = eksikveriler.iloc[:,0:1].values
# print(ulke)

# Kategorik Veriler ********
from sklearn import preprocessing

le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(eksikveriler.iloc[:,0])
# print(ulke)

ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
# print(ulke)

# Verilerin Birleştirilmesi ve DataFrame Oluşturulması ********

sonuc = pd.DataFrame(data=ulke, index=range(22), columns=['fr','tr','us'])
# print(sonuc)

sonuc2 = pd.DataFrame(data=Yas, index=range(22), columns=['boy','kilo','yas'])
# print(sonuc2)

cinsiyet = eksikveriler.iloc[:,-1].values
# print(cinsiyet)

sonuc3  = pd.DataFrame(data=cinsiyet, index=range(22), columns=['cinsiyet'])
# print(sonuc3)

s = pd.concat([sonuc,sonuc2], axis=1)
# print(s)

s2= pd.concat([s,sonuc3], axis=1)
# print(s2)

# Veri Kümesinin Eğitim Ve Test Olarak Bölünmesi ********

from sklearn.model_selection import train_test_split

x_train, x_test, y_test, y_train = train_test_split(s,sonuc3,test_size=0.33, random_state=0)

# Öznitelik Öçeklendirme

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

# Veri Ön İşleme (Data Processing) Şablonu












