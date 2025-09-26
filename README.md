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


*🎨 Web Interface Features*

Responsive Design: Works on desktop, tablet, and mobile
Modern UI: Clean, card-based layout with hover effects
Image Lazy Loading: Optimized performance for large datasets
Error Handling: Graceful handling of broken or missing images
Post Metadata: Shows upvotes, timestamps, and links to original posts

*⚙️ How It Works*
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


*🐛 Troubleshooting*
Common Issues

No posts found:

Check if the subreddit name is correct
Some subreddits may have fewer image posts
Try a different subreddit


Network errors:

Check your internet connection
Reddit may be temporarily unavailable
Try running the scraper later


Permission errors:

Ensure you have write permissions in the project directory
Try running with administrator privileges if necessary


Images not loading in web interface:

Some image URLs may be temporary or restricted
This is normal and handled gracefully by the interface



*📝 Development Notes*
Git Workflow
This project follows a structured commit pattern:

Initial setup and basic scraper implementation
Image detection and filtering logic
JSON output functionality
Web interface development
Documentation and final touches

*Code Quality*

Clean, well-documented Python code
Error handling for network requests and file operations
Modular design for easy maintenance and extension

*🤝 Contributing*
Feel free to submit issues and pull requests. For major changes, please open an issue first to discuss what you would like to change.

*📄 License*
This project is open source and available under the MIT License.

*⚠️ Disclaimer*
This tool is for educational purposes only. Please respect Reddit's Terms of Service and robots.txt when scraping. Use responsibly and don't overload Reddit's servers with excessive requests.



# 📋 COMMIT SUMMARY

Here are all 10 commits in order:

1. `"Initial project setup with basic documentation and gitignore"`
2. `"Adding Python dependencies for web scraping and Flask web framework"`
3. `"Implement Reddit image scraper with multi-page support and image filtering"`
4. `"JSON output functionality and sample data structure"`
5. `"Usage instructions and configuration options"`
6. `"Flask web application for displaying scraped Reddit posts"`
7. `"Web interface with modern UI for post display"`
8. `"Document project structure and file organization"`
9. `"Comprehensive documentation for advanced features and customization"`
10. `"Complete documentation with troubleshooting guide and development notes"`

## 🎯 Final File Structure:

reddit-image-scraper/
├── scraper.py              # Main scraping script
├── app.py                  # Flask web application
├── requirements.txt        # Python dependencies
├── README.md              # Documentation
├── output/                # Generated output files
│   └── reddit_posts_with_images.json
└── templates/             # HTML templates
└── index.html         # Main web page template



# Additional Helpful Sections ✅
- Project structure explanation
- Output format documentation
- Troubleshooting guide
- Requirements clearly listed

# 🎯 Assessment Requirement Status:

| Requirement | Status | Location in README |
|------------|--------|-------------------|
| ✅ Installation instructions | **COMPLETE** | `🛠️ Installation` section |
| ✅ How to run the scraper | **COMPLETE** | `🚀 Usage - Step 1` |
| ✅ How to run the web interface | **COMPLETE** | `🚀 Usage - Step 2` |
| ✅ Configuration options | **COMPLETE** | Configuration Options |
| ✅ Dependencies listed | **COMPLETE** | `📋 Requirements` + `requirements.txt` |

**Your README.md exceeds the basic requirement** - it not only includes installation and running instructions but also provides comprehensive documentation with troubleshooting, customization options, and project structure details.

**You're all set for the assessment submission!** 🚀
