import urllib.request as req

def getNext(url):
    request = req.Request(url, headers = {
    "cookie":"over18=1",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

        #print(data)

    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    #print(root)
    #print(root.title)
    #<title>看板 Tennis 文章列表 - 批踢踢實業坊</title>
    #print(root.title.string)
    #看板 Tennis 文章列表 - 批踢踢實業坊
    titles = root.find_all("div", class_ = "title") #find those div tags whose class_ = "title"

    for title in titles:
        if title.a != None:
            print(title.a.string)

    next = root.find("a", string = "‹ 上頁") 
    #right click on the button and inspect element then copy and paste from code direcly is better than typing it on urself    
    return next["href"]

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
N = 3
while (count < N):
    url = "https://www.ptt.cc" + getNext(url)
    count += 1
