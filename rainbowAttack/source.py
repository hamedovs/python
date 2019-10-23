import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    InF = open(input_file_name)
    hashdict = {}
    reader = csv.reader(InF)
    for row in reader:
        Name = row[0]
        Hash = row[1]
        hashdict[Hash] = Name

    passdict = {}
    for i in range(1000, 10000):
        sha_signature = hashlib.sha256(str(i).encode()).hexdigest()
        if sha_signature in hashdict.keys():
            Temp = hashdict[sha_signature]
            passdict[Temp] = i

    with open(output_file_name, 'w') as OuF:
        for key in passdict.keys():
            OuF.write("%s,%s\n"%(key,passdict[key]))
