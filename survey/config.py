'''
Created on 21. nov. 2024

@author: joschua
'''

import os
import pandas as pd

tasks = {
   
   # 8. choice difficulty as bar chart separated by impairment (with, without, combined)
   8: {
         "var":     ["vanskelighetsgrad-valg"],
         "sets":    ["no","se","all"],
         "subsets": {
            1: {
               "var":         "funksjonsnedsettelse",
               "operators":   [("equal to","Ja")],
               "file-app":    "with-impairment-only",
               "title-app":   "with impairment (not %)",
               "is-percentage":  False
               },
            2: {
               "var":         "funksjonsnedsettelse",
               "operators":   [("not equal to","Ja")],
               "file-app":    "without-impairment-only",
               "title-app":   "without impairment (not %)",
               "is-percentage":  False
               },
            3: {
               "var":         "funksjonsnedsettelse",
               "operators":   [("not equal to","Ja","others"),("equal to","Ja","with-impair")],
               "file-app":    "impair-v-others-pct",
               "title-app":   "Impairments vs. Others (%)",
               "is-percentage":  True
               },
            4: {
               "var":         "funksjonsnedsettelse",
               "operators":   [],
               "file-app":    "all-abilities",
               "title-app":   "all abilities"
               },
         },
         "title":   "What do you think about finding choices in cookie settings?",
         "kind":    "bar"
      },
   }

tasks2 = {
      
   # 0. country as pie chart
   0: { 
         "var":   ["land"],
         "sets":  ["se"],
         "title": "From which country did the answers come in?",
         "kind":  "pie"
      },
   
   # 1. age as pie chart
   1: {
         "var":   ["alder"],
         "sets":  ["no","se","all"],
         "title": "How old were the participants?",
         "kind":  "pie"
      },
   
   # 2. gender as pie chart
   2: {
         "var": ["kjonn"],
         "sets":  ["no","se","all"],
         "title": "Which gender did the participants report?",
         "kind":  "pie"
      },
   
   # 3. impairment as pie chart
   3: {
         "var": ["funksjonsnedsettelse"],
         "sets":  ["no","se","all"],
         "title": "How many participatns had impairment(s)?",
         "kind":  "pie"
      },
   
   # 4. internet habits as pie chart separated by impairment (with, without, combined)
   4: {
         "var": ["internettvaner"],
         "sets":  ["no","se","all"],
         "title": "How often do you use the Internet?",
         "kind":  "pie"
      },
   
   # 5. default choices as bar chart separated by impairment (with, without, combined)
   5: {
         "var":     ["default-valg"],
         "sets":    ["no","se","all"],
         "subsets": {
            4: {
               "var": "funksjonsnedsettelse",
               "operators": [("equal to","Ja","with-impair"), ("not equal to","Ja","others")],
               "file-app": "impair-v-others",
               "title-app": "Impairments vs. Others"
               },
            1: {
               "var": "funksjonsnedsettelse",
               "operators": [("equal to","Ja")],
               "file-app": "with-impairment",
               "title-app": "with impairment"
               },
            2: {
               "var": "funksjonsnedsettelse",
               "operators": [("not equal to","Ja")],
               "file-app": "without-impairment",
               "title-app": "without impairment"
               },
            3: {
               "var": "funksjonsnedsettelse",
               "operators": [],
               "file-app": "all-abilities",
               "title-app": "all abilities"
               }
         },
         "title":   "Hvordan håndterer du varsler om informasjonskapsler?",
         "kind":    "bar"
      },
   
   # 6. general difficulty as bar chart separated by impairment (with, without, combined)
   6: {
         "var":     ["vanskelighetsgrad-generell"],
         "sets":    ["no","se","all"],
         "subsets": {
            1: {
               "var": "funksjonsnedsettelse",
               "operators": [("equal to","Ja")],
               "file-app": "with-impairment",
               "title-app": "with impairment"
               },
            2: {
               "var": "funksjonsnedsettelse",
               "operators": [("not equal to","Ja")],
               "file-app": "without-impairment",
               "title-app": "without impairment"
               },
            3: {
               "var": "funksjonsnedsettelse",
               "operators": [],
               "file-app": "all-abilities",
               "title-app": "all abilities"
               },
         },
         "title":   "Hvordan opplever du generelt sett å håndtere varsler om informasjonskapsler?",
         "kind":    "bar"
      },
   
   # 7. text difficulty a bar chart separated by impairment (with, without, combined)
   7: {
         "var": ["vanskelighetsgrad-tekst"],
         "sets":  ["no","se","all"],
         "subsets": {
            1: {
               "var": "funksjonsnedsettelse",
               "operators": [("equal to","Ja")],
               "file-app": "with-impairment",
               "title-app": "with impairment"
               },
            2: {
               "var": "funksjonsnedsettelse",
               "operators": [("not equal to","Ja")],
               "file-app": "without-impairment",
               "title-app": "without impairment"
               },
            3: {
               "var": "funksjonsnedsettelse",
               "operators": [],
               "file-app": "all-abilities",
               "title-app": "all abilities"
               },
         },
         "title": "Hva synes du generelt om teksten i varsler om informasjonskapsler?",
         "kind":  "bar"
      },
   
   # 8. choice difficulty as bar chart separated by impairment (with, without, combined)
   8: {
         "var":     ["vanskelighetsgrad-valg"],
         "sets":    ["no","se","all"],
         "subsets": {
            1: {
               "var":         "funksjonsnedsettelse",
               "operators":   [("equal to","Ja")],
               "file-app":    "with-impairment-only",
               "title-app":   "with impairment (not %)",
               "is-percentage":  False
               },
            2: {
               "var":         "funksjonsnedsettelse",
               "operators":   [("not equal to","Ja")],
               "file-app":    "without-impairment-only",
               "title-app":   "without impairment (not %)",
               "is-percentage":  False
               },
            3: {
               "var":         "funksjonsnedsettelse",
               "operators":   [("not equal to","Ja","others"),("equal to","Ja","with-impair")],
               "file-app":    "impair-v-others-pct",
               "title-app":   "Impairments vs. Others (%)",
               "is-percentage":  True
               },
            4: {
               "var":         "funksjonsnedsettelse",
               "operators":   [],
               "file-app":    "all-abilities",
               "title-app":   "all abilities"
               },
         },
         "title":   "Er det generelt lett eller vanskelig å ta valg for informasjonskapsler?",
         "kind":    "bar"
      },
   }

# The data sets are determined programmatically in the main module under key "data_set"
lookup = {
   "file-app": {
      "no": "norway-only",
      "se": "sweden-only",
      "all": "all-countries"
      },
   "title-app": {
      "no": "Norway only",
      "se": "Sweden only",
      "all": "All countries combined"
      }
   }