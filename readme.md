# OsintMx - Outil d'OSINT (Open Source Intelligence)

![OsintMx Banner](https://image.noelshack.com/fichiers/2025/10/7/1741535656-make-me-a-banner-where-it-says-osint-mx-in-a-totally-black-background-white-writing-with-the-letter-vq04m6xxnlryr08fvxq2-3.png)  

## Description

**OsintMx** est un outil d'OSINT (Open Source Intelligence) développé en Python par **Matami**. Il permet de collecter des informations publiques sur des adresses e-mail, des domaines, des adresses IP, des numéros de téléphone et des pseudonymes. Cet outil est conçu pour les professionnels de la cybersécurité, les chercheurs et les passionnés d'investigation numérique.

## Fonctionnalités

- **Investigation d'e-mail** : Analyse un e-mail pour obtenir des informations sur le domaine associé (organisation, pays, etc.).
- **Investigation de domaine** : Récupère les informations WHOIS d'un domaine (date de création, expiration, registrar, etc.).
- **Investigation d'adresse IP** : Géolocalise une adresse IP et fournit des informations sur le fournisseur d'accès.
- **Investigation de numéro de téléphone** : Vérifie la validité d'un numéro de téléphone et identifie l'opérateur associé.
- **Investigation de pseudo** : Recherche un pseudonyme sur plusieurs réseaux sociaux (Facebook, Twitter, Instagram, GitHub).

## Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/Matami-dev/osintmx.git
   cd osintmx
   ```

2. **Installer les dépendances** :
   Assurez-vous d'avoir Python 3 installé, puis exécutez :
   ```bash
   pip install -r requirements.txt
   ```

3. **Exécuter l'outil** :
   ```bash
   python osintmx.py
   ```

## Utilisation

1. Lancez le script avec `python osintmx.py`.
2. Choisissez une option dans le menu principal :
   - `1` pour l'investigation d'e-mail.
   - `2` pour l'investigation de domaine.
   - `3` pour l'investigation d'adresse IP.
   - `4` pour l'investigation de numéro de téléphone.
   - `5` pour l'investigation de pseudo.
   - `0` pour quitter.

Suivez les instructions à l'écran pour entrer les informations nécessaires et obtenir les résultats.

## Exemple d'utilisation

### Investigation d'e-mail
```
Entrez l'email: example@domain.com
[+] Analyse de example@domain.com...
=== INFORMATIONS DOMAINE ===
Domaine : domain.com
Organisation : Example Corp
Pays : France
Emails associés : 10
```

### Investigation de domaine
```
Entrez le domaine: example.com
[+] Recherche WHOIS pour example.com...
=== INFORMATIONS WHOIS ===
Créé le : 2020-01-01
Expire le : 2025-01-01
Registrar : Registrar Inc.
Nameservers : ns1.example.com, ns2.example.com
```

## Captures d'écran

![Capture d'écran 1](https://image.noelshack.com/fichiers/2025/10/7/1741535920-mxosint.png)  


## Avertissement

Cet outil est conçu à des fins éducatives et légales uniquement. L'utilisation de cet outil pour des activités illégales est strictement interdite. L'auteur n'est pas responsable de toute utilisation abusive de ce logiciel.

## Crédits

- **Développeur** : [Matami](https://github.com/Matami-dev)

---

**OsintMx** est un projet open source. Les contributions sont les bienvenues ! Si vous souhaitez améliorer cet outil, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.
