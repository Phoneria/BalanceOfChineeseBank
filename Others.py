import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("financial_statement.csv")
data.fillna(0, inplace=True)


total_asset_growth_rate = []
liability_growth_rate = []
debt_ratio = []
total_investors_equity = []
yıllar = []

for i in range(2006,2023):
    yıllar.append(i)
    varlık_büyüme_oranı.append(data[data["announcement date"].str.contains(str(i))]["asset-total asset growth rate"].mean())
    yükümlülük_büyüme_oranı.append(data[data["announcement date"].str.contains(str(i))]["liability-liability growth rate"].mean())
    borc_oranı.append(data[data["announcement date"].str.contains(str(i))]["Debt ratio"].mean())
    yatırımcı_sermayesi.append(data[data["announcement date"].str.contains(str(i))]["Total Investors Equity"].mean())


fig =plt.figure(figsize=(7,7))
axes =fig.add_axes([0.1,0.1,0.8,0.8])
#plt.plot(yıllar,total_investors_equity,color = "blue",linewidth = 2,linestyle ="-",marker = "o",markersize ="5",markerfacecolor = "black")
#axes.set_ylabel("Total Investors Equity")

#plt.plot(yıllar,debt_ratio,color = "black",linewidth = 2,linestyle ="-",marker = "o",markersize ="5",markerfacecolor = "black")
#axes.set_ylabel("Debt Ratio")

#plt.plot(yıllar,liability_growth_rate,color = "red",linewidth = 2,linestyle ="-",marker = "o",markersize ="5",markerfacecolor = "black")
#axes.set_ylabel("Liability Growth Rate")

plt.plot(yıllar,total_asset_growth_rate,color = "green",linewidth = 2,linestyle ="-",marker = "o",markersize ="5",markerfacecolor = "black")
axes.set_ylabel("Total Asset Growth Rate")

axes.set_title(" Çinli Şirketlerin Toplam Bilançosu")
axes.set_xlabel("Yıllar")

plt.show()
