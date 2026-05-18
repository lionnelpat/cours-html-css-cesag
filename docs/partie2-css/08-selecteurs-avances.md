# Leçon 8 — Sélecteurs avancés et pseudo-classes

```{admonition} Objectifs de cette leçon
:class: tip
À la fin de cette leçon, tu sauras :
- Utiliser les sélecteurs de combinaison (descendant, enfant direct, adjacent)
- Appliquer des styles avec les pseudo-classes (`:hover`, `:focus`, `:nth-child`...)
- Utiliser les pseudo-éléments (`::before`, `::after`, `::first-line`...)
- Comprendre les sélecteurs d'attributs
- Créer des effets interactifs CSS sans JavaScript
```

---

## 1. Les sélecteurs de combinaison

Ces sélecteurs permettent de cibler des éléments selon leur **position dans le HTML**.

### Sélecteur descendant (espace)

Cible tous les éléments B qui se trouvent **à l'intérieur** de A (peu importe la profondeur) :

```css
/* Tous les <a> qui sont dans un <nav> */
nav a {
    color: white;
    text-decoration: none;
    padding: 8px 16px;
}

/* Tous les <p> qui sont dans un <article> */
article p {
    font-size: 16px;
    line-height: 1.8;
}
```

```html
<nav>
    <a href="#">Accueil</a>      <!-- ✅ ciblé -->
    <ul>
        <li><a href="#">Formations</a></li>  <!-- ✅ ciblé aussi -->
    </ul>
</nav>
<a href="#">Lien hors du nav</a>  <!-- ❌ pas ciblé -->
```

### Sélecteur enfant direct (`>`)

Cible les éléments B qui sont des **enfants directs** de A uniquement :

```css
/* Seulement les <li> directement dans le <ul>, pas les sous-listes */
ul > li {
    border-bottom: 1px solid #eee;
    padding: 8px 0;
}

/* Seulement les <p> directement dans <section>, pas dans des sous-div */
section > p {
    font-size: 1.1em;
}
```

```html
<ul>
    <li>Item 1</li>          <!-- ✅ enfant direct -->
    <li>Item 2
        <ul>
            <li>Sous-item</li>  <!-- ❌ pas enfant direct du premier ul -->
        </ul>
    </li>
</ul>
```

### Sélecteur adjacent (`+`)

Cible l'élément B qui vient **immédiatement après** A :

```css
/* Le <p> qui suit immédiatement un <h2> */
h2 + p {
    font-size: 1.1em;
    color: #555;
    font-style: italic;
}
```

```html
<h2>Titre de section</h2>
<p>Ce paragraphe est ciblé.</p>    <!-- ✅ immédiatement après h2 -->
<p>Ce paragraphe n'est pas ciblé.</p>  <!-- ❌ pas adjacent -->
```

### Sélecteur de fratrie (`~`)

Cible **tous** les éléments B qui viennent après A (pas seulement le premier) :

```css
/* Tous les <p> qui suivent un <h2> dans le même parent */
h2 ~ p {
    margin-left: 16px;
}
```

### Tableau récapitulatif

| Sélecteur | Syntaxe | Cible |
|-----------|---------|-------|
| Descendant | `A B` | Tous les B dans A |
| Enfant direct | `A > B` | B enfant direct de A |
| Adjacent | `A + B` | B immédiatement après A |
| Fratrie | `A ~ B` | Tous les B après A |

---

## 2. Les sélecteurs d'attributs

Permettent de cibler des éléments selon leurs **attributs HTML** :

```css
/* Éléments ayant l'attribut alt */
img[alt] {
    border: 2px solid green;
}

/* Liens vers des sites externes */
a[href^="https"] {
    color: #1A7A2A;
}

/* Liens vers des PDF */
a[href$=".pdf"] {
    padding-right: 20px;
    background: url('icone-pdf.png') right center no-repeat;
}

/* Liens contenant "cesag" dans l'URL */
a[href*="cesag"] {
    font-weight: bold;
}

/* Inputs de type email */
input[type="email"] {
    border-color: #1A7A2A;
}

/* Éléments avec une classe qui contient "btn" dans une liste */
[class~="btn"] {
    cursor: pointer;
}
```

