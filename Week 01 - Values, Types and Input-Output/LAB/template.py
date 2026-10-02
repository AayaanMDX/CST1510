"""
RECORD CHECK  -  my version
===========================

Name  : Aayaan Imtiaz
Lane  :      AI     
Date  :   27/09/2026

Run it:   python template.py

"""


dataset_name = input("Enter name of dataset: ")      # : replace with an input() call
rows_loaded = float(input("Enter number of loaded rows: "))     # : replace with an input() call, converted
rows_expected = float(input("Enter number of expected rows: "))    # : replace with an input() call, converted




difference = rows_expected - rows_loaded    # 
percent = (rows_loaded / rows_expected) * 100      # 



print()
print("=" * 34)
print(f"  RECORD CHECK    : {dataset_name}")
print("=" * 34)
print(f"  Rows loaded     :{rows_loaded:>10.2f}")
print(f"  Rows expected   :{rows_expected:>10.2f}")
print(f"  Difference      :{difference:>+10.2f}")
print(f"  Percentage      :{percent:>10.2f}%")
print("=" * 34)



