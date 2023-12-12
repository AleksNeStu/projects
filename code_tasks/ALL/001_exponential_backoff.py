import requests
import time

def retry_decorator(max_retries=3, initial_delay=1, backoff=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            delay = initial_delay  # Initialize delay outside the try block
            while retries < max_retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Retry {retries + 1}/{max_retries} after {delay} seconds due to timeout. Exception {e}")
                    time.sleep(delay)
                    delay *= backoff  # Exponential backoff
                    retries += 1
            raise Exception(f"Max retries reached {max_retries}")

        return wrapper
    return decorator

@retry_decorator(max_retries=3, initial_delay=1, backoff=2)
def get_posts(url: int, timeout: int):
    response = requests.get(url, timeout)
    response.raise_for_status()
    return response.json()

try:
    result = get_posts('http://some-api.com/posts', timeout=1)
    print(result)
except Exception as e:
    print(f"Failed to get posts: {e}")


"""
Retry 1/3 after 1 seconds due to timeout. Exception Cannot mix str and non-str arguments
Retry 2/3 after 2 seconds due to timeout. Exception Cannot mix str and non-str arguments
Retry 3/3 after 4 seconds due to timeout. Exception Cannot mix str and non-str arguments
Failed to get posts: Max retries reached 3
"""