| Sélecteur | Signification |
|-----------|---------------|
| `[attr]` | A l'attribut `attr` |
| `[attr="val"]` | `attr` est exactement `"val"` |
| `[attr^="val"]` | `attr` **commence** par `"val"` |
| `[attr$="val"]` | `attr` **finit** par `"val"` |
| `[attr*="val"]` | `attr` **contient** `"val"` |
| `[attr~="val"]` | `attr` contient le mot `"val"` |

---

## 3. Les pseudo-classes

Les pseudo-classes ciblent un élément selon son **état** ou sa **position**.

### Pseudo-classes d'interaction utilisateur

```css
/* Survol de la souris */
a:hover {
    color: #E8420A;
    text-decoration: underline;
}

button:hover {
    background-color: #155f22;
    cursor: pointer;
}

/* Clic (pendant que le bouton est enfoncé) */
button:active {
    transform: scale(0.97);
}

/* Focus (élément sélectionné au clavier ou clic) */
input:focus,
textarea:focus,
select:focus {
    outline: 2px solid #1A7A2A;
    border-color: #1A7A2A;
    background-color: #f0f9f0;
}

/* Lien déjà visité */
a:visited {
    color: #888;
}

/* Lien non encore visité */
a:link {
    color: #1A7A2A;
}
```

### Pseudo-classes de position (enfants)

```css
/* Le premier enfant */
li:first-child {
    font-weight: bold;
    color: #1A7A2A;
}

/* Le dernier enfant */
li:last-child {
    border-bottom: none;
}

/* Le nième enfant (nombre précis) */
tr:nth-child(3) {
    background-color: #fff3ee;
}

/* Lignes paires d'un tableau */
tr:nth-child(even) {
    background-color: #f2f9f2;
}

/* Lignes impaires d'un tableau */
tr:nth-child(odd) {
    background-color: white;
}

/* Tous les 3 éléments en commençant au 1er */
li:nth-child(3n+1) {
    color: #1A7A2A;
}

/* Seul enfant */
p:only-child {
    font-style: italic;
}
```

### Pseudo-classes de formulaire

```css
/* Champ obligatoire */
input:required {
    border-left: 3px solid #E8420A;
}

/* Champ valide */
input:valid {
    border-color: #1A7A2A;
}

/* Champ invalide */
input:invalid {
    border-color: #c62828;
    background-color: #fdf0f0;
}

/* Champ désactivé */
input:disabled {
    background-color: #f0f0f0;
    color: #999;
    cursor: not-allowed;
}

/* Case cochée */
input[type="checkbox"]:checked + label {
    color: #1A7A2A;
    font-weight: bold;
}

/* Champ avec un placeholder affiché */
input:placeholder-shown {
    border-color: #ccc;
}
```

### La pseudo-classe `:not()`

```css
/* Tous les <p> sauf ceux avec la classe .intro */
p:not(.intro) {
    color: #555;
}

/* Tous les liens sauf ceux dans le nav */
a:not(nav a) {
    text-decoration: underline;
}

/* Tous les li sauf le dernier */
li:not(:last-child) {
    border-bottom: 1px solid #eee;
}
```

---

## 4. Les pseudo-éléments

Les pseudo-éléments ciblent une **partie** d'un élément ou insèrent du contenu.

### `::before` et `::after`

Insèrent du contenu **avant** ou **après** un élément (sans modifier le HTML) :

```css
/* Ajouter une icône avant les liens externes */
a[href^="https"]::before {
    content: "🔗 ";
}

/* Ajouter "PDF" après les liens PDF */
a[href$=".pdf"]::after {
    content: " (PDF)";
    font-size: 0.8em;
    color: #E8420A;
}

/* Ligne décorative sous les titres */
h2::after {
    content: "";
    display: block;
    width: 50px;
    height: 3px;
    background-color: #E8420A;
    margin-top: 8px;
}

/* Guillemets automatiques */
blockquote::before {
    content: "\201C";  /* " */
    font-size: 3em;
    color: #1A7A2A;
    line-height: 0;
    vertical-align: -0.4em;
}
```

```{admonition} La propriété content est obligatoire
:class: note
`::before` et `::after` nécessitent **toujours** `content: ""` (même vide) pour s'afficher. Sans cette propriété, le pseudo-élément est ignoré.
```

### `::first-line` et `::first-letter`

```css
/* Style de la première ligne d'un paragraphe */
p::first-line {
    font-weight: bold;
    color: #1A7A2A;
}

/* Lettre capitale stylisée (effet magazine) */
article p:first-child::first-letter {
    font-size: 3em;
    font-weight: bold;
    float: left;
    line-height: 0.8;
    margin-right: 8px;
    color: #1A7A2A;
}
```

