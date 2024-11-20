"""
  Created on 2024-11-19.
  
  Last updated on 2024-11-19.
  
  This package is used to analys the results from the survey in the project Tilgjengelige informasjonskapsler, conducted in October and November of 2024.
"""

import os

import pandas as pd
import matplotlib.pyplot as plt

def basic_chart(data,group_by,kind,title,save_file="",is_values_as_labels=False):
   
   fig, ax = plt.subplots()   
   
   if group_by:
      
      #autopct='%1.f%%'
      labels = None
      if is_values_as_labels:
         labels = data.groupby(group_by)[group_by].count()
         
      curr_data = data.groupby(group_by)[group_by].count()
      
      #res_str += "\n\n{}".format(curr_data)
      
      if kind == "pie":
         pupsi ='%1.f%%'   
         curr_data.plot(kind=kind, autopct=pupsi, ylabel="", cmap="Pastel1")
      else: 
         curr_data.plot(kind=kind, ylabel="", cmap="Pastel1")
         
      
   if title:
      ax.set_title(title)
      
   if save_file:
      fig.savefig(save_file)
      plt.close(fig)
      print("Image save under {}".format(save_file))
   
   return "{}".format(curr_data)
      
def analyze_data():
   
   data_file = os.path.join("data","2024-10-08_Svar-til-sporreundersokelsen-om-universell-utforming-av-cookies.csv")
   if not os.path.exists(data_file):
      print("The file could not be found.")
      return
   
   """
   *** Analysis ***
   
   1. Defining data sets.
   """
   df_all          = pd.read_csv(data_file,sep=";")
   df_norway_only  = df_all[df_all["land"] == "Ukjent"]
   df_sweden_only  = df_all[df_all["land"] != "Ukjent"]
   
   
   """
   2. Defining tasks for the analysis.
   """
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
      3: {
            "var": ["internettvaner"],
            "sets":  ["no","se","all"],
            "title": "How often do you use the Internet?",
            "kind":  "pie"
         },
      
      # 5. default choices as bar chart separated by impairment (with, without, combined)
      5: {
            "var": ["default-valg"],
            "sets":  ["no","se","all"],
            "title": "What do you usually do with the cookie settings?",
            "kind":  "bar"
         },
      
      # 6. general difficulty as bar chart separated by impairment (with, without, combined)
      6: {
            "var": ["vanskelighetsgrad-generell"],
            "sets":  ["no","se","all"],
            "title": "What do you usually do with the cookie settings?",
            "kind":  "bar"
         },
      
      # 7. text difficulty a bar chart separated by impairment (with, without, combined)
      7: {
            "var": ["vanskelighetsgrad-tekst"],
            "sets":  ["no","se","all"],
            "title": "What do you usually do with the cookie settings?",
            "kind":  "bar"
         },
      
      # 8. choice difficulty as bar chart separated by impairment (with, without, combined)
      8: {
            "var": ["vanskelighetsgrad-valg"],
            "sets":  ["no","se","all"],
            "title": "What do you usually do with the cookie settings?",
            "kind":  "bar"
         }
      }
   
   """
   3. Defining basic lookup variables.
   """
   lookup = {
      "data_set": {
         "no": df_norway_only,
         "se": df_sweden_only,
         "all": df_all
         },
      "file-app": {
         "no": "norway-only",
         "se": "sweden-only",
         "all": "all"
         },
      "title-app": {
         "no": "(Norway only)",
         "se": "(Sweden only)",
         "all": "(All combined)"
         }
      }
   
   
   """
   4. Conducting the analysis
   """
   res_str = "# Results from the survey" # All results will be stored in a text file, next to th graphs.
   
   for key,values in tasks.items():
      
      """
      Checking if necessary parameters are present.
      """
      if not "var" in values or not values["var"]:
         print("No variable has been chosen.")
         continue
      
      if not "sets" in values or not values["sets"]:
         print("No set(s) has(have) been chosen.")
         continue
      
      if not "kind" in values or not values["kind"]:
         print("No plot type has been chosen.")
         continue
            
      var  = values["var"][0]
      kind = values["kind"]
      
      title = ""
      if "title" in values:
         title = values["title"]
         res_str += "\n\n## {}".format(title) 
         
      for set in values["sets"]:
         
         if not set in lookup["data_set"]:
            print("No data set exists for {}.".format(set))
            continue
         curr_data_set = lookup["data_set"][set]
         
         if set in lookup["file-app"]:
            appendix = lookup["file-app"][set]
         else:
            appendix = set
         
         curr_title    = title
         if set in lookup["title-app"]:
            curr_title += " {}".format(lookup["title-app"][set])
         else:
            curr_title += " {}".format(set)
         res_str       += "\n\n{}\n".format(lookup["title-app"][set])
         
         ext       = "png"
         save_file = os.path.join("results","{:02d}-{}-{}.{}".format(key,var,appendix,ext))
         curr_res  = basic_chart(curr_data_set,var,kind,curr_title,save_file) # Here, the actually analysis is triggered
         res_str  += "```\n{}\n```".format(curr_res)
   
   """
   5. Writing the results to a text file.
   """
   res_file = os.path.join("results","RESULTS.md")
   with open(res_file,"w",encoding="utf-8") as outfile:
      outfile.write(res_str)   

if __name__=='__main__':
  analyze_data()