from collections import Counter
import time

import requests
from bs4 import BeautifulSoup


def test_for_cycle(article_chain):
	url_dict = Counter(search_history)
	for key in url_dict:
		if url_dict[key] > 1:
			return True
		else:
			return False

def continue_crawl(article_chain, target_url):
	if search_history[-1] == target_url:
		print("Target Article found!")
		return False
	elif len(article_chain) > 25:
		return False
	elif test_for_cycle:
		print("We're in a cycle! Abort search.")
		return False
	else:
		return True

def find_first_link(link):
	# download HTML
	html_text = requests.get(link).text
	#find the first link on the page with BeautifulSoup
	#make it beautiful fist
	soup = BeautifulSoup(html_text, "html_parser")
	return "https://en.wikipedia.org"+ soup.p.a["href"]



def main():
	while continue_crawl(article_chain, target_url):
	# download html of last article in article_chain
    # find the first link in that html
    firstLink = find_first_link(article_chain[-1])
    # add the first link to article_chain
    article_chain.append(firstLink)
    # delay for about two seconds
    time.sleep(2)


if __name__ == '__main__':
	main()