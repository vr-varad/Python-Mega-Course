date = input('Enter today date: ')
rate = input('How do you like to rate yuour day: ') + '\n'
thoughts = input('What are youtr thoughts:')
with open(f'./journal/{date}.txt','w+') as file:
    file.writelines(rate)
    file.writelines(thoughts)
