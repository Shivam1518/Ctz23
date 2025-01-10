import requests

def fetch_data_from_api():
    url = "https://jsonplaceholder.typicode.com/posts/1"  # Example API
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")
    else:
        print("Failed to retrieve data.")

fetch_data_from_api()