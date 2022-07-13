import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("financial_statement.csv")

data.fillna(0, inplace=True)


data["total income"] = data["asset-Cash and cash equivalents"]+data["asset-Account receivable"]\
                       +data["asset-inventory"]+data["asset-total asset"]
data["total outgo"] = data["liability-Account payable"]+data["liability-Advance from customers"]+data["liability-total liability"]
data["balance"] = data["total income"] - data["total outgo"]

yearly_income = []
yearly_outgo = []
yearly_balance = []
years = []

for i in range(2006,2023):
    years.append(i)
    yearly_income.append(data[data["announcement date"].str.contains(str(i))]["total income"].mean())
    yearly_outgo.append(data[data["announcement date"].str.contains(str(i))]["total outgo"].mean())
    yearly_balance.append(data[data["announcement date"].str.contains(str(i))]["balance"].mean())


fig =plt.figure(figsize=(7,7))
axes =fig.add_axes([0.1,0.1,0.8,0.8])
plt.plot(years,yearly_income,color = "green",label = "Income",linewidth = 2,linestyle ="-",marker = "o",markersize ="5",markerfacecolor = "black")
plt.plot(years,yearly_outgo,color = "red",label = "Out go",linewidth = 2,linestyle ="-",marker = "o",markersize ="5",markerfacecolor = "black")
plt.plot(years,yearly_balance, color = "blue",label ="Balance",linewidth = 2,linestyle ="-",marker = "o",markersize ="5",markerfacecolor = "black")
axes.legend()
plt.show()