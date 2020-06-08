import pandas_datareader.data as web
import datetime
import yfinance as yf
import pandas as pd
import numpy as np
import sys
import pymysql

# Database prep
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='stock_database',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)


# panda get yahoo finance data
yf.pdr_override()

start = datetime.datetime(2020, 6, 1)
end = datetime.datetime.today()

apple = web.get_data_yahoo('AAPL', start, end)
microsoft = web.get_data_yahoo('MSFT', start, end)
goldman = web.get_data_yahoo('GS', start, end)
jpmorgan = web.get_data_yahoo('JPM', start, end)
metlife = web.get_data_yahoo('MET', start, end)
americanexpress = web.get_data_yahoo('AXP', start, end)
caterpillar = web.get_data_yahoo('CAT', start, end)
threem = web.get_data_yahoo('MMM', start, end)
generalelectronic = web.get_data_yahoo('GE', start, end)
boeing = web.get_data_yahoo('BA', start, end)
ibm = web.get_data_yahoo('IBM', start, end)
intel = web.get_data_yahoo('INTC', start, end)
cocacola = web.get_data_yahoo('KO', start, end)
pg = web.get_data_yahoo('PG', start, end)
walmart = web.get_data_yahoo('WMT', start, end)

Adj_close = pd.DataFrame({"AAPL": apple["Adj Close"],
                          "MSFT": microsoft["Adj Close"],
                          "GS": goldman["Adj Close"],
                          "JPM": jpmorgan["Adj Close"],
                          "MET": metlife["Adj Close"],
                          "AXP": americanexpress["Adj Close"],
                          "CAT": caterpillar["Adj Close"],
                          "MMM": threem["Adj Close"],
                          "GE": generalelectronic["Adj Close"],
                          "BA": boeing["Adj Close"],
                          "IBM": ibm["Adj Close"],
                          "INTC": intel["Adj Close"],
                          "KO": cocacola["Adj Close"],
                          "PG": pg["Adj Close"],
                          "WMT": walmart["Adj Close"]})

Volume = pd.DataFrame({"AAPL": apple["Volume"],
                       "MSFT": microsoft["Volume"],
                       "GS": goldman["Volume"],
                       "JPM": jpmorgan["Volume"],
                       "MET": metlife["Volume"],
                       "AXP": americanexpress["Volume"],
                       "CAT": caterpillar["Volume"],
                       "MMM": threem["Volume"],
                       "GE": generalelectronic["Volume"],
                       "BA": boeing["Volume"],
                       "IBM": ibm["Volume"],
                       "INTC": intel["Volume"],
                       "KO": cocacola["Volume"],
                       "PG": pg["Volume"],
                       "WMT": walmart["Volume"]})

Std_apple = []
Std_microsoft = []
Std_goldman = []
Std_jpmorgan = []
Std_metlife = []
Std_americanexpress = []
Std_caterpillar = []
Std_threem = []
Std_generalelectronic = []
Std_boeing = []
Std_ibm = []
Std_intel = []
Std_cocacola = []
Std_pg = []
Std_walmart = []

for i in range(len(Adj_close.values)):
    Std_apple.append(np.std(Adj_close.iloc[i:-1, 0:1].values))
    Std_microsoft.append(np.std(Adj_close.iloc[i:-1, 1:2].values))
    Std_goldman.append(np.std(Adj_close.iloc[i:-1, 2:3].values))
    Std_jpmorgan.append(np.std(Adj_close.iloc[i:-1, 3:4].values))
    Std_metlife.append(np.std(Adj_close.iloc[i:-1, 4:5].values))
    Std_americanexpress.append(np.std(Adj_close.iloc[i:-1, 5:6].values))
    Std_caterpillar.append(np.std(Adj_close.iloc[i:-1, 6:7].values))
    Std_threem.append(np.std(Adj_close.iloc[i:-1, 7:8].values))
    Std_generalelectronic.append(np.std(Adj_close.iloc[i:-1, 8:9].values))
    Std_boeing.append(np.std(Adj_close.iloc[i:-1, 9:10].values))
    Std_ibm.append(np.std(Adj_close.iloc[i:-1, 10:11].values))
    Std_intel.append(np.std(Adj_close.iloc[i:-1, 11:12].values))
    Std_cocacola.append(np.std(Adj_close.iloc[i:-1, 12:13].values))
    Std_pg.append(np.std(Adj_close.iloc[i:-1, 13:14].values))
    Std_walmart.append(np.std(Adj_close.iloc[i:-1, 14:15].values))




