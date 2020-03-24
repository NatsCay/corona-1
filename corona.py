import requests

rs = requests.Session()

url = rs.get('https://api.kawalcorona.com')

data = url.json()

indo = data[37]['attributes']

negara = indo['Country_Region']
positif = indo['Confirmed']
mati = indo['Deaths']
sembuh = indo['Recovered']

def menu():
	print('    [ DATA KASUS CORONA DI INDONESIA ]')
	print('')
	print('    [•] Author  : Pandas ID')
	print('    [•] Contact : WA : 082250223147')
	print('                  FB : Pandas ID')
	print('')
	print("    [*] Data diambil dari 'https://kawalcorona.com'")
	print('')
	print('    ==================================')
	info()
	
def info():
	print('')
	print('    [•] Negara :',negara)
	print('    [•] Positif Corona : ' + str(positif) + ' orang')
	print('    [•] Meniggal : ' + str(mati) + ' orang')
	print('    [•] Sembuh : ' + str(sembuh) + ' orang')
menu()
