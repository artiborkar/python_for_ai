import random
import time


def simulate_bank_api(amount:float)->str:
    """simulate bank API payment processing , 50 % chance of sucess, 50% chance of failure"""

    if random.choice([True , False]):
        raise ConnectionError("Bank API is not available / bank gateway time out / network interrputed")
    return f"Payment of rupees {amount:.2f} processed sucessfully"


def process_payment_with_retry(amount:float , max_attemts:int=3)->str:
    """Process payment with retry , if payment fails ,  retry with exponential backoff"""

    for attempt in range(1, max_attemts + 1):
        try:
            print(f"Attempt {attempt} of {max_attemts} to process payment of rupees {amount:.2f}")
            result = simulate_bank_api(amount)
            return result

        except ConnectionError as e:
            print(f"Attempt {attempt} Failture :  {e} ")
            if attempt < max_attemts:
                wait = 2 ** (attempt -1)
                time.sleep(wait)

            else:
                raise ConnectionError("max attempt areached , payment failed")

