import json

from bs4 import BeautifulSoup as soup

f = open("html/united-kingdom.html", "r")

page_soup = soup(f.read(), "html.parser")
last_updated = page_soup.select_one('div.last-updated span')
page_content = page_soup.findAll('div', {"class": "leader-info"})
leaders_arr = []
titles_arr = []

for content in page_content:
    leader = [p.text for p in content.select('p')][0]
    title = [p.text for p in content.select('h4')][0]
    leaders_arr.append(leader)
    titles_arr.append(title)

parsed = [{"name": v, "title": k} for k, v in zip(titles_arr, leaders_arr)]

output = {
    "country": "United Kingdom",
    "last_updated": last_updated.text,
    "leaders": parsed
}

print(json.dumps(output))
