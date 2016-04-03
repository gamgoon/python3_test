from urllib.request import urlopen

file = urlopen('http://www.korea.kr')
htmlcontents = file.read()
print(htmlcontents)
