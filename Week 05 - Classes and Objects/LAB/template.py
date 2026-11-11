"""
RECORD CHECK  -  my version
===========================

Name  : Aayaan imtiaz
Lane  :  AI 
Date  : 00/11/2026

Run it:   python template.py
"""

class Record:
    '''foundation for instances and variables to go through'''
    over_limit_count = 0
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        '''returns the status of the object'''
        p = (self.value/self.limit) * 100
        if p >= 100.0:
            Record.over_limit_count += 1
            return "OVER LIMIT"
        elif p >= 90.0:
            return "WARNING"
        else:
            return "OK"

def load_records(path):
    """reads files and stores objects into a list"""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records

records = load_records("/Users/i.taqdees/Documents/CST1510/Week 05 - Classes and Objects/LAB/template_file.txt")

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  LABEL NAME    -  {record.label}")
    print(f"  VALUE         -  {record.value}")
    print(f"  LIMIT         -  {record.limit}")
    print(f"  STATUS        -  {record.status()}")
    print("=" * 34)

print(f"{Record.over_limit_count} records have returned as \'OVERLIMIT\'\nRecord check Successful.")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
