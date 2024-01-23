import requests
from bs4 import BeautifulSoup
def latest_python_articles():
    url = "https://www.python.org/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text,'html.parser')
        latest_article = []

        for article in soup.select('.blog-widget li'):
            title = article.a.text.strip()
            latest_article.append(title)

        return latest_article
    
    else:
        print(f'failed to retrieve the information.status code : {response.status_code}')
        return []
    
if __name__ == "__main__":
    python_articles = latest_python_articles()
    if python_articles:
        print('Latest articles in python section : ')
        for index,article in enumerate(python_articles,1):
            print(f'{index}.{article}')
                  

    else:
        print('No article found')
    
        