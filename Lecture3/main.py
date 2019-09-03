import requests
from bs4 import BeautifulSoup as bs 
from vacancy import Vacancy 

#Roadmap:
#0 ---- create connection with hh.ru +++++
#1 ---- send GET request to hh.ru ++++++
#1.1 ---- ЗП - это строка, нужно получить число +++++
#2 ---- save data to dataBase
#3 ---- plot data



text_request = input("Enter request: ")
search_area = int(input("Enter area: "))

url = "https://hh.ru/search/vacancy?area=%i&st=searchVacancy&text=%s"%( search_area, text_request)

print(url)






headers = {"accept": "*/*", 
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36"}


session = requests.Session()
req = session.get(url, headers = headers)


if req.status_code == 200:
    soup = bs(req.content, "html.parser")
    divs = soup.find_all("div", attrs = {"data-qa":"vacancy-serp__vacancy"})
    for div in divs:
        try:
            title = div.find("a", attrs = {"data-qa":"vacancy-serp__vacancy-title"}).text
            company = div.find("a", attrs = {"data-qa":"vacancy-serp__vacancy-employer"}).text
            salary = div.find("div", attrs = {"data-qa":"vacancy-serp__vacancy-compensation"}).text
            
            vac = Vacancy(text_request, title, company, salary)
            vac.salaryParse()
            vac.save_to_db()
        except:
            pass
else:
    print("ERROR!", req.status_code)
    










