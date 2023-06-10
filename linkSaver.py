
import requests
from bs4 import BeautifulSoup

def save_links_to_file(url, output_file):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')

    with open(output_file, 'w') as file:
        
        for link in links:
            href = link.get('href')
            if href:
                file.write(href + '\n')

url = 'https://www.example.com'  # Write the address of the website which you want the link addresses
output_file = 'links.txt'

save_links_to_file(url, output_file)