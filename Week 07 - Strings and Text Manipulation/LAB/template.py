"""
RECORD CHECK  -  my version
===========================

Name  :  Aayaan imtiaz
Lane  :  AI 
Date  :  14/11/2026   

Run it:   python template.py
"""

flagged_count = 0

def parse_line(raw_line):
    """converts messy lines into clean lines in a dict."""
    line = raw_line.strip()
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip().lower()

    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = float(value.strip())
        
    return {"hostname": hostname, "used": fields["used"], "total": fields["total"]}


def status_of(used, total, warning_at=90):
    """returns the status of the record"""
    percent = (used / total) * 100
    if percent >= 100:
        return "OVERLIMIT" 
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"
    
print("-" * 34)
print(f"{'RECORD':<8} {'USED/TOTAL':<14} STATUS")
print("-" * 34)

rec_count = 0

with open("/Users/i.taqdees/Documents/CST1510/Week 07 - Strings and Text Manipulation/LAB/messy_temp_lines.txt") as f:
    for raw_record in f:

        record = parse_line(raw_record)
        status = status_of(record["used"], record["total"])
        if status == "OK":
            pass
        else:
            flagged_count += 1
        usage = f"{record['used']:.1f}/{record['total']:.1f}"
        print(f"{record['hostname']:<8} {usage:<14} {status}")
        rec_count += 1
        
print("-" * 34)
print(f"Records checked: {rec_count}| Registered as \'FLAGGED\': {flagged_count}")


