bedrag = int(input('Geef bedrag tussen 0 en 500 eurocent: '))

for munt in 200, 100, 50, 20, 10, 5, 2, 1:
    aantal = 0

    while bedrag >= munt:
        aantal = aantal + 1
        bedrag = bedrag - munt

    if aantal > 0:
        print(aantal, 'x', munt)
