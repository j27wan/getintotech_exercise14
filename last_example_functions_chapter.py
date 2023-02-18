# Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# Country = Country, Population, Capital, Population of capital, Continent, Established, Currency, Religion, Official Languages

countries = []
for line in open ('country.txt'):
    countries.append(line.split(','))

countries.sort(key=lambda c: int(c[1]))
# sorting into size order, smallest population first

for line in countries:
    print(','.join(line), end='')
