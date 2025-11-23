import random
print ("Я загадал число от 1 до 100, угадай его, буду подсказывать")
s = random.randint(1, 100)
while True:
        C = input('введи число (от 1 до 100)')
        c = int(C)
        if c==s:
            print ('ты победил')
            break
        elif c>s:
            print ("меньше")
        elif c<s:
            print ('больше')


