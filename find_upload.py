import requests

# List of common directories to check
common_directories = [
    "uploads", "upload", "files", "images", "media", "content", "assets",
    "wp-content/uploads", "wp-content/themes", "wp-content/plugins"
]

def check_directory(url, directory):
    full_url = f"{url}/{directory}/"
    try:
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"Found: {full_url}")
        elif response.status_code == 403:
            print(f"Forbidden: {full_url}")
        else:
            print(f"Not Found: {full_url}")
    except requests.RequestException as e:
        print(f"Error accessing {full_url}: {e}")

def main():
    website = input("Enter the website URL (e.g., https://example.com): ")
    for directory in common_directories:
        check_directory(website, directory)

if __name__ == "__main__":
    main()