#!/bin/bash

BLOG_DIR="./blog"

# Function to create HTML file
create_html_file() {
    local filename="$1"
    local title="$2"
    local description="$3"
    local keywords="$4"
    local h1="$5"
    local intro="$6"
    local content="$7"
    
    cat > "$BLOG_DIR/$filename" << 'HTMLEND'
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>'$title'</title>
    <meta name="description" content="'$description'">
    <meta name="keywords" content="'$keywords'">
    <meta name="author" content="AgebiologiqueEU">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-E4MKJ0DYER"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-E4MKJ0DYER');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9253381108126567" crossorigin="anonymous"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body class="bg-gray-50">
<nav class="bg-white shadow-md"><div class="container mx-auto px-4 py-4"><div class="flex justify-between items-center"><a href="https://agebiologique.eu/" class="flex items-center space-x-2 text-blue-600"><i data-lucide="arrow-left"></i><span class="font-semibold">Retour</span></a><a href="https://agebiologique.eu/" class="text-2xl font-bold text-blue-600">AgebiologiqueEU</a></div></div></nav>
<div class="container mx-auto px-4 py-4"><div class="bg-gray-200 h-24 flex items-center justify-center text-gray-500">AdSense Top</div></div>
<main class="container mx-auto px-4 py-8 max-w-4xl"><article class="bg-white rounded-lg shadow-lg p-8">
<h1 class="text-4xl font-bold mb-4">'$h1'</h1>
<p class="text-lg text-gray-700 mb-6">'$intro'</p>
'$content'
<div class="bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg p-8 text-white text-center my-8">
<h3 class="text-2xl font-bold mb-4">Calculez Votre Âge Biologique</h3>
<a href="https://agebiologique.eu/" class="inline-block bg-white text-blue-600 font-bold py-3 px-8 rounded-full">Faire le Test</a>
</div>
</article></main>
<footer class="bg-gray-900 text-white py-8"><div class="container mx-auto px-4 text-center"><p class="text-gray-400">Avertissement médical : Informations à titre informatif uniquement.</p><p>&copy; 2025 AgebiologiqueEU</p></div></footer>
<script>lucide.createIcons();</script>
</body>
</html>
HTMLEND
}

echo "Script loaded"
