import requests
import bs4
import pandas as pd

#indicate schedule page on formula 1 website as target url
url = 'https://www.formula1.com/en/racing/2020.html'
res = requests.get(url)
html_page = res.content

#create a beautifulsoup object
soup = bs4.BeautifulSoup(html_page, 'html.parser')

#select elements we are interested in
countries = soup.select('.event-place')
titles = soup.select('.f1--xxs')
months = soup.select('.f1-wide--xxs')
dates = soup.select('.f1-wide--s .no-margin')

#create empty lists for each type of element
l_countries = []
l_titles = []
l_dates = []
l_months = []


#do the loopp through each and get text, remove line breakes 
#and removing extra spaces
for index, item in enumerate(countries):
    l_countries.append(countries[index].getText().replace("\n","").strip())
    
for index, item in enumerate(titles):
    if 'Formula 1' in titles[index].getText():
        l_titles.append(titles[index].getText().replace("\n","").strip())


for index, item in enumerate(dates):
    l_dates.append(dates[index].getText().replace("\n","").replace(" ",""))
    

for index, item in enumerate(months):
    l_months.append(months[index].getText().replace("\n","").strip())

#put dates and months together separated by a space
date = [i + " " +j for i, j in zip(l_dates, l_months)]

#Let's now bring everything together in a dataframe with unicode signes
#in column names

df = pd.DataFrame(list(zip(date, l_countries, l_titles)), 
			columns =['Date \U0001F4C5', 'Location \U0001F4CD', 'Name \U0001F3C1']) 

#And let's now write everything to a csv file
df.to_csv("f1_schedule2020.csv", encoding='utf-8', index=False)
