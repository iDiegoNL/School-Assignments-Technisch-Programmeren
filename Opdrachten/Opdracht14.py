euromunten = [200, 100, 50, 20, 10, 5, 2, 1]

oudeNLmunten = [500, 250, 100, 25, 10, 5, 1]


def openTekstbestand():
    bestandsnaam = input('Geef naam van tekstbestand met bedragen: ')

    return open(bestandsnaam, 'r')


def verwerkTekstbestanden(file_in):
    for regel in file_in:
        bedrag = eval(regel)
        print('%3d:' % bedrag, minimaleBetaling(euromunten, bedrag))
        print('Gulden: ', '%3d: ' % bedrag, minimaleBetaling(oudeNLmunten, bedrag))
    minimaleBetaling(oudeNLmunten, bedrag)


def minimaleBetaling(munten, bedrag):
    betaling = []
    restbedrag = bedrag

    for munt in munten:
        while restbedrag >= munt:
            betaling.append(munt)
            restbedrag = restbedrag - munt
    assert restbedrag == 0
    return betaling


verwerkTekstbestanden(openTekstbestand())
