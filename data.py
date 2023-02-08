import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/IBM/history?p=IBM"   #other companies data can also be used

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

data_rows = soup.find("table", {"data-test": "historical-prices"}).find("tbody").find_all("tr")
for row in data_rows:
    cells = row.find_all("td")
    date = cells[0].text
    close = cells[4].text
    volume = cells[5].text

    # to do something with the extracted data
    print(f"{date}: Close - {close}, Volume - {volume}")
