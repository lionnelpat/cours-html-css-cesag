# Leçon 11 — CSS Grid : mise en page en grille

```{admonition} Objectifs de cette leçon
:class: tip
À la fin de cette leçon, tu sauras :
- Créer une grille avec `display: grid`
- Définir colonnes et lignes avec `grid-template-columns/rows`
- Utiliser `fr`, `repeat()` et `minmax()`
- Placer des éléments précisément dans la grille
- Créer des zones nommées avec `grid-template-areas`
- Choisir entre Flexbox et Grid selon le cas
```

---

## 1. Flexbox vs Grid — Quand utiliser lequel ?

| | **Flexbox** | **CSS Grid** |
|---|-------------|-------------|
| **Dimension** | 1D (une ligne OU une colonne) | 2D (lignes ET colonnes simultanément) |
| **Usage** | Navigation, composants, alignement | Mise en page globale, galeries |
| **Contrôle** | Enfants contrôlent leur espace | Conteneur contrôle tout |

```{admonition} Règle pratique
:class: tip
- **Flexbox** : pour aligner des éléments **dans une seule direction** (une rangée de boutons, une navigation, une liste de cartes sur une ligne)
- **Grid** : pour des **mises en page à 2 dimensions** (colonnes + lignes, layout de page entier)
- On peut (et doit souvent) **les combiner** : Grid pour le layout global, Flexbox pour les composants à l'intérieur
```

---

## 2. Activer CSS Grid

```css
.conteneur {
    display: grid;
}
```

Sans définir de colonnes, les éléments s'empilent comme en `display: block`.

---

## 3. `grid-template-columns` — Définir les colonnes

```css
/* 3 colonnes de 200px chacune */
.grille {
    display: grid;
    grid-template-columns: 200px 200px 200px;
}

/* 3 colonnes : tailles différentes */
.grille {
    grid-template-columns: 300px 1fr 200px;
    /* sidebar fixe | contenu flexible | aside fixe */
}

/* La nouvelle unité fr (fraction) */
.grille {
    grid-template-columns: 1fr 1fr 1fr;  /* 3 colonnes égales */
    grid-template-columns: 1fr 2fr 1fr;  /* Colonne du milieu = 2x plus large */
    grid-template-columns: 2fr 1fr;      /* 2 colonnes : 66% / 33% */
}
```

### La fonction `repeat()`

```css
/* repeat(nombre, taille) */
grid-template-columns: repeat(3, 1fr);         /* 3 colonnes égales */
grid-template-columns: repeat(4, 250px);        /* 4 colonnes de 250px */
grid-template-columns: repeat(3, 1fr) 200px;   /* 3 flexibles + 1 fixe */
```

### La fonction `minmax()`

```css
/* minmax(taille-min, taille-max) */
grid-template-columns: repeat(3, minmax(200px, 1fr));
/* Chaque colonne : minimum 200px, maximum 1fr */
```

### `auto-fill` et `auto-fit` — Grilles auto-adaptatives

```css
/* Autant de colonnes de 250px que possible */
grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
/* Sur un écran large → 4 colonnes, sur mobile → 1 colonne */
/* Sans media query ! */

/* auto-fit : efface les colonnes vides (éléments s'étalent) */
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
```

---

## 4. `grid-template-rows` — Définir les lignes

```css
.grille {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: 100px 1fr 80px;  /* header | contenu | footer */
}
```

---

## 5. `gap` — L'espace entre cellules

```css
.grille {
    display: grid;
    gap: 20px;           /* Même espace entre colonnes et lignes */
    gap: 16px 24px;      /* row-gap | column-gap */
    row-gap: 16px;
    column-gap: 24px;
}
```

---

## 6. Placer les éléments dans la grille

Par défaut, les éléments s'placent automatiquement dans les cellules. On peut aussi les placer **manuellement** :

### `grid-column` et `grid-row`

```
Lignes de grille (colonnes) :
   1     2     3     4
   ↓     ↓     ↓     ↓
   ┌─────┬─────┬─────┐ ← ligne 1
   │  A  │  B  │  C  │
   ├─────┼─────┼─────┤ ← ligne 2
   │  D  │  E  │  F  │
   └─────┴─────┴─────┘ ← ligne 3
```

