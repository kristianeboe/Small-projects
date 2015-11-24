def concatenate_files(filename1, filename2, new_filename):
    file1 = open(filename1, 'r')
    file2 = open(filename2, 'r')
    new_file_txt = file1.read() + file2.read()
    new_file = open(new_filename, 'w+')
    new_file.write(new_file_txt)

concatenate_files("alice1.txt", "alice2.txt", "new_alice.txt")
