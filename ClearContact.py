NameOfFile = '00002.vcf'

with open(NameOfFile) as original_file:
    contacts = [[float(digit) for digit in line.split()] for line in original_file]
