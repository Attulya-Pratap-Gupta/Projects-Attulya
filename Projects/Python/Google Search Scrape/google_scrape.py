import pandas as pd
import time
from serpapi import GoogleSearch

df = pd.read_csv('Example.csv')
names = df['example_column']
save_names = [name.replace(" ", "_") for name in names]

#Creating an empty list for storing all the links to the resume
url = []

#Creating an empty list to store all the names
name_list = []

#Creating a counter (Adjust for respective values)
counter = 0

#Total iterations
total = len(names)

for i in range(counter, total):
  name = names[i]
  #Add your personal API key
  #Change the q parameter to the required search query
  params = {
    "engine": "google",
    "q": f"{name} Medicine Laureate, resume or cv or curriculum vitae pdf",
    "hl": "en",
    "gl": "us",
    "google_domain": "google.com",
    "num": "10",
    "safe": "active",
    "api_key": "YOUR API KEY" 
  }
  
  search = GoogleSearch(params)
  results = search.get_dictionary()

  target_link = ""

  try:
    organic = results['organic_results']

    links = [res['link'] for res in organic]
    
    #Fetching all the pdf links
    pdf_links = [link for link in links if '.pdf' in link]

    #Extracting the target link
    if pdf_links:
      target_link = pdf_links[0]
    else:
      if links:
        target_link = links[0]
      else:
        target_link = "Not Found"
  
  except KeyError:
    target_link = "Not Found"

  #Adding the link to the output list
  url.append(target_link)

  #Printing the url to verify
  print(target_link)

  name_list.append(name)

  #Setting the time weight according to the rate limit
  time.sleep(2)

  new_df = pd.DataFrame({'URLS': url, 'Name': name_list})

  new_df.to_csv("output.csv", index = False)
  






