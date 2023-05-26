# from bs4 import BeautifulSoup

# # Read the HTML file
# file_path = r'D:\website\asuslaptop.html'
# with open(file_path, 'r') as file:
#     html_content = file.read()

# # Parse the HTML content
# soup = BeautifulSoup(html_content, 'html.parser')

# # Scrape the ratings and comments
# feedback_entries = soup.find_all('div', class_='feedback-entry')

# for entry in feedback_entries:
#     stars_element = entry.find('div', class_='rating')
#     username_element = entry.find('div', class_='username')
#     comment_element = entry.find('div', class_='comment-form')

#     stars = stars_element.text.strip() if stars_element else None
#     username = username_element.text.strip() if username_element else None
#     comment = comment_element.text.strip() if comment_element else None

#     print(f"Stars: {stars}")
#     print(f"Username: {username}")
#     print(f"Comment: {comment}")
#     print("----------------------")

from bs4 import BeautifulSoup

# Read the HTML file
with open('G:\MUKESH\py_project\e_commerce\demo\SwiftBuy_Website\\asuslaptop.html', 'r') as file:
    html_data = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_data, 'html.parser')

# Find the feedback entries
feedback_entries = soup.find_all('div', class_='feedback-entry')

# Scrape the values for each feedback entry
feedback_data = []
for entry in feedback_entries:
    stars_element = entry.find('div', class_='stars')
    username_element = entry.find('div', class_='username')
    comment_element = entry.find('div', class_='comment')

    stars = stars_element.get_text() if stars_element else None
    username = username_element.get_text().replace('Username: ', '') if username_element else None
    comment = comment_element.get_text().replace('Comment: ', '') if comment_element else None

    feedback_data.append({'Stars': stars, 'Username': username, 'Comment': comment})

# Print the scraped data
for feedback in feedback_data:
    print('Stars:', feedback['Stars'])
    print('Username:', feedback['Username'])
    print('Comment:', feedback['Comment'])
    print()
