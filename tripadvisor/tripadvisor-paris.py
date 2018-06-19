import sys, os
sys.path.append(os.path.dirname(os.getcwd()))

from bs4 import BeautifulSoup
from beautifultable import BeautifulTable

from _tools import *
from _helpers import *


STARTING_URL = "https://www.tripadvisor.fr/Restaurants-g187147-Paris_Ile_de_France.html"

restaurants = {}

raw_html = simple_get(STARTING_URL)

if raw_html : print('Connection successful...')

html = BeautifulSoup(raw_html, 'html.parser')

restaurant_nodes = html.select('[id^="eatery_"]')

for r in restaurant_nodes :
	key = get_key(r)
	restaurants[key] = {
		'name': get_name(r),
		'rating': get_rating(r),
		'reviews': get_reviews(r),
		'rank': get_rank(r),
	}


table = BeautifulTable()
table.column_headers = ['key', 'name', 'rating', 'reviews', 'rank']
table.column_alignments['key'] = BeautifulTable.ALIGN_LEFT
table.column_alignments['name'] = BeautifulTable.ALIGN_LEFT
table.column_alignments['rating'] = BeautifulTable.ALIGN_RIGHT
table.column_alignments['reviews'] = BeautifulTable.ALIGN_RIGHT

for key, data in restaurants.items() :
	table.append_row([
		key,
		data['name'][:20],
		data['rating'],
		data['reviews'],
		data['rank'],
		])

print(table)