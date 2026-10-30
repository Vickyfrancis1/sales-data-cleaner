# Sales Data Cleaner

A Python script that cleans a messy sales spreadsheet and produces a summary report.


## The problem
The file had repeated rows, a missing item name and inconsistent spelling like 'rice' and 'Rice'.

## What the script does
1. Reads `messy_sales.xlsx`
2. Cleans the text (removes spaces, fixes capital letters)
3. Removes duplicate rows
4. Removes rows with no item name
5. Calculates Total = Qty x Price
6. Adds up sales for each category
7. Saves two Excel files: `sales_report.xlsx` and `sales_clean.xlsx`

## How to run
1. Install pandas and openpyxl: `pip install pandas openpyxl`
2. Run `make_messy.py` to create the sample file
3. Run `clean_sales.py`

## Notes
- Rows with a missing quantity are kept in `sales_clean.xlsx` and marked "Missing", but they are not counted in the totals.
- Rows with no item name are removed.

## Tools used
Python, pandas