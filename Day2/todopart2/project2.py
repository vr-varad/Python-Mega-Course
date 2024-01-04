experiments = ['1.Raw Data.txt','2.Reports.txt','3.Presentation.txt']

experiments = list(map(lambda x:x.replace('.','-',1),experiments))
print(experiments)

print('')