import requests
from bs4 import BeautifulSoup
import json

JSON_PODCAST_LIST_PATH = './json/podcast_list.json'

# function to add to JSON 
def write_json(data, filename=JSON_PODCAST_LIST_PATH): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 

# function to fetch transcript text from website
def extract(url):
    page = requests.get(url)
    content = BeautifulSoup(page.content, 'html.parser')
    transcript_blocks = content.find_all("div", class_='transcription')

    concatenated_content = [block.find('span').text for block in transcript_blocks]
    return " ".join(concatenated_content)

# entry point
if __name__ == "__main__":
    with open(JSON_PODCAST_LIST_PATH) as f:
        json_read = json.load(f)
        data = json_read['podcasts']
    
    for podcast in data:
        show = podcast['show']
        url = podcast['url']
        if "transcript" not in podcast:
            transcript = extract(url)

            # Remove any quotes that mess with the JSON file
            transcript = transcript.replace('"', "")
            transcript = transcript.replace('"', "")
            
            podcast['transcript'] = extract(url)
        
    write_json(json_read)
