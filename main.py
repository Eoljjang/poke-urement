import requests
from bs4 import BeautifulSoup
import urllib.parse
import json

# Note: Each website has a different shopify structure - so we have to have different functions for each.

def check_203(search_url):
    page_html, status_code, page_json = get_page_html(search_url)
    if (status_code != 200):
        print("Error when requesting 203 collectibles.")
        return

    soup = BeautifulSoup(page_html, 'html.parser')
    products = soup.find_all("span", class_="instock")
    print("203 Collectibles Stock (use code WONG5 for 5% off):", len(products))

def check_eclipse(search_url):
    page_html, status_code, page_json = get_page_html(search_url)
    if (status_code != 200):
        print("Error when requesting Eclipse Games.")
        return

    soup = BeautifulSoup(page_html, 'html.parser')
    products = soup.find_all("span", class_="instock")
    print("Eclipse Games Stock:", len(products))

def check_swirl(search_url): # nathan
    page_html, status_code, page_json = get_page_html(search_url)

    soup = BeautifulSoup(page_html, 'html.parser')
    li_elements = soup.find_all('li', attrs={'data-variantqty': True}) # Finds all items that have a quantity > 0. IE: In stock.
    print("Swirl YEG Stock: [NOT RELIABLE]", len(li_elements))

def check_hpw(search_url): # adam
    page_html, status_code, page_json = get_page_html(search_url)
    
    soup = BeautifulSoup(page_html, 'html.parser')
    add_to_cart_btns = soup.find_all('button', string="Add to cart")
    print("HPW Stock: [NOT RELIABLE]", len(add_to_cart_btns))

def check_prisma(search_url): # adam
    pass

def check_taps(search_url): # we'll deal with this later.
    pass

# Generic function to GET a site.
def get_page_html(url):
    page = requests.get(url)
    return page.content, page.status_code, page.json

def main():
    # Sample Query: 'https://203collectibles.com/search?type=product&q=ultra+ball'
    url_203 = 'https://203collectibles.com/search?q='
    url_eclipse = 'https://eclipsegames.ca/search?q='
    url_swirl = "https://swirlyeg.com/search?q="
    url_hpw = "https://hpwcards.com/search?q="
    url_prisma = "https://www.prismatcg.com/store/search/" # append name of item.
    url_taps = 'https://tapsgames.com/search.php?search_query='

    # User Input
    search = input("What do you want to search for? ")
    encoded_search = urllib.parse.quote_plus(search) # Encode search term to handle spaces & special characters.

    # Query every site
    check_203(url_203 + encoded_search)
    check_eclipse(url_eclipse + encoded_search)
    check_swirl(url_swirl + encoded_search)
    check_hpw(url_hpw + encoded_search)
    check_prisma(url_prisma + encoded_search)
    check_taps(url_taps + encoded_search);

main()
