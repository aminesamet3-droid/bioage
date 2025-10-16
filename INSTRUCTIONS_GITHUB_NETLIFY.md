# 🚀 Instructions Déploiement - GitHub + Netlify

## ✅ Préparation Locale (COMPLÉTÉ)

Votre code est prêt :
- ✓ Git initialisé
- ✓ 115 fichiers commités (2 commits)
- ✓ README.md à jour
- ✓ .gitignore configuré
- ✓ netlify.toml + _headers prêts

---

## ÉTAPE 1 : Créer le Dépôt GitHub (5 min)

### A. Créer un compte GitHub (si vous n'en avez pas)
1. Aller sur : https://github.com/signup
2. Entrer votre email
3. Créer un mot de passe
4. Choisir un nom d'utilisateur (ex: `bioage-project` ou votre nom)
5. Vérifier votre email

### B. Créer le dépôt
1. Une fois connecté, aller sur : https://github.com/new

2. Remplir le formulaire :
   ```
   Repository name:    bioage-website
   Description:        Calculateur d'âge biologique - Site SEO optimisé
   Visibility:         ○ Public  (sélectionner Public)

   NE PAS cocher :
   ☐ Add a README file
   ☐ Add .gitignore
   ☐ Choose a license
   ```

3. Cliquer **"Create repository"** (bouton vert en bas)

### C. Copier l'URL du dépôt
Après création, GitHub affiche une page avec des instructions.

**Copier l'URL HTTPS** qui ressemble à :
```
https://github.com/[VOTRE-USERNAME]/bioage-website.git
```

**IMPORTANT :** Remplacez `[VOTRE-USERNAME]` par votre vrai nom d'utilisateur GitHub.

**Exemple :**
- Si votre username est `johnsmith`, l'URL sera :
  ```
  https://github.com/johnsmith/bioage-website.git
  ```

---

## ÉTAPE 2 : Pousser le Code vers GitHub (3 min)

### A. Ouvrir un terminal
1. Appuyer sur **Windows + R**
2. Taper : `cmd` et appuyer sur **Entrée**
3. Vous êtes maintenant dans l'invite de commandes

### B. Naviguer vers le projet
Dans le terminal, copier-coller cette commande :

```bash
cd "C:\Users\Dell\Desktop\claudeprojects\bioage"
```

Appuyer sur **Entrée**

### C. Ajouter l'origine GitHub

**ATTENTION :** Remplacez `[VOTRE-USERNAME]` par votre nom d'utilisateur GitHub réel !

```bash
git remote add origin https://github.com/[VOTRE-USERNAME]/bioage-website.git
```

**Exemple concret :**
```bash
git remote add origin https://github.com/johnsmith/bioage-website.git
```

Appuyer sur **Entrée**

### D. Vérifier que l'origine est ajoutée

```bash
git remote -v
```

**Résultat attendu :**
```
origin  https://github.com/[VOTRE-USERNAME]/bioage-website.git (fetch)
origin  https://github.com/[VOTRE-USERNAME]/bioage-website.git (push)
```

### E. Renommer la branche en 'main'

```bash
git branch -M main
```

Appuyer sur **Entrée**

### F. Pousser le code

```bash
git push -u origin main
```

**Si demandé :**
- Username : `[votre-username-github]`
- Password : **Utilisez un Personal Access Token** (voir section suivante)

#### Créer un Personal Access Token (si demandé)

GitHub ne permet plus les mots de passe simples. Vous devez créer un token :

1. Aller sur : https://github.com/settings/tokens
2. Cliquer **"Generate new token"** → **"Generate new token (classic)"**
3. Remplir :
   ```
   Note:               BioAge Deployment
   Expiration:         90 days
   Scopes:             ☑ repo (cocher toute la section)
   ```
4. Scroller en bas → Cliquer **"Generate token"**
5. **COPIER LE TOKEN** (ghp_xxxxxxxxxxxx)
   ⚠️ Vous ne le verrez qu'une fois !
6. Utiliser ce token comme mot de passe dans le terminal

**Résultat attendu après push :**
```
Enumerating objects: 117, done.
Counting objects: 100% (117/117), done.
Delta compression using up to 8 threads
Compressing objects: 100% (115/115), done.
Writing objects: 100% (117/117), 1.2 MiB | 2.4 MiB/s, done.
Total 117 (delta 15), reused 0 (delta 0)
To https://github.com/[VOTRE-USERNAME]/bioage-website.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

### G. Vérifier sur GitHub
1. Aller sur : `https://github.com/[VOTRE-USERNAME]/bioage-website`
2. Rafraîchir la page (F5)
3. Vous devriez voir tous vos fichiers (115 files)

**Bravo ! Votre code est sur GitHub !** ✅

---

## ÉTAPE 3 : Créer un Compte Netlify (2 min)

