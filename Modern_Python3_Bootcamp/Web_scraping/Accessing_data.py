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

element = soup.select(".special")[0]


print("\n***** get_text *****\n")
print(element.get_text())


print("\n***** get_text from given elements*****\n")
for element in soup.select(".special"):
    print(element.get_text())
    
    
print("\n***** Get element name *****\n")
print(element.name)


print("\n***** Get element attributes *****\n")
print(element.attrs)


print("\n***** Get specific element attribute *****\n")
print(soup.find("h3")["data-example"])


print("\n***** Get specific element attribute *****\n")
print(soup.find("div")["id"])