```css
/* Un élément qui s'étend de la colonne 1 à 3 */
.grand-element {
    grid-column: 1 / 3;    /* De la ligne 1 à la ligne 3 */
    /* Équivalent : grid-column-start: 1; grid-column-end: 3; */
}

/* Raccourci avec span */
.deux-colonnes {
    grid-column: span 2;    /* S'étend sur 2 colonnes */
}

.trois-colonnes {
    grid-column: 1 / -1;    /* De la 1ère à la dernière ligne (-1) */
}

/* Placement précis */
.element {
    grid-column: 2 / 4;    /* Colonnes 2 et 3 */
    grid-row: 1 / 3;       /* Lignes 1 et 2 */
}
```

---

## 7. `grid-template-areas` — Zones nommées

La fonctionnalité la plus puissante de Grid : nommer les zones visuellement.

```css
.layout {
    display: grid;
    grid-template-columns: 280px 1fr;
    grid-template-rows: 64px 1fr 60px;
    grid-template-areas:
        "header  header"
        "sidebar contenu"
        "footer  footer";
    min-height: 100vh;
    gap: 0;
}

/* Assigner chaque élément à sa zone */
.entete   { grid-area: header; }
.sidebar  { grid-area: sidebar; }
.principal { grid-area: contenu; }
.piedpage  { grid-area: footer; }
```

```html
<!-- HTML correspondant -->
<div class="layout">
    <header class="entete">En-tête</header>
    <aside class="sidebar">Sidebar</aside>
    <main class="principal">Contenu principal</main>
    <footer class="piedpage">Pied de page</footer>
</div>
```

```{admonition} grid-template-areas — Visualisation
:class: tip
La déclaration CSS est un **plan visuel** de la page :
```css
grid-template-areas:
    "header  header"    /* ← ligne 1 : header sur toute la largeur */
    "sidebar contenu"   /* ← ligne 2 : sidebar + contenu */
    "footer  footer";   /* ← ligne 3 : footer sur toute la largeur */
```
C'est comme dessiner la maquette directement dans le CSS !
```

### Cellule vide avec `.`

```css
grid-template-areas:
    "header  header  header"
    "sidebar contenu  .    "   /* Cellule vide en bas à droite */
    "footer  footer  footer";
```

---

## 8. Alignement dans la grille

```css
/* Alignement de tous les items dans leurs cellules */
.grille {
    align-items: center;     /* Vertical : start | end | center | stretch */
    justify-items: center;   /* Horizontal : start | end | center | stretch */
    place-items: center;     /* Raccourci : align + justify */
}

/* Alignement de la grille dans son conteneur */
.grille {
    align-content: center;    /* Vertical de la grille entière */
    justify-content: center;  /* Horizontal de la grille entière */
    place-content: center;    /* Raccourci */
}

/* Alignement individuel d'un item */
.item-special {
    align-self: end;
    justify-self: center;
    place-self: center end;
}
```

---

## 9. Exemples pratiques complets

### Layout de page classique

```css
*, *::before, *::after { box-sizing: border-box; }

body { margin: 0; }

.page-layout {
    display: grid;
    grid-template-columns: 260px 1fr;
    grid-template-rows: 64px 1fr auto;
    grid-template-areas:
        "nav    nav    "
        "aside  main   "
        "footer footer ";
    min-height: 100vh;
}

/* Styles des zones */
nav {
    grid-area: nav;
    background: #1A7A2A;
    display: flex;
    align-items: center;
    padding: 0 24px;
    color: white;
}

aside {
    grid-area: aside;
    background: #f4f9f4;
    padding: 24px;
    border-right: 1px solid #c8dfc8;
}

main {
    grid-area: main;
    padding: 24px;
}

footer {
    grid-area: footer;
    background: #1A7A2A;
    color: white;
    padding: 20px 24px;
    text-align: center;
}
```

### Galerie de photos

