

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