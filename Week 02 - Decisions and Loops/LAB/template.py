"""
RECORD CHECK  -  my version
===========================

Name  :  Aayaan Imtiaz
Lane  :  AI  
Date  :  06/10/2026

Run it:   python template.py
"""
OL_count = 0            # "OL" stands for OVER LIMIT
while True:
    label = input("Enter a label: ")
    if label == "quit":
        break     
    loaded_rows = float(input("Enter amount of rows loaded :"))    
    exp_rows = float(input("Enter the expected amount of rows :"))     

    difference = exp_rows - loaded_rows   
    percent = (loaded_rows / exp_rows) * 100     

    status = ""
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK" 
    if status == "OVER LIMIT":
        OL_count+=1

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

print(f"{OL_count} record(s) have \'OVER LIMIT\' as current status.\nReport check successful.")
