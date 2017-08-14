# coding:utf-8
import cookielib
import urllib2

url = "https://baike.baidu.com/item/史记·2016?fr=navbar"

print "part 1"

response = urllib2.urlopen(url)
print response.getcode()
print len(response.read())

print "part 2"

request = urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print "part3"
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
print response3.read()
