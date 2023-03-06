import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#---------Load data from Excel File-----------
def uploadData():
  df = pd.read_excel("Regions.xlsx")
  return df

df = uploadData()

#--------------------Define pie chart function-----------
def plotPieChart(values, labels, titleText):
  plt.figure(figsize=(6,6))
  plt.pie(values,labels = labels,autopct='%0.1f') 
  plt.title(titleText)
  plt.savefig("Regions Exports.png")
  return plt

countries = df["Regions"]
lb = df["FY21"]

countries2 = df["Regions"]
lb2 = df["FY21(services)"]

#-----------------call pie chart function and give values-------------
plotPieChart(lb, countries, '% of Export(Goods) to Regions in FY21')
plotPieChart(lb2, countries2, '% of Export(Services) to Regions in FY21')


#---------Load data from Excel File-----------
def uploadData2():
  dg = pd.read_excel("5 year.xlsx")
  return dg

dg = uploadData2()
#-----------------define line chart function--------------------
def plotLineChart(x, y1, y2, titleText):
  plt.figure(figsize=(12,8))
  plt.plot(x, y1, label="Goods")
  plt.plot(x, y2, label="Services")
  plt.title(titleText)
  plt.xlabel("Years")
  plt.ylabel("Million US$")
  plt.legend()
  plt.savefig("Line Graph.png")
  return plt

Year = dg["Years"]
Goods = dg["Goods"]
Services = dg["Services"]
plotLineChart(Year, Goods, Services, '5 years export in Million US$')

#---------Load data from Excel File-----------
def uploadData3():
  dz = pd.read_excel("Monthly.xlsx")
  return dz

dz = uploadData3()

#-----------------------Define Bar Graph Function--------------------
def plotBarGraph(a, b1, b2, xlabel, ylabel, titleText):
  plt.figure(figsize=(12,8))
  plt.bar(a, b1, label="Goods")
  plt.bar(a, b2, label="Services")
  plt.xlabel(xlabel) 
  plt.ylabel(ylabel) 
  plt.title(titleText) 
  plt.legend()
  plt.savefig("Monthly Exports.png")
  return plt

i = dz["Month"]
y = dz["Goods"]
l = dz["Services"]
plotBarGraph(i, y, l, 'Months', 'Million US$', 'Exports of Goods and Services in FY21')

# plt.figure()
# iyears = years - 5.0 # offset to the left
# # the 2nd argument is the height of the bars
# # width in units of the x-axis
# plt.bar(iyears, inner_pop, width=7.0, label="inner")
# oyears = years + 5.0 # and to the right
# plt.bar(oyears, outer_pop, width=7.0, label="outer")
# # general matters
# plt.title("Population of London")
# plt.xlabel("year")
# plt.ylabel("population (millions)")
# plt.legend()
# plt.show()






