# 2.4 Flexbox : mise en page moderne

```{admonition} Objectifs de cette leçon
:class: tip
À la fin de cette leçon, tu sauras :
- Activer Flexbox avec `display: flex`
- Contrôler la direction avec `flex-direction`
- Aligner les éléments sur les axes principal et secondaire
- Gérer le retour à la ligne avec `flex-wrap`
- Distribuer l'espace avec `justify-content` et `align-items`
- Utiliser `gap` pour espacer les éléments
- Contrôler chaque enfant avec `flex`, `order`, `align-self`
```

---

## 2.4.1 Pourquoi Flexbox ?

Avant Flexbox, créer une mise en page en CSS était une vraie torture — on utilisait des `float`, des `position`, des `table`... tout était compliqué et fragile.

**Flexbox** (Flexible Box Layout) est un système de mise en page CSS qui permet de :
- Aligner des éléments **horizontalement et verticalement** facilement
- Distribuer l'espace **automatiquement** entre les éléments
- Créer des **mises en page responsives** sans calculs complexes

---

## 2.4.2 Concepts de base — Conteneur et enfants

Flexbox fonctionne sur deux niveaux :

```
┌─────────────────────────────────────────┐
│  CONTENEUR FLEX (display: flex)         │
│  ┌───────┐  ┌───────┐  ┌───────┐        │
│  │Enfant1│  │Enfant2│  │Enfant3│        │
│  └───────┘  └───────┘  └───────┘        │
└─────────────────────────────────────────┘
```

- Le **conteneur flex** : l'élément parent avec `display: flex`
- Les **enfants flex** : les éléments directs du conteneur

```html
<!-- HTML -->
<div class="conteneur">   <!-- Conteneur flex -->
    <div class="item">A</div>  <!-- Enfant flex -->
    <div class="item">B</div>  <!-- Enfant flex -->
    <div class="item">C</div>  <!-- Enfant flex -->
</div>
```

```css
/* Activer Flexbox */
.conteneur {
    display: flex;
    /* Les 3 divs s'alignent maintenant horizontalement */
}
```

---

## 2.4.3 L'axe principal et l'axe secondaire

Flexbox utilise deux axes :

```
Axe principal (main axis) → → → → → → → → →
┌─────────────────────────────────────────────┐ ↑
│  ┌───────┐  ┌───────┐  ┌───────┐            │ │ Axe secondaire
│  │  A    │  │  B    │  │  C    │            │ │ (cross axis)
│  └───────┘  └───────┘  └───────┘            │ ↓
└─────────────────────────────────────────────┘
```

- **Axe principal** : direction des éléments (horizontal par défaut)
- **Axe secondaire** : perpendiculaire à l'axe principal

---

## 2.4.4 `flex-direction` — La direction

```css
.conteneur {
    display: flex;
    flex-direction: row;            /* ← Défaut — gauche à droite */
    flex-direction: row-reverse;    /* → droite à gauche */
    flex-direction: column;         /* ↓ haut en bas */
    flex-direction: column-reverse; /* ↑ bas en haut */
}
```

```css
/* Exemple pratique — Barre de navigation */
nav {
    display: flex;
    flex-direction: row;   /* liens côte à côte */
}

/* Exemple pratique — Colonne de liens */
.sidebar {
    display: flex;
    flex-direction: column;  /* liens empilés */
}
```

---

## 2.4.5 `justify-content` — Alignement sur l'axe principal

```css
.conteneur {
    display: flex;

    justify-content: flex-start;    /* ← [A B C     ] (défaut) */
    justify-content: flex-end;      /* →      [A B C] */
    justify-content: center;        /* →    [A B C]   (centré) */
    justify-content: space-between; /* → [A   B   C] */
    justify-content: space-around;  /* → [ A   B   C ] */
    justify-content: space-evenly;  /* → [  A  B  C  ] */
}
```

**Visualisation :**

```
flex-start:   [A][B][C]         ]
flex-end:     [         [A][B][C]]
center:       [    [A][B][C]     ]
space-between:[A]    [B]    [C]  ]
space-around: [ [A]  [B]  [C]   ]
space-evenly: [  [A]  [B]  [C]  ]
```

---

## 2.4.6 `align-items` — Alignement sur l'axe secondaire

