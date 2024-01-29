import requests
from bs4 import BeautifulSoup

def get_latest_python_articles(url,output_file):
    response=requests.get(url)

    if response.status_code==200:
        soup = BeautifulSoup(response.text,'html.parser')
  

        latest_articles=soup.select('.blog-widget li')

        with open(output_file,'w',encoding='utf-8') as file:
            file.write('Latest articles in python section are: \n\n')
            print('\nLatest articles in python section are: \n')
            for index, article in enumerate(latest_articles,1):
                title = article.a.text.strip()
                file.write(f'{index}. {title}\n')
                print(f'{index}. {title}\n')

        print(f"Article saved to : {output_file}\n")

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

get_latest_python_articles('https://www.python.org/','Latest_articles.txt')

