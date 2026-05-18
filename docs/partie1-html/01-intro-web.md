# Leçon 1 — Introduction au Web

```{admonition} Objectifs de cette leçon
:class: tip
À la fin de cette leçon, tu sauras expliquer :
- Ce qu'est Internet et comment il fonctionne
- Ce qu'est le Web et comment les pages sont affichées
- Le rôle de HTML, CSS et JavaScript
- Ce qu'est un navigateur et un serveur
```

---

## 1. Qu'est-ce qu'Internet ?

Internet est un **réseau mondial d'ordinateurs** interconnectés. Imagine une immense toile d'araignée reliant des milliards d'appareils : ordinateurs, téléphones, tablettes, serveurs...

Ces machines communiquent entre elles grâce à des **protocoles** — c'est-à-dire des règles communes que tous les appareils respectent pour se comprendre.

```{admonition} Analogie
:class: note
Internet, c'est comme le réseau téléphonique mondial — une infrastructure de communication. Le Web, lui, est un *service* qui utilise cette infrastructure, comme les appels téléphoniques utilisent le réseau.
```

---

## 2. Qu'est-ce que le Web ?

Le **Web** (World Wide Web, ou simplement "le web") est un système de **pages et de documents reliés entre eux par des liens hypertextes**, accessibles via Internet.

Le Web a été inventé en **1989** par **Tim Berners-Lee**, un ingénieur britannique travaillant au CERN (Suisse).

### Les composants du Web

| Composant | Rôle | Exemple |
|-----------|------|---------|
| **URL** | Adresse d'une page web | `https://www.cesag.sn` |
| **HTTP/HTTPS** | Protocole de communication | Le "langage" entre client et serveur |
| **HTML** | Langage de structure des pages | Le contenu |
| **CSS** | Langage de mise en forme | L'apparence |
| **JavaScript** | Langage de comportement | L'interactivité |

---

## 3. Comment fonctionne une page web ?

Voici ce qui se passe quand tu tapes une adresse web dans ton navigateur :

### Étape 1 — Tu tapes une URL
```
https://www.cesag.sn/formations
```

### Étape 2 — La résolution DNS
Ton ordinateur demande à un **serveur DNS** (comme un annuaire) : *"Quelle est l'adresse IP de www.cesag.sn ?"*

Le DNS répond : *"C'est l'adresse 192.168.1.45"* (par exemple).

### Étape 3 — La requête HTTP
Ton navigateur envoie une **requête** au serveur :
```
GET /formations HTTP/1.1
Host: www.cesag.sn
```
Ce message signifie : *"Donne-moi la page /formations"*

### Étape 4 — La réponse du serveur
Le serveur renvoie le **code HTML** de la page :
```html
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
  <head><title>CESAG — Formations</title></head>
  <body>
    <h1>Nos formations</h1>
    ...
  </body>
</html>
```

### Étape 5 — Le navigateur affiche la page
Le navigateur **lit** le code HTML, **télécharge** les fichiers CSS et images associés, et **affiche** la page à l'écran.

```{admonition} À retenir — Le modèle Client / Serveur
:class: tip
- Le **client**, c'est ton navigateur (Chrome, Firefox, Safari...)
- Le **serveur**, c'est l'ordinateur distant qui stocke les fichiers du site
- Ils communiquent via le protocole **HTTP** (ou **HTTPS** pour la version sécurisée)
```

---

## 4. Le rôle de HTML, CSS et JavaScript

Ces trois langages forment le **trio du développement web front-end** :

### HTML — La structure
HTML définit *ce qu'est* le contenu : un titre, un paragraphe, une image, un lien...

```html
<h1>Bienvenue au CESAG</h1>
<p>Le Centre Africain d'Études Supérieures en Gestion.</p>
```

**Analogie** : HTML, c'est comme les **murs et les pièces** d'une maison.

### CSS — L'apparence
CSS définit *comment* le contenu est affiché : couleurs, polices, tailles, mise en page...

```css
h1 {
  color: #1A7A2A;
  font-size: 36px;
}
```

**Analogie** : CSS, c'est comme la **peinture, le mobilier et la décoration** de la maison.

### JavaScript — Le comportement
JavaScript rend les pages **interactives** : menus qui s'ouvrent, formulaires qui se valident, animations...

```javascript
document.querySelector("h1").addEventListener("click", function() {
  alert("Bonjour !");
});
```

