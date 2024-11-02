# Custom Google Maps Web Scraper

## Overview
This project is a web application that scrapes data from Custom Google Maps based on a provided URL. It utilizes a Flask backend to perform web scraping and a simple HTML frontend to interact with users. Users can input a Google Maps link, and the application will return relevant information, including names, descriptions, and ratings of locations.

## Features
- Scrapes location data from Google Maps URLs.
- Displays the scraped data in a user-friendly table format.
- Responsive design with basic styling.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Web Scraping**: BeautifulSoup, Requests
- **Data Processing**: Pandas

## Getting Started

### Prerequisites
- Python 3.x
- Flask
- BeautifulSoup
- Requests
- Pandas

### Installation

1. **Clone the Repository**

```bash
   git clone https://github.com/holydexboi/custom-google-map-web-scrapper.git
   cd custom-google-map-web-scrapper
```

2. **Install Required Packages**

```bash
    pip install Flask beautifulsoup4 requests pandas

```

3. **Run the Backend**
```bash
    python app.py
```
    The backend will run on http://127.0.0.1:5000.

4. **Open the Frontend Open index.html in your web browser. You can directly open it or use a simple HTTP server to serve the files.**

### Usage

1. **Enter a Google Maps URL into the input field.**
2. **Click the "Scrape" button.**
3. **The scraped data will be displayed in a table below.**

### API Endpoint
- POST /scrape
    - Request Body:
    ```bash
        {
            "url": "<google-maps-url>"
        }
    ```
    - Response:
        - Returns a JSON object containing the scraped data, or an error message if the scraping fails.

### Deployment
- The frontend is hosted on GitHub Pages.
- The backend is deployed on Render
### Contributing
- Contributions are welcome! Please feel free to submit a pull request or open an issue.

### License
- This project is licensed under the MIT License.

### Acknowledgments
- Google Maps
- Flask
- BeautifulSoup
- Pandas

### Important
**This application only works with custom Google Maps URLs. Please ensure that the URL provided is a valid custom Google Maps link for successful scraping.**