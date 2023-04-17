import requests
from bs4 import BeautifulSoup
from openpyxl.reader.excel import load_workbook
row = ['неизвестно','неизвестно','неизвестно']
filpage=[]
def parse():
      url = "https://www.chitai-gorod.ru/search?phrase=python&page="
      url1 = "https://www.chitai-gorod.ru/search?phrase=python&page=1"
      pagefornum = requests.get(url1)
      soupfornum = BeautifulSoup(pagefornum.text, "html.parser")
      numpage=soupfornum.findAll('div',class_='pagination__button')
      for res in numpage:
          filpage.append(res.text.strip().replace('\xa0', ' '))
      print(filpage)
      try:
          for i in range (1,int(filpage[-2])+1):
              page = requests.get(url + str(i))
              filname=[]
              filprice=[]
              filauth=[]
              soup = BeautifulSoup(page.text, "html.parser")
              blockprice =soup.findAll('div', class_='product-price__value'or'product-price__value product-price__value--discount')
              blockname = soup.findAll('div', class_='product-title__head')
              blockauthor = soup.findAll('div', class_='product-title__author')
              maxlen=max(len(blockauthor),len(blockname),len(blockprice))
              for j in range(0,maxlen):
                  filname.append('неизвестно')
                  filauth.append('неизвестно')
                  filprice.append('неизвестно')
              b=0
              for res in blockname:
                filname[b]=res.text.strip().replace('\xa0', ' ')
                b = b + 1
              b = 0
              for res in blockprice:
                filprice[b]=res.text.strip().replace('\xa0', ' ')
                b = b + 1
              b = 0
              for res in blockauthor:
                filauth[b]=res.text.strip().replace('\xa0', ' ')
                if filauth[b]=='':
                    filauth[b]='неизвестно'
                print(filauth[b])
                b = b + 1

              for k in range(0,maxlen):
                  excelf(filname[k],filauth[k],filprice[k])
      except:
          print("отсутствует соединение или сайт не отвечает")
          return

def excelf(a,b,c):
    fn = r"C:\Users\msiuser\PycharmProjects\pythonProject\chitaigorod.xlsx"
    row[0]=a
    row[1] = b
    row[2] = c
    wb = load_workbook(fn)
    ws = wb["Sheet1"]
    ws.append(row)
    wb.save(fn)
    wb.close()