from bs4 import BeautifulSoup as soup
from bs4 import ResultSet

f = open("html/high-risk-third-countries.html", "r")

page_soup = soup(f.read(), "html.parser")
field_contents: ResultSet = page_soup.findAll("div", {"class": "field-content"})
content_arr = []
for field_content in field_contents:
    content = field_content.select("ul:not(:has(li a)) li")
    content_arr = content
countries = [li.get_text().replace('*', '') for li in content_arr]

print(countries)
print(len(countries))
