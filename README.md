
Data wave assignment
Problem1 
To check the implementations please open the folder problem1 and then
First execute key_store_server programm by saying

python key_store_server.py n

where n is number of versions you desire.

And then run key_store_client by executing 

python key_store_client.py

Problem 2
To check how problem2 code works. Please open the problem2 directory and run 

python create_url_dict.py today_file.txt yesterday_file.txt

where today_file.txt and yesterday_file.txt are the locations where today's and yesterday's url file are available.
The folder already has 2 files you can just update those files and run the programm.


Problem 3

To check how problem 3 code works. Please open the problem2 directory and run 

python scrape.py

Which creates to json files.
monitor_details.json which has details of monitors. 
pincheck.json which has details of pin availabilty for given pincodes in assignment.

Note : 1. I have used Json file as a storage to store key-values in problem. Since it was mentioned in assignment doccument
to not to use dictionary or hashmap.

2.In the implementaion of first part of probloem 3. i.e scraping monitor details I have used BeautifulSoup to parse the HTML as 
I think that is the only best way to parse an HTML file. However the second part i.e to check the pincode availability. I have used requests module
to get pincode details by sending get request to url "http://www.shopclues.com/nss.php" which gives me a json format data which gives pincode availability details.

Please review the code. Even if it is a negetive review it doesn't matter. I would love to correct my mistake and learn new things.
Thanks.
