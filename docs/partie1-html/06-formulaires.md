# 1.6 Formulaires HTML

```{admonition} Objectifs de cette leçon
:class: tip
À la fin de cette leçon, tu sauras :
- Créer un formulaire HTML complet
- Utiliser tous les types de champs (`input`, `textarea`, `select`...)
- Associer `<label>` à ses champs pour l'accessibilité
- Utiliser la validation HTML5 native
- Comprendre les attributs `method` et `action`
```

---

## 1.6.1 La balise `<form>`

Tout formulaire commence et se termine par la balise `<form>` :

```html
<form action="traitement.php" method="POST">
  <!-- Champs du formulaire ici -->
  <button type="submit">Envoyer</button>
</form>
```

### Attributs de `<form>`

| Attribut | Valeurs | Description |
|----------|---------|-------------|
| `action` | URL | Où envoyer les données (serveur) |
| `method` | `GET` / `POST` | Comment envoyer les données |
| `enctype` | `multipart/form-data` | Obligatoire pour l'envoi de fichiers |
| `novalidate` | (booléen) | Désactive la validation HTML5 |

```{admonition} GET vs POST
:class: note
- **GET** : données visibles dans l'URL (`?nom=Amadou&prenom=Diallo`). Utilisé pour les recherches.
- **POST** : données dans le corps de la requête (invisibles dans l'URL). Utilisé pour les formulaires sensibles (login, inscription...).

En cours, tu peux laisser `action="#"` — le formulaire ne sera pas traité (pas de serveur).
```

---

## 1.6.2 La balise `<input>`

`<input>` est la balise la plus polyvalente des formulaires. Son comportement change selon l'attribut `type`.

### Les types d'input essentiels

#### Texte simple
```html
<input type="text" name="prenom" placeholder="Entrez votre prénom">
```

#### Email
```html
<input type="email" name="email" placeholder="exemple@cesag.sn">
```
Vérifie automatiquement le format `xxx@xxx.xx`

#### Mot de passe
```html
<input type="password" name="mdp" placeholder="Mot de passe">
```
Masque les caractères tapés

#### Numérique
```html
<input type="number" name="age" min="18" max="99" value="20">
```

#### Téléphone
```html
<input type="tel" name="telephone" placeholder="+221 77 000 00 00">
```

#### Date
```html
<input type="date" name="date-naissance" min="1990-01-01" max="2010-12-31">
```

#### Cases à cocher `checkbox`
```html
<input type="checkbox" name="accord" id="accord" value="oui">
<label for="accord">J'accepte les conditions générales</label>

<!-- Coché par défaut -->
<input type="checkbox" name="newsletter" id="newsletter" checked>
<label for="newsletter">Recevoir la newsletter</label>
```

#### Boutons radio
```html
<fieldset>
  <legend>Votre genre</legend>

  <input type="radio" name="genre" id="homme" value="homme">
  <label for="homme">Homme</label>

  <input type="radio" name="genre" id="femme" value="femme">
  <label for="femme">Femme</label>

  <input type="radio" name="genre" id="autre" value="autre">
  <label for="autre">Autre / Je ne souhaite pas préciser</label>
</fieldset>
```

```{admonition} Important — Même `name` pour les boutons radio
:class: important
Tous les boutons radio d'un même groupe doivent avoir le **même attribut `name`**. Cela indique au navigateur qu'ils font partie du même groupe (un seul sélectionnable à la fois).
```

#### Fichier
```html
<!-- Ne jamais oublier enctype sur le form ! -->
<form enctype="multipart/form-data">
  <input type="file" name="photo" accept="image/*">
  <input type="file" name="document" accept=".pdf,.doc,.docx">
</form>
```

#### Range (curseur)
```html
<label for="satisfaction">Satisfaction : <span id="val">5</span>/10</label>
<input type="range" id="satisfaction" name="satisfaction"
       min="0" max="10" value="5"
       oninput="document.getElementById('val').textContent = this.value">
```

#### Couleur
```html
<label for="couleur">Couleur préférée :</label>
<input type="color" id="couleur" name="couleur" value="#1A7A2A">
```

#### Champ caché (hidden)
```html
<!-- Valeur envoyée mais non visible -->
<input type="hidden" name="source" value="formulaire-accueil">
```

---

## 1.6.3 La balise `<label>`

Le `<label>` est **obligatoire** pour l'accessibilité. Il associe un texte descriptif à un champ.

### Méthode 1 — Attribut `for` (recommandée)

```html
<!-- Le "for" doit correspondre exactement à l'id de l'input -->
<label for="prenom">Prénom :</label>
<input type="text" id="prenom" name="prenom">
```

### Méthode 2 — Imbrication

```html
<label>
  Prénom :
  <input type="text" name="prenom">
</label>
```

```{admonition} Pourquoi label est important ?
:class: tip
1. **Accessibilité** : les lecteurs d'écran lisent le label pour décrire le champ
2. **Ergonomie** : cliquer sur le label active le champ (zone cliquable agrandie)
3. **Obligation** : un formulaire sans labels est mal codé
```

