import pandas as pd
url = ¨https://raw.githubusercontent.com/code-sivil/Population_graph_streamlit/refs/heads/main/population.csv¨
df = pd.read_csv(url)
df = df.drop(columns = ['Unnamed: 0'])
df.head()

#let's define the list pf column headers (country names) (except the first colmn which is the year)

unique_names = df['country'].unique().tolist()

#Let's define the years (the first column)
years = df['year'].unique()
#Then create the first columns of dataframe
df_visu = pd.DataFrame(years,columns = ['year'])

#For all the countries
for country_name in unique_names: 
    df_visu[country_name] = df[df['country']==country_name]['pop'].values

#Make graphics
import streamlit as st
#Define the Figure title
st.title('Population plot')

#Define a selectors (columns to draw)
columns = st.multiselect('Countries: ',unique_names)

#Plot the line chart
st.line_chart(df_visu,x = 'year', y = columns, y_label = 'Population', x_label = "Year")
