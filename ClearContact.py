NameOfFile = '00002.vcf'
numberofcontacts = 0
newcontacts = 0

listofwords = ['BEGIN:', 'VERSION:' ,'N:' , 'FN:', 'TEL;', 'END:'] #Remove field from this list if you want to remove it
lines = [line.rstrip('\n') for line in open(NameOfFile)]
for line in lines:
    if 'BEGIN:' in line:
        numberofcontacts = numberofcontacts +1  #For sanity check to be sure

for line in lines:
    if any(word in line for word in listofwords):
        fh2 = open('cleraed.vcf','a')
        fh2.write(line)
        fh2.write('\n')
        fh2.close()
        if 'BEGIN:' in line:
            newcontacts = newcontacts+1
print ("Original contacts:%d and New Contacts:%d")%(numberofcontacts,newcontacts)
