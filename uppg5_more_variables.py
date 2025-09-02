"""  
Skapa en variabel för ditt namn.
Skapa en variabel för din ålder.
Skriv ut ditt namn med hjälp av variabeln.

Skapa en variabel och låt användaren skriva in sitt namn med hjälp av input.
Skapa en variabel och låt användaren skriva in sin ålder med hjälp av input.

Skriv ut en mening som använder sig av alla 4 variabler. Åldern ska adderas ihop.

Exempel på utskrift, det inom () ska ändras om variablerna ändras:
Välkommen till mitt program (Oskar). Du och (Hampus) är (53) år tillsammans.

"""
# Skapa variabler för ditt eget namn och ålder
mitt_namn = "omar"
min_ålder = 17

# Skriv ut ditt namn med hjälp av variabeln
print("Mitt namn är:", mitt_namn)

# Skapa variabler för användarens namn och ålder
anv_namn = input("Vad heter du? ")
anv_ålder = int(input("Hur gammal är du? "))

# Addera åldrarna
total_ålder = min_ålder + anv_ålder

# Skriv ut meningen
print(f"Välkommen till mitt program {anv_namn}. vi är {total_ålder} år tillsammans.")