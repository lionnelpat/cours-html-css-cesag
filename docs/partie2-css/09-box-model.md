# 2.3 Le modèle de boîte (Box Model)

```{admonition} Objectifs de cette leçon
:class: tip
À la fin de cette leçon, tu sauras :
- Comprendre le modèle de boîte CSS (content, padding, border, margin)
- Utiliser `box-sizing: border-box` correctement
- Maîtriser `display` (block, inline, inline-block, none)
- Utiliser `position` (static, relative, absolute, fixed, sticky)
- Contrôler les débordements avec `overflow`
- Styliser les fonds et les bordures
```

---

## 2.3.1 Qu'est-ce que le Box Model ?

En CSS, **chaque élément HTML est une boîte rectangulaire** composée de 4 zones concentriques :

```
┌──────────────────────────────────┐
│            MARGIN                │  ← Espace extérieur (transparent)
│  ┌────────────────────────────┐  │
│  │          BORDER            │  │  ← Bordure visible
│  │  ┌──────────────────────┐  │  │
│  │  │       PADDING        │  │  │  ← Espace intérieur
│  │  │  ┌────────────────┐  │  │  │
│  │  │  │    CONTENT     │  │  │  │  ← Le contenu (texte, image...)
│  │  │  └────────────────┘  │  │  │
│  │  └──────────────────────┘  │  │
│  └────────────────────────────┘  │
└──────────────────────────────────┘
```

### Les 4 zones

| Zone | Propriété CSS | Description |
|------|--------------|-------------|
| **Content** | `width`, `height` | La zone du contenu réel |
| **Padding** | `padding` | Espace entre le contenu et la bordure |
| **Border** | `border` | La bordure visible |
| **Margin** | `margin` | Espace entre cet élément et les autres |

---

## 2.3.2 Padding — l'espace intérieur

```css
/* Les 4 côtés en une seule propriété */
div { padding: 20px; }                    /* Tous les côtés : 20px */
div { padding: 10px 20px; }              /* Haut/bas : 10px | Gauche/droite : 20px */
div { padding: 10px 20px 15px; }         /* Haut : 10px | Gauche/droite : 20px | Bas : 15px */
div { padding: 10px 20px 15px 25px; }    /* Haut | Droite | Bas | Gauche (sens horaire) */

/* Côtés individuels */
div { padding-top: 10px; }
div { padding-right: 20px; }
div { padding-bottom: 10px; }
div { padding-left: 20px; }
```

```{admonition} Moyen mnémotechnique — TRouBLe
:class: tip
L'ordre des 4 valeurs suit le sens horaire en partant du haut :
**T**op → **R**ight → **B**ottom → **L**eft

Retiens **TRouBLe** : Top, Right, Bottom, Left !
```

**Effet du padding :**
```css
/* Sans padding */
.carte {
    background-color: #e8f5e9;
    border: 1px solid #1A7A2A;
}
/* Avec padding — le contenu "respire" */
.carte {
    background-color: #e8f5e9;
    border: 1px solid #1A7A2A;
    padding: 20px 24px;
}
```

---

## 2.3.3 Margin — l'espace extérieur

```css
/* Mêmes raccourcis que padding */
div { margin: 20px; }
div { margin: 10px auto; }       /* Centrer horizontalement ! */
div { margin: 10px 20px 15px 25px; }

/* Côtés individuels */
div { margin-top: 20px; }
div { margin-right: 0; }
div { margin-bottom: 20px; }
div { margin-left: 0; }

/* Supprimer la marge */
h1 { margin: 0; }

/* Valeur automatique (centrage) */
.conteneur {
    width: 800px;
    margin: 0 auto;   /* 0 haut/bas, auto gauche/droite = centré */
}
```

### La fusion des marges (Margin Collapse)

```css
/* Deux paragraphes consécutifs : leurs marges fusionnent */
p { margin-bottom: 20px; }
p { margin-top: 30px; }
/* → L'espace entre eux est 30px, PAS 50px ! */
/* La règle : la plus grande marge l'emporte */
```

---

## 2.3.4 Border — la bordure

