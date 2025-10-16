#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script d'optimisation SEO pour toutes les pages HTML du site agebiologique.eu
Ajoute les balises meta manquantes, Open Graph, Twitter Cards et Schema.org
"""

import os
import re
from bs4 import BeautifulSoup
from pathlib import Path

def extract_page_info(soup, file_path):
    """Extrait les informations de la page pour générer les meta tags"""
    title_tag = soup.find('title')
    title = title_tag.string if title_tag else "BioAge"

    meta_desc = soup.find('meta', {'name': 'description'})
    description = meta_desc['content'] if meta_desc and meta_desc.get('content') else ""

    h1_tag = soup.find('h1')
    h1 = h1_tag.get_text(strip=True) if h1_tag else title

    # Déterminer l'URL basée sur le chemin du fichier
    # Normaliser le chemin pour éviter les ../
    file_path_normalized = os.path.normpath(file_path)

    # Extraire le chemin relatif depuis le dossier courant
    if 'blog' in file_path_normalized:
        rel_path = 'blog/' + os.path.basename(file_path_normalized)
    elif 'ville' in file_path_normalized:
        rel_path = 'ville/' + os.path.basename(file_path_normalized)
    elif 'thematiques' in file_path_normalized:
        rel_path = 'thematiques/' + os.path.basename(file_path_normalized)
    else:
        rel_path = os.path.basename(file_path_normalized)

    url = f"https://agebiologique.eu/{rel_path.replace(os.sep, '/')}"

    return {
        'title': title,
        'description': description if description else f"{h1} - Découvrez notre guide complet sur l'âge biologique.",
        'url': url,
        'h1': h1
    }

def create_seo_meta_tags(page_info):
    """Génère toutes les balises meta SEO manquantes"""
    meta_tags = []

    # Balises meta de base
    meta_tags.append('<meta name="robots" content="index, follow, max-image-preview:large">')
    meta_tags.append(f'<link rel="canonical" href="{page_info["url"]}">')
    meta_tags.append('<meta name="author" content="BioAge">')
    meta_tags.append('<meta name="language" content="French">')
    meta_tags.append('<meta name="geo.region" content="FR">')

    # Open Graph
    meta_tags.append('<meta property="og:locale" content="fr_FR">')
    meta_tags.append('<meta property="og:type" content="article">')
    meta_tags.append(f'<meta property="og:title" content="{page_info["title"]}">')
    meta_tags.append(f'<meta property="og:description" content="{page_info["description"]}">')
    meta_tags.append(f'<meta property="og:url" content="{page_info["url"]}">')
    meta_tags.append('<meta property="og:site_name" content="BioAge">')
    meta_tags.append('<meta property="og:image" content="https://agebiologique.eu/images/og-image.jpg">')
    meta_tags.append('<meta property="og:image:width" content="1200">')
    meta_tags.append('<meta property="og:image:height" content="630">')

    # Twitter Cards
    meta_tags.append('<meta name="twitter:card" content="summary_large_image">')
    meta_tags.append(f'<meta name="twitter:title" content="{page_info["title"]}">')
    meta_tags.append(f'<meta name="twitter:description" content="{page_info["description"][:200]}">')
    meta_tags.append('<meta name="twitter:image" content="https://agebiologique.eu/images/twitter-card.jpg">')

    return '\n    '.join(meta_tags)

def create_schema_article(page_info):
    """Crée le schema.org Article pour les pages de blog"""
    schema = f'''
    <!-- Schema.org Article -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{page_info["h1"]}",
      "description": "{page_info["description"]}",
      "url": "{page_info["url"]}",
      "datePublished": "2025-10-16",
      "dateModified": "2025-10-16",
      "author": {{
        "@type": "Organization",
        "name": "BioAge",
        "url": "https://agebiologique.eu/"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "BioAge",
        "url": "https://agebiologique.eu/",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://agebiologique.eu/images/logo.png"
        }}
      }},
      "mainEntityOfPage": {{
        "@type": "WebPage",
        "@id": "{page_info["url"]}"
      }},
      "image": "https://agebiologique.eu/images/og-image.jpg"
    }}
    </script>'''
    return schema

def create_schema_local_business(page_info, city_name):
    """Crée le schema.org LocalBusiness pour les pages villes"""
    schema = f'''
    <!-- Schema.org LocalBusiness -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Service",
      "name": "Calculateur d'Âge Biologique à {city_name}",
      "description": "{page_info["description"]}",
      "url": "{page_info["url"]}",
      "areaServed": {{
        "@type": "City",
        "name": "{city_name}",
        "address": {{
          "@type": "PostalAddress",
          "addressCountry": "FR"
        }}
      }},
      "provider": {{
        "@type": "Organization",
        "name": "BioAge",
        "url": "https://agebiologique.eu/"
      }}
    }}
    </script>'''
    return schema

def optimize_html_file(file_path):
    """Optimise un fichier HTML en ajoutant les balises SEO manquantes"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')
        head = soup.find('head')

        if not head:
            print(f"ERREUR - Pas de balise head dans {file_path}")
            return False

        # Verifier si deja optimise (presence de canonical)
        if head.find('link', {'rel': 'canonical'}):
            print(f"OK - Deja optimise : {file_path}")
            return False

        # Extraire les infos de la page
        page_info = extract_page_info(soup, file_path)

        # Créer les balises SEO
        seo_tags = create_seo_meta_tags(page_info)

        # Déterminer le type de schema selon le dossier
        if '/blog/' in file_path.replace('\\', '/'):
            schema = create_schema_article(page_info)
        elif '/ville/' in file_path.replace('\\', '/'):
            # Extraire le nom de la ville du fichier
            city_match = re.search(r'age-biologique-(.+)\.html', os.path.basename(file_path))
            city_name = city_match.group(1).replace('-', ' ').title() if city_match else "France"
            schema = create_schema_local_business(page_info, city_name)
        else:
            schema = create_schema_article(page_info)

        # Insérer les balises avant la fermeture de </head>
        # Trouver la position de </head> dans le contenu original
        head_close_pos = content.lower().find('</head>')

        if head_close_pos == -1:
            print(f"ERREUR - Balise head non trouvee dans {file_path}")
            return False

        # Insérer les nouvelles balises
        new_content = (
            content[:head_close_pos] +
            '\n    <!-- SEO Meta Tags -->\n    ' +
            seo_tags +
            '\n' +
            schema +
            '\n' +
            content[head_close_pos:]
        )

        # Sauvegarder le fichier optimise
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"OPTIMISE : {file_path}")
        return True

    except Exception as e:
        print(f"ERREUR sur {file_path}: {str(e)}")
        return False

