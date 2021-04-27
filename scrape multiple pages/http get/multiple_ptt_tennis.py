import urllib.request as req
url = "https://www.ptt.cc/bbs/Tennis/index.html"
request = req.Request(url, headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
})

current = 2012
end = 2000
for page in range(current, end, -1):
    print(page)
    url2 = "https://www.ptt.cc/bbs/Tennis/index" + str(page) + ".html"
    #from current to end, because page number on ptt is cumulative
    request2 = req.Request(url2, headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
    })
    with req.urlopen(request2) as response:
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