```css
/* Raccourci : largeur | style | couleur */
div { border: 2px solid #1A7A2A; }
div { border: 1px dashed #E8420A; }
div { border: 3px dotted gray; }

/* Côtés individuels */
div { border-top: 3px solid #1A7A2A; }
div { border-right: none; }
div { border-bottom: 2px dashed #ccc; }
div { border-left: 4px solid #E8420A; }

/* Propriétés séparées */
div {
    border-width: 2px;
    border-style: solid;  /* solid | dashed | dotted | double | groove | none */
    border-color: #1A7A2A;
}

/* Coins arrondis */
div { border-radius: 8px; }          /* Tous les coins */
div { border-radius: 50%; }          /* Cercle parfait (si width = height) */
div { border-radius: 8px 0 8px 0; }  /* Coins alternés */
div { border-radius: 20px 4px; }     /* Haut-bas / Gauche-droite */

/* Chaque coin individuellement */
div {
    border-top-left-radius: 16px;
    border-top-right-radius: 16px;
    border-bottom-right-radius: 4px;
    border-bottom-left-radius: 4px;
}
```

---

## 2.3.5 Width et Height

```css
div {
    width: 300px;          /* Largeur fixe */
    height: 200px;         /* Hauteur fixe */

    min-width: 200px;      /* Largeur minimum */
    max-width: 800px;      /* Largeur maximum */
    min-height: 100px;     /* Hauteur minimum */
    max-height: 500px;     /* Hauteur maximum */

    width: 100%;           /* 100% du parent */
    width: 50%;            /* 50% du parent */
    height: 100vh;         /* 100% de la hauteur de l'écran */
}
```

---

## 2.3.6 `box-sizing` — Le calcul des dimensions

Par défaut, `width` ne compte que le **content**. Padding et border s'ajoutent par-dessus :

```css
/* Par défaut : box-sizing: content-box */
.boite {
    width: 200px;
    padding: 20px;
    border: 2px solid black;
}
/* Largeur totale réelle = 200 + 20 + 20 + 2 + 2 = 244px ! */
```

C'est source de confusion. La solution :

```css
/* border-box : width INCLUT padding + border */
* {
    box-sizing: border-box;  /* ← Toujours mettre cette règle en premier ! */
}

.boite {
    width: 200px;
    padding: 20px;
    border: 2px solid black;
}
/* Largeur totale = 200px exactement */
```

```{admonition} Règle absolue — Toujours utiliser box-sizing: border-box
:class: important
Place cette règle au **tout début** de tous tes fichiers CSS. C'est la pratique universelle des développeurs professionnels. Elle évite des calculs complexes et des surprises de mise en page.

```css
*, *::before, *::after {
    box-sizing: border-box;
}
```
```

---

## 2.3.7 La propriété `display`

`display` contrôle comment un élément **occupe l'espace** dans la page.

### `display: block`

- Occupe **toute la largeur** disponible
- Commence sur une **nouvelle ligne**
- `width`, `height`, `margin` fonctionnent
- Exemples natifs : `<div>`, `<p>`, `<h1>`, `<section>`, `<header>`

```css
div { display: block; }  /* déjà par défaut */
```

### `display: inline`

- Occupe **seulement la largeur** de son contenu
- Reste **sur la même ligne** que ses voisins
- `width` et `height` **ignorés**
- `margin` et `padding` horizontaux fonctionnent, verticaux partiellement
- Exemples natifs : `<span>`, `<a>`, `<strong>`, `<em>`

```css
span { display: inline; }  /* déjà par défaut */
```

### `display: inline-block`

Hybride : se comporte comme `inline` (reste en ligne) mais accepte `width`, `height`, et les marges verticales :

```css
.bouton {
    display: inline-block;
    width: 150px;
    padding: 10px 20px;
    background-color: #1A7A2A;
    color: white;
    text-align: center;
    border-radius: 4px;
}
```

### `display: none`

Masque complètement l'élément (comme s'il n'existait pas — aucun espace occupé) :

```css
.menu-mobile {
    display: none;  /* Caché sur desktop */
}
```

### Comparaison

```html
<span>A</span> <span>B</span> <span>C</span>
```

| `display` | Rendu | Width/Height |
|-----------|-------|-------------|
| `inline` | A B C côte à côte | Ignorés |
| `block` | Chacun sur sa ligne | Acceptés |
| `inline-block` | A B C côte à côte | Acceptés |
| `none` | Invisible | N/A |

