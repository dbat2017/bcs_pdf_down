# coding = UTF-8

import urllib.request
import re
import os
import requests


url = "https://bcs.qianxin.com/2020/pptdown.html"
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
response.close()
#print(html)

all_data_1 = re.compile("<!-----8月7日--->(.*?)</table>", re.S)
tu_0 = ''.join(all_data_1.findall(html))
#print(tu_0)

all_data_2 = re.compile("<tr>(.*?)<a href", re.S)
tu_1 = ''.join(all_data_2.findall(tu_0))
#print(tu_1)


tu_2 = re.findall("<td>(.*?)</td>", str(tu_1))
#print(tu_2)
len_lst = len(tu_2)
len_lst_1 = int(len_lst/2)
#print(len_lst_1)

title = [0 for i in range(len_lst_1)]
author = [0 for i in range(len_lst_1)]
title_all = [0 for i in range(len_lst_1)]
#position = [0 for i in range(len_lst_1)]
#print(title)

for i in range(len_lst_1):
    j = i*2+1
    title[i] = tu_2[j]

for i in range(len_lst_1):
    j = i*2
    all_data_3 = re.compile("(.*?)<br>", re.S)
    author[i] = ''.join(all_data_3.findall(tu_2[j]))

for i in range(len_lst_1):
    j = str(i+1)
    title_all[i] = j + '_' + title[i] + '_' + author[i]
    title_all[i] = re.sub('[\/:*?"<>|]','-',title_all[i])


#print(title_all)
#len_1 = len(title_all)
#print(len_1)



url_reg = r'(?:href|HREF)="?((?:https://)?.+?\.pdf)'
url_re = re.compile(url_reg)
url_lst = url_re.findall(html)

#len_lst = len(url_lst)
#print(url_lst)
#print(len_lst)


a = os.path.exists('2020_BCS_PPT')
if a:
    print('2020_BCS_PPT文件夹已存在！')
else:
    print('2020_BCS_PPT文件夹不存在，已创建！')
    os.mkdir('2020_BCS_PPT')
#chdir修改当前工作路径
os.chdir(os.path.join(os.getcwd(), '2020_BCS_PPT'))

point = 0

for url in url_lst:
    r = requests.get(url)
    name = title_all[point]
    point = point + 1 
    filename = name + ".pdf"
    with open(filename, 'wb+') as f:
        f.write(r.content)
    print(filename + '下载完成！')




