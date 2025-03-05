# mode: r / w / a / a+

with open("adatok/szamozott_sorok.txt", "r", encoding="utf-8") as forrasfajl:
    with open("adatok/szamozott_sorok_masolat.txt", "w", encoding="utf-8") as celfajl:
        for sor in forrasfajl:
            print(sor.strip(), file=celfajl)