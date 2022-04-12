from bs4 import BeautifulSoup
import requests

url = 'https://libraries.uky.edu'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
div = soup.find("div", class="sf-middle")
contacts = div.find_all("div", class="dashing-li")
print(contacts[0])
                