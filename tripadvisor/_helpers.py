


def get_key(r):

	return r['id'].replace('eatery_', '')



def get_name(r):

	return r.find(class_='property_title').string.replace('\n', '')



def get_rating(r):

	bubble = r.find(class_='ui_bubble_rating')['class'][1]
	# should look like : bubble_50

	score = str(bubble).replace('bubble_', '')
	# should look like : 50

	rating = float(score)/10
	# should look like : 5.0

	return rating



def get_reviews(r):

	return r.find(class_='reviewCount').a.string.replace(' ', '').replace('avis', '')


def get_rank(r):

	rank_text = r.find(class_='popIndex').string
	# should look like : N°12 sur 13 023 Restaurants à Paris

	return rank_text[3:len(rank_text)-32]