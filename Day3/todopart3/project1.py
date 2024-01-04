waiting_list = ['sen', 'ben', 'ken']
waiting_list.sort()
new_waiting_list = list(map(lambda x: f"{waiting_list.index(x)+1}.{x.capitalize()}", waiting_list))

for x in sorted(new_waiting_list):
    print(x)