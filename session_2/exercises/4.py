"""
برنامه ای که اعداد زوج بین 1 تا 10 بجز 2 را چاپ کند.
"""

for i in range(0,10,2):
    if i == 2:
        continue
    print(i)
