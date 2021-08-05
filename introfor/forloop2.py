#!/usr/bin/env python3

#create list of vendors
vendors = ["cisco","juniper","big_ip","f5","arista","alta3","zach","stuart"]
#create second list of strings
approved_vendors = ["cisco","juniper","big_ip"]
#loop accross the list called vendors
for x in vendors:
    print("\nThe vendor is " + x, end="") #new line, print current vendor, and end without a new line
    if x not in approved_vendors:
        print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.") #print loop has finished.
