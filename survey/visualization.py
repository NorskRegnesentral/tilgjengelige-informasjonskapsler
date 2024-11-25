import os

import pandas as pd
import matplotlib.pyplot as plt

import config

def plot_data(data,kind,title,save_file="",is_percentage=False,fig_size=(),cmap=""):
   """
   Returns the results as string.
   """
   
   colors = "Paired"
   if cmap:
      colors = cmap
      
   fig, ax = plt.subplots()
   
   if fig_size:
      fig.set_size_inches(fig_size)   

   if kind == "pie":
      rounding ='%1.f%%'
      data.plot(kind=kind,subplots=True,ax=ax,autopct=rounding, ylabel="", cmap=colors)

   else: 
      if is_percentage:
         total = data.sum()
         pct = round((data/total) * 100,0)
         data = pct
      
      data.plot(kind=kind,ax=ax, cmap=colors)
      
      for container in ax.containers:
         ax.bar_label(container)
         ax.tick_params(axis='x', labelrotation=0)
         if is_percentage:
            ax.set_ylabel("%") 
           
   if title:
      ax.set_title(title)
   
   folder = os.path.dirname(save_file)
   if not os.path.exists(folder):
      print("Creating folder\"{}\".".format(folder))
      os.makedirs(folder)
      
   if save_file:
      fig.savefig(save_file)
      plt.close(fig)
      print("Image saved under {}".format(save_file))
   
   plt.close()
   
   return