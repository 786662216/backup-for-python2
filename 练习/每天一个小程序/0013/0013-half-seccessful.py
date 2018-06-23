#-*-coding:utf-8-*-
#爬取图片
#打开的网页不全，因为网页有动态加载。于是又写了个基于selenium的爬虫，完全模拟浏览器行为
#urllib也算是处理静态网页最容易上手的库了，简单的爬虫用这个最好写

import re
import urllib2
import urllib
import pyquery

#http头，没啥意义
header = {
   'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
   'Connection: Keep-Alive'
   'Referer: http://www.baidu.com'
   'Pragma: no-cache'
   'Accept: application/json, text/javascript, */*; q=0.01'
}

#读取网页
def openURL(url):
   a = urllib2.Request(url = url,headers = header)
   domin = urllib2.urlopen(a)
   content = domin.read()
   return content

#这个正则可能也有问题，但是一开始不全确实是网页代码是动态加载，URLBIL没加载的关系
def comp(str):
   rere = r'src="(.*?\.jpg)" bdwater='
   compicture = re.compile(rere)
   pictures = re.findall(compicture,str)
   return pictures

def main():
   index = 0
   wanna = comp(openURL('http://tieba.baidu.com/p/2166231880'))
   for i in wanna:
      index = index + 1
      urllib.urlretrieve(i,'pic/%d.jpg' % index)
      print "[+] Saved "+ str(index) + ".jpg"

if __name__ == '__main__':
   main()