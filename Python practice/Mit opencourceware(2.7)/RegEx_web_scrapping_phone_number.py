# import urllib,re
# f = urllib.urlopen("http://www.example.com")
# s = f.read()
# re.findall(r"\+\d{2}\s?0?\d{10}",s)
# re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)

import urllib.request
from re import findall
url = "https://www.summet.com/dmsi/html/codesamples/addresses.html"
response = urllib.requests.urlopen(url)
response = response.read()
htmlstr = html.decode()
pdata = findall("\(\d{3}\)\d{3}-\d{4}",htmlstr)
for item in pdata:
    print item