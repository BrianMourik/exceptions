print("Hoe heet je?")
naam = input("")

jaaroud = -1

while jaaroud == -1:
    try:
        print("Hoe oud ben je? (getal)")
        jaaroud = int(input(""))

    except ValueError:
        print("Typ uw leeftijd in gehele jaren alstublieft (bijv: 16).")

    else:
        tothonderd = (100 - jaaroud)
        print("Hallo " + naam + " je bent " + str(jaaroud) + " oud, dan duurt het nog " + str(tothonderd) + " jaar voordat je 100 bent.")