import sys
def form_dict(file1,file2):
	file1_urls = open(file1,'r').read().split("\n")
	file2_urls = open(file2,'r').read().split("\n")
	#combined_urls = file1_urls+file2_urls
	url_dict = {}
	#creates a dict {url:[repeat_count_today,repetead_yesterday_or_not],url2:[repeat_count_today,repetead_yesterday_or_not]}
	url_dict = {ele:[file1_urls.count(ele),(1 if ele in file2_urls else 0)] for ele in file1_urls if not url_dict.has_key(ele)}
	#set(file1_urls)^set(file2_urls) would also give me the repeated urls.But I thought the above method can be time efiicient.
	return url_dict

if __name__ == "__main__" :	
	 #print len(sys.argv)
	 if len(sys.argv) < 3 :
			print "\n \n Please input yesterday and today file names "
			sys.exit(0)
	 today,yday=sys.argv[1],sys.argv[2]
	 dict = form_dict(today,yday)
	 #print dict
	 print "Stats for today"
	 print "URL                     repetions"
	 rep_urls=[]
	 for url,count in dict.items() :
		 print url,count[0]
		 if count[1]==1:
			 rep_urls.append(url)
	
	 print "\nRepeated Urls"
	 print "\n".join(rep_urls)
			