```css
.conteneur {
    display: flex;
    height: 200px;  /* Nécessite une hauteur définie */

    align-items: stretch;      /* ↕ Étiré (défaut) — occupe toute la hauteur */
    align-items: flex-start;   /* ↑ En haut */
    align-items: flex-end;     /* ↓ En bas */
    align-items: center;       /* ↕ Centré verticalement */
    align-items: baseline;     /* Aligné sur la ligne de base du texte */
}
```

### Centrage parfait — La technique la plus utile de CSS

```css
/* Centrer horizontalement ET verticalement */
.centrage-parfait {
    display: flex;
    justify-content: center;   /* Centre sur l'axe horizontal */
    align-items: center;       /* Centre sur l'axe vertical */
    min-height: 100vh;         /* Toute la hauteur de l'écran */
}
```

---

## 2.4.7 `flex-wrap` — Le retour à la ligne

Par défaut, les éléments flex **ne reviennent pas à la ligne** — ils se rétrécissent pour tenir.

```css
.conteneur {
    display: flex;
    flex-wrap: nowrap;  /* Défaut — tous sur une ligne, rétrécis */
    flex-wrap: wrap;    /* Retour à la ligne si nécessaire */
    flex-wrap: wrap-reverse; /* Retour à la ligne inversé */
}
```

```css
/* Galerie de cartes responsive sans media queries */
.galerie {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.carte {
    flex: 0 0 calc(33.33% - 14px);  /* 3 colonnes avec gap */
    min-width: 280px;                 /* Minimum avant retour à la ligne */
}
```

---

## 2.4.8 `gap` — L'espacement entre éléments

`gap` remplace les marges entre éléments flex (et grid) :

```css
.conteneur {
    display: flex;
    gap: 20px;          /* Même espace horizontal et vertical */
    gap: 10px 20px;     /* row-gap | column-gap */
    row-gap: 10px;
    column-gap: 20px;
}
```

```{admonition} gap vs margin
:class: tip
Utilise `gap` plutôt que `margin` sur les enfants — `gap` ne crée pas d'espace sur les bords extérieurs du conteneur, ce qui évite les problèmes classiques de marge sur le premier/dernier élément.
```

---

## 2.4.9 Propriétés sur les enfants flex

### `flex` — La taille flexible

```css
/* flex: grow shrink basis */
.item { flex: 1; }           /* Raccourci : flex: 1 1 0 — grandit et rétrécit */
.item { flex: 2; }           /* Prend 2x plus d'espace que flex: 1 */
.item { flex: 0 0 200px; }   /* Taille fixe de 200px, ne grandit pas */
.item { flex: 1 0 auto; }    /* Grandit si besoin, taille minimale = contenu */

/* flex-grow : combien l'élément peut grandir */
.item { flex-grow: 0; }   /* Ne grandit pas (défaut) */
.item { flex-grow: 1; }   /* Grandit pour remplir l'espace disponible */
.item { flex-grow: 2; }   /* Grandit 2x plus que les autres */

/* flex-shrink : combien l'élément peut rétrécir */
.item { flex-shrink: 1; } /* Rétrécit si nécessaire (défaut) */
.item { flex-shrink: 0; } /* Ne rétrécit jamais */

/* flex-basis : taille de départ */
.item { flex-basis: 200px; }  /* Démarre à 200px */
.item { flex-basis: auto; }   /* Taille selon le contenu */
```

### `order` — L'ordre d'affichage

```css
/* Modifier l'ordre sans changer le HTML */
.premier  { order: -1; }  /* Avant tous */
.deuxieme { order: 0; }   /* Défaut */
.dernier  { order: 1; }   /* Après tous */
```

### `align-self` — Alignement individuel

```css
/* Écrase align-items pour un seul enfant */
.item-special {
    align-self: center;      /* Centré sur l'axe secondaire */
    align-self: flex-start;  /* En haut */
    align-self: stretch;     /* Étiré */
}
```

---

## 2.4.10 Exemples pratiques complets

### Navigation horizontale

```css
nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 24px;
    background-color: #1A7A2A;
    height: 60px;
}

.logo {
    font-size: 1.3em;
    font-weight: bold;
    color: white;
}

.nav-liens {
    display: flex;
    gap: 8px;
    list-style: none;
    margin: 0;
    padding: 0;
}

.nav-liens a {
    color: white;
    text-decoration: none;
    padding: 8px 16px;
    border-radius: 4px;
    transition: background 0.2s;
}

.nav-liens a:hover {
    background-color: rgba(255,255,255,0.15);
}
```

