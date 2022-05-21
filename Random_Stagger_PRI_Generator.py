
"""""""""""""""""""""""""""""""""""""""""""""""""""
Created on Saturday, May 21st 2022
@author: Ezekiel Lutz
@title: Random/Staggered PRI Generator
"""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
Import Libraries Section of Code
"""""""""""""""""""""""""""""""""""""""""""""""""""

import random 
import pandas as pd

"""""""""""""""""""""""""""""""""""""""""""""""""""
Declaration of Variables Section of Code
"""""""""""""""""""""""""""""""""""""""""""""""""""

PRI_min = (300) #Enter PRI in usec
PRI_max = (500) #Enter PRI in usec 

"""""""""""""""""""""""""""""""""""""""""""""""""""
Random PRI Section of Code
"""""""""""""""""""""""""""""""""""""""""""""""""""

PRI_Range_Random = []
PRI_Range_Random_Converted = []

for i in range(30):
    PRI_Range_Random.append(random.randrange(PRI_min,PRI_max,1))

for x in PRI_Range_Random:
    PRI_Range_Random_Converted.append(x/1000000)
        
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Jittered PRI Section of Code

A note about jittered PRI's: For this code, a jittered PRI is defined
as an intentional random pulse interval variation up to about 10% of the mean PRI

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
PRI_Range_Jittered = []
PRI_Range_Jittered_Converted = []
Mean_PRI = (int((PRI_min+PRI_max)/2))
Jittered_PRI_max = (int(Mean_PRI+(Mean_PRI*0.05)))
Jittered_PRI_min = (int(Mean_PRI-(Mean_PRI*0.05)))

for i in range(30):
    PRI_Range_Jittered.append(random.randrange(Jittered_PRI_min,Jittered_PRI_max,1))

for x in PRI_Range_Jittered:
    PRI_Range_Jittered_Converted.append(x/1000000)
    
"""""""""""""""""""""""""""""""""""""""""""""""""""
Export to Excel Section of Code
"""""""""""""""""""""""""""""""""""""""""""""""""""

df_random = pd.DataFrame(PRI_Range_Random_Converted)
df_random.to_excel('Python Random PRI Generator File.xlsx', sheet_name='Random PRI')
df_jittered = pd.DataFrame(PRI_Range_Jittered_Converted)
df_jittered.to_excel('Python Jittered PRI Generator File.xlsx', sheet_name='Jittered PRI')

