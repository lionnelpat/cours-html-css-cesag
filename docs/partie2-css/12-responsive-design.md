# 2.5 Responsive Design et Media Queries

```{admonition} Objectifs de cette leçon
:class: tip
À la fin de cette leçon, tu sauras :
- Comprendre le concept de Responsive Design
- Utiliser la balise `<meta viewport>` (obligatoire)
- Écrire des Media Queries pour adapter la mise en page
- Appliquer l'approche Mobile First
- Adapter Flexbox et Grid selon la taille d'écran
- Utiliser des images et typographies responsives
```

---

## 2.5.1 Qu'est-ce que le Responsive Design ?

Un site **responsive** (ou adaptatif) s'affiche correctement sur **tous les appareils** : smartphone, tablette, ordinateur portable, grand écran.

Plus de la moitié du trafic web mondial vient des mobiles. Un site non-responsive est donc inutilisable pour 50% des visiteurs.

```{admonition} Chiffre clé — Afrique de l'Ouest
:class: note
En Afrique de l'Ouest, **plus de 80%** des accès au web se font depuis un **téléphone mobile**. Le Responsive Design est donc absolument **critique** pour tout site destiné à ce marché.
```

---

## 2.5.2 La balise `<meta viewport>` — Obligatoire !

Sans cette balise, le navigateur mobile affiche la page comme si l'écran faisait 980px de large (zoom arrière automatique) — résultat illisible.

```html
<head>
    <meta charset="UTF-8">
    <!-- OBLIGATOIRE pour le responsive -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ma page</title>
    <link rel="stylesheet" href="style.css">
</head>
```

| Attribut | Valeur | Signification |
|----------|--------|---------------|
| `width` | `device-width` | Largeur = largeur réelle de l'écran |
| `initial-scale` | `1.0` | Pas de zoom initial |

---

## 2.5.3 Les Media Queries

Une **media query** applique des styles **conditionnellement**, selon les caractéristiques de l'écran.

### Syntaxe de base

```css
@media (condition) {
    /* Styles appliqués uniquement si la condition est vraie */
    .element {
        propriété: valeur;
    }
}
```

### Conditions les plus courantes

```css
/* Écran de 768px maximum (tablette et mobile) */
@media (max-width: 768px) { }

/* Écran d'au moins 768px (tablette et desktop) */
@media (min-width: 768px) { }

/* Entre 768px et 1200px (tablette uniquement) */
@media (min-width: 768px) and (max-width: 1200px) { }

/* Impression */
@media print { }

/* Mode sombre du système */
@media (prefers-color-scheme: dark) { }

/* Orientation paysage */
@media (orientation: landscape) { }
```

---

## 2.5.4 Les breakpoints standards

Les **breakpoints** (points de rupture) sont les largeurs auxquelles la mise en page change.

```css
/* Mobile first — on part du mobile, on monte */

/* --- Styles de base (mobile, < 576px) --- */
body { font-size: 15px; }
.colonne { width: 100%; }

/* --- Petit écran (≥ 576px) --- */
@media (min-width: 576px) {
    body { font-size: 16px; }
}

/* --- Tablette (≥ 768px) --- */
@media (min-width: 768px) {
    .grille { grid-template-columns: repeat(2, 1fr); }
}

/* --- Desktop (≥ 992px) --- */
@media (min-width: 992px) {
    .grille { grid-template-columns: repeat(3, 1fr); }
}

/* --- Grand écran (≥ 1200px) --- */
@media (min-width: 1200px) {
    .conteneur { max-width: 1140px; }
}
```

---

## 2.5.5 Mobile First vs Desktop First

### Approche Desktop First (ancienne)

On code d'abord pour le desktop, puis on **réduit** avec `max-width` :

```css
/* Desktop : 3 colonnes */
.grille { grid-template-columns: repeat(3, 1fr); }

/* On réduit pour tablette */
@media (max-width: 768px) {
    .grille { grid-template-columns: repeat(2, 1fr); }
}

/* On réduit pour mobile */
@media (max-width: 576px) {
    .grille { grid-template-columns: 1fr; }
}
```

### Approche Mobile First (recommandée ✅)

On code d'abord pour le mobile, puis on **augmente** avec `min-width` :

```css
/* MOBILE : 1 colonne (styles de base) */
.grille { grid-template-columns: 1fr; }

/* TABLETTE : 2 colonnes */
@media (min-width: 768px) {
    .grille { grid-template-columns: repeat(2, 1fr); }
}

/* DESKTOP : 3 colonnes */
@media (min-width: 992px) {
    .grille { grid-template-columns: repeat(3, 1fr); }
}
```

