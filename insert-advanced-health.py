#!/usr/bin/env python3
"""
Script pour insérer le code de l'étape 'advanced-health' dans index.html
"""

# Lire le fichier index.html
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Lire le code à insérer
with open('advanced-health-step.js', 'r', encoding='utf-8') as f:
    insert_code = f.read()

# Trouver la ligne où insérer (ligne 993 = index 992)
# On cherche "if (step === 'wellbeing') {"
insert_index = None
for i, line in enumerate(lines):
    if "if (step === 'wellbeing') {" in line:
        insert_index = i
        break

if insert_index is None:
    print("ERREUR: Ligne d'insertion non trouvée!")
    exit(1)

print(f"Insertion à la ligne {insert_index + 1}")

# Insérer le code
# On ajoute des indentations appropriées (12 espaces pour matcher le code environnant)
indented_code = '\n'.join(['            ' + line if line.strip() else line
                           for line in insert_code.split('\n')])

# Insérer
lines.insert(insert_index, indented_code + '\n\n')

# Écrire le nouveau fichier
with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("✅ Code inséré avec succès!")
print(f"   Nombre de lignes ajoutées: {len(insert_code.split(chr(10)))}")
