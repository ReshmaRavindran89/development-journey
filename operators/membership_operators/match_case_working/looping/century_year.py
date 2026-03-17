"""
W.A.P to display all century years from 1800 to 2026.
"""
i = 1800
while(i<=2026):
    if i%100==0:
        print(i, "Century Year")
    i=i+1