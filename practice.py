# import re
# from bs4 import BeautifulSoup
# import json
# import urllib
# import xml.etree.ElementTree as ET
#
# #BeautifulSoup Example + NEED EXAM EXAMPLE
#
# url = 'http://www-personal.umich.edu/~collemc/206Exam/examhtml.html'
#
# request = urllib.request.urlopen(url).read()
# print(type(request))
# soup = BeautifulSoup(request, 'html.parser')
# print(type(soup))
# tags = soup('a')
# print(type(tags))
# d = {}
# for a in tags:
#     hyperlink = a.get('href', 'None')
#     print(type(hyperlink))
#     if len(hyperlink) == 0:
#         hyperlink = 'Empty'
#     if hyperlink not in d:
#         d[hyperlink] = 0
#     d[hyperlink] += 1
# sorted_d = sorted(d.items(), key = lambda x: x[1], reverse = True)
# for a in sorted_d:
#     print(a[0] + ':' + str(a[1]))
#
#
# RegEx Example
#
# fname = 'mbox-short.txt'
# f = open(fname, 'r')
# data = f.read()
#
# l = re.findall('[a-zA-Z0-9]+@\S+[a-zA-Z]', data)
# new_l = set(l)
# newer_l = list(new_l)
# for a in newer_l:
#     print(a)
#
# # XML Example 1
#
# data = '''
# <person>
#   <name>Chuck</name>
#   <phone type="intl">
#      +1 734 303 4456
#    </phone>
#    <email hide="yes"/>
# </person>
# '''
#
# tree = ET.fromstring(data)
# print('Name:', tree.find('name').text)
# print('Attr:', tree.find('email').get('hide'))
#
# # XML Example 2
#
# url = input('Enter URL: ')
# xml = urllib.request.urlopen(url)
# data = xml.read()
# doc = data.decode()
#
# tree = ET.fromstring(doc)
# results = tree.findall('.//comment')
# sum = 0
# for a in results:
#     sum += int(a.find('count').text)
# print(sum)
#
# # JSON Example
#
# import json
# import requests
# url = input('Enter URL: ')
# yerd = urllib.request.urlopen(url)
# data = yerd.read().decode()
#
# data = json.loads(data)
# sum = 0
# for a in data['comments']:
#     for b in a:
#         if b == 'count':
#             sum += int(a['count'])
# print(sum)

d = 1
d = a{d}
print(d)
