# Leçon 5 — Listes et Tableaux

```{admonition} Objectifs de cette leçon
:class: tip
À la fin de cette leçon, tu sauras créer :
- Des listes non ordonnées `<ul>`
- Des listes ordonnées `<ol>`
- Des listes de définitions `<dl>`
- Des listes imbriquées
- Des tableaux HTML complets avec en-têtes, corps et pied
```

---

## 1. Les listes non ordonnées `<ul>`

Une liste **non ordonnée** affiche des éléments avec des puces (•).

```html
<h2>Mes matières préférées</h2>
<ul>
  <li>Mathématiques</li>
  <li>Informatique</li>
  <li>Gestion</li>
  <li>Anglais</li>
</ul>
```

**Rendu :**
- Mathématiques
- Informatique
- Gestion
- Anglais

```{admonition} Structure obligatoire
:class: note
- `<ul>` (unordered list) est le **conteneur** de la liste
- `<li>` (list item) représente **chaque élément** de la liste
- Les `<li>` doivent toujours être **à l'intérieur** d'un `<ul>` ou `<ol>`
```

---

## 2. Les listes ordonnées `<ol>`

Une liste **ordonnée** numérote automatiquement les éléments.

```html
<h2>Étapes pour créer une page web</h2>
<ol>
  <li>Créer un fichier <code>index.html</code></li>
  <li>Écrire la structure HTML5 de base</li>
  <li>Ajouter le contenu dans le <code>&lt;body&gt;</code></li>
  <li>Ouvrir le fichier dans un navigateur</li>
</ol>
```

**Rendu :**
1. Créer un fichier `index.html`
2. Écrire la structure HTML5 de base
3. Ajouter le contenu dans le `<body>`
4. Ouvrir le fichier dans un navigateur

### Attributs de `<ol>`

```html
<!-- Commencer à un autre numéro -->
<ol start="5">
  <li>Cinquième étape</li>
  <li>Sixième étape</li>
</ol>

<!-- Ordre décroissant -->
<ol reversed>
  <li>Or</li>
  <li>Argent</li>
  <li>Bronze</li>
</ol>

<!-- Type de numérotation -->
<ol type="A">   <!-- A, B, C... -->
<ol type="a">   <!-- a, b, c... -->
<ol type="I">   <!-- I, II, III... -->
<ol type="i">   <!-- i, ii, iii... -->
<ol type="1">   <!-- 1, 2, 3... (défaut) -->
```

---

## 3. Les listes imbriquées

On peut mettre une liste **à l'intérieur** d'un élément de liste :

```html
<h2>Programme MIAGE — Cours du semestre 1</h2>
<ul>
  <li>
    Informatique
    <ul>
      <li>Introduction au Développement Web (HTML & CSS)</li>
      <li>Algorithmes et Structures de données</li>
      <li>Base de données</li>
    </ul>
  </li>
  <li>
    Mathématiques
    <ul>
      <li>Algèbre linéaire</li>
      <li>Analyse mathématique</li>
    </ul>
  </li>
  <li>Gestion des entreprises</li>
  <li>Anglais des affaires</li>
</ul>
```

```{admonition} Règle d'imbrication
:class: important
La sous-liste doit être **à l'intérieur du `<li>`** parent, pas après lui.

❌ Incorrect :
```html
<ul>
  <li>Informatique</li>
  <ul>  <!-- Hors du li ! -->
    <li>HTML</li>
  </ul>
</ul>
```

✅ Correct :
```html
<ul>
  <li>Informatique
    <ul>  <!-- Dans le li -->
      <li>HTML</li>
    </ul>
  </li>
</ul>
```
```

---

## 4. Les listes de définitions `<dl>`

Utilisées pour des **glossaires** ou des paires **terme / définition** :

```html
<h2>Glossaire du Web</h2>
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language — langage de structure des pages web.</dd>

  <dt>CSS</dt>
  <dd>Cascading Style Sheets — langage de mise en forme des pages web.</dd>

  <dt>URL</dt>
  <dd>Uniform Resource Locator — adresse unique d'une ressource sur Internet.</dd>

  <dt>Navigateur</dt>
  <dd>Logiciel qui interprète le code HTML/CSS/JS et affiche les pages web.</dd>
</dl>
```

| Balise | Description |
|--------|-------------|
| `<dl>` | Definition List — conteneur |
| `<dt>` | Definition Term — le terme |
| `<dd>` | Definition Description — la définition |

---

## 5. Les tableaux HTML

Les tableaux servent à **présenter des données structurées** (horaires, notes, tarifs...).

```{admonition} Tableaux HTML ≠ Mise en page
:class: important
Les tableaux HTML sont faits pour les **données tabulaires**, pas pour la mise en page visuelle. Pour mettre en page une page web (colonnes, disposition...), on utilise CSS Flexbox ou Grid (Partie 2).
```

### Structure de base d'un tableau

```html
<table>
  <tr>
    <td>Cellule 1</td>
    <td>Cellule 2</td>
  </tr>
  <tr>
    <td>Cellule 3</td>
    <td>Cellule 4</td>
  </tr>
</table>
```

| Balise | Description |
|--------|-------------|
| `<table>` | Conteneur du tableau |
| `<tr>` | Table Row — une ligne |
| `<td>` | Table Data — une cellule de données |
| `<th>` | Table Header — une cellule d'en-tête (gras, centré) |

