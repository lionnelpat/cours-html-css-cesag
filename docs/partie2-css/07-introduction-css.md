# 2.1 Introduction au CSS

```{admonition} Objectifs de cette leçon
:class: tip
À la fin de cette leçon, tu sauras :
- Comprendre le rôle et le fonctionnement de CSS
- Lier un fichier CSS à une page HTML
- Utiliser les sélecteurs de base (élément, classe, id)
- Appliquer des couleurs, des polices et des tailles de texte
- Comprendre la cascade et la spécificité
```

---

## 2.1.1 Qu'est-ce que CSS ?

**CSS** (Cascading Style Sheets — Feuilles de Style en Cascade) est le langage qui contrôle **l'apparence visuelle** des pages web.

Sans CSS, toutes les pages web ressembleraient à un document texte brut. CSS permet de définir :

- 🎨 **Les couleurs** — texte, fond, bordures
- 🔤 **Les polices** — famille, taille, graisse, style
- 📐 **L'espacement** — marges internes et externes
- 📦 **La mise en page** — colonnes, grilles, flexbox
- ✨ **Les effets** — ombres, transitions, animations
- 📱 **L'adaptation** — affichage sur mobile, tablette, desktop

```{admonition} Analogie
:class: note
Si HTML est le **squelette** d'une page (la structure), CSS en est la **peau et les vêtements** (l'apparence). Le même squelette peut être habillé différemment selon les styles appliqués.
```

---

## 2.1.2 Les 3 façons d'écrire du CSS

### Méthode 1 — CSS externe (✅ Recommandée)

Un fichier `.css` séparé, lié au HTML via `<link>` dans le `<head>` :

**Fichier `style.css` :**
```css
h1 {
    color: #1A7A2A;
    font-size: 32px;
}

p {
    color: #333333;
    line-height: 1.6;
}
```

**Fichier `index.html` :**
```html
<head>
    <meta charset="UTF-8">
    <title>Ma page</title>
    <link rel="stylesheet" href="style.css">
</head>
```

✅ **Avantages** : un seul fichier CSS pour tout le site, facile à maintenir, le navigateur met le CSS en cache.

### Méthode 2 — CSS interne

Dans une balise `<style>` dans le `<head>` du HTML :

```html
<head>
    <meta charset="UTF-8">
    <title>Ma page</title>
    <style>
        h1 {
            color: #1A7A2A;
        }
        p {
            color: #333333;
        }
    </style>
</head>
```

⚠️ À utiliser seulement pour une page unique ou des tests rapides.

### Méthode 3 — CSS inline

Directement dans l'attribut `style` d'une balise HTML :

```html
<h1 style="color: #1A7A2A; font-size: 32px;">Titre vert</h1>
<p style="color: #333333;">Paragraphe gris</p>
```

❌ **Déconseillé** : difficile à maintenir, mélange structure et présentation.

```{admonition} Règle d'or
:class: important
Toujours utiliser la **méthode 1** (fichier CSS externe). C'est la bonne pratique professionnelle. Les méthodes 2 et 3 existent mais doivent rester des exceptions.
```

---

## 2.1.3 Syntaxe d'une règle CSS

```css
sélecteur {
    propriété: valeur;
    propriété: valeur;
}
```

**Exemple concret :**

```css
h1 {
    color: #1A7A2A;
    font-size: 32px;
    font-weight: bold;
    text-align: center;
}
```

| Partie | Exemple | Description |
|--------|---------|-------------|
| **Sélecteur** | `h1` | Quelle(s) balise(s) cibler |
| **Propriété** | `color` | Quelle caractéristique modifier |
| **Valeur** | `#1A7A2A` | Quelle valeur donner |
| **Déclaration** | `color: #1A7A2A;` | Propriété + valeur (terminée par `;`) |
| **Bloc** | `{ ... }` | Ensemble des déclarations |
| **Règle** | Tout l'ensemble | Sélecteur + bloc |

```{admonition} Le point-virgule est obligatoire !
:class: warning
Chaque déclaration CSS doit se terminer par un **point-virgule** `;`. L'oublier est l'une des erreurs les plus fréquentes des débutants — toute la règle peut être ignorée par le navigateur.
```

---

## 2.1.4 Les sélecteurs de base

### Sélecteur d'élément (balise)

Cible **toutes** les balises du type indiqué :

```css
/* Tous les paragraphes */
p {
    color: #333;
    line-height: 1.7;
}

/* Tous les titres h2 */
h2 {
    color: #1A7A2A;
    border-bottom: 2px solid #E8420A;
}

/* Toutes les images */
img {
    border-radius: 8px;
}
```

### Sélecteur de classe (`.`)

Cible les éléments ayant un attribut `class` spécifique. **Réutilisable** sur plusieurs éléments :

```html
<!-- HTML -->
<p class="intro">Texte d'introduction mis en valeur.</p>
<p>Paragraphe normal.</p>
<div class="intro">Ce div a aussi la classe intro.</div>
```

```css
/* CSS — le point . indique une classe */
.intro {
    font-size: 18px;
    color: #1A7A2A;
    font-style: italic;
}
```

