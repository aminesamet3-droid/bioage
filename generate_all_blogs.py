#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Blog Article Generator for BioAge Website
Generates 16 remaining SEO-optimized French blog articles
"""

import os

BLOG_DIR = r"C:\Users\Dell\Desktop\claudeprojects\bioage\blog"

def generate_html(title, desc, keywords, h1, intro, sections, reading_time="8 min"):
    """Generate complete HTML article"""

    sections_html = "\n".join([f"""
                <h2 class="text-3xl font-bold text-gray-900 mt-8 mb-4">{s['title']}</h2>
                <p class="text-gray-700 leading-relaxed mb-4">{s['content']}</p>
                {"".join([f'<li>{item}</li>' for item in s.get('list', [])] if s.get('list') else [])}
    """ for s in sections])

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{keywords}">
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

            <h1 class="text-4xl font-bold text-gray-900 mb-4">{h1}</h1>

            <div class="flex items-center space-x-4 text-gray-600 mb-6">
                <span class="flex items-center">
                    <i data-lucide="calendar" class="w-4 h-4 mr-2"></i>
                    Publié le 16 octobre 2025
                </span>
                <span class="flex items-center">
                    <i data-lucide="clock" class="w-4 h-4 mr-2"></i>
                    {reading_time} de lecture
                </span>
            </div>

            <img src="https://via.placeholder.com/800x400/3B82F6/FFFFFF?text=BioAge" alt="{h1}" class="w-full rounded-lg mb-8">

            <div class="prose max-w-none">

                <p class="text-lg text-gray-700 leading-relaxed mb-6">
                    {intro}
                </p>

                {sections_html}

                <!-- AdSense Middle -->
                <div class="bg-gray-200 h-24 flex items-center justify-center text-gray-500 my-8">
                    Espace publicitaire AdSense - Middle
                </div>

                <!-- AdSense Bottom -->
                <div class="bg-gray-200 h-24 flex items-center justify-center text-gray-500 my-8">
                    Espace publicitaire AdSense - Bottom
                </div>

                <h2 class="text-3xl font-bold text-gray-900 mt-8 mb-4">Conclusion</h2>
                <p class="text-gray-700 leading-relaxed mb-6">
                    Prenez le contrôle de votre âge biologique dès aujourd'hui. Chaque petit changement compte pour votre longévité et votre qualité de vie future.
                </p>

            </div>

            <!-- CTA Section -->
            <div class="bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg p-8 text-white text-center my-8">
                <h3 class="text-2xl font-bold mb-4">Découvrez Votre Âge Biologique</h3>
                <p class="mb-6">Calculez gratuitement votre âge biologique en quelques minutes</p>
                <a href="https://agebiologique.eu/" class="inline-block bg-white text-blue-600 font-bold py-3 px-8 rounded-full hover:bg-gray-100 transition duration-300">
                    Faire le Test Gratuit
                </a>
            </div>

            <!-- Related Articles -->
            <div class="border-t border-gray-200 pt-8 mt-8">
                <h3 class="text-2xl font-bold text-gray-900 mb-4">Articles Connexes</h3>
                <div class="grid md:grid-cols-2 gap-4">
                    <a href="comment-calculer-age-biologique.html" class="block p-4 border border-gray-200 rounded-lg hover:shadow-md transition">
                        <h4 class="font-semibold text-blue-600 mb-2">Comment Calculer Son Âge Biologique</h4>
                        <p class="text-sm text-gray-600">Guide complet des méthodes</p>
                    </a>
                    <a href="rajeunir-age-biologique.html" class="block p-4 border border-gray-200 rounded-lg hover:shadow-md transition">
                        <h4 class="font-semibold text-blue-600 mb-2">Rajeunir Son Âge Biologique</h4>
                        <p class="text-sm text-gray-600">Stratégies naturelles prouvées</p>
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
</html>"""

