NameOfFile = '00002.vcf'

lines = [line.rstrip('\n') for line in open(NameOfFile)]
for line in lines:
    if 'URL:' not in line:
        if 'PHOTO;' not in line:
            fh2 = open('cleraed.vcf','a')
            fh2.write(line)
            fh2.write('\n')
            fh2.close()
