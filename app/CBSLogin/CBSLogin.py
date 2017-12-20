import requests
from bs4 import BeautifulSoup

class CBSLogin():
	def __init__(self, username = None, password = None):
		self.payload = {'username': username, 
						'password': password,
						'_eventId':'submit',
						'Submit.x':0,
						'Submit.y':0,
						}
		self.headers = {'User-Agent': 'Mozilla/5.0'}
		self.s = requests.Session()
		cookieFetch = self.s.get("https://expresso.gsb.columbia.edu/cas/login?service=https%3A%2F%2Fwww8.gsb.columbia.edu%2Fcbs-directory%2Fwelcome", headers=self.headers)
		soup = BeautifulSoup(cookieFetch.text, 'html.parser')
		for _input in soup.find_all('input'):
			if _input.get('name') == 'lt':
				self.payload['lt'] = _input.get('value')
			elif _input.get('name') == 'execution':
				self.payload['execution'] = _input.get('value')
		self.cookies = requests.utils.cookiejar_from_dict(requests.utils.dict_from_cookiejar(self.s.cookies))
		loginUrl = self.s.post("https://expresso.gsb.columbia.edu/cas/login?service=https%3A%2F%2Fwww8.gsb.columbia.edu%2Fcbs-directory%2Fwelcome", headers=self.headers,data=self.payload, cookies=self.cookies)
	

	def setUsername(self, username):
		self.payload[username] =  username

	def setPassword(self, password):
		self.payload[password] = password

	def getInfo(self, lifetimeID):
		search = self.s.post("https://www8.gsb.columbia.edu/cbs-directory/directory-search?combine=%s&rid=All" % lifetimeID, headers=self.headers, data=self.payload,cookies=self.cookies)
		search_data = BeautifulSoup(search.text,'html.parser').find('div', class_='full-name')
		if search_data: 
			url = search_data.a.get('href')
			resp = self.s.post("https://www8.gsb.columbia.edu/" + url, headers=self.headers, data=self.payload,cookies=self.cookies)
			soup = BeautifulSoup(resp.text, 'html.parser')
			name = soup.find('h1',class_='primary-heading').text
			about = soup.select("div p b")
			program = about[0].parent.text.split(":")[1].strip()
			entry_term = about[1].parent.text.split(":")[1].strip()
			cluster = about[2].parent.text.split(":")[1].strip()
			email = lifetimeID + "@gsb.columbia.edu"
			return (name, program, entry_term, cluster, email)
		else: 
			return (None, None, None, None, None)