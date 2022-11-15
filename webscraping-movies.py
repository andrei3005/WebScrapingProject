
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)
print()

tablecells = soup.findAll("tr")
counter = 1

#for x in range(5):
for row in tablecells[1:6]:
    '''
    rank = tablecells[0].text
    movie_name = tablecells[1].text

    total_gross = tablecells[7].text
    #total_gross_formatted = float(tablecells[7].text.replace("$","").replace(",",""))

    distributor = tablecells[9].text
    #avg_gross_per_theater = tablecells[counter+3].text
    #num_theaters = float(tablecells[6].text.replace(",",""))

    #avg_gross_per_theater = round((total_gross_formatted/num_theaters) * 100,2)

    counter += 1
    '''
    
    td = row.findAll("td")
    rank = td[0].text
    movie_name = td[1].text

    total_gross = td[7].text
    total_gross_formatted = float(td[7].text.replace("$","").replace(",",""))

    distributor = td[9].text
    #avg_gross_per_theater = tablecells[counter+3].text
    num_theaters = float(td[6].text.replace(",",""))

    avg_gross_per_theater = round((total_gross_formatted/num_theaters) * 100,2)

    counter += 1
    

    print(f"Rank: #{rank}")
    print(f"Movie Name: {movie_name}")
    print(f"Total Gross: {total_gross}")
    print(f"Gross per Theater: ${avg_gross_per_theater:,.2f}")
    print(f"Distributor: {distributor}")
    #print(f"Gross per Theater:${avg_gross_per_theater:,.2f}")
##
##
##
##


