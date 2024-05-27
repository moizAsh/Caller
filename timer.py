import time
import request

def call_website_repeatedly(url, calls_per_minute):
    interval = 60 / calls_per_minute  # Calculate interval in seconds
    while True:
        request.make_request(url)
        time.sleep(interval)