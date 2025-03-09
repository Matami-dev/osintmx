#!/usr/bin/env python3
#THIS VERSION IS ONLY FOR ANDROID TERMUX USER
import os
import re
import sys
import requests
import phonenumbers
import socket
from time import sleep
from datetime import datetime
from termcolor import colored, cprint
import whois  # Module pour WHOIS
import dns.resolver  # Module pour les résolutions DNS
from pyfiglet import Figlet

os.system('clear')

def banner():
    if 'pyfiglet' in sys.modules:
        f = Figlet(font='slant')
        print(colored(f.renderText('OsintMx'), 'red'))
    else:
        title = r"""
  ___  ____ ___ _   _ _____   __  ____  __
 / _ \/ ___|_ _| \ | |_   _| |  \/  \ \/ /
| | | \___ \| ||  \| | | |   | |\/| |\  / 
| |_| |___) | || |\  | | |   | |  | |/  \ 
 \___/|____/___|_| \_| |_|   |_|  |_/_/\_\
        """
        print(colored(title, 'red'))
    print(colored("=" * 55, 'white'))
    print(colored("CREATED BY ", 'white') + colored("Matami", 'red', attrs=['bold']))
    print(colored("=" * 55, 'white'))

def menu():
    print(colored("\n[1]", 'red') + " Investigation Email")
    print(colored("[2]", 'red') + " Investigation Domaine")
    print(colored("[3]", 'red') + " Investigation IP")
    print(colored("[4]", 'red') + " Investigation Numéro")
    print(colored("[5]", 'red') + " Investigation Pseudo")
    print(colored("[0]", 'red') + " Quitter\n")

def check_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(regex, email)

def email_investigation():
    email = input("\nEntrez l'email: ")
    if not check_email(email):
        cprint("\n[!] Email invalide !", 'red')
        return
    
    cprint(f"\n[+] Analyse de {email}...", 'white')
    
    try:
        domain = email.split('@')[1]
        cprint(f"\n=== INFORMATIONS DOMAINE ===", 'red')
        domain_info = whois.whois(domain)
        print(f"Domaine : {domain_info.domain_name}")
        print(f"Créé le : {domain_info.creation_date}")
        print(f"Expire le : {domain_info.expiration_date}")
        print(f"Registrar : {domain_info.registrar}")
        print(f"Nameservers : {', '.join(domain_info.name_servers)}")
    except Exception as e:
        cprint(f"\n[!] Erreur lors de la récupération des informations WHOIS: {e}", 'red')

def domain_investigation():
    domain = input("\nEntrez le domaine: ")
    cprint(f"\n[+] Recherche WHOIS pour {domain}...", 'white')
    
    try:
        domain_info = whois.whois(domain)
        print(colored("\n=== INFORMATIONS WHOIS ===", 'red'))
        print(f"Créé le : {domain_info.creation_date}")
        print(f"Expire le : {domain_info.expiration_date}")
        print(f"Registrar : {domain_info.registrar}")
        print(f"Nameservers : {', '.join(domain_info.name_servers)}")
    except Exception as e:
        cprint(f"\n[!] Erreur WHOIS: {e}", 'red')

def ip_investigation():
    ip = input("\nEntrez l'adresse IP: ")
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        
        print(colored("\n=== GEOLOCALISATION IP ===", 'red'))
        print(f"Pays : {response.get('country', 'N/A')}")
        print(f"Région : {response.get('regionName', 'N/A')}")
        print(f"Ville : {response.get('city', 'N/A')}")
        print(f"Fournisseur : {response.get('isp', 'N/A')}")
        print(f"Coordonnées : {response.get('lat', 'N/A')}, {response.get('lon', 'N/A')}")
    except Exception as e:
        cprint(f"\n[!] Erreur de géolocalisation: {e}", 'red')

def phone_investigation():
    number = input("\nEntrez le numéro (avec indicatif): ")
    try:
        parsed = phonenumbers.parse(number, None)
        
        print(colored("\n=== INFO NUMERO ===", 'red'))
        print(f"Pays : {phonenumbers.region_code_for_number(parsed)}")
        print(f"Valide : {phonenumbers.is_valid_number(parsed)}")
        print(f"Type : {phonenumbers.number_type(parsed)}")
        
        from phonenumbers import carrier
        print(f"Opérateur : {carrier.name_for_number(parsed, 'fr')}")
    except Exception as e:
        cprint(f"\n[!] Erreur avec le numéro: {e}", 'red')

def username_investigation():
    username = input("\nEntrez le pseudo: ")
    print(colored("\n=== RECHERCHE SOCIALE ===", 'red'))
    
    sites = {
        'Facebook': f'https://facebook.com/{username}',
        'Twitter': f'https://twitter.com/{username}',
        'Instagram': f'https://instagram.com/{username}',
        'Github': f'https://github.com/{username}'
    }
    
    for site, url in sites.items():
        try:
            response = requests.head(url)
            print(f"{site}: {'Trouvé' if response.status_code == 200 else 'Non trouvé'}")
        except Exception as e:
            print(f"{site}: Erreur de connexion")

def main():
    banner()
    while True:
        menu()
        choice = input(colored(">>> ", 'red'))
        
        if choice == '1':
            email_investigation()
        elif choice == '2':
            domain_investigation()
        elif choice == '3':
            ip_investigation()
        elif choice == '4':
            phone_investigation()
        elif choice == '5':
            username_investigation()
        elif choice == '0':
            cprint("\n[+] Au revoir !", 'red')
            sys.exit()
        else:
            cprint("\n[!] Choix invalide !", 'red')
        
        input("\nAppuyez sur Entrée pour continuer...")
        os.system('clear')
        banner()

if __name__ == "__main__":
    main()
