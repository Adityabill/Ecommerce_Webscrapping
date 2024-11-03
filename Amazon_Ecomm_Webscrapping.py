#Amazon Fresh
import requests
from bs4 import BeautifulSoup
import random
import time

# Headers to mimic a real browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.9'
}
prices = []
item_name = input("Enter the name of the item: ")

#url = "https://www.amazon.in/s?k=biscuit&i=nowstore"  # Example product URL
url = f"https://www.amazon.in/s?k={item_name}&i=nowstore"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

products = soup.find_all('span', class_ = 'a-price')#'a-declarative')

for product in products:
    price_text = soup.find('span', {'class': 'a-price-whole'}).get_text(strip=True)

    price = float(price_text)

    #print(price)

    prices.append(price)

time.sleep(random.uniform(1, 3))

if prices:
    print(min(prices))
else:
    print('No price available for the item you entered!')

# Extract product title
#title = soup.find(id='productTitle').get_text(strip=True)

# Extract product price
#price = soup.find('span', {'class': 'a-price-whole'}).get_text(strip=True)

# Extract rating
#rating = soup.find('span', {'class': 'a-icon-alt'}).get_text(strip=True)

#print("Title:", title)
#print("Price:", price)
#print("Rating:", rating)