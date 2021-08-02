import os

in_dir = "C:\\Users\\Tim\Desktop\\Protein Files\\KphWT"
out_dir = "C:\\Users\\Tim\\Desktop\\Protein Files\\text"
aa = ["A","R","N","D","B","C","E","Q","Z","G","H","I","L","K","M","F","P","S","T","U","W","Y","V"]
total_files = 0
for index, file in enumerate(os.listdir(in_dir)):
    file_name_to = ""
    aa_seq_curr = ""
    aa_seq_longest =""
    seq_end = -1
    index_last = 0

    file_contents = ""
    file_full = in_dir + "\\" + file
    with open(file_full, 'rb') as i:
            for index, line in enumerate(i):
                str_curr = str(line)
                for char in str_curr:
                    if char in aa:
                        aa_seq_curr += char
                    else: aa_seq_curr = ""
                    if len(aa_seq_curr) > len(aa_seq_longest):
                        aa_seq_longest = aa_seq_curr

    i.close()
    if aa_seq_longest == "":
        print("Didn't find seq for {}".format(file))


    for char in file:
        if not char == ".":
            file_name_to += char
        else: break
    file_name_to
    file_name_to_fasta = file_name_to + ".txt"
    file_dir_to = out_dir + "\\" + file_name_to_fasta

    file_write = aa_seq_longest
    r = open(file_dir_to, 'w')
    r.write(file_write)
    r.close()
    total_files += 1

print(file)
print(file_name_to_fasta)
print(file_dir_to)
print(total_files)