### Sélecteur d'identifiant (`#`)

Cible **un élément unique** ayant un attribut `id` spécifique. **Un seul par page** :

```html
<!-- HTML -->
<header id="entete-principal">
    <h1>CESAG</h1>
</header>
```

```css
/* CSS — le dièse # indique un id */
#entete-principal {
    background-color: #1A7A2A;
    color: white;
    padding: 20px;
}
```

### Sélecteur universel (`*`)

Cible **tous** les éléments :

```css
/* Réinitialisation des marges (technique courante) */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
```

### Grouper des sélecteurs (`,`)

Appliquer les mêmes styles à plusieurs sélecteurs :

```css
/* Ces 4 sélecteurs reçoivent les mêmes styles */
h1, h2, h3, h4 {
    font-family: Georgia, serif;
    color: #1A7A2A;
}
```

---

## 2.1.5 Les couleurs en CSS

### Couleur par nom

```css
p { color: red; }
div { background-color: white; }
h1 { color: green; }
```

Il existe 140 noms de couleurs standards (`red`, `blue`, `green`, `orange`, `black`, `white`, `gray`...), mais on les utilise rarement en production.

### Couleur hexadécimale (`#RRGGBB`)

```css
h1 { color: #1A7A2A; }        /* Vert CESAG */
nav { background-color: #E8420A; } /* Orange CESAG */
p  { color: #333333; }        /* Gris foncé */
body { background-color: #F5F5F5; } /* Gris très clair */
```

Le format `#RRGGBB` est composé de 3 paires hexadécimales (de `00` à `FF`) pour Rouge, Vert, Bleu.

```{admonition} Raccourci hexadécimal
:class: note
Quand les 3 paires sont identiques deux à deux, on peut abréger :
- `#FFFFFF` → `#FFF` (blanc)
- `#000000` → `#000` (noir)
- `#336633` → `#363` (vert foncé)
- `#1A7A2A` → ne peut pas être abrégé (paires différentes)
```

### Couleur RGB

```css
h1 { color: rgb(26, 122, 42); }         /* Vert CESAG */
nav { background-color: rgb(232, 66, 10); } /* Orange CESAG */

/* Avec transparence (canal alpha de 0 à 1) */
.overlay { background-color: rgba(0, 0, 0, 0.5); }   /* Noir 50% transparent */
.bandeau { background-color: rgba(26, 122, 42, 0.15); } /* Vert clair */
```

### Couleur HSL

```css
/* Teinte (0-360°), Saturation (0-100%), Luminosité (0-100%) */
h1 { color: hsl(133, 65%, 29%); }            /* Vert CESAG */
.alert { background-color: hsla(15, 92%, 47%, 0.2); } /* Orange transparent */
```

---

## 2.1.6 Les propriétés de texte

```css
p {
    /* Police */
    font-family: Arial, Helvetica, sans-serif;
    font-size: 16px;
    font-weight: bold;       /* normal | bold | 100 à 900 */
    font-style: italic;      /* normal | italic | oblique */

    /* Texte */
    color: #333333;
    text-align: center;      /* left | right | center | justify */
    text-decoration: underline; /* none | underline | line-through | overline */
    text-transform: uppercase;  /* none | uppercase | lowercase | capitalize */
    line-height: 1.6;        /* Interligne (sans unité = multiplicateur) */
    letter-spacing: 0.05em;  /* Espacement entre lettres */
    word-spacing: 4px;       /* Espacement entre mots */
    text-indent: 30px;       /* Indentation de la première ligne */
}
```

### Les unités CSS

| Unité | Type | Description | Exemple |
|-------|------|-------------|---------|
| `px` | Absolue | Pixel écran | `font-size: 16px` |
| `em` | Relative | Relatif à la police du parent | `padding: 1em` |
| `rem` | Relative | Relatif à la police racine (`html`) | `font-size: 1.2rem` |
| `%` | Relative | Pourcentage du parent | `width: 50%` |
| `vw` | Viewport | % de la largeur de l'écran | `width: 100vw` |
| `vh` | Viewport | % de la hauteur de l'écran | `height: 100vh` |

```{admonition} Bonne pratique — rem pour les tailles de texte
:class: tip
Utilise `rem` pour les tailles de police et `px` pour les bordures et les petits espacements. `rem` s'adapte si l'utilisateur change la taille de police de son navigateur (accessibilité).
```

---

## 2.1.7 Les polices web — Google Fonts

Pour utiliser des polices plus belles que les polices système :

**Étape 1** — Dans le `<head>` du HTML, avant ton `<link>` CSS :
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Lato:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
```

**Étape 2** — Dans ton CSS :
```css
body {
    font-family: 'Roboto', sans-serif;
}

h1, h2, h3 {
    font-family: 'Lato', sans-serif;
    font-weight: 700;
}
```

---

## 2.1.8 La cascade et la spécificité

CSS signifie "Cascading" (en cascade). Quand plusieurs règles s'appliquent au même élément, le navigateur doit décider laquelle "gagne".

