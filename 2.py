import urllib.request
url="https://royallib.com/book/pelevin_viktor/chapaev_i_pustota.html"
with urllib.request.urlopen(url) as webpage:
    for line in webpage:
    line = line.strip()
    line = line.decode('utf-8') # преобразуем тип bytes в utf-8
    print(line)    