### A. S'inscrire
1. Aller sur : https://app.netlify.com/signup

2. **Option recommandée :** Cliquer sur **"Sign up with GitHub"**
   - Autoriser Netlify à accéder à GitHub
   - Connexion automatique
   - Plus simple pour le déploiement

   **Alternative :** Utiliser un email
   - Entrer votre email + mot de passe
   - Vérifier votre email

### B. Vérification
Après connexion, vous devriez voir :
- Dashboard Netlify vide
- Message "You don't have any sites yet"
- URL : `https://app.netlify.com/teams/[votre-username]/overview`

---

## ÉTAPE 4 : Déployer sur Netlify (5 min)

### A. Importer le site
1. Sur le dashboard Netlify, cliquer **"Add new site"** (bouton vert en haut à droite)
2. Sélectionner **"Import an existing project"**

### B. Connecter GitHub
1. Cliquer sur **"Deploy with GitHub"**
2. Si demandé, autoriser Netlify à accéder à vos dépôts GitHub
3. Cliquer **"Authorize Netlify"**

### C. Sélectionner le dépôt
1. Dans la liste, chercher **"bioage-website"**
2. Cliquer dessus

**Si vous ne voyez pas le dépôt :**
- Cliquer **"Configure Netlify on GitHub"**
- Sélectionner **"All repositories"** ou uniquement `bioage-website`
- Sauvegarder
- Retourner sur Netlify et rafraîchir

### D. Configuration du Build
Sur la page de configuration :

```
Site name:           [laissez auto-généré ou changez]
Branch to deploy:    main
Build command:       [LAISSER VIDE]
Publish directory:   .
```

**IMPORTANT :**
- ✓ Branch : `main`
- ✓ Build command : **LAISSER VIDE** (site statique, pas de build)
- ✓ Publish directory : `.` (point = racine du projet)

### E. Déployer
1. Cliquer **"Deploy [nom-du-site]"** (bouton bleu en bas)
2. Attendre 30-60 secondes

**Vous verrez :**
```
Site deploy in progress...
↓
Building...
↓
Uploading...
↓
✓ Site is live
```

### F. Obtenir l'URL
Une fois le déploiement terminé :
- Netlify vous donne une URL aléatoire
- **Exemple :** `https://wonderful-cupcake-123abc.netlify.app`
- Cliquer sur l'URL pour voir votre site en ligne !

**Vérifications rapides :**
1. La page d'accueil s'affiche correctement
2. Les images se chargent
3. Le calculateur fonctionne
4. Le bandeau cookie apparaît

---

## ÉTAPE 5 : Configurer le Domaine agebiologique.eu (10 min)

### A. Ajouter le domaine personnalisé

1. Dans Netlify, aller dans **"Site configuration"** → **"Domain management"**
   (ou cliquer **"Set up a custom domain"** si visible)

2. Cliquer **"Add custom domain"** ou **"Add a domain"**

3. Entrer : `agebiologique.eu`

4. Cliquer **"Verify"**

5. Netlify vérifie si vous possédez le domaine
   - Cliquer **"Add domain"**

### B. Configurer aussi www (optionnel mais recommandé)

1. Cliquer **"Add domain alias"**
2. Entrer : `www.agebiologique.eu`
3. Cliquer **"Add alias"**

### C. Obtenir les serveurs DNS Netlify

Netlify vous proposera 2 options :

**OPTION 1 : Utiliser les DNS Netlify (RECOMMANDÉ)**

Netlify affiche 4 serveurs DNS :
```
dns1.p01.nsone.net
dns2.p01.nsone.net
dns3.p01.nsone.net
dns4.p01.nsone.net
```

**OPTION 2 : Configurer manuellement**

Netlify affiche une adresse IP :
```
Type: A
Nom: @
Cible: 75.2.60.5
```

---

## ÉTAPE 6 : Configurer le DNS chez votre Registraire

### Où avez-vous acheté agebiologique.eu ?
- OVH ?
- Gandi ?
- Namecheap ?
- Autre ?

### Instructions pour OVH (exemple)

1. Se connecter sur : https://www.ovh.com/manager/
2. Aller dans **"Noms de domaine"**
3. Cliquer sur **agebiologique.eu**
4. Onglet **"Zone DNS"** ou **"Serveurs DNS"**

**Si Option 1 (DNS Netlify) :**
5. Cliquer **"Modifier les serveurs DNS"**
6. Remplacer par :
   ```
   dns1.p01.nsone.net
   dns2.p01.nsone.net
   dns3.p01.nsone.net
   dns4.p01.nsone.net
   ```
7. Confirmer

**Si Option 2 (Enregistrements manuels) :**
5. Cliquer **"Ajouter une entrée"**
6. Sélectionner **"A"**
7. Remplir :
   ```
   Sous-domaine:  [vide ou @]
   Cible:         75.2.60.5
   ```
