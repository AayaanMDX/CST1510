"""
RECORD CHECK  -  my version
===========================

Name  :  Aayaan Imtiaz
Lane  :  AI
Date  :  08/10/2026

Run it:   python template.py

"""

OL_count = 0 

def status_of(percent):
    '''Returns the status of the record'''
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return status

def check(loaded_rows, exp_rows):
    '''Returns the difference and percentage'''
    difference = exp_rows - loaded_rows
    percentage = (loaded_rows / exp_rows) * 100
    return difference, percentage

def print_report(label, loaded_rows, exp_rows, difference, percent, status):
    '''Returns the report of the record'''

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Dataset Name   : {label:>10}")
    print(f"  Rows loaded    : {loaded_rows:>10.2f}")
    print(f"  Rows Expected  : {exp_rows:>10.2f}")
    print(f"  Current Status : {status:>10}")
    print(f"  Difference     : {difference:>10.2f}")
    print(f"  Percentage     : {percent:>10.2f}")
    print("=" * 34)
    print()

def record_entry():
    '''This block of code is for input of label, loaded_rows and exp_rows'''
    label = input("Enter a label(or quit): ")
    if label == "quit":
        return None     
    
    loaded_rows = float(input("Enter amount of rows loaded :"))    
    exp_rows = float(input("Enter the expected amount of rows :"))
    return label, loaded_rows, exp_rows    
 
while True:
    record = record_entry()
    if record is None:
        break

    label, loaded_rows, exp_rows = record
    difference, percentage = check(loaded_rows,exp_rows)
    status = status_of(percentage)

    print(status_of(percentage))
    print(check(loaded_rows,exp_rows))           

    if status == "OVER LIMIT":
        OL_count += 1

    print_report(label,loaded_rows,exp_rows,difference,percentage,status)
print(f"{OL_count} record(s) have \'OVER LIMIT\' as current status.\nReport check successful.")

