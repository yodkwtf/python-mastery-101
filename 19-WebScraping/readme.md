## Web Scraping

Web Scraping means programmatically grabbing data from a web page

Three steps: Download, extract data by parsing the html received, use that data

#### Why Scrape?

If a website doesn't provide an APi to work with their data, we can use scraping to get some data off of their website

#### Is it ethical?

- Some websites don't want you to do it, doesn't mean you can't do it.
- Best practice: consult the robots.txt file to see what files are allowed to scraped
- It's not illegal or something, more like they are requesting you not to do it
- If you make too many req, try to time them out
- If you keep on doing it your IP can be blocked

## Beautiful Soup

- Lets us navigate through HTML with python
- Doesn't download HTML - we need requests module for that

```py
from bs4 import BeautifulSoup

html_data = """
some html code returned from the requests module
"""

soup = BeautifulSoup(html_data, "html.parser")
# this will convert the html string into html

# Now we can navigate around the html
print(soup.body) # prints the entire body from html
```

- We have many methods to select specific tags and selectors like _select_ , _find_, _find_all_

The best way to know about these methods is to read the official docs