```{admonition} Pourquoi Mobile First ?
:class: tip
1. **Performance** : les mobiles téléchargent d'abord les styles de base (simples), puis enrichissent si l'écran est plus grand
2. **Priorité** : ça force à réfléchir d'abord à l'essentiel (mobile = contraintes maximales)
3. **Standard** : c'est la pratique recommandée par Google et l'industrie
```

---

## 2.5.6 Adapter Flexbox et Grid avec les Media Queries

### Navigation responsive

```css
/* Mobile : liens empilés */
.nav-liens {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

/* Desktop : liens côte à côte */
@media (min-width: 768px) {
    .nav-liens {
        flex-direction: row;
        gap: 8px;
    }
}
```

### Grid responsive

```css
/* Mobile : 1 colonne */
.grille {
    display: grid;
    grid-template-columns: 1fr;
    gap: 16px;
}

/* Tablette : 2 colonnes */
@media (min-width: 768px) {
    .grille {
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
    }
}

/* Desktop : 3 colonnes */
@media (min-width: 992px) {
    .grille {
        grid-template-columns: repeat(3, 1fr);
        gap: 24px;
    }
}
```

### Layout de page responsive

```css
/* Mobile : tout en colonne */
.page-layout {
    display: grid;
    grid-template-areas:
        "entete"
        "nav"
        "contenu"
        "sidebar"
        "footer";
    grid-template-columns: 1fr;
}

/* Desktop : sidebar à côté */
@media (min-width: 992px) {
    .page-layout {
        grid-template-columns: 1fr 280px;
        grid-template-areas:
            "entete  entete "
            "nav     nav    "
            "contenu sidebar"
            "footer  footer ";
    }
}
```

---

## 2.5.7 Navigation hamburger (menu mobile)

```html
<!-- HTML -->
<nav class="navbar">
    <div class="logo">CESAG</div>

    <!-- Bouton hamburger (visible seulement sur mobile) -->
    <button class="btn-menu" id="btn-menu" aria-label="Ouvrir le menu">
        <span></span>
        <span></span>
        <span></span>
    </button>

    <ul class="nav-liens" id="nav-liens">
        <li><a href="#">Accueil</a></li>
        <li><a href="#">Formations</a></li>
        <li><a href="#">Contact</a></li>
    </ul>
</nav>
```

```css
/* CSS */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
    background: #1A7A2A;
    height: 60px;
    position: relative;
}

.logo { color: white; font-weight: bold; font-size: 1.2em; }

/* Bouton hamburger */
.btn-menu {
    display: none;   /* Caché sur desktop */
    flex-direction: column;
    gap: 5px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 4px;
}

.btn-menu span {
    display: block;
    width: 24px;
    height: 3px;
    background: white;
    border-radius: 2px;
    transition: transform 0.3s, opacity 0.3s;
}

/* Navigation : liens côte à côte sur desktop */
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
    padding: 8px 14px;
    border-radius: 4px;
    transition: background 0.2s;
}

.nav-liens a:hover {
    background: rgba(255,255,255,0.15);
}

/* --------- MOBILE --------- */
@media (max-width: 768px) {

    /* Afficher le bouton hamburger */
    .btn-menu {
        display: flex;
    }

    /* Menu caché par défaut sur mobile */
    .nav-liens {
        display: none;
        position: absolute;
        top: 60px;
        left: 0;
        width: 100%;
        flex-direction: column;
        background: #155f22;
        padding: 16px 0;
        gap: 0;
        z-index: 100;
    }

    /* Menu affiché quand la classe .ouvert est ajoutée */
    .nav-liens.ouvert {
        display: flex;
    }

    .nav-liens a {
        padding: 14px 20px;
        border-radius: 0;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }
}
```

```javascript
/* JavaScript minimal pour ouvrir/fermer le menu */
const btnMenu = document.getElementById('btn-menu');
const navLiens = document.getElementById('nav-liens');

btnMenu.addEventListener('click', function() {
    navLiens.classList.toggle('ouvert');
});
```

---

## 2.5.8 Images responsives

```css
/* Image qui ne dépasse jamais son conteneur */
img {
    max-width: 100%;
    height: auto;   /* Conserve le ratio */
}

/* Image de fond responsive */
.hero {
    background-image: url('hero.jpg');
    background-size: cover;
    background-position: center;
    min-height: 60vh;
}
```

---

## 2.5.9 Typographie responsive

### Méthode 1 — Media queries

```css
body { font-size: 15px; }

@media (min-width: 768px) { body { font-size: 16px; } }
@media (min-width: 1200px) { body { font-size: 17px; } }
```

