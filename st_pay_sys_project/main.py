from get_valid_marks import get_valid_marks 
from simulate_process_payment import simulate_bank_api
from simulate_process_payment import process_payment_with_retry


class InvaliedMarsError(Exception):
    """Raised when the marks are not in between 0-100"""
    pass

class InsufficientBalanceError(Exception):
    """raise when the balance is less than exam fee"""
    pass

def main():

    if __name__ == "__main__" :
        main()


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


