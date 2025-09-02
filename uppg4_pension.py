"""  
Gör ett program som frågar användaren efter namn och ålder.
Programmet ska sedan skriva ut enligt nedan.
Räkna med att man går i pension vid 67 års ålder.

Exempel på utskrift, det inom () ska ändras om variablerna ändras:
Hej och välkommen till mitt program (Hampus). Du har (39) år kvar till pension.
"""

namn = input("Vad heter du? ")
ålder = int(input("Hur gammal är du? "))
pensionsålder = 67
år_kvar = pensionsålder - ålder
print(f"Hej och välkommen till mitt program {namn}. Du har {år_kvar} år kvar till pension.")

