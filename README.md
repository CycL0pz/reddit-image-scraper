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

bash   
git clone <your-repo-url>
cd reddit-image-scraper

Create a virtual environment (recommended):

bash  
python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate

Install dependencies:

bash  
pip install -r requirements.txt

*🚀 Usage*
Step 1: Run the Scraper
bash
python scraper.py

This will:

Scrape 10 pages from r/malaysia subreddit (configurable)
Extract posts with images
Save results to output/reddit_posts_with_images.json

Configuration Options (edit in scraper.py):
SUBREDDIT = "malaysia"  # Change to any subreddit
PAGES_TO_SCRAPE = 10    # Number of pages to scrape

Step 2: View Results in Web Browser
bash
python app.py

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


🎨 Web Interface Features

Responsive Design: Works on desktop, tablet, and mobile
Modern UI: Clean, card-based layout with hover effects
Image Lazy Loading: Optimized performance for large datasets
Error Handling: Graceful handling of broken or missing images
Post Metadata: Shows upvotes, timestamps, and links to original posts

⚙️ How It Works
Scraping Process

HTTP Requests: Uses Reddit's JSON API (no authentication required)
Image Detection: Identifies posts with images through multiple methods:

Direct image URLs (jpg, png, gif, etc.)
Reddit's native image hosting (i.redd.it)
Imgur links
Preview image metadata


Data Extraction: Extracts title, image URL, score, and timestamps
Pagination: Handles Reddit's pagination system to scrape multiple pages
Rate Limiting: Includes delays to be respectful to Reddit's servers

Supported Image Sources

Reddit native images (i.redd.it)
Imgur (direct links and gallery links)
Direct image URLs (.jpg, .png, .gif, .webp, .bmp)
Reddit preview images

🔧 Customization
Change Subreddit
Edit scraper.py line 108:
python
SUBREDDIT = "your_subreddit_name"

Change Number of Pages
Edit scraper.py line 109:
python

PAGES_TO_SCRAPE = 20  # Scrape 20 pages instead of 10
Modify Output Filename
In scraper.py, change the filename in the save_to_json() call:

python
output_file = scraper.save_to_json("custom_filename.json")
