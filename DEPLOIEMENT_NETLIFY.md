# Guide de Déploiement Netlify - BioAge

## Préparation Complétée ✓

Votre site est prêt pour le déploiement :
- ✓ 115 fichiers commités (52 pages HTML, 23 images, configs)
- ✓ Dépôt Git initialisé
- ✓ Images professionnelles générées (0.48 MB)
- ✓ Configuration Netlify prête (netlify.toml + _headers)
- ✓ Sécurité RGPD complète

---

## ÉTAPE 1 : Créer un Compte Netlify (2 min)

### A. Inscription
1. Aller sur : https://app.netlify.com/signup
2. Choisir **"Sign up with GitHub"** (recommandé) ou Email
3. Confirmer votre email

### B. Vérification
- Vous devriez voir le dashboard Netlify vide
- URL : https://app.netlify.com/teams/[votre-username]/sites

---

## ÉTAPE 2 : Créer un Dépôt GitHub (3 min)

### A. Créer le dépôt
1. Aller sur : https://github.com/new
2. Remplir :
   - **Repository name** : `bioage-website`
   - **Description** : `Site de calcul d'âge biologique - agebiologique.eu`
   - **Visibility** : ✓ Public
   - **NE PAS** cocher "Initialize with README" (déjà fait)
3. Cliquer **"Create repository"**

### B. Lier votre projet local au dépôt GitHub

Ouvrir un terminal dans `C:\Users\Dell\Desktop\claudeprojects\bioage` et exécuter :

```bash
# Ajouter l'origine GitHub (remplacer [VOTRE-USERNAME] par votre nom d'utilisateur GitHub)
git remote add origin https://github.com/[VOTRE-USERNAME]/bioage-website.git

# Vérifier que c'est bien ajouté
git remote -v

# Pousser le code
git branch -M main
git push -u origin main
```

**Exemple :**
```bash
git remote add origin https://github.com/johnsmith/bioage-website.git
git branch -M main
git push -u origin main
```

### C. Vérification
- Rafraîchir la page GitHub
- Vous devriez voir tous vos fichiers (115 files)

---

## ÉTAPE 3 : Déployer sur Netlify (5 min)

### A. Importer le site
1. Sur Netlify : https://app.netlify.com/
2. Cliquer **"Add new site"** → **"Import an existing project"**
3. Choisir **"Deploy with GitHub"**
4. Autoriser Netlify à accéder à GitHub (si demandé)
5. Chercher et sélectionner **"bioage-website"**

### B. Configuration du build
Sur l'écran de configuration :

```
Build command:     (laisser vide)
Publish directory: .
Branch to deploy:  main
```

6. Cliquer **"Deploy [nom-du-site]"**

### C. Attendre le déploiement
- Le déploiement prend 30-60 secondes
- Vous verrez : "Site is live" avec une URL aléatoire

**Exemple d'URL temporaire :**
```
https://wonderful-cupcake-123abc.netlify.app
```

---

## ÉTAPE 4 : Configurer le Domaine agebiologique.eu (10 min)

### A. Ajouter le domaine personnalisé
1. Dans Netlify, aller dans **"Site settings"** → **"Domain management"**
2. Cliquer **"Add custom domain"**
3. Entrer : `agebiologique.eu`
4. Cliquer **"Verify"** → **"Add domain"**

### B. Configurer le DNS

Netlify vous donnera des serveurs DNS ou des enregistrements A/CNAME.

**Option 1 : Utiliser les serveurs DNS Netlify (recommandé)**
```
dns1.p01.nsone.net
dns2.p01.nsone.net
dns3.p01.nsone.net
dns4.p01.nsone.net
```

Aller chez votre registraire de domaine (OVH, Gandi, Namecheap, etc.) :
1. Se connecter
2. Aller dans la gestion DNS de `agebiologique.eu`
3. Remplacer les serveurs DNS par ceux de Netlify
4. Sauvegarder

**Option 2 : Configurer manuellement (si Option 1 impossible)**
```
Type   Name             Value
A      agebiologique.eu  75.2.60.5
CNAME  www              wonderful-cupcake-123abc.netlify.app
```

