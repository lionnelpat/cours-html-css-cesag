# 1.2 Balises de texte et liens hypertextes

```{admonition} Objectifs de cette leçon
:class: tip
À la fin de cette leçon, tu sauras utiliser :
- Les balises de titres `<h1>` à `<h6>`
- Les balises de paragraphe et formatage de texte
- Les liens hypertextes `<a>` (internes, externes, ancres)
- Les balises de mise en valeur (`<strong>`, `<em>`, `<mark>`...)
```

---

## 1.2.1 Les titres HTML — `<h1>` à `<h6>`

HTML propose **6 niveaux de titres**, du plus important au moins important :

```html
<h1>Titre de niveau 1 — Le plus important</h1>
<h2>Titre de niveau 2</h2>
<h3>Titre de niveau 3</h3>
<h4>Titre de niveau 4</h4>
<h5>Titre de niveau 5</h5>
<h6>Titre de niveau 6 — Le moins important</h6>
```

### Rendu dans le navigateur

| Balise | Taille par défaut | Usage |
|--------|-------------------|-------|
| `<h1>` | ~32px, gras | Titre principal de la page (un seul par page) |
| `<h2>` | ~24px, gras | Titres de sections principales |
| `<h3>` | ~18px, gras | Sous-sections |
| `<h4>` | ~16px, gras | Sous-sous-sections |
| `<h5>` | ~14px, gras | Rarement utilisé |
| `<h6>` | ~12px, gras | Très rarement utilisé |

```{admonition} Règle importante — Ne jamais sauter des niveaux
:class: important
❌ Mauvaise pratique :
```html
<h1>Titre principal</h1>
<h4>Sous-titre</h4>  <!-- On a sauté h2 et h3 ! -->
```

✅ Bonne pratique :
```html
<h1>Titre principal</h1>
<h2>Section</h2>
<h3>Sous-section</h3>
```

Les titres ont une importance pour le **référencement** (SEO) et l'**accessibilité**.
```

---

## 1.2.2 Les paragraphes et le texte

### Le paragraphe `<p>`

```html
<p>
  Le CESAG est un établissement d'enseignement supérieur spécialisé
  dans la gestion des entreprises. Il forme des cadres de haut niveau
  pour les entreprises d'Afrique de l'Ouest.
</p>
<p>
  Fondé en 1985, le CESAG accueille des étudiants venus de toute
  la sous-région.
</p>
```

```{admonition} À retenir
:class: note
- Un `<p>` crée automatiquement un espace avant et après le paragraphe
- Les sauts de ligne dans le code HTML sont **ignorés** — utilise `<br>` pour forcer un saut de ligne
- Pour créer un nouveau paragraphe, crée un nouveau `<p>`
```

### Saut de ligne `<br>`

```html
<p>
  CESAG<br>
  Dakar, Sénégal<br>
  Tél : +221 33 839 73 60
</p>
```

### Ligne horizontale `<hr>`

```html
<h2>Section 1</h2>
<p>Contenu de la section 1...</p>

<hr>  <!-- Ligne de séparation -->

<h2>Section 2</h2>
<p>Contenu de la section 2...</p>
```

---

## 1.2.3 Le formatage du texte

### Les balises de mise en valeur

```html
<!-- Texte important / gras sémantique -->
<p>Le cours commence à <strong>8h00</strong> précises.</p>

<!-- Texte en emphase / italique sémantique -->
<p>Le terme <em>HTML</em> signifie HyperText Markup Language.</p>

<!-- Texte surligné -->
<p>La date limite est le <mark>15 janvier 2026</mark>.</p>

<!-- Texte barré -->
<p>Ancien prix : <s>25 000 FCFA</s> — Nouveau : 20 000 FCFA</p>

<!-- Texte en indice (formules chimiques) -->
<p>La formule de l'eau est H<sub>2</sub>O.</p>

<!-- Texte en exposant (mathématiques) -->
<p>La surface est de 100 m<sup>2</sup>.</p>

<!-- Code informatique inline -->
<p>La balise <code>&lt;p&gt;</code> crée un paragraphe.</p>

<!-- Citation -->
<blockquote>
  <p>Le savoir est une lumière qui éclaire le chemin de la réussite.</p>
  <footer>— Proverbe africain</footer>
</blockquote>

<!-- Texte préformaté (respecte les espaces et sauts de ligne) -->
<pre>
  Nom    : Amadou Diallo
  Filière: MIAGE L1
  Note   : 18/20
</pre>
```

