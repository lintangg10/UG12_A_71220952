aw = int(input('Masukkan awal deret: '))
ak = int(input('Masukkan akhir deret: '))

for i in range(aw,ak):
    if i%3 != 0 and i%6 !=0 and i%2 != 0:
        print(i, ' ', end='') 
