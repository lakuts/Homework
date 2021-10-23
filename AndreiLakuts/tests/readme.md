For the correct tests work current folder has to contain subfolder "cache"
with the file "rss_reader_cache.json" with such content: 

    [
       {
          "https://news.yahoo.com/rss/": [
             {
                "Title": "Test Title",
                "Link": "https://test.link.com/test.html",
                "PubDate": "20211022",
                "Source": "Test Source"
             }
          ]
       }
    ]
    
If such folder doesn't exist it will be created after tests the first running.