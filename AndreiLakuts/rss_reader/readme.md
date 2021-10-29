#RSS-reader.

##Version 1.4

Author: Andrei Lakuts

RSS reader is a command-line utility which receives RSS URL 
and prints results to stdout. 

During execution, program creates a "cache" folder with "rss_reader_cache.json" file. 
In this file it saves news from the RSS-feed. Inside the cache folder, the program creates 
a subfolder "image_cache", into which it saves images, if they are in the RSS-feed.

##Program runs on pure Python and doesn't require installation of additional modules. 

##Installation:

You can install rss_reader as CLI-utility from "dist" folder in your Python environment like this:

In OS Windows:

   - pip install rss_reader-1.4.zip
   
In OS Linux:

   - pip install rss_reader-1.4.tar.gz

Program also works without installation.



##Usage: 

rss_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT] [--date DATE] 
                                                             [--to_html TO_HTML] [--to_fb2 TO_FB2] [source]

Pure Python command-line RSS reader.

positional arguments:

    source         RSS URL

optional arguments:

     -h, --help     show this help message and exit
     --version      Show program version and exit
     --json         Print result as JSON in stdout
     --verbose      Outputs verbose status messages
     --limit LIMIT  Limit (int) news topics if this parameter provided
     --date DATE    Date (str) in format YYYYMMDD. Print news from cache for this date
     --to_html TO_HTML  Path to folder where news will be saved in file rss_news.html
     --to_fb2 TO_FB2    Path to folder where news will be saved in file rss_news.fb2
     
-------------------------------------------------------------------------------------------------

###Example 1.  

If --limit (int) is specified the same amount of news will be printed. 

If --limit is not specified or is larger than feed size then all available news will be printed:

   - if program is installed
#####rss_reader https://www.theguardian.com/uk/rss --limit 2

   - if program is not installed
#####python rss_reader.py https://www.theguardian.com/uk/rss --limit 2

Feed: The Guardian

Description: Latest news, sport, business, comment, analysis and reviews from the Guardian, the world's leading liberal voice

Link: https://www.theguardian.com/uk

Language: en-gb


News 1

Title: Cop26: Humanity 5-1 down at half-time on climate crisis, says Johnson

Link: https://www.theguardian.com/environment/2021/oct/29/cop26-humanity-5-1-halftime-climate-crisis-boris-johnson

PubDate: 20211029

Source: None

ImageLink: https://i.guim.co.uk/img/media/ca4e9cd673e14879cfa3b6897efd5c52ba28aa51/0_45_1841_1105/master/1841.jpg?width=140&quality=85&auto=format&fit=max&s=8d309a4907bef4d4f48b106ae7998a41

ImageCacheName: httpswwwtheguardiancomenvironment2021oct29cop26humanity51halftimeclimatecrisisborisjohnson.jpg


News 2

Title: The Queen advised to rest for two weeks, says Buckingham Palace

Link: https://www.theguardian.com/uk-news/2021/oct/29/the-queen-advised-to-rest-for-two-weeks-says-buckingham-palace

PubDate: 20211029

Source: None

ImageLink: https://i.guim.co.uk/img/media/87f1e1696d36b0f472a6b60a2948f9362df8ff2c/0_21_1512_907/master/1512.jpg?width=140&quality=85&auto=format&fit=max&s=4c40b60fd64069fae7e1456ccf6b4d51

ImageCacheName: httpswwwtheguardiancomuknews2021oct29thequeenadvisedtorestfortwoweekssaysbuckinghampalace.jpg

-------------------------------------------------

###Example 2.  

If --version is specified program prints prints its version and stops:

   - if program is installed
#####rss_reader --version
   
   - if program is not installed
#####python rss_reader.py --version

"Version 1.4" 

-------------------------------------------------
###JSON format description:

    {
       "Feed": "RSS-feed title.",
       "Description": "RSS-feed description.",
       "Link": "RSS-feed URL",
       "Language": "RSS-feed language.",
       "News": [
          {
             "Title": "News titler",
             "Link": "News URL",
             "PubDate": "News publication date",
             "Source": "News source"
             "ImageLink": "Link to image file",
             "ImageCacheName": "Filename in local cache"

          },
           ...
           ...
           ...
       ]
    }

###Example 3.  

