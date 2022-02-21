import pandas as pd
import csv
import time
from rest.models import Attractions

def run():
    df = pd.read_csv("D:\documents\GitHub\FBLA_2021-2022_CAP\data.csv").to_dict()

    for i in range(737):
        name         = df['name'][i]
        type_s       = df['type'][i]
        loc          = df['loc'][i]
        website      = df['website'][i]
        open_time    = df['open_time'][i]
        address      = df['address'][i]
        number       = df['number'][i]

        try:
            reviews = int(df['reviews'][i])
        except:
            reviews = 0

        try:
            star_rating = float(df['star_rating'][i])
        except:
            star_rating = 0
            

        print(name,type_s,loc,website,open_time,address,number,reviews,star_rating)

        a = Attractions(name=name,type=type_s,loc=loc,website=website,open_time=open_time,address=address,number=number,reviews=reviews,star_rating=star_rating)
        a.save()    

        print("------------------------------------")
        print("FINISHED NEXT: ",i)
        print("------------------------------------")
        time.sleep(0.03)