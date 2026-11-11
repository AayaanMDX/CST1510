"""
RECORD CHECK  -  my version
===========================

Name  : Aayaan imtiaz
Lane  :  AI     
Date  : 00/11/2026

Run it:   python template.py
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

OL_count = 0 
    
def check_record(loaded_rows, exp_rows, warning=90):
    '''Returns the difference, percentage and status'''
    difference = exp_rows - loaded_rows
    percentage = (loaded_rows / exp_rows) * 100

    if percentage >= 100:
        status = "OVER LIMIT"
    elif percentage >= warning:
        status = "WARNING"
    else:
        status = "OK"
    
    return difference, percentage, status

def print_report(label,loaded_rows,exp_rows,difference,percent,status):
    '''Returns the report of the record in borders'''

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

# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

  
def load_records(path):
    '''The function reads the following file and returns a list'''
    with open(path) as f:
        records = []
        for line in f:
            label, loaded_rows, exp_rows = line.strip().split(",")
            records.append({
                "label": label,
                "loaded_rows": float(loaded_rows),
                "exp_rows": float(exp_rows)
            })
        return records


records = load_records("/Users/i.taqdees/Desktop/CST1510/Week 04 - Lists, Dictionaries and Files/03 - Files/temp_file.txt")
# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

while True:
    rec = record_entry()
    if rec is None:
        break

for record in records:
    difference, percentage, status = check_record(record["loaded_rows"], record["exp_rows"])
    print_report(record["label"], record["loaded_rows"], record["exp_rows"], difference, percentage, status)                      
    
    if status == "OVER LIMIT":
        OL_count += 1
    
print(f"{len(records)} records checked.\n{OL_count} record(s) have \'OVER LIMIT\' as current status.\nReport check successful.")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job