If --json is specified program prints news to stdout in JSON format:

   - if program is installed
#####rss_reader https://news.yahoo.com/rss --limit 2 --json

   - if program is not installed
#####python rss_reader.py https://news.yahoo.com/rss --limit 2 --json

    {
       "Feed": "Yahoo News - Latest News & Headlines",
       "Description": "The latest news and headlines from Yahoo! News. Get breaking news stories and in-depth coverage with videos and photos.",
       "Link": "https://www.yahoo.com/news",
       "Language": "en-US",
       "News": [
          {
              "Title": "Asian spider takes hold in Georgia, sends humans scurrying",
              "Link": "https://news.yahoo.com/asian-spider-takes-hold-georgia-134321868.html",
              "PubDate": "20211029",
              "Source": "Associated Press",
              "ImageLink": "https://s.yimg.com/uu/api/res/1.2/Yi6.JOnBe81VmNVIAkmz3w--~B/aD0yMzYwO3c9MzU0MjthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/7019fdea85ace2b1d54dc4dff4f3db33",
              "ImageCacheName": "httpsnewsyahoocomasianspidertakesholdgeorgia134321868html.jpg"
          },
          {
              "Title": "Fully vaccinated people can pass on the Delta variant at home, including to other vaccinated people, a study finds - but unvaccinated people are still at most risk",
              "Link": "https://news.yahoo.com/fully-vaccinated-people-pass-delta-123654331.html",
              "PubDate": "20211029",
              "Source": "Business Insider",
              "ImageLink": "https://s.yimg.com/uu/api/res/1.2/fJ9Pc.rrjR3_Au7r3HSOig--~B/aD0zNDEyO3c9NDU1MDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/business_insider_articles_888/1d9142b5ea160c9f3d661fc481a78a2f",
              "ImageCacheName": "httpsnewsyahoocomfullyvaccinatedpeoplepassdelta123654331html.jpg"
          }
       ]
    }
    
-------------------------------------------------------------------------------------------------

##Example 4.  

If --verbose is specified program prints logs to stdout:

   - if program is installed
#####rss_reader https://news.yahoo.com/rss --limit 1 --verbose
   
   - if program is not installed
#####python rss_reader.py https://news.yahoo.com/rss --limit 1 --verbose

Start program.

RssParser Class object was created.

Method 'run_parsing' is working:

'run_parsing' method calls 'get_content' method:

Method 'get_content' is working:

Trying to get content from RSS source: https://news.yahoo.com/rss ...

Content of the RSS-source has been received successfully.

There are 50 news in the feed.

Method 'get_content' is finished.

'run_parsing' method calls 'process_content' method:

Method 'process_content' is working:

Adding data to the work dict 'rss_feed'...

1 news were added.

Method 'process_content' is finished.

'run_parsing' method calls 'save_news_to_cache' method:

Method 'save_news_to_cache' is working:

Saving news to cache...

Cache file does not exist, a new one will be created.

Method 'save_image_to_image_cache' is working:

Saving image to image_cache...

Image was saved successfully.

Method 'save_image_to_image_cache' is finished.

News were added to cache successfully.

Method 'save_news_to_cache' is finished.

'run_parsing' method calls 'print_content' method:

Method 'print_content' is working:

Print information about RSS-feed:

Feed: Yahoo News - Latest News & Headlines

Description: The latest news and headlines from Yahoo! News. Get breaking news stories and in-depth coverage with videos and photos.

Link: https://www.yahoo.com/news

Language: en-US


1 news will be shown:

News 1
Title: Asian spider takes hold in Georgia, sends humans scurrying

Link: https://news.yahoo.com/asian-spider-takes-hold-georgia-134321868.html

PubDate: 20211029

Source: Associated Press

ImageLink: https://s.yimg.com/uu/api/res/1.2/Yi6.JOnBe81VmNVIAkmz3w--~B/aD0yMzYwO3c9MzU0MjthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/7019fdea85ace2b1d54dc4dff4f3db33

ImageCacheName: httpsnewsyahoocomasianspidertakesholdgeorgia134321868html.jpg

1 news of 50 are showed.

Method 'print_content' is finished.

Program execution completed!

-------------------------------------------------------------------------------------------------

##Example 5.  

If URL is wrong program prints error-message to stdout:

   - if program is installed