---

## 2.3.8 La propriété `position`

### `position: static` (défaut)

Position normale dans le flux du document. `top`, `left`, `right`, `bottom` ignorés.

### `position: relative`

Déplacé **par rapport à sa position normale** — l'espace original est conservé :

```css
.titre {
    position: relative;
    top: 10px;    /* Descend de 10px par rapport à sa position normale */
    left: 20px;   /* Décale de 20px vers la droite */
}
```

### `position: absolute`

Se retire du flux normal. Se positionne par rapport à son **ancêtre positionné** le plus proche (qui a un `position` autre que `static`) :

```css
.parent {
    position: relative;   /* ← Référence pour l'enfant absolu */
    width: 300px;
    height: 200px;
}

.badge {
    position: absolute;
    top: 10px;            /* 10px depuis le haut du parent */
    right: 10px;          /* 10px depuis la droite du parent */
    background-color: #E8420A;
    color: white;
    padding: 4px 10px;
    border-radius: 20px;
}
```

### `position: fixed`

Se retire du flux. Reste **fixe à l'écran** même en scrollant. Se positionne par rapport à la **fenêtre du navigateur** :

```css
/* Barre de navigation fixe en haut */
nav {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 100;   /* Reste au-dessus des autres éléments */
    background-color: #1A7A2A;
}

/* Bouton "Retour en haut" fixe en bas à droite */
.btn-top {
    position: fixed;
    bottom: 30px;
    right: 30px;
}
```

### `position: sticky`

Reste dans le flux jusqu'à atteindre un seuil, puis se "colle" :

```css
/* L'en-tête du tableau colle en haut lors du scroll */
thead th {
    position: sticky;
    top: 0;
    background-color: #1A7A2A;
    z-index: 10;
}
```

### La propriété `z-index`

Contrôle l'ordre d'empilement (quel élément est "devant") :

```css
.modal   { z-index: 1000; }  /* Devant tout */
nav      { z-index: 100; }
.carte   { z-index: 10; }
.contenu { z-index: 1; }     /* Derrière */
```

```{admonition} z-index ne fonctionne que sur les éléments positionnés
:class: note
`z-index` nécessite que l'élément ait `position: relative`, `absolute`, `fixed` ou `sticky`. Sur `position: static`, il est ignoré.
```

---

## 2.3.9 Overflow — La gestion du débordement

Quand le contenu dépasse les dimensions de sa boîte :

```css
div {
    overflow: visible;  /* Défaut — le contenu déborde */
    overflow: hidden;   /* Le débordement est masqué */
    overflow: scroll;   /* Barre de défilement toujours visible */
    overflow: auto;     /* Barre de défilement seulement si nécessaire */
}

/* Axe individuel */
div {
    overflow-x: hidden;   /* Masque le débordement horizontal */
    overflow-y: scroll;   /* Scroll vertical uniquement */
}
```

---

## 2.3.10 Les ombres

```css
/* Ombre de texte */
h1 {
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    /*            x   y  flou   couleur */
}

/* Ombre de boîte */
.carte {
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    /*          x  y  flou   couleur */
}

/* Ombre interne */
input:focus {
    box-shadow: inset 0 2px 4px rgba(26,122,42,0.1);
}

/* Plusieurs ombres */
.carte-premium {
    box-shadow:
        0 2px 4px rgba(0,0,0,0.1),
        0 8px 24px rgba(0,0,0,0.08);
}
```

---

## 2.3.11 Les fonds avancés

```css
div {
    /* Couleur de fond */
    background-color: #f5f5f5;

    /* Image de fond */
    background-image: url('images/motif.png');
    background-repeat: no-repeat;   /* repeat | no-repeat | repeat-x | repeat-y */
    background-size: cover;         /* cover | contain | 300px 200px */
    background-position: center;    /* center | top | bottom | left | right */
    background-attachment: fixed;   /* fixed | scroll | local */

    /* Raccourci */
    background: #1A7A2A url('logo.png') no-repeat center / cover;

    /* Dégradé linéaire */
    background: linear-gradient(135deg, #1A7A2A 0%, #E8420A 100%);

    /* Dégradé radial */
    background: radial-gradient(circle, #1A7A2A 0%, #155f22 100%);
}
```

