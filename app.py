#!/usr/bin/env python3
"""
Flask Web Application to Display Reddit Posts with Images
"""

from flask import Flask, render_template, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

def load_json_data(filename="reddit_posts_with_images.json"):
    """Load JSON data from file"""
    filepath = os.path.join('output', filename)
    
    if not os.path.exists(filepath):
        return []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return []

def format_timestamp(timestamp):
    """Convert Unix timestamp to readable format"""
    try:
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    except:
        return 'Unknown'

@app.route('/')
def index():
    """Main page displaying all posts"""
    posts = load_json_data()
    
    # Add formatted timestamp to each post
    for post in posts:
        post['formatted_date'] = format_timestamp(post.get('created_utc', 0))
    
    return render_template('index.html', posts=posts, total_posts=len(posts))

@app.route('/api/posts')
def api_posts():
    """API endpoint to get posts as JSON"""
    posts = load_json_data()
    return jsonify(posts)

@app.route('/post/<int:post_id>')
def single_post(post_id):
    """Display single post"""
    posts = load_json_data()
    
    if 0 <= post_id < len(posts):
        post = posts[post_id]
        post['formatted_date'] = format_timestamp(post.get('created_utc', 0))
        return render_template('single_post.html', post=post, post_id=post_id)
    else:
        return "Post not found", 404

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    print("Starting Flask web server...")
    print("Open your browser and go to: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    
    app.run(debug=True, host='0.0.0.0', port=5000)