#####rss_reader https://news.yahoo.m/rss   
   
   - if program is not installed
#####python rss_reader.py https://news.yahoo.m/rss

Exception <urlopen error [Errno 11001] getaddrinfo failed> - wrong URL! The program is stopped.

-------------------------------------------------------------------------------------------------

At runtime, the program saves data to the local cache in JSON-file "rss_reader_cache.json" in the subfolder "cache".

Cache file structure:

    [
       {
          "https://news.yahoo.com/rss": [
             {
                "Title": "Employee who killed gunman likely saved lives, police say",
                "Link": "https://news.yahoo.com/employee-killed-gunman-likely-saved-211530368.html",
                "PubDate": "20211022",
                "Source": "Associated Press"
             },
             {
                "Title": "A 55-year-old mother of 9 was sentenced to death by hanging over possessing around 4 ounces of meth",
                "Link": "https://news.yahoo.com/55-old-mother-9-sentenced-054433946.html",
                "PubDate": "20211022",
                "Source": "INSIDER"
                "ImageLink": "https://s.yimg.com/uu/api/res/1.2/Yi6.JOnBe81VmNVIAkmz3w--~B/aD0yMzYwO3c9MzU0MjthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/7019fdea85ace2b1d54dc4dff4f3db33",
                "ImageCacheName": "httpsnewsyahoocomasianspidertakesholdgeorgia134321868html.jpg"
             }
             ...
             
             ...
          ]
       }
    ]



##Example 6.  

If --date in format YYYYMMDD is specified, for example "--date 20211023", program gets news from a local cache
for this date:

   - if program is installed
#####rss_reader --date 20211029 --limit 1 
   
   - if program is not installed
#####python rss_reader.py --date 20211029 --limit 1

Title: Asian spider takes hold in Georgia, sends humans scurrying

Link: https://news.yahoo.com/asian-spider-takes-hold-georgia-134321868.html

PubDate: 20211029

Source: Associated Press

ImageLink: https://s.yimg.com/uu/api/res/1.2/Yi6.JOnBe81VmNVIAkmz3w--~B/aD0yMzYwO3c9MzU0MjthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/7019fdea85ace2b1d54dc4dff4f3db33

ImageCacheName: httpsnewsyahoocomasianspidertakesholdgeorgia134321868html.jpg

-------------------------------------------------------------------------------------------------

If --date specified together with RSS source, then program gets news for this date from 
local cache that were fetched from specified source. Parameter --date also works correctly 
with both --json, --limit, --verbose and their different combinations.

-------------------------------------------------------------------------------------------------

##Example 7.  

If --to_html is specified (for example "--to_html D:\html" in Windows, or "--to_html /home/html" in Linux) 
program creates a folder at the specified path and saves news to file rss_news.html in this folder:

   - if program is installed
#####rss_reader https://www.theguardian.com/uk/rss --limit 1 --verbose --to_html html_folder
   
   - if program is not installed
#####python rss_reader.py https://www.theguardian.com/uk/rss --limit 1 --verbose --to_html html_folder


Start program.

RssParser Class object was created.

...

...

...

'run_parsing' method calls 'save_to_html' method:

Method 'save_to_html' is working:

File html_folder\rss_news.html was created successfully.

Method 'save_to_html' is finished.

Program execution completed!


-------------------------------------------------------------------------------------------------


##Example 8.  

If --to_fb2 is specified (for example "--to_fb2 D:\fb2_folder" in Windows, or "--to_fb2 /home/fb2_folder" in Linux) 
program creates a folder at the specified path and saves news to file rss_news.fb2 in this folder:

   - if program is installed
#####rss_reader https://www.theguardian.com/uk/rss --limit 1 --verbose --to_fb2 fb2_folder
   
   - if program is not installed
#####python rss_reader.py https://www.theguardian.com/uk/rss --limit 1 --verbose --to_fb2 fb2_folder


Start program.

RssParser Class object was created.

...

...

...


'run_parsing' method calls 'save_to_fb2' method:

Method 'save_to_fb2' is working:

File fb2_folder\rss_news.fb2 was created successfully.
Method 'save_to_fb2' is finished.

Program execution completed!


-------------------------------------------------------------------------------------------------

You can also use different combinations of parameters