---

## 1.6.4 La zone de texte `<textarea>`

Pour les messages longs (multi-lignes) :

```html
<label for="message">Votre message :</label>
<textarea
  id="message"
  name="message"
  rows="5"
  cols="40"
  placeholder="Écrivez votre message ici..."
  maxlength="500">
</textarea>
```

| Attribut | Description |
|----------|-------------|
| `rows` | Nombre de lignes visibles |
| `cols` | Nombre de colonnes visibles |
| `maxlength` | Nombre max de caractères |
| `placeholder` | Texte d'exemple |

---

## 1.6.5 La liste déroulante `<select>`

```html
<label for="filiere">Filière :</label>
<select id="filiere" name="filiere">
  <option value="">-- Choisissez votre filière --</option>
  <option value="miage">MIAGE</option>
  <option value="master-fi">Master Finance</option>
  <option value="master-rh">Master RH</option>
  <option value="mba">MBA</option>
</select>
```

```html
<!-- Sélection multiple avec Ctrl+Clic -->
<select name="matieres" multiple size="4">
  <option value="html">HTML & CSS</option>
  <option value="algo">Algorithmes</option>
  <option value="bdd">Base de données</option>
  <option value="gestion">Gestion</option>
</select>
```

### Grouper les options avec `<optgroup>`

```html
<select name="programme">
  <optgroup label="Licences">
    <option value="l1-miage">L1 MIAGE</option>
    <option value="l2-miage">L2 MIAGE</option>
    <option value="l3-miage">L3 MIAGE</option>
  </optgroup>
  <optgroup label="Masters">
    <option value="m1-finance">M1 Finance</option>
    <option value="m2-rh">M2 Ressources Humaines</option>
  </optgroup>
</select>
```

---

## 1.6.6 `<fieldset>` et `<legend>` — Grouper les champs

```html
<form action="#" method="POST">

  <fieldset>
    <legend>Informations personnelles</legend>
    <label for="nom">Nom :</label>
    <input type="text" id="nom" name="nom" required>

    <label for="prenom">Prénom :</label>
    <input type="text" id="prenom" name="prenom" required>

    <label for="email">Email :</label>
    <input type="email" id="email" name="email" required>
  </fieldset>

  <fieldset>
    <legend>Informations académiques</legend>
    <label for="filiere">Filière :</label>
    <select id="filiere" name="filiere">
      <option value="miage">MIAGE</option>
    </select>

    <label for="annee">Année :</label>
    <select id="annee" name="annee">
      <option value="l1">Licence 1</option>
      <option value="l2">Licence 2</option>
      <option value="l3">Licence 3</option>
    </select>
  </fieldset>

</form>
```

---

## 1.6.7 La validation HTML5

HTML5 permet de valider les champs **sans JavaScript** :

```html
<form action="#" method="POST">

  <!-- Champ obligatoire -->
  <input type="text" name="nom" required>

  <!-- Longueur min/max -->
  <input type="text" name="pseudo" minlength="3" maxlength="20">

  <!-- Pattern (expression régulière) -->
  <input
    type="text"
    name="code-etudiant"
    pattern="[A-Z]{2}[0-9]{4}"
    title="Format : 2 lettres majuscules + 4 chiffres (ex: CS2025)"
  >

  <!-- Nombre entre 0 et 20 -->
  <input type="number" name="note" min="0" max="20" step="0.5">

  <button type="submit">Valider</button>

</form>
```

### Attributs de validation

| Attribut | Description | Exemple |
|----------|-------------|---------|
| `required` | Champ obligatoire | `<input required>` |
| `minlength` | Longueur minimum | `minlength="3"` |
| `maxlength` | Longueur maximum | `maxlength="50"` |
| `min` | Valeur minimum (number/date) | `min="0"` |
| `max` | Valeur maximum (number/date) | `max="20"` |
| `pattern` | Expression régulière | `pattern="[0-9]{4}"` |
| `step` | Pas d'incrément | `step="0.5"` |

---

