"""
RECORD CHECK  -  my version
===========================

Name  :  Aayaan imtiaz
Lane  :  AI 
Date  :  10/11/2026

Run it:   python template.py
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/i.taqdees/Documents/CST1510/Week 06 - Pandas/LAB/week6.csv")

df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df["percent"].apply(lambda p: "OVERLIMIT" if p >= 100.0 else "WARNING" if p >= 90.0 else "OK")

print(df)
print("-" * 50)

print(df[df["status"] != "OK"])
print("-" * 50)

grouped = df["status"].value_counts()
grouped.to_csv("/Users/i.taqdees/Documents/CST1510/Week 06 - Pandas/LAB/status_bar.csv")
grouped.plot(kind="bar", title= "counts per status")
plt.tight_layout()
plt.show()
