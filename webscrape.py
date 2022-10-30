from bs4 import BeautifulSoup
import requests
import sys

stdoutOrigin=sys.stdout
sys.stdout = open('log.txt', "w")

html_text = requests.get('https://www.mayhemathletes.com/daily-workout/')
soup = BeautifulSoup(html_text.text, 'lxml')
workouts = soup.find_all('div', class_ = 'tb-field')


for workout in workouts:
    print(workout.text)
    
sys.stdout.close()
sys.stdout=stdoutOrigin
    
    
    




    
