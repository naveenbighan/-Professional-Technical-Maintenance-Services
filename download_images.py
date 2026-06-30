"""
Script to download high-quality professional images for the Bustan Altoor website.
Uses Unsplash's free image API for high-resolution photos.
"""
import os
import urllib.request
import ssl

# Create images directory
os.makedirs('static/images', exist_ok=True)

# Disable SSL verification (in case of issues)
ssl._create_default_https_context = ssl._create_unverified_context

# Image URLs from Unsplash (high-quality, free to use)
images = {
    'hero-bg.jpg': 'https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=1920&q=80',
    'about-main.jpg': 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1200&q=80',
    'about-team.jpg': 'https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=1200&q=80',
    'page-header.jpg': 'https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?w=1920&q=80',
    'service-cleaning.jpg': 'https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=1200&q=80',
    'service-tile.jpg': 'https://images.unsplash.com/photo-1581858726788-75bc0f6a952d?w=1200&q=80',
    'service-electrical.jpg': 'https://images.unsplash.com/photo-1621905251918-48416bd8575a?w=1200&q=80',
    'service-plumbing.jpg': 'https://images.unsplash.com/photo-1607472586893-edb57bdc0e39?w=1200&q=80',
    'service-ac.jpg': 'https://images.unsplash.com/photo-1631545308379-9f5052cd6e8c?w=1200&q=80',
    'service-painting.jpg': 'https://images.unsplash.com/photo-1562259949-e8e7689d7828?w=1200&q=80',
    'service-carpentry.jpg': 'https://images.unsplash.com/photo-1572297870735-2ef638662eda?w=1200&q=80',
}

def download_image(url, filename):
    """Download an image from URL to the static/images directory."""
    filepath = os.path.join('static/images', filename)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as response:
            with open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        print(f"✓ Downloaded: {filename}")
        return True
    except Exception as e:
        print(f"✗ Failed to download {filename}: {e}")
        return False

if __name__ == '__main__':
    print("Downloading images for Bustan Altoor website...")
    print("=" * 50)
    success = 0
    for filename, url in images.items():
        if download_image(url, filename):
            success += 1
    print("=" * 50)
    print(f"Completed: {success}/{len(images)} images downloaded successfully")
