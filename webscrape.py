from bs4 import BeautifulSoup
import requests
import sys

stdoutOrigin=sys.stdout
sys.stdout = open('log.txt', "w")

html_text = requests.get('https://www.crossfitepicallyawesome.com/wod/')
soup = BeautifulSoup(html_text.text, 'lxml')

workouts = soup.find_all('p')

for br in soup.find_all('br'):
    br.replace_with('\n')

for workout in workouts:
    print(workout.text)
    
sys.stdout.close()
sys.stdout=stdoutOrigin
    




    