### Méthode 2 — `clamp()` (moderne)

`clamp(min, préféré, max)` ajuste automatiquement la taille :

```css
/* Titre : minimum 24px, idéal 5% de la largeur, maximum 48px */
h1 { font-size: clamp(24px, 5vw, 48px); }
p  { font-size: clamp(15px, 2.5vw, 18px); }
```

---

## 2.5.10 Tester le responsive

### Dans le navigateur
1. `F12` (DevTools) → icône 📱 (Device Toolbar) ou `Ctrl+Shift+M`
2. Sélectionner un appareil (iPhone, Galaxy, iPad...) ou entrer des dimensions manuelles
3. Tester le scroll, les clics, les formulaires

### Appareils à tester
| Appareil | Largeur |
|----------|---------|
| iPhone SE | 375px |
| iPhone 14 | 390px |
| Galaxy S22 | 360px |
| iPad | 768px |
| iPad Pro | 1024px |
| Laptop | 1366px |
| Desktop | 1920px |

---

## Résumé de la leçon

```{admonition} Ce qu'il faut retenir
:class: tip
| Élément | Description |
|---------|-------------|
| `<meta viewport>` | Obligatoire — active l'affichage responsive |
| `@media (min-width: 768px)` | Applique des styles au-delà de 768px |
| `@media (max-width: 768px)` | Applique des styles en-deçà de 768px |
| Mobile First | Coder d'abord mobile, enrichir pour les grands écrans |
| Breakpoints | 576px / 768px / 992px / 1200px |
| `img { max-width: 100%; }` | Image qui s'adapte au conteneur |
| `clamp(min, val, max)` | Taille fluide entre un min et un max |
| DevTools → Device Toolbar | Tester le rendu mobile dans le navigateur |
```

---

## TP 10 — Site complet responsive (Projet de fin de Partie 2)

```{admonition} Exercice Final CSS — À faire en TD (2 heures) + projet
:class: warning

### Objectif
Rendre le site CESAG créé au TP 11 entièrement responsive.

### Consignes

**1. Balise viewport (1 pt)**
Vérifie que `<meta name="viewport" content="width=device-width, initial-scale=1.0">` est présent dans tous les fichiers HTML.

**2. Approche Mobile First (2 pts)**
Réorganise ton CSS : les styles de base doivent être pour mobile (1 colonne, menu empilé). Les media queries ajoutent des colonnes pour les écrans plus larges.

**3. Navigation hamburger (5 pts)**
- Bouton hamburger visible sur mobile (< 768px)
- Menu masqué par défaut sur mobile, affiché avec `.ouvert`
- Liens empilés sur mobile, côte à côte sur desktop
- JavaScript minimal pour toggle la classe

**4. Grille de formations responsive (4 pts)**
- Mobile : 1 colonne
- Tablette (≥ 768px) : 2 colonnes
- Desktop (≥ 992px) : 3 colonnes

**5. Layout de page responsive (4 pts)**
- Mobile : sidebar sous le contenu (colonne unique)
- Desktop (≥ 992px) : sidebar à droite du contenu

**6. Images responsives (2 pts)**
- `img { max-width: 100%; height: auto; }`
- Image hero en `background-size: cover`

**7. Test sur 3 tailles (2 pts)**
Prendre des captures d'écran dans DevTools pour :
- 375px (mobile)
- 768px (tablette)
- 1200px (desktop)

### Rendu du projet final
À remettre en semaine 15 pour la soutenance :
- Site de 4 à 6 pages HTML/CSS
- Entièrement responsive (mobile + tablette + desktop)
- Navigation fonctionnelle entre les pages
- Utilisation de Flexbox ET Grid
- Thème libre (voir syllabus pour les suggestions)
```

---

```{admonition} 🎉 Félicitations — Fin de la Partie 2 CSS !
:class: tip
Tu maîtrises maintenant les deux langages fondamentaux du Web. Tu sais créer des pages structurées en HTML et les mettre en forme avec CSS, en les rendant responsives sur tous les appareils.

**Récapitulatif de ce que tu sais faire :**
- ✅ Créer une page HTML valide et sémantique
- ✅ Styliser avec CSS (couleurs, polices, Box Model)
- ✅ Utiliser Flexbox pour aligner des éléments
- ✅ Utiliser Grid pour des mises en page complexes
- ✅ Rendre un site responsive avec les Media Queries
- ✅ Créer des effets interactifs avec les pseudo-classes et transitions

**La prochaine étape → JavaScript** pour rendre les pages véritablement interactives ! 🚀
```
