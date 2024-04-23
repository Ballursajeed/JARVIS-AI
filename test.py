from bs4 import BeautifulSoup
import requests

query = "the current temperature in mumbai"
substring = query[query.index("temperature in mumbai"):]
print(substring)

   
search = query.split('temperature in ')[1]
url = f"https://www.google.com/search?q={query}"
r = requests.get(url)
data = BeautifulSoup(r.text, "html.parser")
temp = data.find("div",class_="BNeawe").text
print(f"current temperature in {search} is {temp}")