import pandas as pd
import matplotlib.pyplot as plt


prices = [
	(1, 2.12),
	(2, 2.56),
	(3, 3.10),
	(4, 3.16),
	(5, 3.58),
	(6, 5.12),
	(7, 5.16),
	(8, 5.20),
	(9, 4.12),
	(10, 4.10),
	(11, 3.65),
	(12, 4.25),
]

df = pd.DataFrame(prices)
df = pd.DataFrame(prices, columns=["Month", "Price"])
df = df.set_index("Month")


for column in df:
    polish_prices = df[column].values

usd_prices = []
for i in polish_prices:
		single_price = i / 4
		usd_prices.append(single_price)

df['USD_prices'] = usd_prices

plt.plot(df['USD_prices'], linestyle='dashed', color='red')
plt.title('Price of goods (USD)')
plt.xlabel('Month')
plt.grid()
plt.show()