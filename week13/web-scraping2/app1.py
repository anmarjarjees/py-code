import requests
from bs4 import BeautifulSoup
# A data structure representing a parsed HTML or XML document.

url = "https://www.health.harvard.edu/blog"

# (variable) res: Response
res = requests.get(url)

# print(res)

# Link: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

"""
Examples:
> BeautifulSoup(html_doc, 'html.parser')
> BeautifulSoup(res.content, 'html.parser')
> BeautifulSoup(res.text, 'lxml') <=> we need to pip install lxml if we want to use it (next example)
"""
soup = BeautifulSoup(res.content, 'html.parser' )

# print(soup.title)

# print(soup.title.name)

# print(soup.title.parent.name)

# getting the headings of the blogs
"""
<h2 class="text-2xl font-bold mb-1 leading-tight mt-2 group-hover:text-red group-focus:text-red transition-colors duration-200">
Preventable liver disease is rising: What you eat — and avoid — counts
</h2>
"""

# find() => find the first PageElement that matches the given criteria.
heading = soup.find('h2',class_="text-2xl")
# print(heading)
# print(heading.text)

headings = soup.find_all('h2', class_='text-2xl')
# print(headings)

# print("Main Headings:")
# for heading in headings:
#     print(heading.text)

"""
<div class="prose mt-4">
    <p>
    In the last ten years, an average of four drug recalls a day have occurred in the US. Drug recalls happen for a number of different reasons, and while they are common, most are not for dangerous or life-threatening issues.
    </p>
</div>
"""
# pars = soup.find_all('p')

div = soup.find('div', {'class': 'prose'})
# findChildren() returns a list of the p elements (but we only have one!)
children = div.findChildren('p')

# print(children)

# for child in children:
#     print(child)

# Task: get all the div that contains the post paragraphs:
div_list=soup.find_all('div', {'class' : 'prose'})
# for div in div_list:
#     print (div)

# Task: print only the paragraph elements inside the all divs that contain the post paragraphs:
# for div in div_list:
#     print (div.findChild('p'))

# Task: Select only the paragraph elements inside the all divs that contain the post paragraphs:
p_list = soup.select('div.prose p')
print(type(p_list)) # <class 'bs4.element.ResultSet'>

# for p in p_list:
#     print (p)

# Task: print the contents of each p element
# for p in p_list:
#     # (variable) contents: list[PageElement]
#     print ("\n",p.contents)
""" 
The output of only one iteration:
[
    'Children with neurodevelopmental disabilities like autism spectrum disorder, ADHD, and intellectual disabilities may need extra support in building friendships and participating in social activities. Parents and other adults can help children 
    develop their social and emotional skills.'
]
"""

# for p in p_list:
#     # (variable) contents: list[PageElement]
#     print ("\n",p.contents[0])

"""
Children with neurodevelopmental disabilities like autism spectrum disorder, ADHD, and intellectual disabilities may need 
extra support in building friendships and participating in social activities. Parents and other adults can help children develop their social and emotional skills.
"""

# **********************
# Or even much much easier! :-) :-)
for p in p_list:
    # (variable) contents: list[PageElement]
    print ("\n",p.text)