### Ordre de priorité (du plus fort au plus faible)

```
1. CSS inline          style="color: red"         → priorité maximale
2. ID                  #mon-id { color: red; }
3. Classe              .ma-classe { color: red; }
4. Élément             p { color: red; }           → priorité minimale
```

### Exemple concret

```html
<p id="para-special" class="intro">Quelle couleur ?</p>
```

```css
p          { color: black; }   /* Spécificité : 001 */
.intro     { color: blue; }    /* Spécificité : 010 */
#para-special { color: green; } /* Spécificité : 100 */
```

→ Le texte sera **vert** car `#id` a la spécificité la plus haute.

### `!important` — À éviter

```css
p { color: red !important; } /* Écrase TOUT — à éviter sauf en dernier recours */
```

```{admonition} Règle pratique
:class: tip
Si tu te bats avec la spécificité, c'est souvent signe que ta structure CSS doit être repensée. Évite `!important` — c'est une rustine, pas une solution.
```

---

## 2.1.9 Les commentaires CSS

```css
/* Commentaire sur une ligne */

/*
 * Commentaire
 * sur plusieurs lignes
 */

/* =====================
   Section Navigation
   ===================== */
nav {
    background-color: #1A7A2A; /* Vert CESAG */
}
```

---

## 2.1.10 Les outils de développement — DevTools CSS

Dans Chrome, `F12` → onglet **Elements** :
- Sélectionne un élément dans le HTML → ses styles CSS apparaissent à droite
- Tu peux **modifier les valeurs en direct** (temporairement) pour tester
- Les propriétés barrées sont **écrasées** par une règle plus spécifique
- La case à cocher permet **d'activer/désactiver** une propriété

---

## Résumé de la leçon

```{admonition} Ce qu'il faut retenir
:class: tip
| Concept | Description |
|---------|-------------|
| CSS externe | Fichier `.css` lié avec `<link rel="stylesheet">` |
| Sélecteur élément | `p { }` — cible toutes les balises `<p>` |
| Sélecteur classe | `.nom { }` — cible `class="nom"` (réutilisable) |
| Sélecteur id | `#nom { }` — cible `id="nom"` (unique par page) |
| Couleur hex | `#RRGGBB` — ex: `#1A7A2A` |
| Couleur rgb/rgba | `rgb(r,g,b)` / `rgba(r,g,b,alpha)` |
| `font-family` | Police de caractères |
| `font-size` | Taille du texte |
| `color` | Couleur du texte |
| `background-color` | Couleur de fond |
| `text-align` | Alignement du texte |
| Cascade | Le sélecteur le plus spécifique l'emporte |
```

---

## TP 6 — Première feuille de style

```{admonition} Exercice — À faire en TD (2 heures)
:class: warning

### Objectif
Créer un fichier CSS externe et styliser la page personnelle réalisée en HTML.

### Structure de fichiers attendue
```
mon-site/
├── index.html
├── style.css          ← à créer
└── images/
    └── photo.jpg
```

### Consignes

**1. Créer et lier le fichier CSS (2 pts)**
- Crée `style.css` dans le même dossier que `index.html`
- Lie-le dans le `<head>` de `index.html` avec `<link>`
- Vérifie que le lien fonctionne (ajoute `body { background-color: #f5f5f5; }` et recharge)

**2. Intégrer Google Fonts (2 pts)**
- Choisis 2 polices sur fonts.google.com (une pour les titres, une pour le corps)
- Intègre-les dans le `<head>` avant ton `<link>`
- Applique-les via `font-family` dans le CSS

**3. Styliser les titres (3 pts)**
- `h1` : couleur verte `#1A7A2A`, grande taille, centré
- `h2` : couleur plus sombre, bordure inférieure orange `#E8420A`
- `h3` : couleur grise, italique

**4. Styliser le texte (3 pts)**
- `body` : police choisie, taille 16px, couleur `#333`, interligne 1.7
- `p` : espacement entre paragraphes
- `a` : couleur verte, sans soulignement ; au survol (`a:hover`) couleur orange

**5. Couleurs et fonds (4 pts)**
- `header` : fond vert CESAG `#1A7A2A`, texte blanc, `padding: 30px`, `text-align: center`
- `nav` : fond légèrement coloré, liens espacés
- `footer` : fond gris foncé, texte blanc, centré

**6. Classes personnalisées (3 pts)**
Crée au moins 3 classes CSS et utilise-les dans le HTML :
- `.mise-en-avant` : fond coloré, bordure gauche, padding
- `.citation` : italique, couleur différente, indentation
- `.badge` : petit encadré arrondi (pour ta filière par exemple)

**7. Bonus — Polices et effets (3 pts)**
- Utilise des `letter-spacing` sur les titres
- Ajoute une `text-shadow` sur le `h1`
- Stylise les liens du `nav` comme des boutons

### Rendu
Fichiers `index.html` + `style.css`
```

---

*Leçon suivante → [Leçon 8 — Sélecteurs avancés et pseudo-classes](08-selecteurs-avances)*
