'''
Created on 21. nov. 2024

@author: joschua
'''

import os
import pandas as pd

pie_color = "cool"
bar_color = "Paired"

tasks = {
      
   # 0. country as pie chart
   0: { 
         "var":   ["land"],
         "sets":  ["se"],
         "title": "From which country did the answers come in?",
         "kind":  "pie",
         "cmap":  "gist_ncar"
      },
   
   # 1. age as pie chart
   1: {
         "var":   ["alder"],
         "sets":  ["all"], 
         "title": "Hvor gammel er du?",
         "kind":  "pie",
         "cmap":  pie_color
      },

   # 10. age as pie chart
   10: {
         "var":           ["alder"],
         "sets":          ["se"], #wech: no
         "title":         "Hvor gammel er du?",
         "kind":          "pie",
         "target-folder": "sverige",
         "cmap":  pie_color
      },
   
   # 2. gender as pie chart
   2: {
         "var": ["kjonn"],
         "sets":  ["all"],
         "title": "Er du ...?",
         "kind":  "pie",
         "cmap":  pie_color
      },
   
    # 20. gender as pie chart
   20: {
         "var": ["kjonn"],
         "sets":  ["se"],
         "title": "Er du ...?",
         "kind":  "pie",
         "target-folder": "sverige",
         "cmap":  pie_color
      },
   
   # 3. impairment as pie chart
   3: {
         "var": ["funksjonsnedsettelse"],
         "sets":  ["all"], 
         "title": "Har du en funksjonsnedsettelse eller annen tilstand som påvirker hvordan du bruker nettet?",
         "kind":  "pie",
         "cmap":  pie_color
      },
   
      
   # 3. impairment as pie chart
   30: {
         "var": ["funksjonsnedsettelse"],
         "sets":  ["se"], 
         "title": "Har du en funksjonsnedsettelse eller annen tilstand som påvirker hvordan du bruker nettet?",
         "kind":  "pie",
         "target-folder": "sverige",
         "cmap":  pie_color
      },
   
   # 4. internet habits as pie chart separated by impairment (with, without, combined)
   4: {
         "var": ["internettvaner"],
         "sets":  ["all"], 
         "title": "Hvor ofte bruker du Internett?",
         "kind":  "pie",
         "cmap":  pie_color
      },
   
   # 4. internet habits as pie chart separated by impairment (with, without, combined)
   40: {
         "var": ["internettvaner"],
         "sets":  ["se"], 
         "title": "Hvor ofte bruker du Internett?",
         "kind":  "pie",
         "target-folder": "sverige",
         "cmap":  pie_color
      },
   
   # 5. default choices as bar chart separated by impairment (with, without, combined)
   5: {
         "var":     ["default-valg"],
         "sets":    ["all"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Witout Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "With vs. Without Impairment (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "all abilities",
               "is-percentage": True
               },
         },
         "title":    "Hvordan håndterer du varsler om informasjonskapsler?",
         "kind":     "bar",
         "fig_size": (10,6),
         "cmap":  bar_color
      },
   
   # 5. default choices as bar chart separated by impairment (with, without, combined)
   50: {
         "var":     ["default-valg"],
         "sets":    ["se"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Witout Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "With vs. Without Impairment (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "all abilities",
               "is-percentage": True
               },
         },
         "title":    "Hvordan håndterer du varsler om informasjonskapsler?",
         "kind":     "bar",
         "fig_size": (10,6),
         "target-folder": "sverige",
         "cmap":  bar_color
      },
   
   # 6. general difficulty as bar chart separated by impairment (with, without, combined)
   6: {
         "var":     ["vanskelighetsgrad-generell"],
         "sets":    ["all"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Witout Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "With vs. Without Impairment (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "all abilities",
               "is-percentage": True
               },
         },
         "title":    "Hvordan opplever du generelt sett å håndtere varsler om informasjonskapsler?",
         "kind":     "bar",
         "fig_size": (10,6),
         "cmap":  bar_color
      },
   
   # 6. general difficulty as bar chart separated by impairment (with, without, combined)
   60: {
         "var":     ["vanskelighetsgrad-generell"],
         "sets":    ["se"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Witout Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "With vs. Without Impairment (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "all abilities",
               "is-percentage": True
               },
         },
         "title":    "Hvordan opplever du generelt sett å håndtere varsler om informasjonskapsler?",
         "kind":     "bar",
         "fig_size": (10,6),
         "target-folder": "sverige",
         "cmap":  bar_color
      },
   
   # 7. text difficulty a bar chart separated by impairment (with, without, combined)
   7: {
         "var": ["vanskelighetsgrad-tekst"],
         "sets":  ["all"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Witout Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "With vs. Without Impairment (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "all abilities",
               "is-percentage": True
               },
         },
         "title":    "Hva synes du generelt om teksten i varsler om informasjonskapsler?",
         "kind":     "bar",
         "fig_size": (10,6),
         "cmap":  bar_color
      },
   
   # 7. text difficulty a bar chart separated by impairment (with, without, combined)
   70: {
         "var": ["vanskelighetsgrad-tekst"],
         "sets":  ["se"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Witout Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "With vs. Without Impairment (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "all abilities",
               "is-percentage": True
               },
         },
         "title":    "Hva synes du generelt om teksten i varsler om informasjonskapsler?",
         "kind":     "bar",
         "fig_size": (10,6),
         "target-folder": "sverige",
         "cmap":  bar_color
      },
   
   # 8. choice difficulty as bar chart separated by impairment (with, without, combined)
   8: {
         "var":     ["vanskelighetsgrad-valg"],
         "sets":    ["all"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Witout Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "With vs. Without Impairment (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "all abilities",
               "is-percentage": True
               },
         },
         "title":    "Er det generelt lett eller vanskelig å ta valg for informasjonskapsler?",
         "kind":     "bar",
         "fig_size": (10,6),
         "cmap":  bar_color
      },
   
   # 8. choice difficulty as bar chart separated by impairment (with, without, combined)
   80: {
         "var":     ["vanskelighetsgrad-valg"],
         "sets":    ["se"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Witout Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "With vs. Without Impairment (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "all abilities",
               "is-percentage": True
               },
         },
         "title":    "Er det generelt lett eller vanskelig å ta valg for informasjonskapsler?",
         "kind":     "bar",
         "fig_size": (10,6),
         "target-folder": "sverige",
         "cmap":  bar_color
      },
   }

vanskelighetsgrad = {
   -1: "-1 - Svarte ikke",
   1: "1 - Veldig lett",
   2: "2 - Ganske lett",
   3: "3 - Verken lett/\neller vanskelig",
   4: "4 - Ganske vanskelig",
   5: "5 - Veldig vanskelig" 
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
      },
   "answers-repl": {
      "default-valg": {
         "Jeg ignorerer dem.": "Ignorere",
         "Jeg godtar alle cookies uten å lese informasjonsteksten.": "Godta",
         "Jeg avviser alle cookies, hvis mulig.": "Avvise",
         "Jeg leser informasjonsteksten og deretter bestemmer jeg hva jeg skal avvise eller akseptere.": "Tilpasse",
         },
      "vanskelighetsgrad-generell": vanskelighetsgrad,
      "vanskelighetsgrad-tekst": vanskelighetsgrad,
      "vanskelighetsgrad-valg": vanskelighetsgrad,
      }
   }