### Tableau récapitulatif

| Balise | Rendu | Signification sémantique |
|--------|-------|--------------------------|
| `<strong>` | **gras** | Très important |
| `<em>` | *italique* | Emphase, accentuation |
| `<b>` | **gras** | Stylisation (sans importance) |
| `<i>` | *italique* | Style (sans emphase) |
| `<mark>` | surligné | Mis en valeur |
| `<s>` | ~~barré~~ | Information obsolète |
| `<u>` | souligné | Annotation (attention : ressemble à un lien) |
| `<code>` | `monospace` | Code informatique |
| `<sub>` | H₂O | Indice |
| `<sup>` | m² | Exposant |

```{admonition} `<strong>` vs `<b>` — Quelle différence ?
:class: note
- `<b>` : met en **gras** visuellement, sans signification particulière
- `<strong>` : indique une importance **sémantique** forte (les lecteurs d'écran le lisent avec insistance)

Préfère toujours `<strong>` et `<em>` pour un code sémantiquement correct.
```

---

## 1.2.4 Les liens hypertextes `<a>`

Les liens sont l'essence du Web — ils relient les pages entre elles.

### Syntaxe de base

```html
<a href="URL">Texte cliquable</a>
```

### Types de liens

#### Lien externe (vers un autre site)

```html
<a href="https://www.cesag.sn">Visiter le site du CESAG</a>

<!-- Ouvrir dans un nouvel onglet -->
<a href="https://www.cesag.sn" target="_blank" rel="noopener">
  Visiter le CESAG (nouvel onglet)
</a>
```

```{admonition} Sécurité — Toujours ajouter rel="noopener"
:class: important
Quand tu utilises `target="_blank"`, ajoute toujours `rel="noopener noreferrer"`. Sans cela, la page cible peut accéder à ta page via JavaScript (faille de sécurité).

```html
<a href="https://cesag.sn" target="_blank" rel="noopener noreferrer">CESAG</a>
```
```

#### Lien interne (vers une autre page de ton site)

```html
<!-- Lien vers un fichier dans le même dossier -->
<a href="formations.html">Nos formations</a>

<!-- Lien vers un fichier dans un sous-dossier -->
<a href="pages/contact.html">Contact</a>

<!-- Lien vers un fichier dans le dossier parent -->
<a href="../index.html">Accueil</a>
```

#### Lien ancre (vers une section de la même page)

```html
<!-- Définir l'ancre cible avec un id -->
<h2 id="contact">Nous contacter</h2>

<!-- Créer le lien vers cette ancre -->
<a href="#contact">Aller à la section Contact</a>

<!-- Ancre vers une section d'une autre page -->
<a href="formations.html#miage">Programme MIAGE</a>
```

#### Lien email et téléphone

```html
<!-- Ouvre le client email -->
<a href="mailto:info@cesag.sn">Envoyer un email</a>

<!-- Avec sujet et corps pré-remplis -->
<a href="mailto:info@cesag.sn?subject=Demande d'information&body=Bonjour,">
  Nous écrire
</a>

<!-- Lien téléphonique (utile sur mobile) -->
<a href="tel:+221338397360">+221 33 839 73 60</a>
```

#### Lien de téléchargement

```html
<!-- L'attribut download force le téléchargement -->
<a href="syllabus-html-css.pdf" download>
  Télécharger le syllabus (PDF)
</a>

<!-- Avec un nom de fichier personnalisé -->
<a href="docs/syllabus-v2.pdf" download="Syllabus_HTML_CSS_CESAG.pdf">
  Télécharger le syllabus
</a>
```