## 1.6.8 Formulaire complet — Exemple récapitulatif

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Inscription CESAG</title>
</head>
<body>

  <h1>Formulaire d'inscription — CESAG</h1>

  <form action="#" method="POST" enctype="multipart/form-data">

    <fieldset>
      <legend>État civil</legend>

      <label for="nom">Nom * :</label>
      <input type="text" id="nom" name="nom" required maxlength="50"
             placeholder="DIALLO">

      <label for="prenom">Prénom * :</label>
      <input type="text" id="prenom" name="prenom" required maxlength="50"
             placeholder="Amadou">

      <fieldset>
        <legend>Genre</legend>
        <input type="radio" name="genre" id="m" value="M">
        <label for="m">Masculin</label>
        <input type="radio" name="genre" id="f" value="F">
        <label for="f">Féminin</label>
      </fieldset>

      <label for="ddn">Date de naissance * :</label>
      <input type="date" id="ddn" name="date-naissance" required
             min="1990-01-01" max="2010-12-31">

      <label for="nationalite">Nationalité :</label>
      <select id="nationalite" name="nationalite">
        <option value="">-- Choisir --</option>
        <option value="SN" selected>Sénégalaise</option>
        <option value="ML">Malienne</option>
        <option value="CI">Ivoirienne</option>
        <option value="autre">Autre</option>
      </select>
    </fieldset>

    <fieldset>
      <legend>Coordonnées</legend>

      <label for="email">Email * :</label>
      <input type="email" id="email" name="email" required
             placeholder="amadou.diallo@cesag.sn">

      <label for="tel">Téléphone :</label>
      <input type="tel" id="tel" name="telephone"
             placeholder="+221 77 000 00 00">
    </fieldset>

    <fieldset>
      <legend>Inscription</legend>

      <label for="programme">Programme * :</label>
      <select id="programme" name="programme" required>
        <option value="">-- Choisir un programme --</option>
        <optgroup label="Licences">
          <option value="l1-miage">L1 MIAGE</option>
          <option value="l2-miage">L2 MIAGE</option>
        </optgroup>
        <optgroup label="Masters">
          <option value="m1-finance">M1 Finance</option>
          <option value="m2-rh">M2 Ressources Humaines</option>
        </optgroup>
      </select>

      <label for="photo">Photo d'identité :</label>
      <input type="file" id="photo" name="photo" accept="image/jpeg,image/png">

      <label for="motivation">Lettre de motivation :</label>
      <textarea id="motivation" name="motivation"
                rows="6" maxlength="1000"
                placeholder="Expliquez votre motivation en 3-5 phrases...">
      </textarea>

      <input type="checkbox" id="cgu" name="cgu" value="oui" required>
      <label for="cgu">J'accepte les conditions générales d'utilisation *</label>

      <input type="checkbox" id="newsletter" name="newsletter" value="oui">
      <label for="newsletter">Recevoir les actualités du CESAG par email</label>
    </fieldset>

    <p><small>* Champs obligatoires</small></p>

    <button type="reset">Réinitialiser</button>
    <button type="submit">Soumettre ma candidature</button>

  </form>

</body>
</html>
```

---

## Résumé de la leçon

```{admonition} Ce qu'il faut retenir
:class: tip
| Élément | Usage |
|---------|-------|
| `<form action method>` | Conteneur du formulaire |
| `<input type="text">` | Champ texte |
| `<input type="email">` | Email (validé) |
| `<input type="password">` | Mot de passe |
| `<input type="number">` | Numérique |
| `<input type="checkbox">` | Case à cocher |
| `<input type="radio">` | Bouton radio (groupe = même `name`) |
| `<input type="file">` | Envoi de fichier |
| `<input type="date">` | Sélecteur de date |
| `<textarea>` | Zone de texte multi-lignes |
| `<select>` + `<option>` | Liste déroulante |
| `<label for="id">` | Étiquette liée au champ |
| `<fieldset>` + `<legend>` | Groupe de champs |
| `required` | Champ obligatoire |
| `<button type="submit">` | Bouton d'envoi |
| `<button type="reset">` | Bouton de réinitialisation |
```

---

## TP 6 — Formulaire d'inscription CESAG

```{admonition} Exercice Final HTML — À faire en TD (2 heures)
:class: warning

### Objectif
Créer un formulaire d'inscription complet pour le CESAG.

### Consignes

Crée un fichier `inscription.html` contenant un formulaire avec :

**1. Informations personnelles (5 pts)**
- Nom (texte, obligatoire)
- Prénom (texte, obligatoire)
- Sexe (boutons radio : Masculin / Féminin)
- Date de naissance (type date)
- Nationalité (liste déroulante avec au moins 5 pays)

**2. Coordonnées (3 pts)**
- Adresse email (type email, obligatoire)
- Numéro de téléphone (type tel)
- Adresse (textarea, 3 lignes)

**3. Inscription académique (4 pts)**
- Programme souhaité (select avec optgroups : Licences / Masters)
- Niveau d'entrée (radio : L1 / L2 / L3 / M1 / M2)
- Matières d'intérêt (checkboxes : HTML, Algo, Gestion, Finance, RH — au moins 3)

**4. Documents (3 pts)**
- Photo d'identité (type file, accepter images)
- Lettre de motivation (textarea, 6 lignes, max 1500 caractères)

**5. Qualité et validation (5 pts)**
- Tous les champs ont un `<label>` associé (`for` + `id`)
- Les champs obligatoires ont `required`
- Les champs sont groupés avec `<fieldset>` + `<legend>`
- Bouton Soumettre et bouton Réinitialiser
- Code indenté et commenté

### Fichiers à rendre
Fichier `inscription.html` + lien depuis `index.html`
```

---

```{admonition} 🎉 Félicitations — Fin de la Partie 1 HTML !
:class: tip
Tu as maintenant les bases solides du HTML. Tu sais créer des pages structurées, avec du texte mis en forme, des images, des liens, des tableaux et des formulaires.

**La suite → Partie 2 : CSS — Donner vie à tes pages** 🎨
```
