"""  
Skapa en variabel för ditt födelseår
Programmet ska sedan skriva ut din ålder

Exempel på utskrift, det inom () ska ändras om variablerna ändras:
Du är (16) år gammal.

"""
# Skapa en variabel för ditt födelseår
fodelsear = 2008  # Ändra till ditt födelseår

# Hämta det aktuella året automatiskt
from datetime import datetime
aktuellt_ar = datetime.now().year

# Beräkna åldern
alder = aktuellt_ar - fodelsear

# Skriv ut åldern
print(f"Du är ({alder}) år gammal.")