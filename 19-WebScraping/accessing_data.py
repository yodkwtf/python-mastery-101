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

# parse html string to html
soup = BeautifulSoup(html, "html.parser")

# select first element w this class
el = soup.select(".special")[0]

print(el)  # <li class="special">This list item is special.</li>
print(el.get_text())  # This list item is special.
print(el.name)  # li
print(el.attrs)  # {'class': ['special']}
