import timer

if __name__ == "__main__":
    url = "https://moizarshad.com"  # Replace with the target URL
    calls_per_minute = 100
    timer.call_website_repeatedly(url, calls_per_minute)