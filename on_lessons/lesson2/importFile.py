def something_boom(rng, boom):
    d = range(1, rng)
    for num in d:
        if (num % boom) == 0:
            print('BOOM!!!!')
        elif str(boom) in str(num):
            print(f'it Has A - {boom}  : {num}')
        else:
            print(f'number -  {num}')
        num += 1