### C. Attendre la propagation DNS
- Délai : 15 minutes à 48 heures (généralement 1-2 heures)
- Vérifier sur : https://dnschecker.org/#A/agebiologique.eu

---

## ÉTAPE 5 : Activer HTTPS (automatique)

1. Dans Netlify : **"Site settings"** → **"Domain management"** → **"HTTPS"**
2. Cliquer **"Verify DNS configuration"**
3. Attendre que Netlify génère le certificat SSL (5-10 min après DNS propagé)
4. Activer **"Force HTTPS"** (redirection HTTP → HTTPS automatique)

---

## ÉTAPE 6 : Vérifier le Déploiement

### A. Tester les pages principales
```
✓ https://agebiologique.eu/
✓ https://agebiologique.eu/blog/comment-calculer-age-biologique.html
✓ https://agebiologique.eu/privacy-policy.html
```

### B. Vérifier les images
- Les 23 images doivent s'afficher correctement
- Pas de placeholder `via.placeholder.com`

### C. Vérifier les headers de sécurité
Tester sur : https://securityheaders.com/?q=https://agebiologique.eu

**Score attendu : A ou A+**

Vérifier que vous avez :
- ✓ Content-Security-Policy
- ✓ X-Frame-Options
- ✓ X-Content-Type-Options
- ✓ Strict-Transport-Security
- ✓ Referrer-Policy

### D. Tester la politique de cookies
1. Ouvrir https://agebiologique.eu/ en navigation privée
2. Vérifier que le bandeau cookie s'affiche
3. Cliquer "Accepter" → doit disparaître et se souvenir
4. Vérifier que la page privacy-policy fonctionne

---

## ÉTAPE 7 : Soumettre à Google Search Console (15 min)

### A. Ajouter la propriété
1. Aller sur : https://search.google.com/search-console
2. Cliquer **"Ajouter une propriété"**
3. Choisir **"Préfixe d'URL"** : `https://agebiologique.eu`

### B. Vérifier la propriété
Netlify rend la vérification facile :