def main():
    """Fonction principale"""
    print("=" * 80)
    print("OPTIMISATION SEO AUTOMATIQUE - agebiologique.eu")
    print("=" * 80)
    print()

    base_dir = Path('.')

    # Dossiers à traiter
    folders = ['blog', 'ville', 'thematiques']

    stats = {
        'total': 0,
        'optimized': 0,
        'skipped': 0,
        'errors': 0
    }

    for folder in folders:
        folder_path = base_dir / folder

        if not folder_path.exists():
            print(f"ATTENTION - Dossier non trouve : {folder_path}")
            continue

        print(f"\nTraitement du dossier : {folder}/")
        print("-" * 80)

        html_files = list(folder_path.glob('*.html'))

        for html_file in html_files:
            stats['total'] += 1

            result = optimize_html_file(str(html_file))

            if result:
                stats['optimized'] += 1
            elif result is False:
                stats['skipped'] += 1
            else:
                stats['errors'] += 1

    # Afficher les statistiques
    print("\n" + "=" * 80)
    print("STATISTIQUES D'OPTIMISATION")
    print("=" * 80)
    print(f"Total fichiers traites  : {stats['total']}")
    print(f"Fichiers optimises      : {stats['optimized']}")
    print(f"Fichiers ignores        : {stats['skipped']}")
    print(f"Erreurs                 : {stats['errors']}")
    print()

    if stats['optimized'] > 0:
        print("Optimisation terminee avec succes !")
        print()
        print("ACTIONS SUIVANTES :")
        print("1. Verifiez quelques fichiers pour confirmer les modifications")
        print("2. Testez avec Google Rich Results Test")
        print("3. Deployez sur le serveur")
        print("4. Soumettez a Google Search Console")
    else:
        print("Aucun fichier a optimiser (tous deja optimises)")

    print("=" * 80)

if __name__ == "__main__":
    main()
