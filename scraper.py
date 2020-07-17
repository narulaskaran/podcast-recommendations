import requests
from bs4 import BeautifulSoup
import json

JSON_PODCAST_LIST_PATH = './json/podcast_list.json'

# function to add to JSON 
def write_json(data, filename=JSON_PODCAST_LIST_PATH): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 

# function to fetch transcript text from website
def extract_transcript(url):
    page = requests.get(url)
    content = BeautifulSoup(page.content, 'html.parser')
    transcript_blocks = content.find_all("div", class_='transcription')

    split_transcript = [block.find('span').text for block in transcript_blocks]
    formatted = " ".join(split_transcript)
    formatted = escape_double_quotes(formatted)
    return formatted.lower()


def extract_stream(url):
    page = requests.get(url)
    content = BeautifulSoup(page.content, 'html.parser')
    audio_block = content.find("audio", id="player")
    return 'https:{}'.format(audio_block.find("source")['src'])
    
def escape_double_quotes(string):
    return string.replace("\'", "\\\"")

# entry point
if __name__ == "__main__":
    with open(JSON_PODCAST_LIST_PATH) as f:
        json_read = json.load(f)
        data = json_read['podcasts']
    
    for podcast in data:
        show = podcast['show']
        url = podcast['url']
        podcast['show_desc'] = escape_double_quotes(podcast['show_desc'])
        podcast['transcript'] = extract_transcript(url).lower()
        podcast['stream'] = extract_stream(url)
        
    write_json(json_read)
