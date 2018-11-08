try:
    # For Python 3.0 and later
    from urllib.request import Request, urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import Request, urlopen

#import urllib2
from bs4 import BeautifulSoup
import requests
import os

#Asks users what they might want to scrap
SearchTerm = str(input("What do you want to scrap?: "))
SearchTermFilename = SearchTerm.replace(" ", "_")
SearchTermURL = SearchTerm.replace(" ", "%20")


Masterfilename = "./ScrapedImages/"+str(SearchTermFilename)

print(SearchTerm)
print(SearchTermFilename)
print(SearchTermURL)

#--------------------------------------------------------------------------------
URL = 'https://www.google.com/search?q='+str(SearchTermURL)+'&source=lnms&tbm=isch'
req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
#print(webpage) # Content

soup = BeautifulSoup(webpage, features="lxml")
#--------------------------------------------------------------------------------

#Creates new Directory based off 'SearchTerm'
SearchTerm = SearchTerm.replace("%20", "_")
if not os.path.exists("./ScrapedImages/"+str(SearchTermFilename)):
    os.makedirs("./ScrapedImages/"+str(SearchTermFilename))


#if not os.path.exists("./ScrapedImages/"+str(SearchTerm)+"'s"):		--> Plural form
#    os.makedirs("./ScrapedImages/"+str(SearchTerm)+"'s")			--> Plural form


count = 1
for link in soup.select("img[src^=http]"):
        count = count + 1
        lnk = link["src"]
        print(lnk)
#        filename = "./ScrapedImages/"+str(SearchTerm)+"'s/"+str(SearchTerm)+"_"+str(count)+".jpg"    --> Plural form
        filename = str(Masterfilename)+"/"+str(SearchTermFilename)+"_"+str(count)+".jpg"

        with open(filename,"wb") as f:
            f.write(requests.get(lnk).content)