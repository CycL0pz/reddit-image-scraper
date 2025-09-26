**Reddit Image Scraper**
A Python-based web scraper that extracts Reddit posts containing images from any subreddit and displays them in a beautiful web interface.

*🚀 Features*
Web Scraping: Scrapes Reddit posts with images from any subreddit
Smart Image Detection: Identifies various image formats and hosting services
JSON Export: Saves scraped data in structured JSON format
Web Display: Beautiful responsive web interface to view scraped posts
Configurable: Easy to change subreddit and number of pages to scrape

*📋 Requirements*
Python 3.7 or higher
Internet connection
Web browser (for viewing results)

*🛠️ Installation*
Clone the repository:

bash   git clone <your-repo-url>
   cd reddit-image-scraper

Create a virtual environment (recommended):

bash   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate

Install dependencies:

bash   pip install -r requirements.txt

*🚀 Usage*
Step 1: Run the Scraper
bashpython scraper.py
This will:

Scrape 10 pages from r/malaysia subreddit (configurable)
Extract posts with images
Save results to output/reddit_posts_with_images.json

Configuration Options (edit in scraper.py):
pythonSUBREDDIT = "malaysia"  # Change to any subreddit
PAGES_TO_SCRAPE = 10    # Number of pages to scrape

Step 2: View Results in Web Browser
bashpython app.py
Then open your web browser and go to: http://localhost:5000

*📁 Project Structure*
reddit-image-scraper/
├── scraper.py              # Main scraping script
├── app.py                  # Flask web application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── output/                # Generated output files
│   └── reddit_posts_with_images.json
└── templates/             # HTML templates
    └── index.html         # Main web page template
    
*📊 Output Format*
The scraper generates a JSON file with the following structure:
json[
  {
    "post_title": "Example Post Title",
    "image_url": "https://i.redd.it/example.jpg",
    "permalink": "https://reddit.com/r/malaysia/comments/...",
    "score": 123,
    "created_utc": 1640995200
  }
]
