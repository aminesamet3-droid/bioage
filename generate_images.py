#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur d'Images Automatique pour BioAge
Crée 23 images professionnelles avec dégradés et texte
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Configuration couleurs brand
COLORS = {
    'blue': (59, 130, 246),      # #3B82F6
    'purple': (147, 51, 234),    # #9333EA
    'white': (255, 255, 255),
    'dark': (17, 24, 39),        # #111827
    'light_blue': (96, 165, 250) # #60A5FA
}

def create_gradient(width, height, color1, color2, direction='horizontal'):
    """Crée un dégradé entre deux couleurs"""
    base = Image.new('RGB', (width, height), color1)
    top = Image.new('RGB', (width, height), color2)
    mask = Image.new('L', (width, height))
    mask_data = []

    if direction == 'horizontal':
        for x in range(width):
            mask_data.extend([int(255 * (x / width))] * height)
    elif direction == 'vertical':
        for y in range(height):
            mask_data.extend([int(255 * (y / height))] * width)
    elif direction == 'diagonal':
        for y in range(height):
            for x in range(width):
                mask_data.append(int(255 * ((x + y) / (width + height))))

    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def add_text_with_shadow(draw, text, position, font, fill_color, shadow_color, shadow_offset=3):
    """Ajoute du texte avec ombre portée"""
    x, y = position
    # Ombre
    draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill=shadow_color)
    # Texte principal
    draw.text(position, text, font=font, fill=fill_color)

def wrap_text(text, font, max_width):
    """Découpe le texte en plusieurs lignes si trop long"""
    words = text.split(' ')
    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = font.getbbox(test_line)
        width = bbox[2] - bbox[0]

        if width <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    return lines

def create_image(width, height, title, subtitle='', output_path='image.jpg', gradient_direction='diagonal'):
    """Crée une image avec titre et sous-titre"""

    # Créer dégradé
    img = create_gradient(width, height, COLORS['blue'], COLORS['purple'], gradient_direction)
    draw = ImageDraw.Draw(img)

    # Overlay semi-transparent pour améliorer lisibilité
    overlay = Image.new('RGBA', (width, height), (17, 24, 39, 100))
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    draw = ImageDraw.Draw(img)

    try:
        # Essayer de charger une police système
        title_font = ImageFont.truetype('arial.ttf', int(height * 0.12))
        subtitle_font = ImageFont.truetype('arial.ttf', int(height * 0.06))
        small_font = ImageFont.truetype('arial.ttf', int(height * 0.04))
    except:
        try:
            title_font = ImageFont.truetype('Arial.ttf', int(height * 0.12))
            subtitle_font = ImageFont.truetype('Arial.ttf', int(height * 0.06))
            small_font = ImageFont.truetype('Arial.ttf', int(height * 0.04))
        except:
            # Fallback sur police par défaut
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            small_font = ImageFont.load_default()

    # Calculer position centrée pour le titre
    title_lines = wrap_text(title, title_font, width - 100)
    total_height = len(title_lines) * (height * 0.15)

    if subtitle:
        total_height += height * 0.1

    start_y = (height - total_height) / 2

    # Dessiner titre (multi-lignes si nécessaire)
    current_y = start_y
    for line in title_lines:
        bbox = title_font.getbbox(line)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) / 2
        add_text_with_shadow(draw, line, (x, current_y), title_font, COLORS['white'], (0, 0, 0, 180))
        current_y += height * 0.15

    # Dessiner sous-titre
    if subtitle:
        subtitle_lines = wrap_text(subtitle, subtitle_font, width - 100)
        for line in subtitle_lines:
            bbox = subtitle_font.getbbox(line)
            text_width = bbox[2] - bbox[0]
            x = (width - text_width) / 2
            add_text_with_shadow(draw, line, (x, current_y), subtitle_font, COLORS['light_blue'], (0, 0, 0, 150))
            current_y += height * 0.08

    # Ajouter branding en bas
    branding = 'agebiologique.eu'
    bbox = small_font.getbbox(branding)
    brand_width = bbox[2] - bbox[0]
    brand_x = (width - brand_width) / 2
    brand_y = height - height * 0.08
    add_text_with_shadow(draw, branding, (brand_x, brand_y), small_font, COLORS['white'], (0, 0, 0, 180), shadow_offset=2)

    # Sauvegarder avec compression optimale
    img.save(output_path, 'JPEG', quality=85, optimize=True)
    print(f'[OK] Cree: {output_path}')

def main():
    """Génère toutes les images nécessaires"""

    # Créer dossier images s'il n'existe pas
    images_dir = 'images'
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
        print(f'Dossier {images_dir}/ créé')

    print('\n=== GÉNÉRATION DES IMAGES BIOAGE ===\n')

    # 1. Hero Image Calculateur (1200x600)
    create_image(
        1200, 600,
        'Calculez Votre Âge Biologique',
        'Test Gratuit • Résultats Instantanés',
        f'{images_dir}/hero-calculateur.jpg',
        'diagonal'
    )

    # 2. Open Graph Image (1200x630)
    create_image(
        1200, 630,
        'BioAge',
        'Calculateur d\'Âge Biologique Gratuit',
        f'{images_dir}/og-image.jpg',
        'horizontal'
    )

    # 3. Twitter Card (1200x630)
    create_image(
        1200, 630,
        'Quel est Votre Âge Biologique ?',
        'Test Gratuit en 3 Minutes',
        f'{images_dir}/twitter-card.jpg',
        'vertical'
    )

    # 4-23. Images Blog (800x400)
    blog_images = {
        'comment-calculer-age-biologique': 'Comment Calculer Son Âge Biologique',
        'tests-age-biologique-fiables': 'Tests d\'Âge Biologique Fiables',
        'age-biologique-vs-chronologique': 'Âge Biologique vs Chronologique',
        'rajeunir-age-biologique': 'Rajeunir Son Âge Biologique',
        'facteurs-vieillissement': 'Facteurs du Vieillissement',
        'alimentation-anti-age': 'Alimentation Anti-Âge',
        'sport-age-biologique': 'Sport et Âge Biologique',
        'sommeil-vieillissement': 'Sommeil et Vieillissement',
        'stress-age-biologique': 'Stress et Âge Biologique',
        'calculateur-age-biologique-gratuit': 'Calculateur Gratuit',
        'jeunesse-biologique': 'Jeunesse Biologique',
        'vieillissement-cellulaire': 'Vieillissement Cellulaire',
        'telomeres-longevite': 'Télomères et Longévité',
        'antioxydants-anti-age': 'Antioxydants Anti-Âge',
        'mode-vie-sain': 'Mode de Vie Sain',
        'biomarqueurs-vieillissement': 'Biomarqueurs du Vieillissement',
        'supplements-anti-age': 'Suppléments Anti-Âge',
        'meditation-longevite': 'Méditation et Longévité',
        'hormones-age-biologique': 'Hormones et Âge Biologique',
        'calcul-esperance-vie': 'Calcul Espérance de Vie'
    }

    gradients = ['horizontal', 'vertical', 'diagonal']
    gradient_index = 0

    for filename, title in blog_images.items():
        create_image(
            800, 400,
            title,
            'Guide Complet',
            f'{images_dir}/blog-{filename}.jpg',
            gradients[gradient_index % 3]
        )
        gradient_index += 1

    print(f'\n=== TERMINE ===')
    print(f'[OK] 23 images creees dans {images_dir}/')
    print(f'[OK] Taille totale: ~2-3 MB')
    print(f'[OK] Pretes pour integration')
    print(f'\nProchaine etape: Remplacer les placeholders dans le code HTML')

if __name__ == '__main__':
    main()
