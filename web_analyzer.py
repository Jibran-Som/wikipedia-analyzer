import requests 
from bs4 import BeautifulSoup 
import matplotlib.pyplot as plt
import re

def remove_non_letters(input_string):
    return re.findall(r'\b\w+\b', input_string)



url = "https://en.wikipedia.org/wiki/University_of_Calgary" 

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; WebAnalyzer/1.0)"
}

try: 
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    num_of_h1 = len(soup.find_all("h1"))
    print("Number of h1 tags:", num_of_h1)


    print(f"Successfully fetched content from {url}") 
except Exception as e: 
    print(f"Error fetching content: {e}")

num_of_h1 = soup.find_all("h1")
num_of_h2 = soup.find_all("h2")
num_of_h3 = soup.find_all("h3")
num_of_h4 = soup.find_all("h4")
num_of_h5 = soup.find_all("h5")
num_of_h6 = soup.find_all("h6")

num_of_links = soup.find_all("a")
num_of_paragraphs = soup.find_all("p")


num_of_headers = len(num_of_h1) + len(num_of_h2) + len(num_of_h3) + len(num_of_h4) + len(num_of_h5) + len(num_of_h6)


print(f'h1: {len(num_of_h1)}\n')
print(f'h2: {len(num_of_h2)}\n')
print(f'h3: {len(num_of_h3)}\n')
print(f'h4: {len(num_of_h4)}\n')
print(f'h5: {len(num_of_h5)}\n')
print(f'h6: {len(num_of_h6)}\n')

print(f'a: {len(num_of_links)}\n')

print(f'p: {len(num_of_paragraphs)}\n')


user_input = str(input("Enter word you would like to find: "))

data = soup.get_text()

print(f'Number of occurences: {data.lower().count(user_input.lower())}')

filtered_data = remove_non_letters(data.lower())

check_vals = []
word_dict = {}


for i in filtered_data:
    if i not in check_vals:
        check_vals.append(i)
        word_dict.setdefault(i, filtered_data.count(i))

sorted_dict = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse=True))

x=0
print("\nMost frequent words:")
for i in sorted_dict:
    print(f'{i}: {word_dict[i]}')
    x += 1
    if(x == 5):
        break

paragraphs = soup.find_all('p')
para_to_text = []

for i in paragraphs:
    para_to_text.append(i.get_text())

max_para = 0
max_para_len = 0

for i in para_to_text:
    if len(i.split(" ")) > max_para_len:
        max_para_len = len(i.split(" "))
        max_para = i

print(f'\nLargest Paragraph: {max_para} \nLength of paragraph: {max_para_len}')

labels = ['Headings', 'Links', 'Paragraphs']
values = [num_of_headers, len(num_of_links), len(num_of_paragraphs)]

bar_colors = ['tab:blue', 'tab:green', 'tab:red']


plt.bar(labels, values, color=bar_colors)
plt.title('Group 13')
plt.ylabel('Count')
plt.savefig("output.png")