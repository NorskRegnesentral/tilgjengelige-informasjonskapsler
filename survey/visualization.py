import os

import pandas as pd
import matplotlib.pyplot as plt

def plot_data(data,kind,title,save_file=""):
   """
   Returns the results as string.
   """
   
   colors = "Pastel1"
   fig, ax = plt.subplots()   
         
   if kind == "pie":
      pupsi ='%1.f%%'   
      data.plot(kind=kind, ax=ax,autopct=pupsi, ylabel="", cmap=colors)
   else: 
      #total = data.sum()
      #percentage = []
      #for i in data:
      #   pass
         #pct = (i / total) * 100
         #percentage.append(round(pct, 2))
      #ax = round(data/total*100).plot(kind=kind, ylabel="%", cmap="Pastel1")
      #print(data)
      data.plot(kind=kind,ax=ax,cmap=colors)
      
      for container in ax.containers:
         ax.bar_label(container)
           
   if title:
      ax.set_title(title)
      
   if save_file:
      fig.savefig(save_file)
      plt.close(fig)
      print("Image saved under {}".format(save_file))
   
   plt.close()
   
   return