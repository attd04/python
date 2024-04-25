from bs4 import BeautifulSoup
# import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# --- how to access different tags and items in html file
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())

# --- finding all items instead of only first
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get('href'))
#
# heading = soup.find(name='h1', id='name') # can do same w/ class attribute

# --- being even more specific;
# company_url = soup.select_one(selector="p a") # same as css selector
# selector one finds only first, select finds all
