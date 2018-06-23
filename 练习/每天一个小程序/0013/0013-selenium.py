#-*-coding:utf-8-*-
#完全模仿浏览器行为,利用第四行的库可以打开一个浏览器，模拟浏览器操作

from selenium import webdriver
import urllib
import re

#一开始存网页源代码的时候编码有问题，以前有过类似的的情况
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#模拟浏览器操作，这也算是处理动态网页通用的方法
def getwholesource(url):
    chrome = webdriver.Chrome()
    chrome.get('http://tieba.baidu.com/p/2166231880')
    #用js把网页拉到最下面，主要目的是触发JS事件使Ajax加载内容（前两天看XSS的时候学了一点JS
    js = "var q=document.documentElement.scrollTop=40000"
    chrome.execute_script(js)
    str1 = chrome.page_source
    return str1

#正则匹配，找出图片的URL
def comp(str1):
    #发现所有图片的URL的长度是一样的，这个正则有点偷懒了，但确实有用
    rere = r'http://.{182}\.jpg'
    compicture = re.compile(rere)
    pictures = re.findall(compicture,str1)
    return pictures

#最后利用urlbin.urlretrieve方法下载图片
def main():
    pic = comp(getwholesource('http://tieba.baidu.com/p/2166231880'))
    index = 0
    for i in pic:
        index = index + 1
        urllib.urlretrieve(i, 'pic/%d.jpg' % index)
        print "[+] Saved " + str(index) + ".jpg"

if __name__ == '__main__':
   main()