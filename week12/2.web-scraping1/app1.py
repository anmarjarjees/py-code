# For full comments and details, please refer to 
# Import the requests library: 
# Link: https://github.com/anmarjarjees/py-web-scraping
"""
NOTE: 
If you get the error: "requests" could not be resolved from source Pylance"
From Select the Interpreter (you can click it from the VS Code status bar)
> Make sure to select the recommended settings for the current VENV Interpreter
> Don't select the global python interpreter
"""
import requests 
from bs4 import BeautifulSoup

# url = "https://www.heartandstroke.ca/healthy-living"
# Error 203 => Forbidden

url = "https://www.health.harvard.edu/blog"
# Ok 202

# url = "https://www.pluralsight.com/blog/technology"
# url = "https://www.freecodecamp.org/news/"


res = requests.get(url)
# print(res)

"""
Examples:
> BeautifulSoup(html_doc, 'html.parser')
> BeautifulSoup(res.content, 'html.parser')
> BeautifulSoup(res.text, 'lxml') <=> we need to pip install lxml if we want to use it (next example)
"""
soup = BeautifulSoup(res.content,'html.parser')
print(type(soup))

heading = soup.find('h2')
print(heading) # <h2 class="heading-subtle text-xs mb-2">Main Content</h2>

headings = soup.find_all('h2')
print(headings)

"""
<h2 class="text-2xl fo nt-bold mb-1 leading-tight mt-2 group-hover:text-red group-focus:text-red transition-colors duration-200">Drug recalls are common</h2>
"""

headings = soup.find_all('h2', class_='text-2xl')
print(headings)