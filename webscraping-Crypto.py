# 1) web scraping setup & imports
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font
import csv

#--------------------------------------------------------------
# 2) web scraping variables & testing
site_address = 'https://www.investing.com/crypto/'

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

request = Request(site_address, headers=header)

webpage = urlopen(request).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

print(title) # testing if site scrappable
print()

#--------------------------------------------------------------
# 3) twilio imports
import keys
from twilio.rest import Client

client = Client(keys.accountSID,keys.authToken)

TwilioNumber = "+17432093337"

myCellPhone = "+19565335931"

#--------------------------------------------------------------
# 4) webscraping loops
tablecells = soup.findAll("tr")
counter = 1

for row in tablecells[1:6]:
    
    #variables for scraped items
    td = row.findAll("td")
    rank = (td[0].text.strip())
    currency_name = (td[2].text.strip())
    currency_symbol = (td[3].text.strip())
    current_price = float(td[4].text.replace(",",""))
    percent_change = (td[8].text.strip())

    #calculating corresponding price to % change
    current_price_formatted = float(td[4].text.replace(",",""))
    price_change = float(td[8].text.replace("+","").replace("%","")) / 100
    corresponding_price = round((current_price_formatted+(current_price_formatted * price_change)),4)

    #printing web scraping results
    print(f"Rank: #{rank}")
    print(f"Name of Currency: {currency_name}")
    print(f"Currency Symbol: {currency_symbol}")
    print(f"Current Price: ${current_price:,.2f}")
    print(f"% Change (last 24 hrs): {percent_change}")
    print(f"Corresponding Price w/ % Change: ${corresponding_price:,.2f}")
    print()

#--------------------------------------------------------------
# 5) Twilio Loops
#sending text if Bitcoin <$40,000 & Etherium <$3,000
for row in tablecells[1:6]:
    td = row.findAll("td")

    currency_name = (td[2].text.strip())
    current_price = float(td[4].text.replace(",",""))

    #Alert for BTC
    if currency_name == "Bitcoin" and current_price < 40000:
        textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, 
        body=f"ALERT: BTC has fallen below $40,000. Buy it now at ${current_price:,.2f}!")

    #Alert for ETH
    if currency_name == "Ethereum" and current_price < 3000:
        textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, 
        body=f"ALERT: ETH has fallen below $3,000. Buy it now at ${current_price:,.2f}!")


