munten = [200, 100, 50, 20, 10, 5, 2, 1]

bestandsnaam_in = input('Geef naam van het tekstbestand met bedragen: ')

file_in = open(bestandsnaam_in, 'r')
print()

bestandsnaam_out = input('Geef naam voor tekstbestand voor opslaan: ')
file_out = open(bestandsnaam_out, 'at')

for regel in file_in:
    bedrag = eval(regel)
    print('%3d:' % (bedrag), end=' ')
    print('%3d:' % (bedrag), end=' ', file=file_out)

    betaling = []
    restbedrag = bedrag

    for munt in munten:
        while restbedrag >= munt:
            betaling.append(munt)
            restbedrag = restbedrag - munt

    assert restbedrag == 0

    print(betaling)
    print(betaling, file=file_out)

file_in.close()
file_out.close()
