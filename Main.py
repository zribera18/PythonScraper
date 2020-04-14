import requests, re, sqlite3 

print "hi"


r = requests.get('https://www.tactics.com/burton/cartel-snowboard-bindings/black', 0)

title = re.findall(r'<meta name="description" content="(.*?)">', r.text)

price = re.findall(r'\'price\':(.*?)\}', r.text)

brand = re.findall(r'\'brand\':(.*?),', r.text)
print "title:" + str(title)
print "price:" + str(price)

print "brand:" + str(brand)