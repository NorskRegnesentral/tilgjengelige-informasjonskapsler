'''
Created on 21. nov. 2024

@author: joschua
'''

import os
import pandas as pd

tasks = {
      
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
               "operators": [("equal to","Ja","with-impair"), ("not equal to","Ja","without-impair")],
               "file-app": "pupsi",
               "title-app": "pupsi"
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
         "title":   "What do you usually do with the cookie settings?",
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
         "title":   "What do you think about the cookies in general?",
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
         "title": "What do you think about the text in cookie settings?",
         "kind":  "bar"
      },
   
   # 8. choice difficulty as bar chart separated by impairment (with, without, combined)
   8: {
         "var":     ["vanskelighetsgrad-valg"],
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
            4: {
               "var": "funksjonsnedsettelse",
               "operators": [("equal to","Ja"), ("not equal to","Ja")],
               "file-app": "pupsi",
               "title-app": "pupsi"
               }
         },
         "title":   "What do you think about finding choices in cookie settings?",
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