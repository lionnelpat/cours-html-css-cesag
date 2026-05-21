# 1.3 Images et Multimédia

```{admonition} Objectifs de cette leçon
:class: tip
À la fin de cette leçon, tu sauras :
- Intégrer des images avec `<img>`
- Utiliser les attributs `src`, `alt`, `width`, `height`
- Choisir le bon format d'image pour le web
- Utiliser `<figure>` et `<figcaption>`
- Intégrer des vidéos et de l'audio HTML5
- Intégrer une vidéo YouTube ou une carte Google Maps
```

---

## 1.3.1 La balise `<img>`

```html
<img src="photo.jpg" alt="Description de l'image">
```

`<img>` est une balise **auto-fermante** (pas de balise de fermeture).

### Attributs essentiels

| Attribut | Obligatoire | Description |
|----------|-------------|-------------|
| `src` | ✅ Oui | Chemin vers le fichier image |
| `alt` | ✅ Oui | Texte alternatif (accessibilité + SEO) |
| `width` | Non | Largeur en pixels |
| `height` | Non | Hauteur en pixels |
| `title` | Non | Info-bulle au survol |
| `loading` | Non | `lazy` pour le chargement différé |

### Exemples

```html
<!-- Image locale -->
<img src="images/photo-profil.jpg" alt="Photo de profil d'Amadou Diallo">

<!-- Image avec dimensions -->
<img
  src="images/logo-cesag.png"
  alt="Logo du CESAG"
  width="200"
  height="100"
>

<!-- Image depuis Internet (URL absolue) -->
<img
  src="https://www.cesag.sn/images/logo.png"
  alt="Logo CESAG"
  width="150"
>

<!-- Image avec chargement différé (performance) -->
<img
  src="images/banniere.jpg"
  alt="Bannière du CESAG"
  loading="lazy"
>
```

```{admonition} L'attribut alt est obligatoire !
:class: important
L'attribut `alt` est **obligatoire** pour :
- ♿ **L'accessibilité** : les lecteurs d'écran (pour personnes malvoyantes) lisent ce texte
- 🔍 **Le SEO** : les moteurs de recherche lisent ce texte pour comprendre l'image
- 🖼️ **Le fallback** : affiché si l'image ne se charge pas

Pour les images décoratives (sans valeur informative), utilise `alt=""` (vide).
```

---

## 1.3.2 Les formats d'images pour le Web

| Format | Extension | Usage recommandé | Transparence |
|--------|-----------|-----------------|--------------|
| **JPEG** | `.jpg`, `.jpeg` | Photos, images complexes | ❌ Non |
| **PNG** | `.png` | Logos, captures d'écran, transparence | ✅ Oui |
| **WebP** | `.webp` | Tout (format moderne, plus léger) | ✅ Oui |
| **SVG** | `.svg` | Icônes, logos, illustrations vectorielles | ✅ Oui |
| **GIF** | `.gif` | Animations simples | ✅ Partielle |
| **AVIF** | `.avif` | Format très moderne, ultra-compressé | ✅ Oui |

```{admonition} Conseils pratiques
:class: tip
- Utilise **JPEG** pour les photos (fichiers plus petits)
- Utilise **PNG** pour les logos et images avec fond transparent
- **WebP** est le meilleur compromis taille/qualité (supporté par tous les navigateurs modernes)
- Ne jamais mettre une image de 5 Mo sur un site web — **optimise** toujours tes images
```

### Outil de compression gratuit
- [Squoosh.app](https://squoosh.app) — compresse les images en ligne, très efficace

---

## 1.3.3 `<figure>` et `<figcaption>` — Images avec légende

```html
<figure>
  <img
    src="images/campus-cesag.jpg"
    alt="Vue aérienne du campus du CESAG à Dakar"
    width="600"
  >
  <figcaption>
    Le campus du CESAG, situé dans la Zone de Captage à Dakar.
    Photo prise en 2024.
  </figcaption>
</figure>
```

`<figure>` encapsule l'image (ou un schéma, un tableau...) et `<figcaption>` fournit sa légende.

---

## Résumé de la leçon

```{admonition} Ce qu'il faut retenir
:class: tip
| Élément | Usage |
|---------|-------|
| `<img src="..." alt="...">` | Insérer une image |
| `alt` | Texte alternatif — toujours obligatoire |
| `width` / `height` | Dimensions de l'image |
| `loading="lazy"` | Chargement différé (performance) |
| `<figure>` + `<figcaption>` | Image avec légende |
| JPEG | Photos |
| PNG | Logos, transparence |
| WebP | Format moderne universel |
```

---

## TP 3 — Page personnelle avec médias

```{admonition} Exercice — À faire en TD
:class: warning

### Objectif
Ajouter des images et un média à ta page personnelle.

### Consignes

**1. Photo de profil (4 pts)**
- Ajoute une photo de toi (ou une image de placeholder depuis [https://picsum.photos/200](https://picsum.photos/200))
- Utilise `<figure>` et `<figcaption>` avec une légende
- L'image doit avoir un `alt` descriptif
- Redimensionne-la à 200×200 pixels avec `width` et `height`

**2. Image dans le contenu (3 pts)**
- Ajoute au moins une image illustrative dans une de tes sections
- Utilise un format approprié
- L'image doit être dans un dossier `images/`

**3. Qualité (6 pts)**
- Toutes les images ont un attribut `alt` correct
- Les images sont dans un dossier `images/`
- Les chemins sont relatifs (pas d'URL absolues pour les images locales)

**Bonus (2 pts)**
- Utilise l'attribut `loading="lazy"` sur au moins une image
- Crée une galerie de photos avec `<figure>` et grille CSS (anticipation !)

### Astuce — Images de placeholder gratuites
- `https://picsum.photos/400/300` → image aléatoire 400×300
- `https://picsum.photos/200` → image carrée 200×200
- `https://via.placeholder.com/300x200/1A7A2A/FFFFFF?text=CESAG` → placeholder coloré
```

---

*Leçon suivante → [Leçon 5 — Listes et Tableaux](05-listes-tableaux)*