**Analogie** : JavaScript, c'est comme **l'électricité et la domotique** de la maison.

```{admonition} Dans ce cours
:class: note
Nous allons apprendre **HTML** (Partie 1) et **CSS** (Partie 2). JavaScript sera abordé dans un cours ultérieur.
```

---

## 5. Les navigateurs web

Un **navigateur** est un logiciel qui lit le code HTML/CSS/JS et affiche les pages web.

### Les principaux navigateurs

| Navigateur | Éditeur | Part de marché |
|------------|---------|---------------|
| Google Chrome | Google | ~65% |
| Safari | Apple | ~19% |
| Firefox | Mozilla | ~4% |
| Edge | Microsoft | ~4% |
| Opera | Opera | ~3% |

```{admonition} Bonne pratique
:class: tip
Pour le développement web, utilise **Google Chrome** ou **Firefox**. Ils possèdent d'excellents **outils de développement** (accessible avec la touche `F12`) qui te permettront d'inspecter et déboguer ton code.
```

---

## 6. Un éditeur de code — VS Code

Pour écrire du HTML et du CSS, tu as besoin d'un **éditeur de code**. Nous utiliserons **Visual Studio Code** (VS Code), développé par Microsoft.

### Pourquoi VS Code ?
- ✅ Gratuit et open source
- ✅ Coloration syntaxique (le code s'affiche en couleurs selon sa nature)
- ✅ Auto-complétion (VS Code suggère la suite de ce que tu tapes)
- ✅ Extension **Live Server** (la page se met à jour automatiquement à chaque sauvegarde)

### Téléchargement
👉 [code.visualstudio.com](https://code.visualstudio.com)

### Extensions recommandées
Une fois VS Code installé, installe ces extensions (icône puzzle à gauche) :

1. **Live Server** — recharge automatiquement la page dans le navigateur
2. **Prettier** — formate automatiquement ton code
3. **Auto Rename Tag** — renomme automatiquement les balises paires

---

## 7. Les outils de développement du navigateur

Appuie sur `F12` (ou `Ctrl+Shift+I`) dans Chrome pour ouvrir les **DevTools** :

- **Elements** : affiche le HTML de la page et te permet de l'inspecter
- **Console** : affiche les erreurs et messages JavaScript
- **Network** : montre toutes les requêtes HTTP de la page

---

## Résumé de la leçon

```{admonition} Ce qu'il faut retenir
:class: tip
| Concept | Définition |
|---------|-----------|
| **Internet** | Réseau mondial d'ordinateurs |
| **Web** | Service de pages reliées par des liens, accessible via Internet |
| **Navigateur** | Logiciel qui affiche les pages web |
| **Serveur** | Ordinateur qui stocke et envoie les fichiers web |
| **HTTP/HTTPS** | Protocole de communication entre navigateur et serveur |
| **HTML** | Langage de structure des pages web |
| **CSS** | Langage de mise en forme des pages web |
| **JavaScript** | Langage de comportement (interactivité) |
```

---

## TP 1 — Exploration du Web

```{admonition} Exercice — À faire en classe
:class: warning

**Durée : 30 minutes**

### Partie A — Analyser une page web (10 min)
1. Ouvre Google Chrome et va sur **https://www.cesag.sn**
2. Appuie sur `F12` pour ouvrir les outils développeurs
3. Dans l'onglet **Network**, recharge la page (`F5`)
4. Réponds aux questions :
   - Combien de fichiers sont téléchargés pour afficher cette page ?
   - Quel est le premier fichier chargé ? Quel est son type ?
   - Trouve un fichier `.css` — à quoi sert-il ?

### Partie B — Inspecter le HTML (10 min)
1. Dans l'onglet **Elements** des DevTools, clique sur le triangle ▶ pour déplier le code HTML
2. Identifie et note :
   - La balise qui contient le titre de la page
   - Une balise `<p>` (paragraphe) et son contenu
   - Une balise `<img>` (image)

### Partie C — Modifier temporairement une page (10 min)
1. Dans l'onglet **Elements**, double-clique sur un texte quelconque
2. Modifie le texte et appuie sur Entrée
3. Observe : la page change, mais c'est **temporaire** — un rechargement (`F5`) annule tout

**Question de réflexion** : Pourquoi peut-on modifier l'affichage d'une page sans changer le vrai fichier sur le serveur ?
```

---

*Leçon suivante → [Leçon 2 — Structure d'un document HTML](02-structure-html)*
