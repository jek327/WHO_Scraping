import requests
from bs4 import BeautifulSoup
import json
import os

# STEP 1: Your new WHO Q&A topic URL
url = "https://www.who.int/news-room/questions-and-answers/item/long-term-studies-on-children-s-health-and-the-environment-how-can-we-identify-assess-and-follow-up-the-effects-of-exposure-to-environmental-factors"

# STEP 2: Scrape questions from the page
response = requests.get(url, headers={"Accept": "text/html"}) 
soup = BeautifulSoup(response.text, "html.parser")
questions = soup.find_all("a", class_="sf-accordion__link")

question_list = [q.text.strip() for q in questions if q.text.strip()]

# STEP 3: Build a new entry
new_entry = {
    "url": url,
    "questions": question_list
}

# STEP 4: Load existing JSON file (if it exists)
filename = "questions.json"
if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    data = []

# STEP 5: Append the new entry
data.append(new_entry)

# STEP 6: Write everything back (overwrites the file safely)
with open(filename, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added {len(question_list)} questions from:\n{url}")
