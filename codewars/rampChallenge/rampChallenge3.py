from bs4 import BeautifulSoup

# Sample HTML document (replace with your actual HTML)
with open('myHTML.html', 'r') as f:
    html_doc = f.read()

# Parse the HTML document
soup = BeautifulSoup(html_doc, 'html.parser')

# Find all <code> elements with data-class="23*"
code_elements = soup.find_all('code', attrs={'data-class': lambda x: x and x.startswith('23')})

# Initialize an empty list to store the URL characters
url_characters = []

# Iterate through the code elements and extract characters (ignoring asterisks)
for code_element in code_elements:
    # Check for div elements ending in '93'
    div_element = code_element.find('div', attrs={'data-tag': lambda x: x and x.endswith('93')})
    if div_element:
        # Check for span elements containing '21'
        span_element = div_element.find('span', attrs={'data-id': lambda x: x and '21' in x})
        if span_element:
            # Check for char elements with class 'char'
            char_element = span_element.find('i', class_='char')
            if char_element:
                char_value = char_element.get('value')
                if char_value:
                    url_characters.append(char_value)

# Print the extracted URL
print(''.join(url_characters))
