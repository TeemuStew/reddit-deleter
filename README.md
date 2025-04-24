# reddit-deleter
Automatically deletes comments and posts

**Requirements**
Before using the script, you’ll need:
- Python 3.x installed on your system.
- PRAW (Python Reddit API Wrapper)
  * ```pip install praw```
 
**Setting up Reddit app**
1. Go to Reddit's App Preferences
2. Click "create app":
   - app type: script
   - redirect url: http://localhost:8080 // Just a placeholder required by Reddit
3. Save info for later

**Script**
1. Fill the info in the reddit-deleter.py
2. Run the script in terminal ```python reddit-deleter.py```

The script will then delete posts while showing you the information. After deleting the posts, it will delete comments.

**Notes**
- You might need to disable 2FA, if authentication fails.
- If installing praw doesn't work, use ```python -m pip install praw```

**Disclaimer**
- Use at Your Own Risk: This script is intended for personal use and should be used responsibly. Deleting posts/comments is permanent.
- Reddit API Limits: Ensure that you're following Reddit's API Terms of Service when using the script.
