#!/bin/bash

# Script de vérification pré-déploiement BioAge
# Usage: bash verification.sh

echo "🔍 VÉRIFICATION PRÉ-DÉPLOIEMENT BIOAGE"
echo "======================================"
echo ""

# Couleurs
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Compteurs
total_checks=0
passed_checks=0
failed_checks=0

# Fonction de vérification
check() {
    total_checks=$((total_checks + 1))
    if [ $1 -eq 0 ]; then
        echo -e "${GREEN}✅ $2${NC}"
        passed_checks=$((passed_checks + 1))
    else
        echo -e "${RED}❌ $2${NC}"
        failed_checks=$((failed_checks + 1))
    fi
}

# 1. Vérifier fichiers racine
echo "📄 Fichiers de Configuration"
echo "----------------------------"

[ -f "index.html" ]
check $? "index.html existe"

[ -f "sitemap.xml" ]
check $? "sitemap.xml existe"

[ -f "robots.txt" ]
check $? "robots.txt existe"

echo ""

# 2. Vérifier dossiers
echo "📁 Structure des Dossiers"
echo "-------------------------"

[ -d "blog" ]
check $? "Dossier blog/ existe"

[ -d "ville" ]
check $? "Dossier ville/ existe"

[ -d "thematiques" ]
check $? "Dossier thematiques/ existe"

echo ""

# 3. Compter les fichiers
echo "📊 Comptage des Pages"
echo "---------------------"

blog_count=$(find blog -name "*.html" 2>/dev/null | wc -l)
[ "$blog_count" -eq 20 ]
check $? "20 articles de blog (trouvé: $blog_count)"

ville_count=$(find ville -name "*.html" 2>/dev/null | wc -l)
[ "$ville_count" -ge 20 ]
check $? "20+ pages villes (trouvé: $ville_count)"

theme_count=$(find thematiques -name "*.html" 2>/dev/null | wc -l)
[ "$theme_count" -eq 10 ]
check $? "10 pages thématiques (trouvé: $theme_count)"

total_pages=$((blog_count + ville_count + theme_count + 1))
echo -e "${YELLOW}ℹ️  Total pages: $total_pages${NC}"

echo ""

# 4. Vérifier Google Analytics
echo "📈 Google Analytics"
echo "-------------------"

ga_count=$(grep -r "G-E4MKJ0DYER" --include="*.html" . 2>/dev/null | wc -l)
[ "$ga_count" -ge 50 ]
check $? "Analytics sur toutes les pages (trouvé: $ga_count)"

echo ""

# 5. Vérifier Google AdSense
echo "💰 Google AdSense"
echo "-----------------"

adsense_count=$(grep -r "ca-pub-9253381108126567" --include="*.html" . 2>/dev/null | wc -l)
[ "$adsense_count" -ge 50 ]
check $? "AdSense sur toutes les pages (trouvé: $adsense_count)"

echo ""

# 6. Vérifier liens internes
echo "🔗 Liens Internes"
echo "-----------------"

cta_count=$(grep -r "agebiologique.eu" --include="*.html" blog/ 2>/dev/null | wc -l)
[ "$cta_count" -ge 20 ]
check $? "CTAs vers page principale (trouvé: $cta_count)"

echo ""

# 7. Vérifier sitemap
echo "🗺️  Sitemap.xml"
echo "---------------"

sitemap_urls=$(grep -c "<loc>" sitemap.xml 2>/dev/null)
[ "$sitemap_urls" -ge 52 ]
check $? "52+ URLs dans sitemap (trouvé: $sitemap_urls)"

# Vérifier syntaxe XML
if command -v xmllint &> /dev/null; then
    xmllint --noout sitemap.xml 2>/dev/null
    check $? "Sitemap XML valide"
else
    echo -e "${YELLOW}⚠️  xmllint non installé, syntaxe XML non vérifiée${NC}"
fi

echo ""

# 8. Vérifier robots.txt
echo "🤖 Robots.txt"
echo "-------------"

