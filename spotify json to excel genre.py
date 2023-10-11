# This code was used to separate the genres list for each song and export it to excel so that it can be used in analysis.

import pandas as pd
import json
from pandas import json_normalize

# Read the history files

kath = pd.read_json('Kathleenhistory copy.json')
dave = pd.read_json('Davehistory copy.json')
regi = pd.read_json('Reginahistory copy.json')
meli0 = pd.read_json('Melissahistory0 copy.json')
meli1 = pd.read_json('Melissahistory1 copy.json')
cori0= pd.read_json('Coritahistory0 copy.json')
cori1= pd.read_json('Coritahistory1 copy.json')


# Expolde the list of genres

kath_gen = kath.explode('artist_gen')
dave_gen = dave.explode('artist_gen')
regi_gen = regi.explode('artist_gen')
meli0_gen = meli0.explode('artist_gen')
meli1_gen = meli1.explode('artist_gen')
cori0_gen = cori0.explode('artist_gen')
cori1_gen = cori1.explode('artist_gen')

# create a list of dataframes
frames = [kath_gen, dave_gen, regi_gen, meli0_gen, meli1_gen, cori0_gen, cori1_gen]

#  combine all the dataframes

genre_all = pd.concat(frames)

# drop any records that are null
genre_all.dropna()
print('all after drop', len(genre_all))

# saving the excel
file_name = 'genre_all.xlsx'
genre_all.to_excel(file_name)
