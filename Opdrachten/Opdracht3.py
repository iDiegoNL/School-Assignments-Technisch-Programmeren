bedrag = int(input('Geef bedrag tussen 0 en 500 eurocent: '))
totaal = 0

for munt in 1, 5, 10, 100, 250, 500:
    aantal = 0

    while bedrag >= munt:
        aantal += 1
        bedrag -= munt
        totaal += 1

    if aantal > 0:
        print(aantal, 'x', munt)

print('Aantal munten: ', totaal)
