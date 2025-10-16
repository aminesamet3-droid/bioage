#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to generate SEO-optimized blog articles in French for BioAge website
"""

import os

# Base directory
BLOG_DIR = "/c/Users/Dell/Desktop/claudeprojects/bioage/blog"

# Common HTML template
def create_article_html(data):
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['title']}</title>
    <meta name="description" content="{data['description']}">
    <meta name="keywords" content="{data['keywords']}">
    <meta name="author" content="AgebiologiqueEU">

    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-E4MKJ0DYER"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', 'G-E4MKJ0DYER');
    </script>

    <!-- Google AdSense -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9253381108126567"
     crossorigin="anonymous"></script>

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>

    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body class="bg-gray-50 text-gray-800">

    <!-- Navigation -->
    <nav class="bg-white shadow-md">
        <div class="container mx-auto px-4 py-4">
            <div class="flex justify-between items-center">
                <a href="https://agebiologique.eu/" class="flex items-center space-x-2 text-blue-600 hover:text-blue-800">
                    <i data-lucide="arrow-left"></i>
                    <span class="font-semibold">Retour au Calculateur</span>
                </a>
                <a href="https://agebiologique.eu/" class="text-2xl font-bold text-blue-600">AgebiologiqueEU</a>
            </div>
        </div>
    </nav>

    <!-- AdSense Top -->
    <div class="container mx-auto px-4 py-4">
        <div class="bg-gray-200 h-24 flex items-center justify-center text-gray-500">
            Espace publicitaire AdSense - Top
        </div>
    </div>

    <!-- Main Content -->
    <main class="container mx-auto px-4 py-8 max-w-4xl">

        <article class="bg-white rounded-lg shadow-lg p-8">

            <h1 class="text-4xl font-bold text-gray-900 mb-4">{data['h1']}</h1>

            <div class="flex items-center space-x-4 text-gray-600 mb-6">
                <span class="flex items-center">
                    <i data-lucide="calendar" class="w-4 h-4 mr-2"></i>
                    Publié le 16 octobre 2025
                </span>
                <span class="flex items-center">
                    <i data-lucide="clock" class="w-4 h-4 mr-2"></i>
                    {data['reading_time']} de lecture
                </span>
            </div>

            <img src="https://via.placeholder.com/800x400/{data['color']}/FFFFFF?text={data['placeholder']}" alt="{data['alt']}" class="w-full rounded-lg mb-8">

            <div class="prose max-w-none">

                <p class="text-lg text-gray-700 leading-relaxed mb-6">
                    {data['intro']}
                </p>

                {data['content']}

                <!-- AdSense Middle -->
                <div class="bg-gray-200 h-24 flex items-center justify-center text-gray-500 my-8">
                    Espace publicitaire AdSense - Middle
                </div>

                {data['content2']}

                <!-- AdSense Bottom -->
                <div class="bg-gray-200 h-24 flex items-center justify-center text-gray-500 my-8">
                    Espace publicitaire AdSense - Bottom
                </div>

                {data['conclusion']}

            </div>

            <!-- CTA Section -->
            <div class="bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg p-8 text-white text-center my-8">
                <h3 class="text-2xl font-bold mb-4">{data['cta_title']}</h3>
                <p class="mb-6">{data['cta_text']}</p>
                <a href="https://agebiologique.eu/" class="inline-block bg-white text-blue-600 font-bold py-3 px-8 rounded-full hover:bg-gray-100 transition duration-300">
                    {data['cta_button']}
                </a>
            </div>

            <!-- Related Articles -->
            <div class="border-t border-gray-200 pt-8 mt-8">
                <h3 class="text-2xl font-bold text-gray-900 mb-4">Articles Connexes</h3>
                <div class="grid md:grid-cols-2 gap-4">
                    <a href="{data['related1_link']}" class="block p-4 border border-gray-200 rounded-lg hover:shadow-md transition">
                        <h4 class="font-semibold text-blue-600 mb-2">{data['related1_title']}</h4>
                        <p class="text-sm text-gray-600">{data['related1_desc']}</p>
                    </a>
                    <a href="{data['related2_link']}" class="block p-4 border border-gray-200 rounded-lg hover:shadow-md transition">
                        <h4 class="font-semibold text-blue-600 mb-2">{data['related2_title']}</h4>
                        <p class="text-sm text-gray-600">{data['related2_desc']}</p>
                    </a>
                </div>
            </div>

        </article>

    </main>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-8 mt-16">
        <div class="container mx-auto px-4 text-center">
            <p class="text-gray-400 mb-4">
                <strong>Avertissement médical :</strong> Les informations fournies sur ce site sont à titre informatif uniquement et ne constituent pas un avis médical. Consultez toujours un professionnel de santé qualifié pour toute question concernant votre santé.
            </p>
            <p class="text-gray-500">
                &copy; 2025 AgebiologiqueEU. Tous droits réservés.
            </p>
        </div>
    </footer>

    <script>
        lucide.createIcons();
    </script>

</body>
</html>'''

# Articles data
articles = [
    {
        "filename": "facteurs-vieillissement.html",
        "title": "Les 7 Facteurs Qui Accélèrent Votre Vieillissement Biologique",
        "description": "Découvrez les 7 facteurs principaux qui accélèrent votre vieillissement biologique et comment les éviter pour préserver votre jeunesse.",
        "keywords": "facteurs vieillissement, accélération âge, stress oxydatif, inflammation, santé",
        "h1": "Les 7 Facteurs Qui Accélèrent Votre Vieillissement Biologique",
        "intro": "Savez-vous que certains choix de vie peuvent vous faire vieillir biologiquement de 10 à 15 ans plus vite ? Comprendre les facteurs qui accélèrent le vieillissement est la première étape pour les éviter et préserver votre jeunesse. Découvrez les 7 ennemis principaux de votre longévité et comment vous en protéger.",
        "content": """
                <h2 class="text-3xl font-bold text-gray-900 mt-8 mb-4">1. L'Inflammation Chronique : L'Incendie Silencieux</h2>

                <p class="text-gray-700 leading-relaxed mb-4">
                    L'inflammation chronique de bas grade est considérée comme la racine de presque toutes les maladies liées à l'âge. Contrairement à l'inflammation aiguë qui guérit vos blessures, l'inflammation chronique détruit lentement vos tissus de l'intérieur.
                </p>

                <div class="bg-red-50 border-l-4 border-red-600 p-6 mb-6 rounded-r-lg">
                    <h4 class="font-bold text-red-900 mb-3">Sources d'inflammation chronique :</h4>
                    <ul class="space-y-2 text-gray-700">
                        <li>• Alimentation pro-inflammatoire (sucres, graisses trans, aliments ultra-transformés)</li>
                        <li>• Surpoids et graisse viscérale excessive</li>
                        <li>• Sédentarité prolongée</li>
                        <li>• Stress chronique non géré</li>
                        <li>• Manque de sommeil</li>
                        <li>• Infections chroniques (gencives, intestins)</li>
                    </ul>
                </div>

                <p class="text-gray-700 leading-relaxed mb-6">
                    <strong>Impact :</strong> Peut ajouter 5-7 ans à votre âge biologique. L'inflammation accélère le raccourcissement des télomères et augmente dramatiquement le risque de maladies cardiovasculaires, diabète, Alzheimer et cancer.
                </p>

                <div class="bg-green-50 p-6 rounded-lg mb-6">
                    <h4 class="font-bold text-green-900 mb-3 flex items-center">
                        <i data-lucide="shield-check" class="w-5 h-5 mr-2"></i>
                        Comment se protéger :
                    </h4>
                    <ul class="space-y-2 text-gray-700">
                        <li>✓ Régime anti-inflammatoire (méditerranéen, DASH)</li>
                        <li>✓ Oméga-3 (2-3g/jour de poissons gras ou suppléments)</li>
                        <li>✓ Curcumine, gingembre, thé vert</li>
                        <li>✓ Exercice régulier modéré</li>
                        <li>✓ Maintenir un poids santé</li>
                    </ul>
                </div>

                <h2 class="text-3xl font-bold text-gray-900 mt-8 mb-4">2. Le Stress Oxydatif : La Rouille de Votre Corps</h2>

                <p class="text-gray-700 leading-relaxed mb-4">
                    Le stress oxydatif survient lorsque les radicaux libres (molécules instables) dépassent la capacité de vos antioxydants à les neutraliser. Ces radicaux libres endommagent vos cellules, votre ADN et accélèrent le vieillissement.
                </p>

                <ul class="list-disc pl-6 mb-6 space-y-2 text-gray-700">
                    <li><strong>Tabagisme :</strong> La pire source de radicaux libres</li>
                    <li><strong>Pollution :</strong> Air, eau, produits chimiques</li>
                    <li><strong>UV excessifs :</strong> Exposition solaire non protégée</li>
                    <li><strong>Alcool :</strong> Génère du stress oxydatif hépatique</li>
                </ul>

                <h2 class="text-3xl font-bold text-gray-900 mt-8 mb-4">3. La Glycation : Le Caramélisation de Vos Protéines</h2>

                <p class="text-gray-700 leading-relaxed mb-4">
                    La glycation se produit lorsque le sucre se lie aux protéines, formant des AGEs (Advanced Glycation End-products). Ces molécules rigidifient vos tissus, créant rides, perte d'élasticité vasculaire et dommages organiques.
                </p>

                <p class="text-gray-700 leading-relaxed mb-6">
                    <strong>Impact :</strong> Accélère le vieillissement cutané de 5-10 ans et augmente drastiquement le risque cardiovasculaire. Les diabétiques vieillissent biologiquement 10-15 ans plus vite.
                </p>
        """,
        "content2": """
                <h2 class="text-3xl font-bold text-gray-900 mt-8 mb-4">4. Le Déclin Mitochondrial</h2>

                <p class="text-gray-700 leading-relaxed mb-4">
                    Les mitochondries sont les centrales énergétiques de vos cellules. Avec l'âge, elles deviennent moins efficaces, produisant moins d'ATP (énergie) et plus de radicaux libres. C'est un cercle vicieux qui accélère le vieillissement.
                </p>

                <div class="bg-blue-50 p-6 rounded-lg mb-6">
                    <h4 class="font-bold text-blue-900 mb-3">Stratégies pour protéger vos mitochondries :</h4>
                    <ul class="space-y-2 text-gray-700">
                        <li>✓ HIIT et musculation (stimulent la biogenèse)</li>
                        <li>✓ NAD+ boosters (NMN, NR)</li>
                        <li>✓ CoQ10 (100-200mg/jour)</li>
                        <li>✓ Jeûne intermittent</li>
                        <li>✓ PQQ (10-20mg)</li>
                    </ul>
                </div>

                <h2 class="text-3xl font-bold text-gray-900 mt-8 mb-4">5. Le Raccourcissement des Télomères</h2>

                <p class="text-gray-700 leading-relaxed mb-4">
                    Les télomères sont les capuchons protecteurs à l'extrémité de vos chromosomes. Ils raccourcissent à chaque division cellulaire. Des télomères courts = vieillissement accéléré et risque de mortalité élevé.
                </p>

                <p class="text-gray-700 leading-relaxed mb-6">
                    Le stress chronique, le tabac, l'obésité et le manque de sommeil accélèrent ce raccourcissement. À l'inverse, la méditation, l'exercice et les oméga-3 peuvent les préserver voire les rallonger.
                </p>

                <h2 class="text-3xl font-bold text-gray-900 mt-8 mb-4">6. La Dysbiose Intestinale</h2>

                <p class="text-gray-700 leading-relaxed mb-4">
                    Votre microbiome intestinal influence votre immunité, votre inflammation et même votre humeur. Un déséquilibre (dysbiose) accélère le vieillissement via l'inflammation systémique et la perméabilité intestinale.
                </p>

                <ul class="list-disc pl-6 mb-6 space-y-2 text-gray-700">
                    <li>Consommez 30-40g de fibres variées par jour</li>
                    <li>Mangez des aliments fermentés quotidiennement</li>
                    <li>Évitez les antibiotiques inutiles</li>
                    <li>Diversifiez votre alimentation</li>
                </ul>

                <h2 class="text-3xl font-bold text-gray-900 mt-8 mb-4">7. Le Déséquilibre Hormonal</h2>

                <p class="text-gray-700 leading-relaxed mb-4">
                    Vos hormones régulent pratiquement tous les processus corporels. Le déclin hormonal naturel avec l'âge peut être accéléré par le stress, les toxines environnementales (perturbateurs endocriniens), le surpoids et le manque de sommeil.
                </p>

                <p class="text-gray-700 leading-relaxed mb-6">
                    Un déséquilibre hormonal se manifeste par fatigue, prise de poids, perte musculaire, libido réduite et humeur dépressive. La musculation, le sommeil optimal et l'évitement des plastiques aident à maintenir l'équilibre.
                </p>

                <div class="bg-blue-50 border-l-4 border-blue-600 p-6 my-8">
                    <p class="text-blue-900 font-semibold mb-2">
                        <i data-lucide="activity" class="inline w-5 h-5 mr-2"></i>
                        Évaluez Votre Exposition
                    </p>
                    <p class="text-blue-800">
                        Découvrez quels facteurs impactent votre âge biologique avec notre <a href="https://agebiologique.eu/" class="underline font-semibold">calculateur personnalisé gratuit</a>.
                    </p>
                </div>
        """,
        "conclusion": """
                <h2 class="text-3xl font-bold text-gray-900 mt-8 mb-4">Conclusion : Prenez le Contrôle</h2>

                <p class="text-gray-700 leading-relaxed mb-6">
                    Ces 7 facteurs peuvent sembler intimidants, mais la bonne nouvelle est que vous avez le pouvoir d'agir sur chacun d'eux. Même des changements modérés peuvent avoir un impact significatif. Commencez par identifier vos plus grands facteurs de risque et concentrez-vous sur un ou deux changements à la fois. La cohérence bat la perfection. Chaque jour où vous minimisez ces facteurs est un jour où vous ralentissez votre horloge biologique.
                </p>
        """,
        "reading_time": "9 min",
        "color": "EF4444",
        "placeholder": "Facteurs+Vieillissement",
        "alt": "Facteurs accélérant le vieillissement biologique",
        "cta_title": "Identifiez Vos Facteurs de Risque",
        "cta_text": "Calculez votre âge biologique et découvrez vos points d'amélioration prioritaires",
        "cta_button": "Faire Mon Diagnostic Gratuit",
        "related1_link": "rajeunir-age-biologique.html",
        "related1_title": "Comment Rajeunir Son Âge Biologique",
        "related1_desc": "Stratégies pour inverser le vieillissement",
        "related2_link": "stress-age-biologique.html",
        "related2_title": "Stress et Âge Biologique",
        "related2_desc": "L'impact du stress chronique"
    }
]

# Create articles
for article in articles:
    filepath = os.path.join(BLOG_DIR, article['filename'])
    html_content = create_article_html(article)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Created: {article['filename']}")

print(f"\nSuccessfully created {len(articles)} article(s)")
