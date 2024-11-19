"""
  Created on 2024-11-19.
  
  Last updated on 2024-11-19.
  
  This package is used to analys the results from the survey in the project Tilgjengelige informasjonskapsler, conducted in October and November of 2024.
"""

import os

import pandas as pd
import matplotlib.pyplot as plt

print("Hello world!")

def analyze_data():
   
   data_file = "./data/2024-10-08_Svar-til-sporreundersokelse-om-universell-utforming-av-cookies.xlsx"
   if not os.path.exists(data_file):
      print("The file could not be found.")
      return
   
   df = pd.read_excel("./data/2024-10-08_Svar-til-sporreundersokelse-om-universell-utforming-av-cookies.xlsx")
   
   """
   *** Analysis ***
   """
   
   is_sweden_only = True
   
   """
   1. Country: land
   
   Type: Pie chart
   """
   
   if is_sweden_only:
      country = df[df["land"] != "Ukjent" ]
   else:
      country = df["land"]
   
   country = country["land"]
   print(country)
   
   df.groupby("land")["land"].count().plot(kind="pie")
   plt.show()

   """
   2. Age: alder
   
   Type: Pie chart
   """
   
   """
   3. Gender: kjonn
   
   Type: Pie chart
   """
   
   """
   4. Impairment: funksjonsnedsettelse
   
   Type: Pie chart
   """
   
   """
   5. Internet: internettvaner
   
   Type: Pie chart
   """
   
   """
   6. Default choice: default_valg
   
   Type: Pie chart
   """
   
   """
   7. Difficulty (general): vanskelighetsgrad-generell
   
   Type: Bar chart
   """
   
   """
   8. Difficulty (text): vanskelighetsgrad-tekst
   
   Type: Bar chart
   """

   """
   9. Difficulty (choice): vanskelighetsgrad-generell
   
   Type: Bar chart
   """

if __name__=='__main__':
  analyze_data()