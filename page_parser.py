import requests
from bs4 import BeautifulSoup

def get_all_pages():
    urls = []
    page_number = 1
    for i in range(104):
        i = f"https://www.barreaudenice.com/annuaire/avocats/?fwp_paged={page_number}"
        urls.append(i)
        page_number += 1
    return urls


def get_avocat_names(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    avocats = soup.find_all('div', class_= 'callout secondary annuaire-single')
    for avocat in avocats:
        nom = avocat.find('h3')
        print(nom)
    
if __name__=='__main__':

    urls = get_all_pages()
    noms = get_avocat_names(urls[100])