**Méthode 1 : Balise HTML**
1. Google vous donne une balise : `<meta name="google-site-verification" content="ABC123...">`
2. Ajouter cette balise dans `index.html` (après l'ouverture de `<head>`)
3. Commit + Push :
   ```bash
   git add index.html
   git commit -m "Add Google Search Console verification"
   git push
   ```
4. Attendre 1 min (déploiement auto Netlify)
5. Retourner sur Search Console → Cliquer **"Vérifier"**

**Méthode 2 : Enregistrement DNS** (si vous préférez)
1. Ajouter un TXT record chez votre registraire
2. Attendre propagation DNS
3. Vérifier

### C. Soumettre le sitemap
1. Une fois vérifié, aller dans **"Sitemaps"** (menu gauche)
2. Entrer : `sitemap.xml`
3. Cliquer **"Envoyer"**

**Résultat attendu :**
```
Statut : Réussite
URLs découvertes : 52
```

### D. Demander l'indexation des pages principales
1. Aller dans **"Inspection de l'URL"** (menu gauche)
2. Entrer : `https://agebiologique.eu/`
3. Cliquer **"Tester l'URL en direct"**
4. Cliquer **"Demander une indexation"**

Répéter pour :
- `https://agebiologique.eu/blog/comment-calculer-age-biologique.html`
- `https://agebiologique.eu/blog/tests-age-biologique-fiables.html`
- 3-5 autres articles blog importants

---

## ÉTAPE 8 : Installer Google Analytics (10 min)

### A. Créer une propriété GA4
1. Aller sur : https://analytics.google.com/
2. **"Admin"** (roue dentée en bas à gauche)
3. **"Créer une propriété"**
   - Nom : `BioAge - agebiologique.eu`
   - Fuseau horaire : `France`
   - Devise : `EUR`
4. Continuer → Remplir les infos entreprise
5. Choisir **"Générer des prospects"** + **"Examiner le comportement des utilisateurs"**

### B. Créer un flux de données Web
1. Sélectionner **"Web"**
2. URL : `https://agebiologique.eu`
3. Nom du flux : `Site Web Principal`
4. Cliquer **"Créer un flux"**

### C. Obtenir l'ID de mesure
Vous recevrez un **Measurement ID** : `G-XXXXXXXXXX`

### D. Ajouter le code Google Analytics

Ouvrir `index.html` et ajouter juste après `<head>` :

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

**Répéter pour TOUTES les pages** (52 pages HTML) ou créer un script automatisé.

### E. Vérifier que ça fonctionne
1. Commit + Push les modifications
2. Attendre 1 min (déploiement Netlify)
3. Aller sur https://agebiologique.eu/
4. Dans Google Analytics → **"Rapports"** → **"Temps réel"**
5. Vous devriez voir **1 utilisateur actif** (vous)

---

## ÉTAPE 9 : Configurer Google AdSense (20 min)

### A. Créer un compte AdSense
1. Aller sur : https://www.google.com/adsense/start/
2. Se connecter avec le même compte Google que Analytics
3. Cliquer **"Commencer"**
4. Entrer : `agebiologique.eu`
5. Remplir les informations :
   - Pays : France
   - Accepter les conditions
   - Continuer

### B. Ajouter le code AdSense

Google vous donnera un code similaire à :

```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXX"
     crossorigin="anonymous"></script>
```

Ajouter ce code dans **TOUTES les pages** (entre `<head>` et `</head>`).

### C. Attendre la vérification
- Google vérifie votre site (1-3 jours)
- Vous recevrez un email de confirmation

**IMPORTANT :** Ne créez PAS encore d'annonces. Attendez :
1. Que le site ait du trafic (50+ visiteurs/jour minimum)
2. L'approbation initiale d'AdSense
3. 2-4 semaines de trafic organique

**Raison :** Google détecte les fausses impressions. Un site sans trafic avec AdSense = risque de bannissement.

---

## ÉTAPE 10 : Stratégie Backlinks (Semaine 2-4)

Voir le fichier `PLAN_ACTION_IMMEDIAT.md` pour la stratégie complète.

### Actions prioritaires :

#### Semaine 1 (après déploiement)
- ✓ Soumettre à Google Search Console
- ✓ Installer Analytics
- ✓ Partager sur réseaux sociaux (Reddit, Twitter, Facebook)

#### Semaine 2
- Créer 3 backlinks de qualité :
  1. Article invité sur un blog santé/bien-être
  2. Inscription annuaire niche (ex: annuaire-sante.fr)
  3. Partage sur forum santé (Doctissimo, Reddit r/longevity)

#### Semaine 3-4
- 5-7 backlinks supplémentaires
- 2 nouveaux articles blog
- Répondre aux questions Quora/Reddit avec lien vers votre site

**Objectif M1 :** 10-15 backlinks + 200-500 visiteurs/mois

---

## CHECKLIST FINALE AVANT LANCEMENT

```
Phase Préparation (COMPLÉTÉ ✓)
✓ Images générées (23 images, 0.48 MB)
✓ Placeholders remplacés
✓ Git initialisé + commit initial
✓ Configuration Netlify (.toml + _headers)
✓ Privacy policy + cookies

Phase Déploiement (À FAIRE)
☐ Compte Netlify créé
☐ Dépôt GitHub créé et poussé
☐ Site déployé sur Netlify
☐ Domaine agebiologique.eu configuré
☐ HTTPS activé
☐ Headers sécurité vérifiés (score A+)

Phase SEO (À FAIRE)
☐ Google Search Console configuré
☐ Sitemap soumis
☐ 5 pages principales indexées
☐ Google Analytics installé
☐ Google Analytics fonctionnel (1+ utilisateur détecté)

Phase Monétisation (ATTENDRE 2-4 SEMAINES)
☐ Trafic > 50 visiteurs/jour
☐ Google AdSense compte créé
☐ Code AdSense ajouté
☐ Vérification AdSense approuvée
☐ Annonces activées

Phase Backlinks (Semaine 2-4)
☐ 3 backlinks créés (Semaine 2)
☐ 5 backlinks créés (Semaine 3)
☐ 7 backlinks créés (Semaine 4)
☐ 2 nouveaux articles blog publiés
☐ Partage réseaux sociaux (Reddit, Twitter, Facebook)
```

---

## COMMANDES RAPIDES

### Mettre à jour le site (après modifications)
```bash
cd "C:\Users\Dell\Desktop\claudeprojects\bioage"
git add .
git commit -m "Description des modifications"
git push
```

### Vérifier le statut du déploiement
- Netlify déploie automatiquement à chaque `git push`
- Durée : 30-60 secondes
- Dashboard : https://app.netlify.com/

### Voir les logs de déploiement
1. Aller sur Netlify dashboard
2. Cliquer sur votre site
3. **"Deploys"** → Cliquer sur le dernier déploiement
4. Voir les logs en temps réel

---

## SUPPORT ET DÉPANNAGE

### Problème : Le site ne se déploie pas
1. Vérifier les logs Netlify
2. Vérifier que le push Git a fonctionné : `git log`
3. Vérifier la branche : `git branch` (doit être `main`)

### Problème : Le domaine ne fonctionne pas
1. Vérifier la propagation DNS : https://dnschecker.org/#A/agebiologique.eu
2. Attendre 1-2 heures (parfois 24h)
3. Vider le cache DNS local : `ipconfig /flushdns` (Windows)

### Problème : HTTPS ne s'active pas
1. Vérifier que le DNS est correctement configuré
2. Attendre 10-15 minutes après configuration DNS
3. Netlify génère automatiquement le certificat Let's Encrypt

### Problème : Les images ne s'affichent pas
1. Vérifier que les images sont bien dans `/images/`
2. Vérifier les chemins relatifs : `../images/blog-xxx.jpg`
3. Ouvrir la console navigateur (F12) → Onglet "Network" → Vérifier les 404

### Problème : Headers sécurité non détectés
1. Vérifier que `_headers` est à la racine du projet
2. Vérifier que Netlify l'a bien déployé (voir logs)
3. Attendre 5 minutes après déploiement
4. Vider le cache navigateur (Ctrl+Shift+R)

---

## PROCHAINES ÉTAPES

### Aujourd'hui (Jour J)
1. ☐ Créer compte Netlify
2. ☐ Créer dépôt GitHub
3. ☐ Pousser le code
4. ☐ Déployer sur Netlify
5. ☐ Configurer le domaine

### Jour J+1
6. ☐ Vérifier HTTPS
7. ☐ Soumettre à Search Console
8. ☐ Installer Google Analytics
9. ☐ Tester tout le site

### Semaine 1
10. ☐ Partager sur réseaux sociaux (Reddit, Twitter, Facebook)
11. ☐ Répondre à 3-5 questions Quora/Reddit avec lien
12. ☐ Créer 2 premiers backlinks

### Semaine 2-4
13. ☐ Créer 10-15 backlinks totaux
14. ☐ Publier 2 nouveaux articles
15. ☐ Analyser Analytics (comportement utilisateurs)

### Mois 2-3
16. ☐ Atteindre 50+ visiteurs/jour
17. ☐ Soumettre à Google AdSense
18. ☐ Attendre approbation AdSense
19. ☐ Activer les annonces

---

## PROJECTION REVENUE (RAPPEL)

**Scénario Réaliste (si toutes les étapes suivies) :**

| Mois | Visiteurs/jour | Pages vues/jour | Revenue/mois |
|------|----------------|-----------------|--------------|
| M1   | 15-25          | 45-75           | €5-10        |
| M2   | 40-60          | 120-180         | €50-80       |
| M3   | 80-120         | 240-360         | €280-320     |
| M6   | 200-300        | 600-900         | €650-850     |
| M12  | 350-450        | 1050-1350       | €1,160       |

**Total Année 1 : €6,450**

**Condition critique :** Suivre la stratégie backlinks + 2 articles/mois

---

## BUDGET TOTAL

| Poste                    | Coût        |
|--------------------------|-------------|
| Domaine agebiologique.eu | €10-15/an   |
| Hébergement Netlify      | €0 (gratuit)|
| SSL Certificate          | €0 (inclus) |
| Google Services          | €0          |
| **TOTAL**                | **€10-15/an** |

---

**Votre site est prêt à être lancé ! 🚀**

Suivez ce guide étape par étape et vous serez en ligne dans 1-2 heures.

Bonne chance avec BioAge !
