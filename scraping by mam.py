import requests
from bs4 import BeautifulSoup
def upcoming_events(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text,'html.parser')
        new_events = []

        for events in soup.select('.event-widget.last li'):
            title = events.a.text.strip()
            new_events.append(title)

        return new_events
    
    else:
        print(f'failed to retrieve the information.status code : {response.status_code}')
        return []
    
if __name__ == "__main__":
    coming_events = upcoming_events("https://www.python.org/")
    if coming_events is not None:
        print('Upcoming events in python section: ')
        for index,article in enumerate(coming_events,1):
            print(f'{index}. {article}')
            
                  

    else:
        print('No article found')
    
        