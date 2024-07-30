#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests


url = "https://sports.ndtv.com/olympics-2024/medals-tally"
response = requests.get(url)

stats = {}
if response.status_code == 200:
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    countries = soup.find_all('ul', class_="OlyT_ul")
    
    for country in countries:
        lands = country.find_all('div', class_="OlyT_tab-li OlyT_tab-nam OlyT_tab-nwap")
        medals = country.find_all('div', class_="OlyT_tab-rt")  
        
        for land, medal in zip(lands, medals):
            land_name = land.text.strip()
            golden = medal.find('div', class_="OlyT_tab-li OlyT_gld OlyT_tab-swp")
            second = medal.find('div', class_="OlyT_tab-li OlyT_slv OlyT_tab-swp")
            third = medal.find('div', class_="OlyT_tab-li OlyT_brz OlyT_tab-swp")
            total = medal.find('div', class_="OlyT_tab-li OlyT_tab-swp OlyT_tab-nrr").text
            
            gold = golden.find('span', class_="OlyT_tab-li-nm").text 
            silver = second.find('span', class_="OlyT_tab-li-nm").text 
            bronze = third.find('span', class_="OlyT_tab-li-nm").text 
            
            stats[land_name] = {
                "Gold": gold,
                "Silver": silver,
                "Bronze": bronze,
                "Total" : total
            }
 
for country, medals in stats.items():
    print(f"{country}")
    print(f"{medals}")
    print()
    #when ran like this full information is not displayed in the terminal
       # print(f"{country}")
       # print(f"Gold - {medals['Gold']}")
       # print(f"Silver - {medals['Silver']}")
       # print(f"Bronze - {medals['Bronze']}")
       # print(f"Total - {medals['Total']}")
search = input("Name of Country: ")
if search in stats.keys():
    points = stats[search]
    print(f"Gold - {points['Gold']}")
    print(f"Silver - {points['Silver']}")
    print(f"Bronze - {points['Bronze']}")
    print(f"Total - {points['Total']}")
else:
    print("Invalid Name of Country")
    