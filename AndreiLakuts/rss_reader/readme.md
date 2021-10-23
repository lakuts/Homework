#RSS-reader.

##Version 1.3

Author: Andrei Lakuts

RSS reader is a command-line utility which receives RSS URL 
and prints results to stdout. 

##Program runs on pure Python and doesn't require installation of additional modules. 

##Installation:

You cal install rss_reader as CLI-utility from "dist" folder in your Python environment like this:

In OS Windows:

   - pip install rss_reader-1.3.zip
   
In OS Linux:

   - pip install rss_reader-1.3.tar.gz

Program also works without installation.



##Usage: 

rss_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT] [--date DATE] [source]

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

-------------------------------------------------------------------------------------------------

###Example 1.  

If --limit (int) is specified the same amount of news will be printed. 
If --limit is not specified or is larger than feed size then all available news will be printed:

   - if program is installed
#####rss_reader https://news.yahoo.com/rss --limit 2

   - if program is not installed
#####python rss_reader.py https://news.yahoo.com/rss --limit 2

Feed: Yahoo News - Latest News & Headlines

Description: The latest news and headlines from Yahoo! News. Get breaking news stories and in-depth coverage with videos and photos.

Link: https://www.yahoo.com/news

Language: en-US

News 1

Title: Now 41, killer of 4-year-old boy granted parole on 11th try

Link: https://news.yahoo.com/now-41-killer-4-old-143242635.html

PubDate: 2021-10-16T14:32:42Z

Source: Associated Press


News 2

Title: How Sarah Baartman's hips went from a symbol of exploitation to a source of empowerment for Black women

Link: https://news.yahoo.com/sarah-baartmans-hips-went-symbol-122627107.html

PubDate: 2021-10-16T14:43:32Z

Source: The Conversation

-------------------------------------------------

###Example 2.  

If --version is specified program prints prints its version and stops:

   - if program is installed
#####rss_reader --version
   
   - if program is not installed
#####python rss_reader.py --version

"Version 1.3" 

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
             "Title": "Now 41, killer of 4-year-old boy granted parole on 11th try",
             "Link": "https://news.yahoo.com/now-41-killer-4-old-143242635.html",
             "PubDate": "2021-10-16T14:32:42Z",
             "Source": "Associated Press"
          },
          {
             "Title": "Hooters employees are pushing back against new revealing uniforms that include shorts so short that they're 'like underwear'",
             "Link": "https://news.yahoo.com/hooters-employees-pushing-back-against-155622068.html",
             "PubDate": "2021-10-16T15:56:22Z",
             "Source": "Business Insider"
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

Trying to get content from RSS source: https://news.yahoo.com/rss/ ...

Content of the RSS-source has been received successfully.

Tere are 50 news in the feed.

Method 'get_content' is finished.


'run_parsing' method calls 'process_content' method:

Method 'process_content' is working:
Adding data to the work dict 'rss_feed'...
1 news were added.
Method 'process_content' is finished.

'run_parsing' method calls 'print_content' method:

Method 'print_content' is working:

Print information about RSS-feed:

Feed: Yahoo News - Latest News & Headlines

Description: The latest news and headlines from Yahoo! News. Get breaking news stories and in-depth coverage with videos and photos.

Link: https://www.yahoo.com/news

Language: en-US


1 news will be shown:

News 1

Title: Now 41, killer of 4-year-old boy granted parole on 11th try

Link: https://news.yahoo.com/now-41-killer-4-old-143242635.html

PubDate: 2021-10-16T14:32:42Z

Source: Associated Press

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
             }
             ...
             
             ...
          ]
       }
    ]



##Example 6.  

If --date in format YYYYMMDD is specified, for example "--date 20211023", program gets news from a local cache
for :

   - if program is installed
#####rss_reader --date 20211023 --limit 1 
   
   - if program is not installed
#####python rss_reader.py --date 20211023 --limit 1

Title: Every Day, Biden Smells Like More of a Loser
Link: https://news.yahoo.com/every-day-biden-smells-more-033653915.html
PubDate: 20211023
Source: The Daily Beast


-------------------------------------------------------------------------------------------------

If --date specified together with RSS source, then program gets news for this date from 
local cache that were fetched from specified source. Parameter --date also works correctly 
with both --json, --limit, --verbose and their different combinations.
