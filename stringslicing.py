mystr = "vinayak paimode"
mystr1= "vinayakpaimode"
    #    012345678911234
    #    543211987654321 -   negative
print(mystr[2])        # output :- n
print(len(mystr))      # output :-15
#print(mystr[50])      # output :-IndexError: string index out of range
 #there is no error
print(mystr[0:7:2])    # output :-vnyk
print(mystr[0:7:5])    # output :-va
print(mystr[:7:3])     # output :-vak
print(mystr[::2])      # output :-vnykpioe
print(mystr[0:7])      # output :-vinayak
print(mystr[:7])       # output :-vinayak
print(mystr[:7])       # output :-vinayak
print(mystr[:7:])      # output :-vinayak
print(mystr[0:50])     # output :-vinayak paimode
print(mystr[0::])      # output :-vinayak paimode
print(mystr[::])       # output :-vinayak paimode
print(mystr[::])       # output :-vinayak paimode


#negative indixeing

print(mystr[-4:-2])    # output :-mo  # note :-  both  are same
print(mystr[11:13])    # output :-mo  # note :-  both  are same
print(mystr[::-2])     # output :-eoipkynv

# some function
print(mystr.isalnum()) # output :- False
print(mystr1.isalnum()) # output :-True
print(mystr.isalpha()) # output :-False
print(mystr1.isalpha()) # output :-True


#  endswith function

print(mystr1.endswith("mode")) # output :-True
print(mystr1.endswith("gmode")) # output :-False

#count function
print(mystr.count("a"))           # output :-3

print(mystr.capitalize())         # output :-Vinayak paimode
print(mystr.count("a"))
print(mystr.lower())               # output :vinayak paimode
print(mystr.upper())               # output :-VINAYAK PAIMODE
print(mystr.replace("mo","he"))     # output :-vinayak paihede
