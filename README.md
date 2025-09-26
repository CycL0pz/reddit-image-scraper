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
