# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data



def save_csv(qualifying_loans,output_path):
    """writes the CSV file from path provided. Created a list of lists (header) for the csv file named qualifying_loans.

    Args:
        Write the qualified loans from all the items in the existing file in the new csv file.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """

    header=['Lender','Max Loan Amount','Max LTV','Max DTI','Min Credit Score','Interest Rate']
    print(qualifying_loans)

    with open(output_path,"w") as csvfile:          #creating a csvfile in a write mode to assign values.
        csvwriter=csv.writer(csvfile,delimiter=(','))   #using csv.writer function from the csv library to write in the file and seperating it with delimiter","
        csvwriter.writerow(header)                       #firstly writing a row and assigning headings to it.
        for item in qualifying_loans:                       # writing items in a row from the list created above using for loop.
            csvwriter.writerow(item)