```css
.galerie {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 16px;
    padding: 24px;
}

.photo {
    width: 100%;
    height: 220px;
    object-fit: cover;
    border-radius: 8px;
    transition: transform 0.2s, box-shadow 0.2s;
}

.photo:hover {
    transform: scale(1.03);
    box-shadow: 0 8px 24px rgba(0,0,0,0.15);
}

/* Photo vedette — occupe 2 colonnes et 2 lignes */
.photo-vedette {
    grid-column: span 2;
    grid-row: span 2;
    height: 100%;
}
```

### Grille de cards de cours

```css
.grille-cours {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    max-width: 1100px;
    margin: 0 auto;
    padding: 40px 24px;
}

.card-cours {
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    transition: transform 0.2s, box-shadow 0.2s;
}

.card-cours:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(0,0,0,0.12);
}

.card-cours-header {
    background: #1A7A2A;
    padding: 20px;
    color: white;
}

.card-cours-body {
    padding: 20px;
}
```

---

## Résumé de la leçon

```{admonition} Ce qu'il faut retenir
:class: tip
| Propriété | Valeurs clés | Usage |
|-----------|-------------|-------|
| `display: grid` | — | Active Grid |
| `grid-template-columns` | `repeat(3, 1fr)` | Définit les colonnes |
| `grid-template-rows` | `64px 1fr auto` | Définit les lignes |
| `fr` | `1fr`, `2fr` | Fraction de l'espace disponible |
| `repeat(n, taille)` | `repeat(3, 1fr)` | Répète la définition |
| `minmax(min, max)` | `minmax(200px, 1fr)` | Taille min et max |
| `auto-fit` | — | Colonnes auto-adaptatives |
| `gap` | `20px` | Espace entre cellules |
| `grid-column` | `1 / 3`, `span 2` | Placement en colonnes |
| `grid-row` | `1 / 3`, `span 2` | Placement en lignes |
| `grid-template-areas` | `"header header"` | Zones nommées (le plus lisible) |
| `grid-area` | `header` | Assigne un item à sa zone |
```

---

## TP 11 — Site CESAG avec Grid

```{admonition} Exercice — À faire en TD
:class: warning

### Objectif
Créer la maquette complète d'un site CESAG en utilisant CSS Grid pour le layout et Flexbox pour les composants.

### Structure HTML à créer

```html
<body>
    <div class="page-layout">
        <header class="entete">...</header>
        <nav class="navigation">...</nav>
        <main class="contenu">
            <section class="hero">...</section>
            <section class="nos-formations">
                <div class="grille-formations">
                    <!-- 6 cards de formations -->
                </div>
            </section>
        </main>
        <aside class="sidebar">...</aside>
        <footer class="pied-page">...</footer>
    </div>
</body>
```

**1. Layout de page avec grid-template-areas (6 pts)**
```css
.page-layout {
    display: grid;
    grid-template-columns: 1fr 280px;
    grid-template-rows: auto auto 1fr auto;
    grid-template-areas:
        "entete    entete "
        "navigation navigation"
        "contenu   sidebar"
        "footer    footer ";
}
```

**2. Grille de 6 formations en 3 colonnes (5 pts)**
- `grid-template-columns: repeat(3, 1fr)`
- `gap: 20px`
- Chaque card : icône + titre + description + bouton
- Au survol : `transform: translateY(-4px)` + ombre

**3. Photo vedette dans la grille (3 pts)**
Ajoute une image `grid-column: span 2` ou `grid-area` nommée pour qu'elle occupe plus de place.

**4. Section stats avec Grid (3 pts)**
```html
<section class="stats">
    <div>45 ans d'existence</div>
    <div>+15 000 diplômés</div>
    <div>20 pays représentés</div>
    <div>95% d'insertion</div>
</section>
```
`grid-template-columns: repeat(4, 1fr)` — chiffres clés côte à côte.

**5. Qualité et organisation CSS (3 pts)**
- `box-sizing: border-box` en premier
- CSS bien commenté et organisé par section
- Flexbox utilisé à l'intérieur des composants (nav, cards...)

### Rendu
Fichiers `cesag.html` + `style.css`
```

---

*Leçon suivante → [Leçon 12 — Responsive Design et Media Queries](12-responsive-design)*
