# 1.1 Structure d'un document HTML

```{admonition} Le Web en 5 points — ce qu'il faut savoir avant de coder
:class: note
- **Internet** est un réseau mondial d'ordinateurs connectés.
- **Le Web** est un ensemble de pages accessibles via un navigateur grâce au protocole HTTP.
- Quand tu tapes une URL, ton navigateur envoie une requête à un **serveur** qui renvoie un fichier HTML.
- **HTML** structure le contenu, **CSS** le met en forme, **JavaScript** le rend interactif.
- Outil du développeur : **VS Code** + l'extension **Live Server** pour voir tes modifications en direct.
```

---

```{admonition} Objectifs de cette leçon
:class: tip
À la fin de cette leçon, tu sauras :
- Créer un fichier HTML valide de A à Z
- Comprendre la structure obligatoire d'un document HTML5
- Utiliser les balises `<head>` et `<body>` correctement
- Utiliser les balises sémantiques (`<header>`, `<main>`, `<footer>`...)
- Ouvrir une page HTML dans un navigateur
```

---

## 1.1.1 Créer son premier fichier HTML

### Étape 1 — Installer VS Code et Live Server

1. Télécharge et installe **VS Code** depuis [code.visualstudio.com](https://code.visualstudio.com)
2. Ouvre VS Code → clique sur l'icône Extensions (carré puzzle à gauche)
3. Cherche **"Live Server"** → Installe l'extension de **Ritwick Dey**

### Étape 2 — Créer un dossier de travail

1. Crée un dossier sur ton bureau : `mes-cours-html`
2. Dans VS Code : **Fichier → Ouvrir le dossier** → Sélectionne `mes-cours-html`

### Étape 3 — Créer le fichier

1. Dans VS Code, clique sur l'icône **Nouveau fichier** (ou `Ctrl+N`)
2. Nomme le fichier : `index.html`
3. L'extension `.html` est obligatoire — elle indique au système que c'est une page web

```{admonition} Convention importante
:class: note
Par convention, la **page principale** d'un site s'appelle toujours `index.html`. C'est le fichier que le serveur envoie automatiquement quand on visite l'adresse racine du site.
```

---

## 1.1.2 La structure de base HTML5

Voici la structure **minimale obligatoire** de tout fichier HTML5 :

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ma première page</title>
  </head>
  <body>
    <h1>Bonjour, monde !</h1>
    <p>Ceci est ma première page web.</p>
  </body>
</html>
```

### Décortiquons chaque ligne

| Ligne | Explication |
|-------|-------------|
| `<!DOCTYPE html>` | Déclare que c'est un document **HTML5**. Toujours en première ligne. |
| `<html lang="fr">` | Racine du document. `lang="fr"` indique la langue (important pour l'accessibilité). |
| `<head>` | Contient les **informations sur la page** (non affichées à l'écran). |
| `<meta charset="UTF-8">` | Encodage des caractères — permet d'afficher les accents (é, à, ç...). |
| `<meta name="viewport"...>` | Indispensable pour que la page s'adapte aux mobiles. |
| `<title>` | Titre affiché dans **l'onglet du navigateur**. |
| `</head>` | Fermeture du `<head>`. |
| `<body>` | Contient le **contenu visible** de la page. |
| `<h1>` | Titre principal. |
| `<p>` | Paragraphe. |
| `</body>` | Fermeture du `<body>`. |
| `</html>` | Fermeture de la balise racine. |

```{admonition} Raccourci VS Code — le squelette automatique !
:class: tip
Dans un fichier `.html` vide, tape simplement `!` puis appuie sur `Tab` (ou `Entrée`).
VS Code génère automatiquement toute la structure de base ! C'est un **Emmet abbreviation**.
```

---

## 1.1.3 Anatomie d'une balise HTML

Une balise HTML se compose de :

```html
<nom-balise attribut="valeur">contenu</nom-balise>
```

### Les parties d'une balise

```
<p class="intro">Bienvenue au CESAG.</p>
│                │               │
│ Balise ouvrante│               Balise fermante
│ avec attribut  │               avec slash /
│                Contenu de la balise
```

### Balises avec et sans contenu

**Balises à contenu** (paires) — ont une ouverture et une fermeture :
```html
<h1>Titre</h1>
<p>Paragraphe</p>
<a href="...">Lien</a>
```

**Balises auto-fermantes** — n'ont pas de contenu, se ferment elles-mêmes :
```html
<img src="photo.jpg" alt="Ma photo">
<br>         <!-- Saut de ligne -->
<hr>         <!-- Ligne horizontale -->
<meta charset="UTF-8">
<input type="text">
```

### Les attributs

Les attributs apportent des **informations supplémentaires** à une balise :

```html
<a href="https://cesag.sn" target="_blank" title="Site CESAG">
  Visiter le CESAG
</a>
```

| Attribut | Valeur | Signification |
|----------|--------|---------------|
| `href` | `"https://cesag.sn"` | Lien vers cette adresse |
| `target` | `"_blank"` | Ouvrir dans un nouvel onglet |
| `title` | `"Site CESAG"` | Info-bulle au survol |

```{admonition} Règles sur les attributs
:class: note
- La valeur est toujours entre **guillemets doubles** `""`
- On peut mettre **plusieurs attributs** dans une balise
- Certains attributs sont **obligatoires** (ex: `src` pour `<img>`, `href` pour `<a>`)
- L'ordre des attributs n'a pas d'importance
```

---

## 1.1.4 Les commentaires HTML

Un commentaire est du texte ignoré par le navigateur — il n'est pas affiché. Il sert à documenter ton code :

```html
<!-- Ceci est un commentaire sur une ligne -->

<!--
  Ceci est un commentaire
  sur plusieurs lignes
-->

<body>
  <!-- Navigation principale -->
  <nav>...</nav>

  <!-- Contenu principal de la page -->
  <main>...</main>
</body>
```

---

## 1.1.5 La structure sémantique HTML5

HTML5 a introduit des **balises sémantiques** — elles donnent du *sens* à la structure de la page, ce que de simples `<div>` ne font pas.

### Les principales balises sémantiques

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Site du CESAG</title>
</head>
<body>

  <!-- En-tête du site -->
  <header>
    <h1>CESAG</h1>
    <p>Centre Africain d'Études Supérieures en Gestion</p>
  </header>

  <!-- Navigation principale -->
  <nav>
    <a href="index.html">Accueil</a>
    <a href="formations.html">Formations</a>
    <a href="contact.html">Contact</a>
  </nav>

  <!-- Contenu principal -->
  <main>

    <!-- Une section thématique -->
    <section>
      <h2>Nos programmes</h2>
      <p>Le CESAG propose...</p>
    </section>

    <!-- Un article indépendant -->
    <article>
      <h2>Actualité : Journée portes ouvertes</h2>
      <p>Le CESAG ouvre ses portes le...</p>
    </article>

    <!-- Contenu secondaire (publicité, liens connexes...) -->
    <aside>
      <h3>Liens utiles</h3>
      <ul>
        <li><a href="#">UEMOA</a></li>
      </ul>
    </aside>

  </main>

  <!-- Pied de page -->
  <footer>
    <p>© 2025 CESAG — Dakar, Sénégal</p>
  </footer>

</body>
</html>
```

### Rôle de chaque balise sémantique

| Balise | Rôle |
|--------|------|
| `<header>` | En-tête de la page ou d'une section |
| `<nav>` | Bloc de navigation (liens) |
| `<main>` | Contenu principal de la page (unique par page) |
| `<section>` | Section thématique du contenu |
| `<article>` | Contenu autonome (article de blog, actualité...) |
| `<aside>` | Contenu secondaire, barre latérale |
| `<footer>` | Pied de page ou bas d'une section |

### `<div>` et `<span>` — les balises génériques

Quand aucune balise sémantique ne convient, on utilise :
- `<div>` : conteneur **bloc** (occupe toute la largeur)
- `<span>` : conteneur **inline** (dans un texte)

```html
<div class="carte-etudiant">
  <p>Nom : <span class="nom">Amadou Diallo</span></p>
  <p>Filière : <span class="filiere">MIAGE</span></p>
</div>
```

---

## 1.1.6 Indentation et lisibilité

Un code bien indenté est **essentiel** — c'est une question professionnelle.

```html
<!-- ❌ Code illisible -->
<html><head><title>Page</title></head><body><h1>Titre</h1><p>Texte</p></body></html>

<!-- ✅ Code bien indenté -->
<html>
  <head>
    <title>Page</title>
  </head>
  <body>
    <h1>Titre</h1>
    <p>Texte</p>
  </body>
</html>
```

**Règle** : Chaque balise enfant est indentée de **2 espaces** (ou 1 tabulation) par rapport à sa balise parente.

```{admonition} Astuce VS Code
:class: tip
- `Shift+Alt+F` : formate automatiquement tout le fichier (Windows/Linux)
- `Shift+Option+F` : formate automatiquement tout le fichier (Mac)
- Ou installe l'extension **Prettier** pour le formatage automatique à chaque sauvegarde
```

---

## Résumé de la leçon

```{admonition} Ce qu'il faut retenir
:class: tip
| Élément | Description |
|---------|-------------|
| `<!DOCTYPE html>` | Déclaration HTML5 — toujours en ligne 1 |
| `<html lang="fr">` | Racine du document |
| `<head>` | Métadonnées (non visibles) |
| `<meta charset="UTF-8">` | Encodage — permet les accents |
| `<title>` | Titre dans l'onglet navigateur |
| `<body>` | Contenu visible de la page |
| Balises sémantiques | `header`, `nav`, `main`, `section`, `article`, `aside`, `footer` |
| Commentaires | `<!-- texte ignoré -->` |
```

---

## TP 1 — Mon premier fichier HTML

```{admonition} Exercice — À faire en TD (2 heures)
:class: warning

### Objectif
Créer une page web de présentation personnelle complète et bien structurée.

### Consignes

**1. Structure obligatoire (4 pts)**
Ton fichier `index.html` doit contenir la structure HTML5 complète :
- `<!DOCTYPE html>`, `<html lang="fr">`, `<head>`, `<body>`
- `<meta charset="UTF-8">` et `<meta name="viewport"...>`
- Un `<title>` pertinent

**2. Structure sémantique (4 pts)**
La page doit utiliser les balises sémantiques :
- `<header>` : ton nom et ta filière
- `<nav>` : liens vers les sections (Accueil, À propos, Études)
- `<main>` : contenu principal
- `<section>` : au moins 2 sections (présentation, études)
- `<footer>` : année et ton nom

**3. Contenu (4 pts)**
- Un titre `<h1>` avec ton nom complet
- Un sous-titre `<h2>` avec ta filière
- Au moins 2 paragraphes `<p>` de présentation
- Une liste de tes matières préférées (tu apprendras `<ul>/<li>` dans la prochaine leçon)

**4. Qualité du code (4 pts)**
- Indentation correcte (2 espaces ou tabulation)
- Commentaires pour expliquer les sections
- Aucune faute dans les noms de balises

**5. Ouverture dans le navigateur (4 pts)**
- Utiliser Live Server pour visualiser la page
- La page doit s'afficher sans erreur dans Chrome

### Critères de notation
- Structure HTML5 valide : 4 pts
- Balises sémantiques présentes et correctes : 4 pts
- Contenu complet : 4 pts
- Code propre et indenté : 4 pts
- Page visible dans le navigateur : 4 pts

### Fichiers à rendre
`index.html` (dans un dossier portant ton prénom et nom)
```

---

*Leçon suivante → [Leçon 3 — Balises de texte, titres et liens](03-balises-texte-liens)*
