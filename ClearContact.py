NameOfFile = '00002.vcf'

lines = [line.rstrip('\n') for line in open(NameOfFile)]
for line in lines:
    print line
