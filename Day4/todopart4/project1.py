filename = ['1.doc', '2.report', '3.presentation']

new_filename = [x.replace('.', '-')+'.txt' for x in filename]
print(new_filename)