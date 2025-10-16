#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de correction des URLs canoniques pour agebiologique.eu
Supprime les balises SEO mal formées et les remplace par les bonnes
"""

import os
import re
from pathlib import Path

def fix_canonical_urls(file_path):
    """Corrige les URLs canoniques dans un fichier HTML"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Sauvegarder le contenu original
        original_content = content

        # Supprimer toutes les balises SEO ajoutées précédemment (entre <!-- SEO Meta Tags --> et </script>)
        # Pattern pour trouver le bloc entier ajouté
        pattern = r'\n    <!-- SEO Meta Tags -->.*?</script>\n'
        content = re.sub(pattern, '\n', content, flags=re.DOTALL)

        # Si le contenu a changé, sauvegarder
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"NETTOYE : {file_path}")
            return True
        else:
            print(f"RIEN A FAIRE : {file_path}")
            return False

    except Exception as e:
        print(f"ERREUR sur {file_path}: {str(e)}")
        return False

def main():
    """Fonction principale"""
    print("=" * 80)
    print("NETTOYAGE DES BALISES SEO - agebiologique.eu")
    print("=" * 80)
    print()

    base_dir = Path('.')
    folders = ['blog', 'ville', 'thematiques']

    stats = {
        'total': 0,
        'fixed': 0,
        'skipped': 0
    }

    for folder in folders:
        folder_path = base_dir / folder

        if not folder_path.exists():
            continue

        print(f"\nNettoyage du dossier : {folder}/")
        print("-" * 80)

        html_files = list(folder_path.glob('*.html'))

        for html_file in html_files:
            stats['total'] += 1

            result = fix_canonical_urls(str(html_file))

            if result:
                stats['fixed'] += 1
            else:
                stats['skipped'] += 1

    print("\n" + "=" * 80)
    print("STATISTIQUES")
    print("=" * 80)
    print(f"Total fichiers traites : {stats['total']}")
    print(f"Fichiers nettoyes      : {stats['fixed']}")
    print(f"Fichiers ignores       : {stats['skipped']}")
    print()
    print("Maintenant relancez optimize_all_pages.py pour reoptimiser avec les bonnes URLs")
    print("=" * 80)

if __name__ == "__main__":
    main()
