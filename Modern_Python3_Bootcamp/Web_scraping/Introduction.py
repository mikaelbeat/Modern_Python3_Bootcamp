from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")


print("\n***** Print full html *****\n")
print(soup)


print("\n***** Get body *****\n")
print(soup.body)


print("\n***** Get div in body. Prints only the first one *****\n")
print(soup.body.div)


print("\n***** Search given element *****\n")
print(soup.find("div"))


print("\n***** Search given element *****\n")
print(soup.find("div"))


print("\n***** Search given elements using find_all *****\n")
print(soup.find_all("div"))


print("\n***** Search given attribute *****\n")
print(soup.find(id="first"))


print("\n***** Search given elements using find_all *****\n")
print(soup.find_all(class_="special"))


print("\n***** Search given argument name *****\n")
print(soup.find_all(attrs={"data-example": "yes"}))

