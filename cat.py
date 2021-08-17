import json
import os
import requests


def getcat(number=1):
	response = requests.request(
		"GET",
		f"https://api.thecatapi.com/v1/images/search?limit={number}",
		headers={
			'Content-Type': 'application/json',
			'x-api-key': os.getenv('TOKEN'),
		}, data={})
	links = ""
	for i in range(number):
		links += response.json()[i]['url'] + "\n"
	return links
