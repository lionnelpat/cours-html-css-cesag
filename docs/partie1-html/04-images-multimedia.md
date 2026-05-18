# 1.4 Images et Multimédia

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

## 1.4.1 La balise `<img>`

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

## 1.4.2 Les formats d'images pour le Web

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

## 1.4.3 `<figure>` et `<figcaption>` — Images avec légende

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

## 1.4.4 Images responsives — `srcset`

Sur un téléphone, on n'a pas besoin d'une image de 2000px de large. L'attribut `srcset` permet de fournir plusieurs versions d'une image :

```html
<img
  src="images/photo-400.jpg"
  srcset="
    images/photo-400.jpg   400w,
    images/photo-800.jpg   800w,
    images/photo-1200.jpg 1200w
  "
  sizes="(max-width: 600px) 400px, (max-width: 1200px) 800px, 1200px"
  alt="Photo du campus"
>
```

Le navigateur choisit automatiquement la bonne taille selon l'écran.

---

## 1.4.5 La vidéo HTML5 — `<video>`

HTML5 permet d'intégrer des vidéos directement sans plugin :

```html
<video width="640" height="360" controls>
  <source src="videos/presentation-cesag.mp4" type="video/mp4">
  <source src="videos/presentation-cesag.webm" type="video/webm">
  <p>Votre navigateur ne supporte pas la balise vidéo.
     <a href="videos/presentation-cesag.mp4">Télécharger la vidéo</a>
  </p>
</video>
```

### Attributs de `<video>`

| Attribut | Description |
|----------|-------------|
| `controls` | Affiche les boutons lecture/pause/volume |
| `autoplay` | Lance la vidéo automatiquement (déconseillé) |
| `muted` | Coupe le son (souvent nécessaire avec autoplay) |
| `loop` | Rejoue en boucle |
| `poster` | Image affichée avant lecture |
| `width` / `height` | Dimensions |

```html
<!-- Vidéo en autoplay silencieuse (bannière animée) -->
<video autoplay muted loop poster="images/preview.jpg" width="100%">
  <source src="videos/banniere.mp4" type="video/mp4">
</video>
```

---

## 1.4.6 L'audio HTML5 — `<audio>`

```html
<audio controls>
  <source src="audio/podcast.mp3" type="audio/mpeg">
  <source src="audio/podcast.ogg" type="audio/ogg">
  <p>Votre navigateur ne supporte pas l'audio HTML5.</p>
</audio>
```

---

## 1.4.7 Intégrer une vidéo YouTube (iframe)

La méthode la plus simple pour les vidéos YouTube :

```html
<iframe
  width="560"
  height="315"
  src="https://www.youtube.com/embed/ID_DE_LA_VIDEO"
  title="Titre de la vidéo"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope"
  allowfullscreen>
</iframe>
```

Pour trouver le code : Sur YouTube → Partager → Intégrer → Copier le code.

---

## 1.4.8 Intégrer Google Maps

```html
<iframe
  src="https://www.google.com/maps/embed?pb=!1m18...VOTRE_CLE"
  width="600"
  height="450"
  style="border:0;"
  allowfullscreen=""
  loading="lazy"
  referrerpolicy="no-referrer-when-downgrade">
</iframe>
```

Sur Google Maps : Partager → Intégrer une carte → Copier le code HTML.

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
| `<video controls>` | Vidéo native HTML5 |
| `<audio controls>` | Audio natif HTML5 |
| `<iframe>` | Contenu externe (YouTube, Maps) |
```

---

## TP 4 — Page personnelle avec médias

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

**3. Intégration externe (3 pts)**
Choisis et intègre l'un de ces éléments :
- Une vidéo YouTube en rapport avec le web ou l'informatique
- Une carte Google Maps montrant le CESAG à Dakar

**4. Qualité (4 pts)**
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
