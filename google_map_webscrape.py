from flask import Flask, request, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes
# Function to perform the web scraping
def scrape_google_map(url):
   # url = "https://www.google.com/maps/d/u/0/viewer?mid=1IfRqpMMA8JBwH_XvIyxW8MYyzzg&ll=52.37174422271906%2C4.911542985549802&z=15"


    mapPage = requests.get(url).text

    soup = BeautifulSoup(mapPage, 'html.parser')

    script_tag = soup.find("script", string=re.compile(r"_pageData"))

    if script_tag:
        json_text = re.search(r'var _pageData = "(.+?)";', script_tag.string).group(1)

    split_text = json_text.split('[[\\"name\\"')

    pattern = r'\[\\"([^\"]+?)\\"\],1\]'
    rate_pattern = r'\b\d+\.\d{6}\b' 
    output = []
    for idx, part in enumerate(split_text):
        new_loc = {}
        location = re.findall(pattern, part)
        if len(location) > 0:
            new_loc['name'] = location[0]
        else:
            new_loc['name'] = ''
        if len(location) > 1:
            new_loc['description'] = location[1]
        else:
            new_loc['description'] = ''

        rate = re.findall(rate_pattern, part)
        if len(rate) > 1:
            new_loc['rate'] = rate[1]
        elif len(rate) == 1:
            if rate[0][0:2] != '52':
                new_loc['rate'] = rate[0]
        output.append(new_loc)

    
    return output

@app.route('/scrape', methods=['POST'])
def scrape():
    if request.is_json:
        data = request.json
        url = data.get("url")

        if not url:
            return jsonify({"error": "URL is required"}), 400

        try:
            result = scrape_google_map(url)
            return jsonify(result), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Unsupported Media Type"}), 415

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

