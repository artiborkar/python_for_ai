# student marks should be in between 0 to 100 in number format.

import random
import time

class InvaliedMarsError(Exception):
    """Raised when the marks are not in between 0-100"""
    pass

class InsufficientBalanceError(Exception):
    """raise when the balance is less than exam fee"""
    pass


def get_valid_marks(subject_name: str)-> float:

    while True:

        try:
            raw_marks = input(f"Enter the Marks for {subject_name} in between 0 to 100:")

            marks  = float(raw_marks)

            if marks < 0 or marks > 100:
                raise InvaliedMarsError(f"Invalid marks for {subject_name} ,must be in between 0-100")

            return marks

        except (ValueError ) as e :
            print(f"Error : {e}")
        except InvaliedMarsError as e:
            print(f"Error : {e}")


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



def main():
    print("="*50)
    print("welcome to the student marks and payment syatem")
    print("="*50)

    student_bank_balance = 1000.00
    per_subject_exam_fee = 200

    while True:

        try:
            mark_phy = get_valid_marks("physics")
            mark_chem = get_valid_marks("Chemistry")
            mark_bio = get_valid_marks("Biology")

            total_marks = mark_phy + mark_chem  + mark_bio 
            percentage = (total_marks /300) *100

            if percentage < 50 or mark_phy < 50 or mark_chem < 50 or mark_bio < 50:
                print("❌ sorry , you are failed in the exam")
                print("❌ you need to pay the exam fee again")

            else:
                print(f"congratuation , you are passed in the exam with {percentage:.2f}%")
                print("You Don't need to pay the exam fee again")
                return None

            total_fee = per_subject_exam_fee * 3

            if student_bank_balance < total_fee:
                raise InsufficientBalanceError (f"Insufficient Balance in  the bank account , you need to pay {total_fee:.2f} reppes")
            
            receipt = process_payment_with_retry(total_fee)

        except InsufficientBalanceError as e:
            print(f"❌ Registration Canceled : {e}")

        except  ConnectionError as e:
            print(f"❌ Network failure : {e}")
        except Exception as e:
            print(f"❌ An unexpected error occurred :{e}")
        else:
            print("Registration Sucessful")
            print(f"Student Registraction Receipt : {receipt}")

        finally:
            print("🔒Session Closed securely. Thank You for using our system")



if __name__ == "__main__" :
    main()
