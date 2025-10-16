#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Remplacement Automatique des Placeholders
Remplace toutes les images placeholder par les vraies images dans les articles blog
"""

import os
import re

def replace_placeholders_in_file(filepath):
    """Remplace les placeholders dans un fichier HTML"""

    # Lire le fichier
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extraire le nom du fichier sans extension
    filename = os.path.basename(filepath).replace('.html', '')

    # Pattern pour trouver les placeholders
    pattern = r'<img\s+src="https://via\.placeholder\.com/[^"]+"\s+alt="([^"]+)"'

    # Nouvelle image
    new_image = f'<img src="../images/blog-{filename}.jpg" alt="\\1" loading="lazy"'

    # Remplacer
    new_content = re.sub(pattern, new_image, content)

    # Vérifier s'il y a eu des changements
    if new_content != content:
        # Écrire le fichier modifié
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    """Traite tous les fichiers blog"""

    blog_dir = 'blog'

    if not os.path.exists(blog_dir):
        print(f'[ERREUR] Dossier {blog_dir}/ introuvable')
        return

    print('\n=== REMPLACEMENT DES PLACEHOLDERS ===\n')

    modified_count = 0
    total_count = 0

    # Parcourir tous les fichiers HTML du blog
    for filename in os.listdir(blog_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(blog_dir, filename)
            total_count += 1

            if replace_placeholders_in_file(filepath):
                print(f'[OK] {filename}')
                modified_count += 1
            else:
                print(f'[SKIP] {filename} (pas de placeholder trouve)')

    print(f'\n=== TERMINE ===')
    print(f'[OK] {modified_count}/{total_count} fichiers modifies')
    print(f'[OK] Les placeholders sont remplaces par les vraies images')
    print(f'\nProchaine etape: Verifier 2-3 pages dans navigateur')

if __name__ == '__main__':
    main()
