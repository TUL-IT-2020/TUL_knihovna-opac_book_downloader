# TUL knihovna opac book downloader

Toto je jednoduchý skript, který stahuje knihy z OPACu TUL knihovny. Skript je napsaný v Pythonu a je určen pro Linux, ale měl by fungovat i na Windows.

## Instalace:

1. Stáhněte si Python 3.6 nebo novější.
2. Stáhněte si repozitář.
3. Nainstalujte potřebné knihovny:

- Windows: 
```cmd
pip install -r dependencies.txt
```

- Linux: 
```bash
./install_libs.sh
```

## Použití:

1. Připojte se do sítě TUL pomocí VPN.
2. Otevřete si v prohlížeči školní knihovnu.
- https://knihovna-opac.tul.cz
3. Přihlaste se do svého účtu v knihovně.
4. Vyhledejte si knihu, kterou chcete stáhnout.
5. Rozklikněte si dokumenty ke stažení a zkopírujte **zkrácený** odakz na první stránku.
- Například v podobě: "https://knihovna-opac.tul.cz/media-viewer?rootDirectory=207986"
6. Spusťte na počítači skript:
```bash
python3 book_downloader.py
```

## Vývoj:
### Testování:
```bash
python -m unittest
```