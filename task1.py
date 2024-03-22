from random import uniform


with open('my_digit.txt', 'w') as f:
    i = 0
    while i < 10000:
        digit = uniform(0, 10000)
        digit_string = str(digit)
        f.write(digit_string + '\n')
        i +=1
    f.close()

with open('my_digit.txt', 'r') as f:
    data = f.read()
    data = data.split('\n')
    sum = 0
    try:
        for i in data:
            sum = sum + float(i)
    except ValueError:
            reesult = 'Числа закінчились'
            print(reesult)
    f.close()

print(sum)