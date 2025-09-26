#!/usr/bin/env python3
"""
Reddit Image Scraper
Scrapes Reddit posts with images and saves them to JSON file
"""

import requests
import json
import time
import re
from urllib.parse import urlparse
import os

class RedditImageScraper:
    def __init__(self, subreddit="malaysia", pages=10):
        self.subreddit = subreddit
        self.pages = pages
        self.base_url = f"https://www.reddit.com/r/{subreddit}"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.posts_with_images = []
        
    def is_image_url(self, url):
        """Check if URL points to an image"""
        if not url:
            return False
            
        # Direct image extensions
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp']
        parsed_url = urlparse(url.lower())
        
        # Check direct image URLs
        if any(parsed_url.path.endswith(ext) for ext in image_extensions):
            return True
            
        # Check common image hosting domains
        image_domains = ['i.redd.it', 'i.imgur.com', 'imgur.com']
        if parsed_url.netloc in image_domains:
            return True
            
        # Handle imgur links without direct extension
        if 'imgur.com' in parsed_url.netloc and '/a/' not in parsed_url.path:
            return True
            
        return False
    
    def extract_image_url(self, post_data):
        """Extract image URL from post data"""
        # Check direct URL first
        if 'url' in post_data and self.is_image_url(post_data['url']):
            return post_data['url']
            
        # Check preview images
        if 'preview' in post_data and 'images' in post_data['preview']:
            try:
                preview_url = post_data['preview']['images'][0]['source']['url']
                # Decode HTML entities
                preview_url = preview_url.replace('&amp;', '&')
                return preview_url
            except (KeyError, IndexError):
                pass
        
        # Check media metadata
        if 'media_metadata' in post_data:
            try:
                for media_id, media_info in post_data['media_metadata'].items():
                    if 's' in media_info and 'u' in media_info['s']:
                        media_url = media_info['s']['u'].replace('&amp;', '&')
                        return media_url
            except (KeyError, TypeError):
                pass
                
        return None
    
    def scrape_page(self, after=None):
        """Scrape a single page of Reddit posts"""
        url = f"{self.base_url}.json"
        params = {'limit': 25}
        if after:
            params['after'] = after
            
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            posts = []
            next_after = None
            
            if 'data' in data and 'children' in data['data']:
                for post in data['data']['children']:
                    if post['kind'] == 't3':  # t3 indicates a post
                        post_data = post['data']
                        
                        # Extract image URL
                        image_url = self.extract_image_url(post_data)
                        
                        if image_url:
                            post_info = {
                                'post_title': post_data.get('title', ''),
                                'image_url': image_url,
                                'permalink': f"https://reddit.com{post_data.get('permalink', '')}",
                                'score': post_data.get('score', 0),
                                'created_utc': post_data.get('created_utc', 0)
                            }
                            posts.append(post_info)
                
                # Get next page token
                next_after = data['data'].get('after')
                
            return posts, next_after
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return [], None
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            return [], None
    
    def scrape_multiple_pages(self):
        """Scrape multiple pages of Reddit posts"""
        print(f"Starting to scrape r/{self.subreddit} for posts with images...")
        print(f"Target: {self.pages} pages")
        
        after = None
        page_count = 0
        
        while page_count < self.pages:
            print(f"\nScraping page {page_count + 1}...")
            
            posts, after = self.scrape_page(after)
            
            if not posts and not after:
                print("No more posts found or reached end of subreddit")
                break
                
            self.posts_with_images.extend(posts)
            print(f"Found {len(posts)} posts with images on this page")
            print(f"Total posts with images so far: {len(self.posts_with_images)}")
            
            page_count += 1
            
            if not after:
                print("Reached end of available posts")
                break
                
            # Be respectful to Reddit's servers
            time.sleep(1)
        
        print(f"\nScraping completed!")
        print(f"Total posts with images collected: {len(self.posts_with_images)}")
        return self.posts_with_images
    
    def save_to_json(self, filename="reddit_posts_with_images.json"):
        """Save scraped data to JSON file"""
        try:
            # Create output directory if it doesn't exist
            os.makedirs('output', exist_ok=True)
            filepath = os.path.join('output', filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.posts_with_images, f, indent=2, ensure_ascii=False)
            
            print(f"Data saved to {filepath}")
            print(f"Saved {len(self.posts_with_images)} posts with images")
            return filepath
            
        except Exception as e:
            print(f"Error saving to JSON: {e}")
            return None

def main():
    # Configuration
    SUBREDDIT = "malaysia"  # Change this to any subreddit you prefer
    PAGES_TO_SCRAPE = 10
    
    print("Reddit Image Scraper")
    print("=" * 50)
    
    # Initialize scraper
    scraper = RedditImageScraper(subreddit=SUBREDDIT, pages=PAGES_TO_SCRAPE)
    
    # Scrape posts
    posts = scraper.scrape_multiple_pages()
    
    if posts:
        # Save to JSON
        output_file = scraper.save_to_json()
        
        if output_file:
            print(f"\nScraping completed successfully!")
            print(f"Output file: {output_file}")
            
            # Display sample data
            print(f"\nSample of scraped data:")
            print("-" * 30)
            for i, post in enumerate(posts[:3]):  # Show first 3 posts
                print(f"{i+1}. {post['post_title'][:60]}...")
                print(f"   Image: {post['image_url']}")
                print(f"   Score: {post['score']}")
                print()
        else:
            print("Failed to save data to file")
    else:
        print("No posts with images were found")

if __name__ == "__main__":
    main()