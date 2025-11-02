#!/usr/bin/env python3
"""
Script pour supprimer tous les blocs AdSense React du fichier index.html
"""

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Pattern à supprimer : le bloc AdSense complet (5 lignes)
# React.createElement('div', { className: 'mb-6 bg-gray-100... },
#     React.createElement('p', { className: 'text-sm font-semibold mb-2' }, '📢 ESPACE PUBLICITAIRE GOOGLE ADSENSE'),
#     React.createElement('p', { className: 'text-xs' }, 'Collez votre code AdSense ici une fois approuvé (728x90 pixels)')
# ),

new_lines = []
skip_count = 0
removed_count = 0

for i, line in enumerate(lines):
    # Si on est en mode skip, décrémenter et passer
    if skip_count > 0:
        skip_count -= 1
        continue

    # Détecter le début d'un bloc AdSense
    if 'ESPACE PUBLICITAIRE GOOGLE ADSENSE' in line:
        # C'est la ligne 2 du bloc (la première ligne de texte)
        # On doit supprimer 5 lignes au total:
        # - La ligne avant (div opener)
        # - Cette ligne
        # - La ligne après (deuxième texte)
        # - La ligne après (fermeture p)
        # - La ligne après (fermeture div + virgule)

        # Supprimer la dernière ligne ajoutée (div opener)
        if new_lines:
            new_lines.pop()

        # Skip les 4 prochaines lignes
        skip_count = 4
        removed_count += 1
        continue

    new_lines.append(line)

# Écrire le résultat
with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Removed {removed_count} AdSense blocks")
print(f"Lines removed: {len(lines) - len(new_lines)}")
