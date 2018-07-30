from collections import Counter
import time

import requests
from bs4 import BeautifulSoup


def test_for_cycle(article_chain):
	url_dict = dict(Counter(article_chain))
	for key in url_dict:
		if url_dict[key] > 1:
			return True
			break

def continue_crawl(article_chain, target_url):
	if article_chain[-1] == target_url:
		print("Target Article found!")
		return False
	elif len(article_chain) > 25:
		print("too many articles!")
		return False
	elif test_for_cycle(article_chain):
		print("We're in a cycle! Abort search.")
		return False
	else:
		return True

def find_first_link(link):
	# download HTML
	html_text = requests.get(link).text
	#find the first link on the page with BeautifulSoup
	#make it beautiful fist
	soup = BeautifulSoup(html_text, "html.parser")
	content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
	for element in content_div.find_all("p", recursive=False):
		if element.find("a", recursive=False):
			first_relative_link = element.find("a", recursive=False).get('href')
			break
	first_link = "https://en.wikipedia.org"+ first_relative_link
	return first_link


def main():
	article_chain = []
	startLink = "https://en.wikipedia.org/wiki/Special:Random"
	article_chain.append(startLink)
	target_url = "https://en.wikipedia.org/wiki/Semiotics"
	while continue_crawl(article_chain, target_url):
		print(article_chain[-1])
		first_link = find_first_link(article_chain[-1])
		article_chain.append(first_link)
		time.sleep(0.5)

	print(article_chain[-1])


if __name__ == '__main__':
	main()