from bs4 import BeautifulSoup
import requests

index = {"a": 100, "b": 96, "c": 99, "d": 97, "e": 99, "f": 99, "g": 100, "h": 95, "i": 99, "j": 80, "k": 87, "l": 95,
         "m": 97, "n": 92, "o": 94, "p": 98, "q": 76, "r": 95, "s": 99, "t": 95, "u": 84, "v": 96, "w": 93, "x": 81}

urls = []
skills = []

for key,value in index.items():
    for i in range(1,value+1):
        urls.append("https://www.linkedin.com/directory/topics-"+str(key)+"-"+str(i)+"/")

urls.append("https://www.linkedin.com/directory/topics-y/")
urls.append("https://www.linkedin.com/directory/topics-z/")

client = requests.Session()

HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

html = client.get(HOMEPAGE_URL).content
soup = BeautifulSoup(html,"lxml")
csrf = soup.find(id="loginCsrfParam-login")['value']

login_information = {
    'session_key':'EMAIL_ID',
    'session_password':'PASSWORD',
    'loginCsrfParam': csrf,
}

client.post(LOGIN_URL, data=login_information)

for url in urls:
    print "Crawling: "+str(url)
    response = client.get(url)
    parse_response = BeautifulSoup(response.content,"lxml")
    parse_class = parse_response.find("ul",{"class":"column quad-column"})
    for anchor in parse_class.findAll("a"):
        skills.append(anchor.text)

f = open("output/skills.txt","w")
for skill in skills:
    f.write(skill)
    f.write("\n")