8. Sauvegarder
9. Répéter pour www :
   ```
   Type:          CNAME
   Sous-domaine:  www
   Cible:         wonderful-cupcake-123abc.netlify.app
   ```

### Attendre la propagation DNS
- Délai : **15 min à 48 heures** (généralement 1-2 heures)
- Vérifier sur : https://dnschecker.org/#A/agebiologique.eu

**Quand c'est propagé :**
- Vous verrez l'IP `75.2.60.5` partout dans le monde
- Ou les DNS Netlify si vous avez choisi l'option 1

---

## ÉTAPE 7 : Activer HTTPS (Automatique)

Une fois le DNS propagé (1-2h) :

1. Retourner sur Netlify
2. **"Site configuration"** → **"Domain management"** → **"HTTPS"**
3. Netlify détecte automatiquement le DNS
4. Cliquer **"Verify DNS configuration"**
5. Netlify génère un certificat SSL Let's Encrypt (2-10 minutes)
6. Une fois généré, activer **"Force HTTPS"**

**Résultat :**
- ✓ `http://agebiologique.eu` → redirige vers `https://agebiologique.eu`
- ✓ Cadenas vert dans le navigateur
- ✓ Site sécurisé

---

## ÉTAPE 8 : Vérifier le Site en Ligne

### A. Tester les URLs
Ouvrir dans votre navigateur :

```
✓ https://agebiologique.eu/
✓ https://agebiologique.eu/blog/comment-calculer-age-biologique.html
✓ https://agebiologique.eu/privacy-policy.html
✓ https://www.agebiologique.eu/ (doit rediriger vers sans www)
```

### B. Vérifier les images
1. Ouvrir : https://agebiologique.eu/blog/comment-calculer-age-biologique.html
2. L'image dégradé bleu→violet doit s'afficher
3. Pas de placeholder `via.placeholder.com`
4. Ouvrir F12 (DevTools) → Onglet "Network" → Filtrer "Images"
5. Vérifier que `blog-comment-calculer-age-biologique.jpg` charge (200 OK)

### C. Vérifier les headers de sécurité
1. Aller sur : https://securityheaders.com/
2. Entrer : `https://agebiologique.eu`
3. Cliquer **"Scan"**

**Score attendu : A ou A+**

Vérifier la présence de :
- ✓ Content-Security-Policy
- ✓ X-Frame-Options
- ✓ X-Content-Type-Options
- ✓ Strict-Transport-Security
- ✓ Referrer-Policy

### D. Tester la politique cookies
1. Ouvrir https://agebiologique.eu/ en **navigation privée**
2. Le bandeau cookie doit apparaître en bas
3. Cliquer **"Accepter tous les cookies"**
4. Le bandeau disparaît
5. Rafraîchir la page (F5)
6. Le bandeau ne doit PAS réapparaître (cookie mémorisé)

### E. Vérifier le calculateur
1. Sur la page d'accueil
2. Entrer des données dans le formulaire
3. Cliquer **"Calculer mon âge biologique"**
4. Le résultat doit s'afficher

---

## ÉTAPE 9 : Google Search Console (15 min)

### A. Créer un compte / Se connecter
1. Aller sur : https://search.google.com/search-console
2. Se connecter avec votre compte Google

### B. Ajouter la propriété
1. Cliquer **"Ajouter une propriété"**
2. Choisir **"Préfixe d'URL"**
3. Entrer : `https://agebiologique.eu`
4. Cliquer **"Continuer"**

### C. Vérifier la propriété

Google propose plusieurs méthodes. **La plus simple :**

**Méthode : Balise HTML**

1. Google vous donne une balise comme :
   ```html
   <meta name="google-site-verification" content="ABC123XYZ456..." />
   ```

2. **Copier cette balise complète**

3. Retourner sur votre ordinateur local

4. Ouvrir le fichier : `C:\Users\Dell\Desktop\claudeprojects\bioage\index.html`

5. Chercher la ligne `<head>` (ligne ~5)

6. Coller la balise juste après `<head>` :
   ```html
   <head>
       <meta name="google-site-verification" content="ABC123XYZ456..." />
       <meta charset="UTF-8">
       ...
   ```

7. Sauvegarder le fichier

8. Dans le terminal, pousser la modification :
   ```bash
   cd "C:\Users\Dell\Desktop\claudeprojects\bioage"
   git add index.html
   git commit -m "Add Google Search Console verification tag"
   git push
   ```

9. Attendre 1-2 minutes (déploiement automatique Netlify)

10. Retourner sur Google Search Console

11. Cliquer **"Vérifier"**

**Résultat :** ✓ Propriété vérifiée

### D. Soumettre le sitemap

