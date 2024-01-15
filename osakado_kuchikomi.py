import requests
from bs4 import BeautifulSoup
import pandas as pd

Name = []
Review = []

for num in range(1,60):
    url = 'https://osakadou.cool/product_reviews/rpg/page:'+str(num)+'/lmt:100/odb:1/purl:005010_placentrexgel.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    kuchikomi = soup.find('div',{'class':'tab'})
    item_names = kuchikomi.find_all('p',{'class':'reviewItem'})
    reviews = kuchikomi.find_all('p',{'class':'reviewComment'})
    for i in item_names:
        Name.append(i.text)
    for r in reviews:
        r = r.text.replace('\t','').replace('\n','')
        Review.append(r)



df = pd.DataFrame(columns = ['Item Names','Review'])
df['Item Names'] = Name
df['Review'] = Review

df.to_csv('/Users/Ken/Downloads/placenta_kuchikomi.csv')

osk = pd.read_csv('/Users/Ken/Downloads/placenta_kuchikomi.csv', encoding="utf_8_sig", index_col=0)
print(osk.head())
