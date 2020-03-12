import requests
from bs4 import BeautifulSoup


def get_mean_temperature(zipcode,date):

	url = 'https://www.almanac.com/weather/history/zipcode/ + ' + str(zipcode) +'/'+ str(date)

	response = requests.get(url)


	print(response)
	print(type(response.text))
	# print((response.text))

	data = response.text

	soup = BeautifulSoup(data, "xml")

	mydivs = soup.findAll("tr", {"class": "weatherhistory_results_datavalue temp"})

	mean_temperature = (mydivs[0].find("span",{"class": "value"}).contents[0])
	return(mean_temperature)



zipcode = '20816'
date = '2019-04-02'

print(get_mean_temperature(zipcode,date))