---

## 2.3.12 Les transitions CSS

Les transitions permettent d'animer le changement d'une propriété :

```css
.bouton {
    background-color: #1A7A2A;
    color: white;
    padding: 12px 24px;
    border-radius: 6px;
    /* Transition : propriété durée timing-function délai */
    transition: background-color 0.3s ease, transform 0.2s ease;
}

.bouton:hover {
    background-color: #E8420A;
    transform: translateY(-2px);    /* Monte légèrement */
}

.bouton:active {
    transform: translateY(0);       /* Revient en place au clic */
}
```

| Timing function | Effet |
|----------------|-------|
| `ease` | Lent → rapide → lent (défaut) |
| `linear` | Vitesse constante |
| `ease-in` | Démarre lentement |
| `ease-out` | Finit lentement |
| `ease-in-out` | Lent au début et à la fin |

---

## Résumé de la leçon

```{admonition} Ce qu'il faut retenir
:class: tip
| Propriété | Description |
|-----------|-------------|
| `padding` | Espace intérieur (entre contenu et bordure) |
| `margin` | Espace extérieur (entre l'élément et ses voisins) |
| `margin: 0 auto` | Centre un élément bloc horizontalement |
| `border` | Bordure (largeur style couleur) |
| `border-radius` | Coins arrondis |
| `box-sizing: border-box` | Width inclut padding + border (toujours utiliser) |
| `display: block` | Pleine largeur, nouvelle ligne |
| `display: inline` | Largeur du contenu, même ligne |
| `display: inline-block` | Même ligne + width/height acceptés |
| `display: none` | Masque l'élément |
| `position: relative` | Décalé par rapport à sa position normale |
| `position: absolute` | Relatif au parent positionné |
| `position: fixed` | Fixe sur l'écran |
| `position: sticky` | Colle au scroll |
| `overflow: hidden` | Masque le débordement |
| `box-shadow` | Ombre de la boîte |
| `transition` | Anime le changement de propriété |
```

---

## TP 9 — Carte de visite web

```{admonition} Exercice — À faire en TD (2 heures)
:class: warning

### Objectif
Créer une carte de visite numérique en maîtrisant le Box Model.

### Résultat attendu
Une page centrée avec une carte élégante contenant :
- Photo de profil circulaire
- Nom et titre
- Informations de contact
- Liens sociaux avec hover animé

### Consignes

**1. Mise en page de la page (3 pts)**
```css
/* La page entière */
body {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #1A7A2A, #155f22);
}
```

**2. La carte principale (4 pts)**
```css
.carte {
    width: 360px;
    background: white;
    border-radius: 16px;
    padding: 40px 32px;
    text-align: center;
    box-shadow: 0 20px 60px rgba(0,0,0,0.2);
}
```

**3. Photo de profil circulaire (3 pts)**
```css
.photo {
    width: 120px;
    height: 120px;
    border-radius: 50%;       /* Rend l'image circulaire */
    border: 4px solid #1A7A2A;
    object-fit: cover;
    margin-bottom: 16px;
}
```

**4. Informations de contact (3 pts)**
- Chaque ligne de contact : icône + texte, `padding: 8px 0`
- Séparation entre les sections avec `border-top`
- `margin` bien calculés pour l'espacement

**5. Hover sur les boutons de contact (3 pts)**
- État normal : fond transparent, bordure verte, texte vert
- Au `:hover` : fond vert, texte blanc, `transform: translateY(-2px)`
- Transition de `0.2s ease` sur toutes les propriétés

**6. Badge "MIAGE" en position absolute (2 pts)**
```css
.conteneur-carte {
    position: relative;
}
.badge-filiere {
    position: absolute;
    top: 20px;
    right: 20px;
    /* ... */
}
```

**7. `box-sizing: border-box` obligatoire (2 pts)**
Placer `*, *::before, *::after { box-sizing: border-box; }` au tout début du CSS.

### Rendu
Fichier `carte.html` + `style.css`
```

---

*Leçon suivante → [Leçon 10 — Flexbox](10-flexbox)*
