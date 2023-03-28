import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

raw_data = pd.read_csv('Covid-19-WHO-Regions.csv')
#raw_data

#print(raw_data.to_string()) 

data_df = pd.DataFrame(raw_data)
data_df.drop(data_df.columns[[0, 2, 3]], axis = 1, inplace=True)
#data_df

#print(data_df.to_string()) 

Active_Cases_In_Country_df = data_df.groupby(['Country/Region'])[['Active']].sum()
Active_Cases_In_Country_df.sort_values(['Active'], ascending=False, inplace=True)
Active_Cases_In_Country_df.head(10)

print(Active_Cases_In_Country_df.to_string()) 

fig, ax = plt.subplots(figsize=(15, 15))
graph = sns.barplot(data=Active_Cases_In_Country_df.head(10), x=Active_Cases_In_Country_df.head(10).index, y="Active", ax=ax).set(title='Top 10 Countries of Most Active Cases (1e8)')

#print(graph)