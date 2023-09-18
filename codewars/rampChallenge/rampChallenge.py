from bs4 import BeautifulSoup

# Your HTML content (replace with your actual HTML content)
html_content = """
<code data-class="23*">
  <div data-tag="*93">
    <span data-id="*21*">
      <i class="char" value="V"></i>
    </span>
  </div>
</code>
<code data-class="23*">
  <div data-tag="*93">
    <span data-id="*21*">
      <i class="char" value="A"></i>
    </span>
  </div>
</code>
<code data-class="23*">
  <div data-tag="*93">
    <span data-id="*21*">
      <i class="char" value="L"></i>
    </span>
  </div>
</code>
<code data-class="23*">
  <div data-tag="*93">
    <span data-id="*21*">
      <i class="char" value="I"></i>
    </span>
  </div>
</code>
"""

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Initialize an empty string to store the URL
hidden_url = ""

# Find all matching elements and extract the VALID_CHARACTER
for code in soup.find_all('code', data_class="23*"):
    i_element = code.find('i', class_="char")
    if i_element and 'value' in i_element.attrs:
        hidden_url += i_element['value']

# Print the hidden URL
print("Hidden URL:", hidden_url)
