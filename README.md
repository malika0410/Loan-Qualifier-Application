## Loan Qualifier Application

This Project is about the Loan Qualifier Application in the fintech lending startup. In this project variety of functions have been created to identify potential users who become eligible for getting loan on the basis of some pre conditioned acceptance criteria from the list of banks. 
In this Application user can get list of lending insitutions from where he/she gets the desired loan for their various needs.They do not need to go to banks in person or individual platform of each lending insitution as they get all the details and result in one platform just by providing some inputs.

---

## Technologies Used

To develop this application I have used Python as my programming language.
I have also used various python libraries - 'csv', 'fire','questionary','path'.Importing the needed library helped me by saving time to write many functions.
I have used visual code to read,write and run the program created.
This programme can be run on windows operating system,linux operating system and mac os operating system. 

---

## Installation Guide
![alt text](https://github.com/malika0410/Loan-Qualifier-Application/blob/main/installation%20screenshot.png)

![alt text](https://github.com/malika0410/Loan-Qualifier-Application/blob/main/imported_files.png) 

"BLOCK OF CODE USED TO INSTALL LIBRARIES AND ALSO IMPORTED MANY FUNCTIONS FROM THE HELPING FILE"
import csv
import sys
import fire
import questionary
from pathlib import Path

from qualifier.utils.fileio import (load_csv,save_csv)

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value


---

## Usage

This section should include screenshots, code blocks, or animations explaining how to use your project.

---






## Contributors

In this section, list all the people who contribute to this project. You might want recruiters or potential collaborators to reach you, so include your contact email and, optionally, your LinkedIn or Twitter profile.

---

## License

When you share a project on a repository, especially a public one, it's important to choose the right license to specify what others can and can't with your source code and files. Use this section to include the license you want to use.
