from datetime import datetime
from colorama import Fore
import time
import os
import platform 
import requests


while(True):
	r = requests.get('https://api.moonpay.com/v3/currencies/ask_price?cryptoCurrencies=btc,eth,usdt&fiatCurrencies=usd,pln,eur,gbp,jpy&apiKey=pk_live_QWvwDl3WJAq7S8fDjsOUMfjn09DSw8R')
	r = r.json()
	btc_eur = r['BTC']['EUR']
	btc_usd = r['BTC']['USD']
	btc_pln = r['BTC']['PLN']
	eth_eur = r['ETH']['EUR']
	eth_usd = r['ETH']['USD']
	eth_pln = r['ETH']['PLN']
	if(platform.system().lower()=="windows"):
		cmd='cls'
	else:
		cmd='clear'
	os.system(cmd)
	now = datetime.now()
	print(f'╔═══════════════════════════════════════════╗')
	print(f'║                  {Fore.YELLOW}BTC {Fore.WHITE}PRICE ')
	print(f'╠═══════════════════════════════════════════╣')
	print(f'║EUR: {Fore.YELLOW}{btc_eur}{Fore.WHITE} €{Fore.WHITE}')
	print(f'║USD: {Fore.YELLOW}{btc_usd}{Fore.WHITE} ${Fore.WHITE}')
	print(f'║PLN: {Fore.YELLOW}{btc_pln}{Fore.WHITE} zł{Fore.WHITE}')
	print(f'╠═══════════════════════════════════════════╣')
	print(f'║                  {Fore.CYAN}ETH {Fore.WHITE}PRICE')
	print(f'╠═══════════════════════════════════════════╣')
	print(f'║EUR: {Fore.CYAN}{eth_eur}{Fore.WHITE} €{Fore.WHITE} ')
	print(f'║USD: {Fore.CYAN}{eth_usd}{Fore.WHITE} ${Fore.WHITE}')
	print(f'║PLN: {Fore.CYAN}{eth_pln}{Fore.WHITE} zł{Fore.WHITE}')
	print(f'╚═══════════════════════════════════════════╝')
	print()
	print(f'                  {Fore.WHITE}{now.strftime(f"%H{Fore.WHITE}:{Fore.WHITE}%M{Fore.WHITE}:{Fore.WHITE}%S")}{Fore.WHITE}')
	print()
	time.sleep(1)