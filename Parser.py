import requests
from bs4 import BeautifulSoup
import pandas as pd
def parse():
      url = "https://www.chitai-gorod.ru/search?phrase=python&page="
      newbook=[]
      excel = ['Name', 'Author', 'Price']
      try:
          for i in range (1,6,1):
              page = requests.get(url + str(i))
              book=[]
              myDict = []
              filname=[]
              filprice=[]
              filauth=[]
              soup = BeautifulSoup(page.text, "html.parser")
              blockprice = soup.findAll('div', class_='product-price__value'or'product-price__value product-price__value--discount')
              blockname = soup.findAll('div', class_='product-title__head')
              blockauthor = soup.findAll('div', class_='product-title__author')
              for res in blockname:
                filname.append(res.text.strip().replace('\xa0', ' '))
              for res in blockprice:
                filprice.append(res.text.strip().replace('\xa0', ' '))
              for res in blockauthor:
                filauth.append(res.text.strip().replace('\xa0', ' '))
              #print(len(filprice))
              for j in range(0, len(filname), 1):
                if j>=len(filprice):
                    myDict = {excel[0]: filname[j], excel[1]: filauth[j],excel[2]:'неизвестно'}
                else:
                    myDict = {excel[0]: filname[j], excel[1]: filauth[j], excel[2]: filprice[j]}
                book.append(myDict)
              print(book)
              newbook =newbook+book
      except:
          print("отсутствует соединение или сайт не отвечает")
          return
      df = pd.DataFrame.from_dict(newbook)
      df.to_excel("chitaigorod.xlsx")