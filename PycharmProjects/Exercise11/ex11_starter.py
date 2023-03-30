#!/usr/bin/python
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print(Belgium,'\n',"-"* len(Belgium))
print()
print(Belgium.replace(",","'"))
print()
print()
fields = Belgium.split(",")
popu = (fields[1])
popr = (fields[3])
print ("Population of Belgium" ,
       fields[1] ,"+" , "population of Brussels",
       fields[3] , "gives you a total population of" ,
       int(popu) + int(popr))