1. Dans Search Console, menu gauche → **"Sitemaps"**
2. Dans le champ "Ajouter un sitemap", entrer : `sitemap.xml`
3. Cliquer **"Envoyer"**

**Résultat attendu :**
```
Statut:            Réussite
URLs découvertes:  52
```

### E. Demander l'indexation des pages prioritaires

1. Menu gauche → **"Inspection de l'URL"**
2. Entrer : `https://agebiologique.eu/`
3. Attendre le test
4. Cliquer **"Demander une indexation"**
5. Attendre la confirmation (1-2 min)

**Répéter pour :**
- `https://agebiologique.eu/blog/comment-calculer-age-biologique.html`
- `https://agebiologique.eu/blog/tests-age-biologique-fiables.html`
- `https://agebiologique.eu/blog/rajeunir-age-biologique.html`

**Total : 5 pages indexées manuellement**

---

## ✅ CHECKLIST COMPLÈTE

```
Phase Préparation
✓ Images générées (23 images)
✓ Git initialisé
✓ Commits créés (2)
✓ README mis à jour
✓ Configuration Netlify prête

Phase GitHub
☐ Compte GitHub créé
☐ Dépôt bioage-website créé
☐ Code poussé (git push)
☐ 115 fichiers visibles sur GitHub

Phase Netlify
☐ Compte Netlify créé
☐ Connexion GitHub ↔ Netlify
☐ Site importé depuis GitHub
☐ Déploiement réussi
☐ URL temporaire fonctionne (https://xxx.netlify.app)

Phase Domaine
☐ Domaine agebiologique.eu ajouté à Netlify
☐ DNS configuré chez registraire
☐ Propagation DNS vérifiée (dnschecker.org)
☐ HTTPS activé
☐ Force HTTPS activé
☐ https://agebiologique.eu fonctionne

Phase Vérifications
☐ Images s'affichent correctement
☐ Headers sécurité score A+ (securityheaders.com)
☐ Cookie consent fonctionne
☐ Calculateur fonctionne
☐ Toutes les pages accessibles

Phase SEO
☐ Google Search Console configuré
☐ Propriété vérifiée (balise HTML)
☐ Sitemap soumis (52 URLs)
☐ 5 pages indexées manuellement
```

---

## 🚀 PROCHAINES ÉTAPES (Après Déploiement)

### Semaine 1
- ☐ Installer Google Analytics (voir DEPLOIEMENT_NETLIFY.md)
- ☐ Partager sur Reddit (r/longevity, r/biohacking)
- ☐ Partager sur Twitter/Facebook
- ☐ Créer 2-3 premiers backlinks

### Semaine 2-4
- ☐ Créer 10-15 backlinks de qualité
- ☐ Publier 2 nouveaux articles blog
- ☐ Guest post sur blog santé
- ☐ Répondre à questions Quora avec lien

### Mois 2-3
- ☐ Atteindre 50+ visiteurs/jour
- ☐ Soumettre à Google AdSense
- ☐ Attendre approbation (1-2 semaines)
- ☐ Activer les annonces

---

## 📞 SUPPORT

### Problème : Git push refuse
**Erreur :** `Authentication failed`

**Solution :**
- Créer un Personal Access Token (voir ÉTAPE 2.F)
- Utiliser le token comme mot de passe

### Problème : Le dépôt GitHub n'apparaît pas sur Netlify
**Solution :**
1. Sur Netlify → Cliquer "Configure Netlify on GitHub"
2. Sélectionner "All repositories"
3. Sauvegarder
4. Retourner sur Netlify et rafraîchir

### Problème : Le domaine ne fonctionne pas
**Solution :**
1. Vérifier dnschecker.org (propagation DNS)
2. Attendre 1-24h
3. Vider cache DNS local : `ipconfig /flushdns`
4. Tester en navigation privée

### Problème : HTTPS ne s'active pas
**Solution :**
1. Vérifier que DNS est propagé (dnschecker.org)
2. Attendre 10-15 minutes
3. Netlify génère automatiquement le certificat
4. Rafraîchir la page Netlify

### Problème : Headers sécurité non détectés
**Solution :**
1. Vérifier que `_headers` est bien dans le dépôt GitHub
2. Vérifier les logs de déploiement Netlify
3. Attendre 5 minutes après déploiement
4. Vider cache navigateur (Ctrl+Shift+R)

---

## 🎉 C'EST PARTI !

Suivez ces instructions étape par étape et votre site sera en ligne dans **1-2 heures maximum**.

**Bonne chance avec BioAge !** 🚀

---

**Fichiers de référence :**
- `DEPLOIEMENT_NETLIFY.md` - Guide complet détaillé
- `PLAN_ACTION_IMMEDIAT.md` - Stratégie post-déploiement
- `EVALUATION_GLOBALE_SITE.md` - Projections revenus