### Image cliquable

```html
<!-- Une image qui est aussi un lien -->
<a href="https://www.cesag.sn">
  <img src="logo-cesag.png" alt="Logo CESAG — Retour à l'accueil">
</a>
```

---

## 1.2.5 Les chemins de fichiers (paths)

Comprendre les chemins est **essentiel** pour les liens et les images.

```
mon-site/
├── index.html          ← page d'accueil
├── formations.html
├── images/
│   ├── logo.png
│   └── photo.jpg
└── pages/
    └── contact.html
```

### Chemin absolu vs relatif

| Type | Exemple | Usage |
|------|---------|-------|
| **Absolu** | `https://cesag.sn/logo.png` | Fichier sur un autre serveur |
| **Relatif** | `images/logo.png` | Fichier sur ton propre site |

### Syntaxe des chemins relatifs

```html
<!-- Depuis index.html -->
<a href="formations.html">Formations</a>           <!-- même dossier -->
<a href="pages/contact.html">Contact</a>           <!-- sous-dossier pages/ -->
<img src="images/logo.png" alt="Logo">             <!-- sous-dossier images/ -->

<!-- Depuis pages/contact.html -->
<a href="../index.html">Accueil</a>                <!-- dossier parent -->
<img src="../images/logo.png" alt="Logo">          <!-- image dans parent/images/ -->
```

---

## Résumé de la leçon

```{admonition} Ce qu'il faut retenir
:class: tip
| Balise | Usage |
|--------|-------|
| `<h1>` à `<h6>` | Titres (du plus au moins important) |
| `<p>` | Paragraphe |
| `<br>` | Saut de ligne forcé |
| `<hr>` | Ligne de séparation |
| `<strong>` | Texte très important (gras) |
| `<em>` | Texte en emphase (italique) |
| `<mark>` | Texte surligné |
| `<code>` | Code informatique inline |
| `<blockquote>` | Citation |
| `<a href="...">` | Lien hypertexte |
| `target="_blank"` | Ouvre dans un nouvel onglet |
| `href="#id"` | Lien ancre vers une section |
| `href="mailto:..."` | Lien email |
```

---

## TP 2 — Page de présentation enrichie

```{admonition} Exercice — À faire en TD
:class: warning

### Objectif
Enrichir la page personnelle créée au TP 2 avec du formatage de texte et des liens.

### Consignes

**1. Titres et hiérarchie (3 pts)**
- Un seul `<h1>` avec ton nom complet
- Des `<h2>` pour chaque grande section (Présentation, Études, Contacts)
- Des `<h3>` si tu as des sous-sections

**2. Formatage du texte (4 pts)**
- Utilise `<strong>` pour mettre en valeur des informations importantes
- Utilise `<em>` pour les termes techniques ou étrangers
- Utilise `<mark>` pour une information clé (ex: ta note favorite)
- Ajoute une citation `<blockquote>` avec ta citation préférée

**3. Navigation avec ancres (4 pts)**
En haut de la page, crée un menu de navigation interne :
```html
<nav>
  <a href="#presentation">Présentation</a> |
  <a href="#etudes">Mes études</a> |
  <a href="#contact">Me contacter</a>
</nav>
```
Et ajoute les `id` correspondants sur tes sections.

**4. Liens externes (3 pts)**
- Un lien vers le site du CESAG (s'ouvre dans un nouvel onglet)
- Un lien `mailto:` vers ton adresse email CESAG
- Un lien de téléchargement vers un fichier (PDF fictif ou réel)

**5. Bonus (2 pts)**
- Ajoute un lien de retour en haut de page (ancre `#top`) en bas de page
- Crée une deuxième page `contact.html` et lie les deux pages

### Rendu
Fichier `index.html` modifié (et `contact.html` si bonus)
```

---

*Leçon suivante → [Leçon 4 — Images et Multimédia](04-images-multimedia)*
