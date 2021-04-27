
import pandas as pd 

# Veri Yükleme*****

poke_data = pd.read_csv("pokemon_data.csv")
print(poke_data)
print(poke_data.head(5))

# Veriyi Okuma*****

# Columnları çağırmak için => .columns
print(poke_data.columns)

# spesifik bir columna ulaşmak ve istenilen kadar row için => poke_data['columnName'][0:5]]
print(poke_data['Name'][0:7])
print(poke_data.HP)
print(poke_data[['Name','HP','Type 1']])

# Herbir row için => .head(rowAdet) ya da .iloc[rowAdet]
print(poke_data.head(4))
print(poke_data.iloc[0:4])
# spesifik lokasyon için; (ROW,COLUMN)
print(poke_data.iloc[0,1])
for index, row in poke_data.iterrows():
    print(index, row['Type 1'])
print(poke_data.loc[poke_data['Type 1'] == 'Fire'])
sugrubu = poke_data.loc[poke_data['Type 1'] == 'Water']
print(sugrubu)

# Veri İstatistiği Çıkarma****

descriptive = poke_data.describe()
print(descriptive)

# Veri Sıralaması (Sorting)

isim_azalan = poke_data.sort_values('Name', ascending=False)
print(isim_azalan)

type1_attack = poke_data.sort_values(['Type 1', 'Attack'], ascending=False)
print(type1_attack)

# COlumn Ekleme****

toplam = poke_data['Toplam'] = poke_data['HP'] + poke_data['Attack'] + poke_data['Defense'] + poke_data['Sp. Atk'] + poke_data['Sp. Def'] + poke_data['Speed']
print(poke_data[['Name','Toplam']].head(5))
# YA DA;
poke_data['Toplam'] = poke_data.iloc[:,4:10].sum(axis=1)

# Column Silme****
poke_data.drop(columns=['Toplam'])

# COlumn Sıralamasını Değiştirmek

cols = list(poke_data.columns)
poke_data = poke_data[cols[0:4] + [cols[-1]] + cols[4:12]]
print(cols)

# Yapılan İşlemleri Yeni Dosyaya Kaydetmek

poke_data.to_csv('Ypokemon_data.csv', index=False)


# Veri Filtreleme****

grass = poke_data.loc[poke_data['Type 1'] == 'Grass']
print(grass)

grass_poison = poke_data.loc[(poke_data['Type 1'] == 'Grass') & (poke_data['Type 2'] == 'Poison') & (poke_data['HP'] > 65)]
print(grass_poison)

# Adında Mega olan Pokeleri Filtreleme**** '~' = hariç diğerleri

mega = poke_data.loc[~poke_data['Name'].str.contains('Mega')]
print(mega)

mega.to_csv('megalar.csv', index=False)

# Regex Filtrelemesi****

import re 

pi_icerenler = poke_data.loc[poke_data['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
print(pi_icerenler)

# Spesifik Rowları Değiştirme****

poke_data.loc[poke_data['Type 1'] == 'Flamer', 'Type 1'] = 'Fire'

# Gruplama yapmak ****

type1_grup = poke_data.groupby(['Type 1']).mean().sort_values('Attack', ascending=False)
type1_toplam = poke_data.groupby(['Type 1']).sum()
type1_adet = poke_data.groupby(['Type 1']).count()
print(type1_adet)














