munten = [200, 100, 50, 20, 10, 5, 2, 1]

bestandsnaam = input('Geef naam van tekstbestand met bedragen: ')

file_in = open(bestandsnaam, 'r')

for regel in file_in:
    bedrag = eval(regel)
    print('%3d:' % (bedrag), end=' ')

    betaling = []
    restbedrag = bedrag

    for munt in munten:
        while restbedrag >= munt:
            betaling.append(munt)
            restbedrag = restbedrag - munt

    assert restbedrag == 0

    print(betaling)
