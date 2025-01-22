'''
Created on 21. nov. 2024

@author: joschua
'''

import os
import pandas as pd

pie_color = "cool"
bar_color = "Paired"

tasks_no = {
      
   # 0. country as pie chart
   0: { 
         "var":   ["land"],
         "sets":  ["se"],
         "title": "Fra hvilket land kom svarene inn?",
         "kind":  "pie",
         "cmap":  "Spectral"
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
         "title": "Har du en funksjonsnedsettelse eller annen tilstand?",
         "kind":  "pie",
         "cmap":  pie_color
      },
   
   9: {
         "var": ["funksjonsnedsettelse-type-kode"],
         "data-sep": ",",
         "sets": ["all"],
         "title": "Beskriv funskjonsnedsettelsen din. Den er relatert til …",
         "kind": "pie",
         "cmap": "Spectral",
         "text_bckgrd": True
      },
      
   # 3. impairment as pie chart
   30: {
         "var": ["funksjonsnedsettelse"],
         "sets":  ["se"], 
         "title": "Har du en funksjonsnedsettelse eller annen tilstand?",
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
               "title-app":      "Med vs. Uten funksjonsnedsettelse (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "Med vs. Uten funksjonsnedsettelse (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "uansett funksjonsevne",
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
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "Med vs. Uten funksjonsnedsettelse (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "Med vs. Uten funksjonsnedsettelse (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "uansett funksjonsevne",
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
               "title-app":      "Med vs. Uten funksjonsnedsettelse (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "Med vs. Uten funksjonsnedsettelse (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "uansett funksjonsevne",
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
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "Med vs. Uten funksjonsnedsettelse (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "Med vs. Uten funksjonsnedsettelse (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "uansett funksjonsevne",
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
               "title-app":      "Med vs. Uten funksjonsnedsettelse (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "Med vs. Uten funksjonsnedsettelse (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "uansett funksjonsevne",
               "is-percentage": True
               },
         },
         "title":    "Hva synes du generelt om teksten i varsler om informasjonskapsler?",
         "kind":     "bar",
         "fig_size": (11,6),
         "cmap":  bar_color
      },
   
   # 7. text difficulty a bar chart separated by impairment (with, without, combined)
   70: {
         "var": ["vanskelighetsgrad-tekst"],
         "sets":  ["se"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "Med vs. Uten funksjonsnedsettelse (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "Med vs. Uten funksjonsnedsettelse (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "uansett funksjonsevne",
               "is-percentage": True
               },
         },
         "title":    "Hva synes du generelt om teksten i varsler om informasjonskapsler?",
         "kind":     "bar",
         "fig_size": (11,6),
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
               "title-app":      "Med vs. Uten funksjonsnedsettelse (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "Med vs. Uten funksjonsnedsettelse (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "uansett funksjonsevne",
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
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "Med vs. Uten funksjonsnedsettelse (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "Med vs. Uten funksjonsnedsettelse (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "uansett funksjonsevne",
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

tasks_en = {
      
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
         "title": "How old are you?",
         "kind":  "pie",
         "cmap":  pie_color
      },

   # 10. age as pie chart
   10: {
         "var":           ["alder"],
         "sets":          ["se"], #wech: no
         "title":         "How old are you?",
         "kind":          "pie",
         "target-folder": "sverige",
         "cmap":  pie_color
      },
   
   # 2. gender as pie chart
   2: {
         "var": ["kjonn"],
         "sets":  ["all"],
         "title": "Are you ...?",
         "kind":  "pie",
         "cmap":  pie_color
      },
   
    # 20. gender as pie chart
   20: {
         "var": ["kjonn"],
         "sets":  ["se"],
         "title": "Are you ...?",
         "kind":  "pie",
         "target-folder": "sverige",
         "cmap":  pie_color
      },
   
   # 3. impairment as pie chart
   3: {
         "var": ["funksjonsnedsettelse"],
         "sets":  ["all"], 
         "title": "Do you have an impairment or other condition?",
         "kind":  "pie",
         "cmap":  pie_color
      },
   
   9: {
         "var": ["funksjonsnedsettelse-type-kode"],
         "data-sep": ",",
         "sets": ["all"],
         "title": "Describe your impairment or condition. It is related to …",
         "kind": "pie",
         "cmap": "Spectral",
         "text_bckgrd": True
      },
      
   # 3. impairment as pie chart
   30: {
         "var": ["funksjonsnedsettelse"],
         "sets":  ["se"], 
         "title": "Do you have an impairment or other condition that affects how you use the internet?",
         "kind":  "pie",
         "target-folder": "sverige",
         "cmap":  pie_color
      },
   
   # 4. internet habits as pie chart separated by impairment (with, without, combined)
   4: {
         "var": ["internettvaner"],
         "sets":  ["all"], 
         "title": "How often do you use the internet?",
         "kind":  "pie",
         "cmap":  pie_color
      },
   
   # 4. internet habits as pie chart separated by impairment (with, without, combined)
   40: {
         "var": ["internettvaner"],
         "sets":  ["se"], 
         "title": "How often do you use the internet?",
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
               "title-app":      "With vs. Without Impairment (%)",
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
         "title":    "How do you generally handle cookie notifications?",
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
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Without Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
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
         "title":    "How do you generally handle cookie notifications?",
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
               "title-app":      "With vs. Without Impairment (%)",
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
         "title":    "How do you generally find managing cookie notifications?",
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
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Without Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
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
         "title":    "How do you generally find managing cookie notifications?",
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
               "title-app":      "With vs. Without Impairment (%)",
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
         "title":    "What do you generally think about the text in cookie notifications?",
         "kind":     "bar",
         "fig_size": (11,6),
         "cmap":  bar_color
      },
   
   # 7. text difficulty a bar chart separated by impairment (with, without, combined)
   70: {
         "var": ["vanskelighetsgrad-tekst"],
         "sets":  ["se"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Without Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
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
         "title":    "What do you generally think about the text in cookie notifications?",
         "kind":     "bar",
         "fig_size": (11,6),
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
               "title-app":      "With vs. Without Impairment (%)",
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
         "title":    "Is it generally easy or difficult to make choices for cookies?",
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
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Without Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
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
         "title":    "Is it generally easy or difficult to make choices for cookies?",
         "kind":     "bar",
         "fig_size": (10,6),
         "target-folder": "sverige",
         "cmap":  bar_color
      },
   }

vanskelighetsgrad_no = {
   -1: "-1 - Svarte ikke",
   1: "1 - Veldig lett",
   2: "2 - Ganske lett",
   3: "3 - Verken lett/\neller vanskelig",
   4: "4 - Ganske vanskelig",
   5: "5 - Veldig vanskelig" 
   }

# The data sets are determined programmatically in the main module under key "data_set"
lookup_no = {
   "file-app": {
      "no": "norway-only",
      "se": "sweden-only",
      "all": "all-countries"
      },
   "title-app": {
      "no": "Kun Norge",
      "se": "Kun Sverige",
      "all": "Alle land"
      },
   "answers-repl": {
      "default-valg": {
         "Jeg ignorerer dem.": "Ignorere",
         "Jeg godtar alle cookies uten å lese informasjonsteksten.": "Godta",
         "Jeg avviser alle cookies, hvis mulig.": "Avvise",
         "Jeg leser informasjonsteksten og deretter bestemmer jeg hva jeg skal avvise eller akseptere.": "Tilpasse",
         },
      "vanskelighetsgrad-generell": vanskelighetsgrad_no,
      "vanskelighetsgrad-tekst": vanskelighetsgrad_no,
      "vanskelighetsgrad-valg": vanskelighetsgrad_no,
      }
   }

alder_en = {
   "19 - 30 år": "19 - 30 years",
   "31 - 49 år": "31 - 49 years",
   "50 - 65 år": "50 - 65 years",
   "66 og eldre": "66 years and older"
   }

kjonn_en = {
   "Mann": "Male",
   "Kvinne": "Female",
   "Ikke-binær": "Non-Binary"
   }

bool_en = {
   "Ja": "Yes",
   "Nei": "No",
   "Onsker ikke å oppgi": "Prefer not to say"
   }

vanskelighetsgrad_en = {
   -1: "-1 - No answer",
   1: "1 - Very easy",
   2: "2 - Quite easy",
   3: "3 - Neither easy/\nnor difficult",
   4: "4 - Quite difficutl",
   5: "5 - Very difficult" 
   }

funksjonsnedsettelser_type_en = {
   "hørsel": "hearing",
   "kognisjon": "cognition",
   "mobilitet": "mobility",
   "motor": "motor",
   "motorikk": "motor",
   "syn": "vision",
   "syn (blind)": "vision (blind)",
   "ubestemt": "unknown"
   }

internettvaner_en = {
   "Daglig": "Daily",
   "Flere ganger om dagen": "Multiple times a day",
   "Ukentlig": "Weekly"
   }

# The data sets are determined programmatically in the main module under key "data_set"
lookup_en = {
   "file-app": {
      "no": "norway-only",
      "se": "sweden-only",
      "all": "all-countries"
      },
   "title-app": {
      "no": "Norway only",
      "se": "Sweden only",
      "all": "All countries combined" #wech
      },
   "answers-repl": {
      "alder": alder_en,
      "kjonn": kjonn_en,
      #"funksjonsnedsettelse-type-kode": funksjonsnedsettelser_type_en,
      "internettvaner": internettvaner_en,
      "default-valg": {
         "Jeg ignorerer dem.": "Ignore",
         "Jeg godtar alle cookies uten å lese informasjonsteksten.": "Accept",
         "Jeg avviser alle cookies, hvis mulig.": "Reject",
         "Jeg leser informasjonsteksten og deretter bestemmer jeg hva jeg skal avvise eller akseptere.": "Adjust"
         },
      #"funksjonsnedsettelse": bool_en,
      "vanskelighetsgrad-generell": vanskelighetsgrad_en,
      "vanskelighetsgrad-tekst": vanskelighetsgrad_en,
      "vanskelighetsgrad-valg": vanskelighetsgrad_en,
      }
   }

"""
Setting tasks for each language
"""

tasks = {
   "no": tasks_no,
   "en": tasks_en
   }

lookup = {
   "no": lookup_no,
   "en": lookup_en
   }