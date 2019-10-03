bedrag = int(input('Geef bedrag tussen 0 en 500 eurocent: '))

betaling = ''
restbedrag = bedrag

for munt in 200, 100, 50, 20, 10, 5, 2, 1:
    aantal = restbedrag // munt
    restbedrag = restbedrag % munt

    if aantal > 0:
        betaling = betaling + str(aantal) + ' x ' + str(munt) + '\n'

print(betaling)