### Layout 2 colonnes (sidebar + contenu)

```css
.layout {
    display: flex;
    gap: 24px;
    max-width: 1200px;
    margin: 0 auto;
    padding: 24px;
}

.sidebar {
    flex: 0 0 280px;     /* Largeur fixe — ne grandit pas */
    background: #f4f9f4;
    padding: 20px;
    border-radius: 8px;
}

.contenu-principal {
    flex: 1;             /* Prend tout l'espace restant */
}
```

### Grille de cartes

```css
.grille-cartes {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.carte {
    flex: 1 1 300px;     /* Grandit, rétrécit, base 300px */
    max-width: calc(33.33% - 14px);
    background: white;
    border-radius: 8px;
    padding: 24px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
```

### Footer avec Flexbox

```css
footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 40px;
    background-color: #1A7A2A;
    color: white;
}

.footer-liens {
    display: flex;
    gap: 20px;
    list-style: none;
    margin: 0;
    padding: 0;
}
```

---

## Résumé de la leçon

```{admonition} Ce qu'il faut retenir
:class: tip
| Propriété | Valeurs clés | Usage |
|-----------|-------------|-------|
| `display: flex` | — | Active Flexbox sur le conteneur |
| `flex-direction` | `row` / `column` | Direction des éléments |
| `justify-content` | `center`, `space-between`, `flex-end`... | Alignement axe principal |
| `align-items` | `center`, `flex-start`, `stretch`... | Alignement axe secondaire |
| `flex-wrap: wrap` | — | Retour à la ligne automatique |
| `gap` | `20px`, `10px 20px` | Espace entre éléments |
| `flex: 1` | — | L'enfant prend l'espace disponible |
| `flex: 0 0 200px` | — | Taille fixe pour l'enfant |
| `order` | Nombre entier | Ordre d'affichage |
| `align-self` | Comme `align-items` | Alignement individuel |

**Recette magique — Centrer en Flexbox :**
```css
.parent {
    display: flex;
    justify-content: center;
    align-items: center;
}
```
```

---

## TP 10 — Navigation et layout avec Flexbox

```{admonition} Exercice — À faire en TD (2 heures)
:class: warning

### Objectif
Utiliser Flexbox pour créer une navigation responsive et un layout en colonnes.

### Consignes

**1. Navigation avec logo + liens (5 pts)**
Créer une `<nav>` avec :
```html
<nav>
    <div class="logo">CESAG</div>
    <ul class="nav-liens">
        <li><a href="#">Accueil</a></li>
        <li><a href="#">Formations</a></li>
        <li><a href="#">Étudiants</a></li>
        <li><a href="#">Contact</a></li>
    </ul>
</nav>
```
- Logo à gauche, liens à droite avec `justify-content: space-between`
- Alignement vertical centré avec `align-items: center`
- Fond vert CESAG, hauteur 64px
- Liens côte à côte avec `gap` et hover animé

**2. Section "hero" centrée (3 pts)**
```html
<section class="hero">
    <h1>Bienvenue au CESAG</h1>
    <p>Formation d'excellence en Afrique de l'Ouest</p>
    <a href="#" class="btn">Découvrir nos formations</a>
</section>
```
- Flexbox avec `flex-direction: column`
- `justify-content: center` + `align-items: center`
- Hauteur `80vh`, fond dégradé vert

**3. Grille de 3 cartes (5 pts)**
```html
<section class="grille">
    <div class="carte">HTML</div>
    <div class="carte">CSS</div>
    <div class="carte">JavaScript</div>
</section>
```
- `display: flex`, `gap: 24px`
- Chaque carte : `flex: 1`, padding, border-radius, ombre
- Au survol : `transform: translateY(-4px)` + transition

**4. Layout 2 colonnes (4 pts)**
- Sidebar fixe `280px` (flex: 0 0 280px)
- Contenu principal qui prend le reste (flex: 1)
- Gap de 24px entre les deux

**5. Footer 3 colonnes (3 pts)**
- `display: flex`, `justify-content: space-between`
- 3 sections : Logo + copyright | Liens rapides | Réseaux sociaux

### Rendu
Fichiers `layout.html` + `style.css`
```

---

*Leçon suivante → [Leçon 11 — CSS Grid](11-css-grid)*
