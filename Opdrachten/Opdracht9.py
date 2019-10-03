euromunten = [1, 2, 5, 10, 20, 50, 100, 200]

munten = euromunten
munten.sort()
print('Beschikbare munten: ', munten)
munten.reverse()
maxaantal = 0
maxbedrag = 0

for bedrag in range(0, 501):
    aantal = 0
    restbedrag = bedrag

    for munt in munten:
        aantal = aantal + restbedrag // munt
        restbedrag = restbedrag % munt

    if aantal > maxaantal:
        maxaantal = aantal
        maxbedrag = bedrag

print('Minimale betaling van ', maxbedrag, ' vergt ', maxaantal, ' munten ')