---

### Tableau complet avec en-tête, corps et pied

```html
<table>

  <!-- En-tête du tableau -->
  <thead>
    <tr>
      <th>Matière</th>
      <th>Enseignant</th>
      <th>Volume horaire</th>
      <th>Coefficient</th>
    </tr>
  </thead>

  <!-- Corps du tableau -->
  <tbody>
    <tr>
      <td>Introduction HTML & CSS</td>
      <td>Dr. Diallo</td>
      <td>30h</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Algorithmes</td>
      <td>Dr. Sow</td>
      <td>45h</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Gestion des entreprises</td>
      <td>Dr. Ndiaye</td>
      <td>30h</td>
      <td>3</td>
    </tr>
  </tbody>

  <!-- Pied du tableau -->
  <tfoot>
    <tr>
      <td colspan="2"><strong>Total</strong></td>
      <td><strong>105h</strong></td>
      <td><strong>10</strong></td>
    </tr>
  </tfoot>

</table>
```

### Fusionner des cellules

#### `colspan` — fusionner des colonnes

```html
<tr>
  <td colspan="2">Cette cellule occupe 2 colonnes</td>
  <td>Cellule normale</td>
</tr>
```

#### `rowspan` — fusionner des lignes

```html
<tr>
  <td rowspan="2">Cette cellule occupe 2 lignes</td>
  <td>Ligne 1</td>
</tr>
<tr>
  <!-- Pas de première cellule ici car fusionnée -->
  <td>Ligne 2</td>
</tr>
```

### Exemple complet avec fusion

```html
<table>
  <caption>Emploi du temps — Semaine type L1 MIAGE</caption>
  <thead>
    <tr>
      <th>Heure</th>
      <th>Lundi</th>
      <th>Mardi</th>
      <th>Mercredi</th>
      <th>Jeudi</th>
      <th>Vendredi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>08h00 – 10h00</td>
      <td>HTML & CSS (CM)</td>
      <td>Algorithmes</td>
      <td colspan="2">Projet Tutoré</td>
      <td>Gestion</td>
    </tr>
    <tr>
      <td>10h00 – 12h00</td>
      <td>HTML & CSS (TD)</td>
      <td rowspan="2">Mathématiques</td>
      <td>Anglais</td>
      <td>Base de données</td>
      <td>Sport</td>
    </tr>
    <tr>
      <td>14h00 – 16h00</td>
      <td>—</td>
      <!-- rowspan : pas de cellule ici -->
      <td>Conf. invité</td>
      <td>Algorithmes (TD)</td>
      <td>—</td>
    </tr>
  </tbody>
</table>
```

### La balise `<caption>`

`<caption>` ajoute un **titre au tableau** (affiché au-dessus par défaut). Elle est recommandée pour l'accessibilité.

```html
<table>
  <caption>Résultats du semestre 1 — MIAGE L1 2025-2026</caption>
  ...
</table>
```

---

## Résumé de la leçon

```{admonition} Ce qu'il faut retenir
:class: tip
| Balise | Description |
|--------|-------------|
| `<ul>` + `<li>` | Liste non ordonnée (puces) |
| `<ol>` + `<li>` | Liste ordonnée (numéros) |
| `<dl>`, `<dt>`, `<dd>` | Liste de définitions |
| `<table>` | Tableau |
| `<thead>`, `<tbody>`, `<tfoot>` | Sections du tableau |
| `<tr>` | Ligne de tableau |
| `<th>` | Cellule d'en-tête |
| `<td>` | Cellule de données |
| `colspan="n"` | Fusion de n colonnes |
| `rowspan="n"` | Fusion de n lignes |
| `<caption>` | Titre du tableau |
```

---

## TP 5 — Tableau de classe et listes

```{admonition} Exercice — À faire en TD
:class: warning

### Objectif
Créer une page avec un tableau de classe et une liste de programmes.

### Consignes

**1. Créer le fichier `classe.html`**
Ce fichier doit avoir la structure HTML5 complète et être lié à `index.html`.

**2. Tableau des étudiants (8 pts)**
Crée un tableau listant les étudiants de ta promotion avec :
- `<caption>` : "Promotion MIAGE L1 — 2025-2026"
- En-tête (`<thead>`) : Numéro, Nom, Prénom, Ville d'origine, Email
- Corps (`<tbody>`) : au moins 8 étudiants (invente si nécessaire)
- Pied (`<tfoot>`) : une ligne indiquant le nombre total d'étudiants

Utilise `colspan` pour le pied de tableau.

**3. Programme du semestre (6 pts)**
Crée une liste imbriquée des matières du semestre :
```html
<ul>
  <li>Informatique
    <ul>
      <li>...</li>
    </ul>
  </li>
  ...
</ul>
```

**4. Glossaire (3 pts)**
Crée un mini-glossaire avec `<dl>` contenant au moins 5 termes informatiques vus en cours.

**5. Navigation (3 pts)**
Ajoute des liens entre `index.html`, `classe.html` et les autres pages créées.

### Rendu
Fichiers `classe.html` mis à jour (et les autres pages liées)
```

---

*Leçon suivante → [Leçon 6 — Formulaires HTML](06-formulaires)*
