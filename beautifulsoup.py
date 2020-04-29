import requests
from bs4 import BeautifulSoup


#getting top news from ITV
itv = requests.get("https://www.itv.com/news/")
itv_soup = BeautifulSoup(itv.content, 'html.parser')
itv_news = itv_soup.find(class_="top-articles__items").find_all(class_="top-articles__item-title")

#getting top news from FOX
fox = requests.get("https://www.foxnews.com/")
fox_soup = BeautifulSoup(fox.content, 'html.parser')
fox_news = fox_soup.find(class_="collection collection-spotlight").find_all(class_="title title-color-default")

#getting top news from USA TODAY
usa = requests.get("https://www.usatoday.com/")
usa_soup = BeautifulSoup(usa.content, 'html.parser')
usa_news = usa_soup.find(class_="gnt_rr").find_all(class_="gnt_m_th_a")

news_list = [[itv_news, "ITV"], [fox_news, "FOX"], [usa_news, "USA NEWS"]]

for source in news_list:
    print ("Top 4 news items from " + source[1] + ":")
    for i in range (4):
        print (str(i + 1) + ". " + (source[0][i].get_text()).strip())
    print ("")


