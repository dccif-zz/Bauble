import urllib
from urllib import request
import re
TargetUrl = "http://www.zdfans.com/"
sock = urllib.request.urlopen(TargetUrl)
htmlSource = sock.read()
htmlSource = htmlSource.decode('utf-8')
sock.close()

print("Open tags:")
print(re.findall(r"<[^/][^>]*[^/>]>",htmlSource)[0:6])
print("Close tags:")
print(re.findall(r"</[^>]+>",htmlSource)[0:3])
print("self-closing tags:")
print(re.findall(r"<[^>/]+/>",htmlSource)[0:3])

for hyperlink1 in re.findall(r"<a\s[\s\S]+?</a>",htmlSource):
    print(hyperlink1)

for hyperlink2 in re.findall(r"<a(?=\s)[^>]*(?<=\s)href\s*=\s*[\"']?([^\"'\s]+)[\"']?[^>]*?>([^<]+)</a>",htmlSource):
    print(hyperlink2[1],hyperlink2[0])

# for headtitle in re.findall(r"<head>([^<]+?)</head>",htmlSource):
#     print(headtitle.group())
print(re.sub("((\\d{4})-(\\d{2})-(\\d{2}))",r"\1","2010-12-22"))
