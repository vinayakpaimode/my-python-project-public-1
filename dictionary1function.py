#search on net dictionary  function

print("dictionary knoting but keyn value pair")
d1 = {}
d2 ={"gopal":"program","shubham":"eaditing","vinayak":"program","sager":"agiculture"}
print(type(d1))#output-><class 'dict'>
print(d2)  #output->{'gopal': 'program', 'shubham': 'eaditing', ' vinayak': 'program', 'sager': 'agiculture'}
print(d2["gopal"])        #output -> program

#dictionary within dictionary
d3 ={"gopal":"program","shubham":"eaditing"," vinayak":"program","sager":"agiculture","home" : {"go":"vadgaon","sh":"kanhur","vi":"takali","sa":"kanhur"}}
print(d3)
#{'gopal': 'program', 'shubham': 'eaditing', ' vinayak': 'program', 'sager': 'agiculture', 'home': {'go': 'vadgaon', 'sh': 'kanhur', 'vi': 'takali', 'sa': 'kanhur'}}

print(d3["home"])       #output->{'go': 'vadgaon', 'sh': 'kanhur', 'vi': 'takali', 'sa': 'kanhur'}

# uses of copy function
#lets we take


d4 = d2
print("before deleting d4(\"vinayak\") = ",d4)   # output->before deleting d4("vinayak") =  {'gopal': 'program', 'shubham': 'eaditing', 'vinayak': 'program', 'sager': 'agiculture'}

print("before deleting d2(\"vinayak\") = ",d2) # output->before deleting d2("vinayak") =  {'gopal': 'program', 'shubham': 'eaditing', 'vinayak': 'program', 'sager': 'agiculture'}
del d4["vinayak"]  #output->after deleting d2("vinayak") =  {'gopal': 'program', 'shubham': 'eaditing', 'sager': 'agiculture'}
print("after deleting d4(\"vinayak\") = ",d4)   #output->after deleting d2("vinayak") =  {'gopal': 'program', 'shubham': 'eaditing', 'sager': 'agiculture'}
print("after deleting d2(\"vinayak\") = ",d2)    #ouput->after deleting d2("vinayak") =  {'gopal': 'program', 'shubham': 'eaditing', 'sager': 'agiculture'}


   #note : hence we use copy function

d5 ={"gopal":"program","shubham":"eaditing","vinayak":"program","sager":"agiculture"}

d6 = d5.copy()
print("before deleting d6(\"vinayak\") = ",d6) #output->before deleting d6("vinayak") =  {'gopal': 'program', 'shubham': 'eaditing', 'vinayak': 'program', 'sager': 'agiculture'}
print("before deleting d5(\"vinayak\") = ",d5) #output->before deleting d5("vinayak") =  {'gopal': 'program', 'shubham': 'eaditing', 'vinayak': 'program', 'sager': 'agiculture'}
del d6["vinayak"]
print("after deleting d6(\"vinayak\") = ",d6)  #output->after deleting d6("vinayak") =  {'gopal': 'program', 'shubham': 'eaditing', 'sager': 'agiculture'}
print("after deleting d5(\"vinayak\") = ",d5)   #output->after deleting d5("vinayak") =  {'gopal': 'program', 'shubham': 'eaditing', 'vinayak': 'program', 'sager': 'agiculture'}

 #  add more values in dictionary

print("before add values d2 = ",d2)  #output->before add values d2 =  {'gopal': 'program', 'shubham': 'eaditing', 'sager': 'agiculture'}
d2["vinu"]= "singing"                #at "vinu" we also write numbers
print("after add values d2 = ",d2)   #output->after add values d2 =  {'gopal': 'program', 'shubham': 'eaditing', 'sager': 'agiculture', 'vinu': 'singing'}

#delete values form  dictionary
print("before delete value from d2 = ",d2) #output->before delete value from d2 =  {'gopal': 'program', 'shubham': 'eaditing', 'sager': 'agiculture', 'vinu': 'singing'}
del d2["vinu"]
print("after delet values from d2 = ",d2) #output->after delet values from d2 =  {'gopal': 'program', 'shubham': 'eaditing', 'sager': 'agiculture'}\


# get() function

print(d2.get("gopal"))                     #output->program

#update() function
print("before update d2 ",d2)    #output->before update d2  {'gopal': 'program', 'shubham': 'eaditing', 'sager': 'agiculture'}
d2.update({"rahul":"dance"})
print("after update d2 ",d2)      #output->after update d2  {'gopal': 'program',                                 'shubham': 'eaditing', 'sager': 'agiculture', 'rahul': 'dance'}

# keys and items
print("key in d2",d2.keys())               #output->key in d2 dict_keys(['gopal',                                                   'shubham', 'sager', 'rahul'])
print("item in d2",d2.items())      #output->item in d2 dict_items([('gopal', 'program'), ('shubham', 'eaditing'), ('sager', 'agiculture'), ('rahul', 'dance')])


