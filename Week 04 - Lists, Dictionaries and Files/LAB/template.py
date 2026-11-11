"""
RECORD CHECK  -  my version
===========================

Name  : Aayaan imtiaz
Lane  :  AI     
Date  : 00/11/2026

Run it:   python template.py
"""


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


records = load_records("/Users/i.taqdees/Documents/CST1510/Week 04 - Lists, Dictionaries and Files/03 - Files/temp_file.txt")

while True:
    rec = record_entry()
    if rec is None:
        break

for record in records:
    difference, percentage, status = check_record(record["loaded_rows"], record["exp_rows"])
    print_report(record["label"], record["loaded_rows"], record["exp_rows"], difference, percentage, status)                      
    
    if status == "OVER LIMIT":
        OL_count += 1

print("-" * 40)

with open("/Users/i.taqdees/Documents/CST1510/Week 04 - Lists, Dictionaries and Files/LAB/results.txt") as f:
    text = f.read()
    print(text)

print("-" * 40)


print(f"{len(records)} records checked.\n{OL_count} record(s) have \'OVER LIMIT\' as current status.\nReport check successful.")

print("-" * 40)