grep -q "Sitemap: https://agebiologique.eu/sitemap.xml" robots.txt 2>/dev/null
check $? "Sitemap déclaré dans robots.txt"

grep -q "User-agent: Googlebot" robots.txt 2>/dev/null
check $? "Googlebot configuré"

echo ""

# 9. Vérifier meta tags
echo "🏷️  Meta Tags SEO"
echo "----------------"

title_count=$(grep -r "<title>" --include="*.html" . 2>/dev/null | wc -l)
[ "$title_count" -ge 50 ]
check $? "Titles sur toutes les pages (trouvé: $title_count)"

desc_count=$(grep -r 'name="description"' --include="*.html" . 2>/dev/null | wc -l)
[ "$desc_count" -ge 50 ]
check $? "Descriptions sur toutes les pages (trouvé: $desc_count)"

echo ""

# 10. Vérifier responsivité
echo "📱 Responsive Design"
echo "--------------------"

viewport_count=$(grep -r 'name="viewport"' --include="*.html" . 2>/dev/null | wc -l)
[ "$viewport_count" -ge 50 ]
check $? "Viewport meta sur toutes les pages (trouvé: $viewport_count)"

tailwind_count=$(grep -r "tailwindcss.com" --include="*.html" . 2>/dev/null | wc -l)
[ "$tailwind_count" -ge 50 ]
check $? "Tailwind CSS chargé partout (trouvé: $tailwind_count)"

echo ""

# 11. Vérifier performance
echo "⚡ Performance"
echo "-------------"

lucide_count=$(grep -r "lucide@latest" --include="*.html" . 2>/dev/null | wc -l)
[ "$lucide_count" -ge 50 ]
check $? "Lucide Icons (légers) partout (trouvé: $lucide_count)"

# Vérifier absence d'images lourdes
heavy_images=$(find . -name "*.jpg" -o -name "*.png" -o -name "*.gif" | wc -l)
[ "$heavy_images" -eq 0 ]
check $? "Pas d'images lourdes (placeholders uniquement)"

echo ""

# 12. Sécurité
echo "🔒 Sécurité"
echo "-----------"

[ ! -d ".git" ] || [ -f ".gitignore" ]
check $? "Pas de .git exposé (ou .gitignore présent)"

sensitive_files=$(find . -name "*.env" -o -name "*.key" -o -name "*.pem" | wc -l)
[ "$sensitive_files" -eq 0 ]
check $? "Pas de fichiers sensibles (.env, .key, etc.)"

echo ""

# RÉSUMÉ FINAL
echo "======================================"
echo "📊 RÉSUMÉ"
echo "======================================"
echo ""
echo -e "Total vérifications: ${YELLOW}$total_checks${NC}"
echo -e "Réussies: ${GREEN}$passed_checks${NC}"
echo -e "Échouées: ${RED}$failed_checks${NC}"
echo ""

# Calcul du pourcentage
percentage=$((passed_checks * 100 / total_checks))

if [ $percentage -eq 100 ]; then
    echo -e "${GREEN}🎉 PARFAIT ! Site prêt au déploiement (100%)${NC}"
    echo ""
    echo "📋 Prochaines étapes:"
    echo "1. Upload vers hébergeur"
    echo "2. Configurer DNS"
    echo "3. Activer HTTPS"
    echo "4. Soumettre sitemap à Google"
    exit 0
elif [ $percentage -ge 90 ]; then
    echo -e "${GREEN}✅ Excellent ! Site prêt au déploiement ($percentage%)${NC}"
    echo ""
    echo "⚠️  Vérifiez les points échoués ci-dessus"
    exit 0
elif [ $percentage -ge 75 ]; then
    echo -e "${YELLOW}⚠️  Presque prêt ($percentage%) - Corrigez les erreurs${NC}"
    exit 1
else
    echo -e "${RED}❌ Attention ! Plusieurs problèmes détectés ($percentage%)${NC}"
    echo "Corrigez les erreurs avant déploiement"
    exit 1
fi
