#Question-1

import re
s=re.match('internity','hi internity')
print(s)

#output--(2,11)

#Question-2

import re
s=re.search('dataloves','how are you student and dataloves begins the training')
print(s)

#output--datalove,26,35

#Question-3

import re
s=re.findall("dataloves","vinit,vishal join dataloves provide services like dataloves cloud")
print(s)
print(tuple(s))
print(set(s))
print(frozenset(s))

#output--['dataloves', 'dataloves']
#('dataloves', 'dataloves')
#{'dataloves'}
#frozenset({'dataloves'})


#Question 4

import re
r=re.match(r"[a-z]+bh","saurabh sir how are you")
print(r.group())

#output--saurabh

#Question 5

import re
r=re.match(r"[a-z]?an","taran sir how are you")
print(r)

#output--None

#Question 6

import re
r=re.match(r"[a-z]?","taran sir how are you")
print(r)

#output-- <re.Match object; span=(0, 1), match='t'>

#Question 7

import re
r=re.match(r"[a-z]?an","ran sir how are you")
print(r.group())

#output--ran

#Question 8

import re
r=re.search(r"[a,b,c]*soft","saurabh sir how are you datasoft are you")
print(r.group())

#output--asoft

#Question 9

import re
r=re.search(r"[a,b,c,d,e,f]*soft","saurabh sir how are you datasoft are you")
print(r.group())

#output--asoft

#Question 10

import re
r=re.search(r"[a-j]*b","taran sir how are you dabasoft are you")
print(r.group())

#output-- dab

#Question 11

import re
msg='call me at 278323974'
regex=re.compile(r'\d+') # compile is new digit function
nu=regex.search(msg)
print(nu.group())

#output-278323974
