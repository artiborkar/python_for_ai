# retry mein ek case add karo jahan saare attempts fail 
# hon — aakhri error dekho.

import time


def retry(func, max_attempts: int = 3, delay: float = 1.0):
    """Run func, retrying on failure with a wait between attempts.

    Args:
        func: A no-argument function to call.
        max_attempts: How many times to try before giving up.
        delay: Base seconds to wait between attempts.

    Returns:
        Whatever func returns on success.

    Raises:
        The last exception if all attempts fail.
    """
    last_error = None
    for attempt in range(1, max_attempts + 1):
        try:
            return func()                       # koshish
        except Exception as e:                  # koi bhi failure
            last_error = e
            print(f"Attempt {attempt} failed: {e}")
            if attempt < max_attempts:
                wait = delay * (2 ** (attempt - 1))    # backoff
                print(f"Retrying in {wait}s...")
                time.sleep(wait)
    # saare attempts fail — aakhri error wapas phenko
    raise last_error


# --- test ---
counter = {"calls": 0}

def unreliable():
    counter["calls"] += 1
    if counter["calls"] < 3:
        raise ConnectionError("Temporary failure")
    return "Data fetched!"

result = retry(unreliable, max_attempts=5, delay=0.5)
print(result)       # Data fetched!  (3rd attempt par)


def last_attempt():
    raise ValueError("Value is not valied")

try:
    retry(last_attempt, max_attempts = 3, delay = 1.0)

except ValueError as e:
    print(f"Error : {e}")