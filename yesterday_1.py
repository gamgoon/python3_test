f = open("D:\yesterday.song", 'r')
yesterday_lyric = ""

while 1:
    line = f.readline()
    if not line:
        break
    yesterday_lyric = yesterday_lyric + line.strip() + "\n"

f.close()
n_of_yesterday = yesterday_lyric.upper().count("YESTERDAY")
un_of_yesterday = yesterday_lyric.count("Yesterday")
dn_of_yesterday = yesterday_lyric.count("yesterday")
print("Number of A word 'Yesterday'", n_of_yesterday)
print("Number of A word 'Yesterday'", un_of_yesterday)
print("Number of A word 'yesterday'", dn_of_yesterday)