Std_apple = Std_apple[::-1]
Std_microsoft = Std_microsoft[::-1]
Std_goldman = Std_goldman[::-1]
Std_jpmorgan = Std_jpmorgan[::-1]
Std_metlife = Std_metlife[::-1]
Std_americanexpress = Std_americanexpress[::-1]
Std_caterpillar = Std_caterpillar[::-1]
Std_threem = Std_threem[::-1]
Std_generalelectronic = Std_generalelectronic[::-1]
Std_boeing = Std_boeing[::-1]
Std_ibm = Std_ibm[::-1]
Std_intel = Std_intel[::-1]
Std_cocacola = Std_cocacola[::-1]
Std_pg = Std_pg[::-1]
Std_walmart = Std_walmart[::-1]

Volatility = pd.DataFrame({"AAPL": Std_apple,
                           "MSFT": Std_microsoft,
                           "GS": Std_goldman,
                           "JPM": Std_jpmorgan,
                           "MET": Std_metlife,
                           "AXP": Std_americanexpress,
                           "CAT": Std_caterpillar,
                           "MMM": Std_threem,
                           "GE": Std_generalelectronic,
                           "BA": Std_boeing,
                           "IBM": Std_ibm,
                           "INTC": Std_intel,
                           "KO": Std_cocacola,
                           "PG": Std_pg,
                           "WMT": Std_walmart}, index=Adj_close.index)

pd.set_option('display.max_rows', sys.maxsize)
pd.set_option('display.max_columns', sys.maxsize)

companies = ["AAPL", "MSFT", "GS", "JPM", "MET", "AXP", "CAT", "MMM", "GE", "BA", "IBM", "INTC", "KO", "PG", "WMT"]
dic_adj = {}
for j in range(len(companies)):
    values = {}
    dic_adj[companies[j]] = values
    for i in range(len(Adj_close.index)):
        temp = []
        temp.append(format(np.array(Adj_close.iloc[[i], [j]]).tolist()[0][0], '.3f'))
        temp.append(np.array(Volume.iloc[[i], [j]]).tolist()[0][0])
        try:
            temp.append(format(np.array(Volatility.iloc[[i], [j]]).tolist()[0][0], '.3f'))
        except:
            temp.append(0)
        values[str(Adj_close.index[i])] = temp

# dic_volume = {}
# for j in range(len(companies)):
#     values = {}
#     dic_volume[companies[j]] = values
#     for i in range(len(Volume.index)):
#         values[str(Volume.index[i])] = np.array(Volume.iloc[[i], [j]]).tolist()[0][0]
#
# dic_volatility = {}
# for j in range(len(companies)):
#     values = {}
#     dic_volatility[companies[j]] = values
#     for i in range(len(Volatility.index)):
#         values[str(Volatility.index[i])] = np.array(Volatility.iloc[[i], [j]]).tolist()[0][0]



print(dic_adj)
# print(dic_volume)
# print(dic_volatility)


for i in dic_adj:
    for j in dic_adj[i]:
        cursor = conn.cursor()
        query = "INSERT INTO stock VALUES (%s,%s,%s,%s,%s)"
        try:
            cursor.execute(query, (i, j, dic_adj[i][j][0], dic_adj[i][j][1], dic_adj[i][j][2]))
            conn.commit()
        except:
            print("already exists!")
            continue
        cursor.close()

# for i in dic_volume:
#     for j in dic_volume[i]:
#         cursor = conn.cursor()
#         query = "UPDATE stock " \
#                 "SET volume = %s " \
#                 "WHERE (company_name,date) = %s,%s"
#         cursor.execute(query, (dic_volume[i][j], i, j))
#         conn.commit()
#         print("Already exists!")
#         cursor.close()
#
# for i in dic_volatility:
#     for j in dic_volatility[i]:
#         cursor = conn.cursor()
#         query = "UPDATE stock " \
#                 "SET volatility = %s " \
#                 "WHERE (company_name,date) = %s,%s"
#         try:
#             cursor.execute(query, (dic_volatility[i][j], i, j))
#             conn.commit()
#         except:
#             print("already exists!")
#             continue
#         cursor.close()