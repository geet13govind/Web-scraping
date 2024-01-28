import requests
from bs4 import BeautifulSoup

def get_latest_python_articles(url,output_file):
    response=requests.get(url)

    if response.status_code==200:
        soup = BeautifulSoup(response.text,'html.parser')
        
        file=open('Latest_articles.txt','w')
        file.write('\n')
        file.write('Latest articles in python section are: \n\n')
        print('Latest articles in python section are: \n\n')

        latest_articles=soup.select('.blog-widget li')

        with open(output_file,'a',encoding='utf-8') as file:
            for index, article in enumerate(latest_articles,1):
                title = article.a.text.strip()
                file.write(f'{index}. {title}\n')
                print(f'{index}. {title}\n')

        print(f"Article saved to : {output_file}")

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

get_latest_python_articles('https://www.python.org/','Latest_articles.txt')

