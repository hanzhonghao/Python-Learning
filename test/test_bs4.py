from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time the re were three little sisters; and their names were
<a href="www.baidu.com" class="sister" id="link1">Elsie</a>,
<a href="www.qq.com" class="sister" id="link2">Lacie</a> and
<a href="www.weixin.com" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup =BeautifulSoup(html_doc,'html.parser')
print("获取所有的链接")
links =soup.find_all('a');
for link in links:
    print(link.name,link['href'],link.get_text())
