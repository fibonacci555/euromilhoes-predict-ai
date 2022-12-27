import os
import requests
from bs4 import BeautifulSoup

numeros_full = []
id = 0


def readAll(ano):
	global numeros_full
	global id

	url = "https://www.euro-millions.com/pt/arquivo-de-resultados-" + str(ano)
	response = requests.get(url)
	if response.ok:
		soup = BeautifulSoup(response.text, "lxml")

		scraped = []
		job_elements = list(soup.find_all(class_="balls small"))

		for element in job_elements:

			if "new" in str(element):
				scraped.append(list(element))

		for i in range(len(scraped)):
			edicao = [id]
			for j in range(len(scraped[i])):
				for letter in scraped[i][j]:
					if str(letter).isnumeric():
						if len(letter) == 1:
							letter = f"0{letter}"
						edicao.append(letter)
			numeros_full.append(edicao)
			id += 1