### `::placeholder`

```css
/* Style du texte placeholder dans les inputs */
input::placeholder,
textarea::placeholder {
    color: #aaa;
    font-style: italic;
}
```

### `::selection`

```css
/* Style du texte sélectionné (surligné) par l'utilisateur */
::selection {
    background-color: #1A7A2A;
    color: white;
}
```

---

## 5. Exemple complet — Navigation stylisée

```html
<!-- HTML -->
<nav>
    <ul>
        <li><a href="index.html" class="actif">Accueil</a></li>
        <li><a href="formations.html">Formations</a></li>
        <li><a href="classe.html">Notre classe</a></li>
        <li><a href="contact.html">Contact</a></li>
    </ul>
</nav>
```

```css
/* CSS */
nav {
    background-color: #1A7A2A;
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;  /* On verra Flexbox en leçon 10 */
}

nav ul > li {
    position: relative;
}

nav a {
    display: block;
    color: white;
    text-decoration: none;
    padding: 16px 20px;
    transition: background-color 0.2s;
}

nav a:hover {
    background-color: #155f22;
}

nav a.actif {
    background-color: #E8420A;
    font-weight: bold;
}

/* Indicateur sous le lien au survol */
nav a::after {
    content: "";
    display: block;
    height: 3px;
    background-color: white;
    transform: scaleX(0);
    transition: transform 0.2s;
}

nav a:hover::after {
    transform: scaleX(1);
}
```

---

## Résumé de la leçon

```{admonition} Ce qu'il faut retenir
:class: tip
| Sélecteur | Syntaxe | Usage |
|-----------|---------|-------|
| Descendant | `A B` | B dans A (tout niveau) |
| Enfant direct | `A > B` | B directement dans A |
| Adjacent | `A + B` | B juste après A |
| Attribut | `[attr^="val"]` | Commence par val |
| Survol | `:hover` | Au passage de la souris |
| Focus | `:focus` | Champ actif |
| Nième enfant | `:nth-child(n)` | Position dans le parent |
| Paires/impaires | `:nth-child(even/odd)` | Lignes alternées |
| Négation | `:not(sélecteur)` | Tout sauf... |
| Contenu avant | `::before` | Insérer avant (avec `content`) |
| Contenu après | `::after` | Insérer après (avec `content`) |
| Première lettre | `::first-letter` | Lettre capitale |
| Placeholder | `::placeholder` | Texte d'exemple des inputs |
```

---

## TP 8 — Navigation et effets interactifs

```{admonition} Exercice — À faire en TD
:class: warning

### Objectif
Améliorer la navigation et les formulaires avec des sélecteurs avancés.

### Consignes

**1. Navigation interactive (5 pts)**
Dans le CSS, stylise la navigation sans toucher au HTML :
- Liens du nav : fond vert, texte blanc, pas de soulignement
- Au `:hover` : fond plus sombre + transition douce (`transition: 0.2s`)
- Lien actif (classe `.actif`) : fond orange CESAG
- Ajouter un `::after` décoratif sous les liens au survol

**2. Tableau avec lignes alternées (3 pts)**
- Lignes paires : fond vert très clair `#f2f9f2`
- Ligne au survol : fond vert clair + curseur pointer
- Première ligne (`thead tr`) : fond vert CESAG + texte blanc

**3. Formulaire stylisé (5 pts)**
- Inputs en `:focus` : bordure verte + fond légèrement teinté
- Inputs `:invalid` : bordure rouge
- Champs `:required` : bordure gauche orange
- `::placeholder` en gris italique
- Bouton submit en vert, au `:hover` plus sombre + `transform: scale(1.02)`

**4. Effets typographiques (3 pts)**
- `article p:first-child::first-letter` : grande lettre capitale colorée
- `::selection` : couleur de sélection aux couleurs CESAG
- `blockquote::before` et `::after` : guillemets décoratifs

**5. Liens intelligents (2 pts)**
- `a[href^="http"]::after` : ajouter " ↗" après les liens externes
- `a[href$=".pdf"]::before` : ajouter un indicateur PDF

### Rendu
Fichier `style.css` mis à jour
```

---

*Leçon suivante → [Leçon 9 — Le modèle de boîte (Box Model)](09-box-model)*
