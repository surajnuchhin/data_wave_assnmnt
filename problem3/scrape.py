import requests
from BeautifulSoup import BeautifulSoup
import json
headers = {'Accept-Encoding': 'identity'}
html = requests.get("http://www.shopclues.com/computers/desktops-and-monitors/monitors.html",headers).text # get html of link
html = BeautifulSoup(html)
divs = html.findAll("div",{"class":"grid-product special category_grid_4 "}) # get the divisons of all products
product_details = {}
for div in divs :  # for each product grid
	product_id = div.find("input",{'type':'hidden'})['id'] # scrape the data and insert it to update it to a dictionary
	img = div.find("img")
	title = img['title']
	thumb_nail = ""
	if img.has_key('src') :
		thumbnail = img['src']
	url = div.find("a")['href']
	discount = div.find("label" )
	price = "".join(div.find("span",{'class':'price'}).findAll(text=True))
	if discount != None :
			discount = "".join(discount.findAll(text=True))
	product_details[product_id] = {'title':title,'url':url,'thumbnail':thumbnail,'price':price,'discount':discount}
	
print "Scraped details of ",len(product_details)," monitors"

monitor_details = open("monitors_details.json","w") # open json file
monitor_details.write(json.dumps(product_details)) # write to json file

# to check the pincode availability
pin_check = {}
for monitor in product_details.keys()[:10] :
	#print monitor
	pin_check[monitor]={}
	pincodes = ['560070', '575001','671551']
	for pin in pincodes :
		pin_check_url = "http://www.shopclues.com/nss.php?pincode_no=%s&product_ids=%s"%(pin,monitor) # this is where you can get the pincode availability
		json_r = json.loads(requests.get(pin_check_url).content)
		#print json_r
		if json_r['pin_result'] != 0 : # if pin result!=0 then the pin code is available for delivery
			available = "yes"
			cash_on_delivery =  'available' if json_r['pin_result'] == 3 else 'unavailable' # cash on delivary is available only if pin_result is 3
			from_date = json_r['fdate']
			to_date = json_r['sdate']
			pin_check[monitor][pin] = {'available':available,'from_date':from_date,'to_date':to_date,'cas_on_delivery':cash_on_delivery} # form a dict of all values
		else :
			pin_check[monitor][pin] = {'available':"no"}
			
	pin_file = open('pincheck.json',"w")
	pin_file.write(json.dumps(pin_check)) # write it into a json file
		#print json_r['pin_result']
		