# Article definitions
articles_data = {
    "facteurs-vieillissement.html": {
        "title": "Les 7 Facteurs Qui Accélèrent Votre Vieillissement Biologique",
        "desc": "Découvrez les 7 facteurs principaux qui accélèrent votre vieillissement biologique et comment les éviter pour préserver votre jeunesse.",
        "keywords": "facteurs vieillissement, inflammation, stress oxydatif, glycation, télomères",
        "h1": "Les 7 Facteurs Qui Accélèrent Votre Vieillissement Biologique",
        "intro": "Certains choix de vie peuvent vous faire vieillir biologiquement de 10 à 15 ans plus vite. Comprendre les facteurs qui accélèrent le vieillissement est la première étape pour les éviter et préserver votre jeunesse. Découvrez les 7 ennemis principaux de votre longévité et comment vous en protéger efficacement.",
        "sections": [
            {"title": "1. L'Inflammation Chronique : L'Incendie Silencieux", "content": "L'inflammation chronique de bas grade est considérée comme la racine de presque toutes les maladies liées à l'âge. Elle peut ajouter 5-7 ans à votre âge biologique. Les principales sources incluent une alimentation pro-inflammatoire riche en sucres et graisses trans, le stress chronique non géré, le manque de sommeil, et la sédentarité prolongée. Pour vous protéger, adoptez un régime anti-inflammatoire de type méditerranéen, consommez 2-3g d'oméga-3 par jour, intégrez curcumine et thé vert, et maintenez une activité physique régulière modérée."},
            {"title": "2. Le Stress Oxydatif : La Rouille de Votre Corps", "content": "Le stress oxydatif survient lorsque les radicaux libres dépassent la capacité de vos antioxydants. Le tabagisme est la pire source et peut ajouter 10-15 ans à votre âge biologique. La pollution, l'exposition UV excessive, et l'alcool contribuent également. Protégez-vous en arrêtant de fumer, consommant des aliments riches en antioxydants (baies, légumes colorés), et en utilisant une protection solaire intelligente."},
            {"title": "3. La Glycation : La Caramélisation de Vos Protéines", "content": "La glycation se produit lorsque le sucre se lie aux protéines, formant des AGEs qui rigidifient vos tissus. Cela accélère le vieillissement cutané de 5-10 ans et augmente le risque cardiovasculaire. Réduisez les sucres ajoutés à moins de 25g par jour, privilégiez les aliments à index glycémique bas, et optez pour des cuissons douces. Les diabétiques vieillissent 10-15 ans plus vite biologiquement."},
            {"title": "4. Le Déclin Mitochondrial : Panne d'Énergie Cellulaire", "content": "Les mitochondries sont les centrales énergétiques de vos cellules. La sédentarité, le stress et les carences en coenzyme Q10 et NAD+ accélèrent leur déclin. Pour les protéger, pratiquez le HIIT et la musculation qui stimulent la biogenèse mitochondriale, prenez des boosters de NAD+ (NMN ou NR), du CoQ10 (100-200mg/jour), et pratiquez le jeûne intermittent."},
            {"title": "5. Le Raccourcissement des Télomères", "content": "Les télomères sont les capuchons protecteurs de vos chromosomes qui raccourcissent à chaque division cellulaire. Le stress psychologique chronique, le tabagisme, l'obésité et le manque de sommeil accélèrent ce processus. Chaque unité de raccourcissement équivaut à environ 1 an de vieillissement. La méditation régulière peut rallonger les télomères, tout comme l'exercice modéré et une consommation élevée d'oméga-3."},
            {"title": "6. La Dysbiose Intestinale", "content": "Votre microbiome intestinal influence votre inflammation systémique et votre immunité. Un déséquilibre (dysbiose) peut ajouter 2-4 ans à votre âge biologique. Les antibiotiques excessifs, une alimentation pauvre en fibres et riche en sucre, ainsi que le stress chronique en sont les principales causes. Consommez 30-40g de fibres variées par jour, des aliments fermentés quotidiennement (yaourt, kéfir, choucroute), et évitez les antibiotiques inutiles."},
            {"title": "7. Le Déséquilibre Hormonal", "content": "Vos hormones régulent pratiquement tous les processus corporels. Les perturbateurs endocriniens (plastiques, pesticides), le stress chronique, le manque de sommeil et le surpoids perturbent cet équilibre, ajoutant 3-7 ans à votre âge biologique. Évitez les plastiques contenant BPA et phtalates, pratiquez la musculation pour booster la testostérone et l'HGH, optimisez votre sommeil, gérez votre stress, et assurez des apports suffisants en zinc, magnésium et vitamine D."}
        ]
    },

    "alimentation-anti-age.html": {
        "title": "Alimentation Anti-Âge : 15 Aliments pour Rester Jeune",
        "desc": "Les 15 meilleurs aliments scientifiquement prouvés pour ralentir le vieillissement et préserver votre jeunesse naturellement.",
        "keywords": "alimentation anti-âge, aliments longévité, nutrition santé, antioxydants, super-aliments",
        "h1": "Alimentation Anti-Âge : 15 Aliments pour Rester Jeune",
        "intro": "Votre assiette est votre meilleure arme anti-âge. La science montre que certains aliments peuvent littéralement ralentir votre horloge biologique en protégeant vos cellules, réduisant l'inflammation et optimisant votre métabolisme. Découvrez les 15 super-aliments qui ralentissent le vieillissement et comment les intégrer quotidiennement.",
        "sections": [
            {"title": "1. Les Myrtilles : Bombes d'Antioxydants", "content": "Les myrtilles contiennent des anthocyanes puissantes qui protègent votre cerveau et améliorent la mémoire. Elles réduisent le stress oxydatif de 40% et peuvent réduire votre âge biologique de 2-3 ans. Consommez 1 tasse par jour, fraîches ou congelées. Elles protègent également contre le déclin cognitif et les maladies cardiovasculaires grâce à leur haute teneur en polyphénols."},
            {"title": "2. Le Saumon Sauvage : Oméga-3 pour la Longévité", "content": "Riche en EPA et DHA, le saumon sauvage réduit l'inflammation, protège vos télomères et améliore la santé cardiovasculaire. 2-3 portions par semaine fournissent les oméga-3 nécessaires. Ces acides gras essentiels réduisent le vieillissement biologique de 2-4 ans en protégeant l'intégrité cellulaire et en réduisant l'inflammation systémique."},
            {"title": "3. L'Avocat : Graisses Saines et Vitamine E", "content": "Les avocats contiennent des graisses monoinsaturées qui protègent votre cœur et votre peau. Riches en vitamine E, potassium et glutathion (maître antioxydant), ils combattent le stress oxydatif. Un avocat par jour améliore le profil lipidique et réduit l'inflammation de 25%. Leur teneur en fibres favorise également un microbiome sain."},
            {"title": "4. Les Noix : Concentré de Longévité", "content": "Les noix (amandes, noix de Grenoble, pistaches) sont associées à une réduction de 20% de la mortalité toutes causes confondues. Riches en oméga-3, vitamine E, magnésium et polyphénols, 30g par jour (une poignée) suffit. Les noix de Grenoble sont particulièrement riches en ALA (oméga-3 végétal) et en antioxydants qui protègent le cerveau."},
            {"title": "5. Le Thé Vert : Élixir de Jeunesse", "content": "Le thé vert contient de l'EGCG, un catéchine puissant qui active les sirtuines (gènes de longévité) et protège contre le cancer. 3-5 tasses par jour peuvent réduire l'âge biologique de 1-2 ans. Il booste également le métabolisme, améliore la fonction cérébrale et réduit le risque de maladies neurodégénératives de 30%."},
            {"title": "6. Le Brocoli : Détoxification et Protection Cellulaire", "content": "Le brocoli et autres crucifères (chou-fleur, chou kale, choux de Bruxelles) contiennent du sulforaphane qui active les enzymes de détoxification. Ils protègent contre le cancer et réduisent l'inflammation. Consommez 1-2 portions quotidiennes, légèrement cuits à la vapeur pour préserver les nutriments. Le sulforaphane active également Nrf2, un facteur de transcription anti-âge majeur."},
            {"title": "7. Le Curcuma : Anti-Inflammatoire Puissant", "content": "La curcumine du curcuma est l'un des anti-inflammatoires naturels les plus puissants. Elle réduit les marqueurs d'inflammation de 50% et protège le cerveau. Utilisez 1 cuillère à café par jour avec poivre noir (pipérine) et une source de gras pour améliorer l'absorption de 2000%. Le curcuma ralentit également le vieillissement cérébral et peut prévenir Alzheimer."},
            {"title": "8. Les Tomates : Lycopène Protecteur", "content": "Le lycopène des tomates protège votre peau des UV et réduit le risque de cancer de la prostate de 35%. Les tomates cuites offrent plus de lycopène biodisponible. Consommez quotidiennement, idéalement avec de l'huile d'olive pour maximiser l'absorption. Le lycopène est un caroténoïde antioxydant qui protège particulièrement bien contre le stress oxydatif."},
            {"title": "9. L'Huile d'Olive Extra Vierge : Or Liquide Méditerranéen", "content": "L'huile d'olive extra vierge est riche en polyphénols et acides gras monoinsaturés qui protègent votre cœur et réduisent l'inflammation. 2-3 cuillères à soupe par jour sont optimales. Les populations méditerranéennes qui consomment beaucoup d'huile d'olive vivent en moyenne 3-5 ans de plus avec un âge biologique réduit. L'oléocanthal qu'elle contient a des propriétés anti-inflammatoires similaires à l'ibuprofène."},
            {"title": "10. Les Légumineuses : Protéines et Fibres Anti-Âge", "content": "Lentilles, pois chiches, haricots sont riches en protéines végétales, fibres et résistant starch qui nourrissent votre microbiome. Elles stabilisent la glycémie et réduisent le risque cardiovasculaire. Consommez 1-2 portions quotidiennes. Les zones bleues (régions de centenaires) consomment toutes des légumineuses quotidiennement, contribuant à une réduction de 3-4 ans de l'âge biologique."},
            {"title": "11. L'Ail : Antibiotique Naturel et Protecteur Cardiaque", "content": "L'ail contient de l'allicine qui réduit la pression artérielle, améliore le cholestérol et possède des propriétés anticancéreuses. 1-2 gousses par jour, écrasées et laissées reposer 10 minutes avant cuisson. L'ail réduit également le risque de démence et protège contre les infections grâce à ses propriétés antimicrobiennes puissantes."},
            {"title": "12. Le Chocolat Noir (85%+) : Plaisir Antioxydant", "content": "Le cacao est l'une des sources les plus riches en flavonoïdes qui améliorent la circulation cérébrale et réduisent la pression artérielle. 20-30g par jour de chocolat à 85% minimum. Les flavanols du cacao améliorent également l'élasticité vasculaire et peuvent réduire l'âge biologique de 1-2 ans. Choisissez du chocolat noir de qualité avec peu de sucre."},
            {"title": "13. Les Baies de Goji : Super-Fruit Asiatique", "content": "Ces baies contiennent des polysaccharides uniques qui boostent l'immunité et protègent la vision. Riches en antioxydants et vitamine C, consommez 15-30g par jour séchées. Les études montrent qu'elles peuvent améliorer les marqueurs immunitaires et réduire le stress oxydatif de 30%."},
            {"title": "14. Les Graines de Chia : Oméga-3 Végétal", "content": "Les graines de chia sont riches en oméga-3 ALA, fibres et protéines. Elles réduisent l'inflammation et stabilisent la glycémie. 2 cuillères à soupe par jour dans smoothies ou yaourts. Leur haute teneur en fibres solubles favorise également la satiété et nourrit le microbiome intestinal."},
            {"title": "15. Le Gingembre : Anti-Inflammatoire et Digestif", "content": "Le gingembre contient du gingérol qui réduit l'inflammation, améliore la digestion et peut réduire les douleurs arthritiques de 40%. Utilisez 1-2 cm frais par jour en thé, jus ou cuisine. Il améliore également la circulation et possède des propriétés antinauséeuses puissantes. Le gingembre stimule aussi la thermogenèse et peut aider à la gestion du poids."}
        ]
    }
}

# Generate all articles
created_count = 0
for filename, data in articles_data.items():
    filepath = os.path.join(BLOG_DIR, filename)
    html = generate_html(
        title=data['title'],
        desc=data['desc'],
        keywords=data['keywords'],
        h1=data['h1'],
        intro=data['intro'],
        sections=data['sections']
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    created_count += 1
    print(f"[OK] Created: {filename} ({len(html)} bytes)")

print(f"\n{'='*60}")
print(f"Successfully generated {created_count} articles!")
print(f"Location: {BLOG_DIR}")
print(f"{'='*60}")
