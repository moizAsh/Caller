import requests

def make_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Request to {url} succeeded with a status code: {response.status_code}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request to {url} failed: {e}")
        return None