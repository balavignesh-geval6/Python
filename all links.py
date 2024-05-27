from bs4 import BeautifulSoup
import requests

root = "https://subslikescript.com"
website = f"{root}/movies_letter-A"
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())
pagination = soup.find('ul', class_="pagination")
pages = pagination.find_all("li", class_="page-item")
last_page = pages[-2].text
print(last_page)

links = []

for page in range(1, int(last_page)+1)[:2]:
    # https://subslikescript.com/movies_letter-A?page=1
    # website = f"{root}/movies_letter-A/?page={page}"
    # print(website)
    result = requests.get(f"{root}/movies_letter-A/?page={page}")
    content = result.text
    soup = BeautifulSoup(content, 'lxml')


    box = soup.find('article', class_="main-article")
    box.find_all('a', href=True)

    for link in box.find_all('a', href=True):
        links.append(link['href'])

    for link in links:
        try:
            website = f"{root}/{link}"
            result = requests.get(website)
            content = result.text
            soup = BeautifulSoup(content, 'lxml')
            box = soup.find('article', class_="main-article")

            title = soup.find('h1').get_text()
            print(title)
            print(box)
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
            #print(transcript)
            with open(f'{title}.txt', 'w', encoding='utf-8') as file:
                file.write(transcript)
        except:
            print(f"---------not working link {link}")
            print(f"{link}")