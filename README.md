# NETHUB

<!-- BANNER — upload nethub_banner.svg to this repo as banner.svg -->
<p align="center">
  <img src="./banner.svg" width="100%" alt="NETHUB — Full Stack Web Application">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Content%20Sections-4-dc2626?style=for-the-badge&logo=fire&logoColor=white">&nbsp;
  <img src="https://img.shields.io/badge/Songs-10-be123c?style=for-the-badge">&nbsp;
  <img src="https://img.shields.io/badge/Novels-10-9f1239?style=for-the-badge">&nbsp;
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white"></a>&nbsp;
  <a href="https://flask.palletsprojects.com"><img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"></a>&nbsp;
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">
</p>

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Key Features at a Glance](#-key-features-at-a-glance)
- [Architecture](#-architecture)
- [Features](#-features)
- [Tech Stack](#️-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Pipeline Details](#-pipeline-details)
- [File Structure](#-file-structure)
- [License](#-license)

---

## 🎯 Overview

A full-stack entertainment and utility web application built with **Flask** and **Python**, serving as a multi-content hub accessible at **NETHUB.in**. The platform consolidates an in-browser music player, a romance novels library, an English movies viewer, and a user registration system — all served through Jinja2 templates and Flask routing.

Given a user visit, the application:
1. Greets the user via an **animated welcome portal** with red smoke particle effects
2. Routes them to a **multi-section content hub** (music, novels, movies)
3. Streams audio directly in-browser via the **HTML5 Audio API**
4. Serves novel PDFs and movie links from a **dynamically rendered catalogue**
5. Handles **user registration** via a Flask POST route — extensible to database writes
6. Supports **genre-based music selection** through a standalone Python `MusicSelector` class

---

## 📊 Key Features at a Glance

| Section | Technology | Highlights |
|---------|-----------|------------|
| Welcome Portal | HTML5 + CSS Animations | Red smoke particle effects, full-screen background |
| Music Player | HTML5 Audio API + JS | 10 songs, floating now-playing card, Play/Pause/Stop |
| Novels Library | HTML + PDF links | 10 romance novels, cover art, direct PDF access |
| Movies Viewer | HTML + YouTube embeds | 6 English movies, thumbnail previews |
| User Registration | Flask POST route | Name + email form, Jinja2 thank-you response |
| Music Selector | Python class | Random pick + genre filter (Pop · Rock · Jazz) |

- **Total content pages:** 9 HTML files across 3 categories
- **Backend routes:** `GET /` (welcome) · `POST /submit` (form handling)

---

## 🧠 Architecture

```
User Browser
      │
      ▼
┌───────────────────┐
│  Flask App        │  app.py — GET / and POST /submit
│  (Jinja2 routes)  │  render_template · request.form
└───────────────────┘
      │
      ├──────────────────────────────────┐
      ▼                                  ▼
┌───────────────────┐        ┌───────────────────────┐
│  index.html       │        │  2.html (Form)        │
│  Welcome Portal   │        │  POST /submit         │
│  Red smoke FX     │        │  Name + Email capture │
└───────────────────┘        └───────────────────────┘
      │
      ├──────────────┬──────────────┐
      ▼              ▼              ▼
┌──────────┐  ┌──────────┐  ┌──────────────┐
│ m1–m3    │  │ n1–n3    │  │ p1–p3        │
│ .html    │  │ .html    │  │ .html        │
│ Music    │  │ Novels   │  │ Movies       │
│ Player   │  │ Library  │  │ Viewer       │
└──────────┘  └──────────┘  └──────────────┘
      │
      ▼
┌───────────────────┐
│  p1.py            │  MusicSelector class
│  Python Backend   │  Random · Genre-based selection
└───────────────────┘
```

---

## ✨ Features

- **Animated welcome portal** — CSS keyframe red smoke particles on both sides of the viewport, full-screen background image
- **In-browser music player** — HTML5 `<audio>` API streams MP3s directly; floating music card with track name and cover art persists while browsing
- **Genre-based music selection** — Python `MusicSelector` class supports random picks and genre filtering across Pop, Rock, and Jazz
- **Romance novels library** — 10 novels with cover images, author names, and direct PDF read links
- **English movies viewer** — 6 films with poster thumbnails linked to YouTube
- **User registration form** — Flask `POST /submit` route captures name and email; returns a personalised Jinja2 response
- **Multi-page routing** — clean Flask `GET /` route serves the welcome portal; all content pages served as static templates

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| Backend | Python 3, Flask |
| Templating | Jinja2 (via `render_template`) |
| Frontend | HTML5, CSS3, JavaScript (vanilla) |
| Audio playback | HTML5 `<audio>` API |
| Routing | Flask GET / POST routes |
| Styling | CSS gradients, keyframe animations, flexbox |
| Music selection | Python `random` module · `MusicSelector` class |

---

## 🔧 Installation

```bash
git clone https://github.com/ShettyShravya03/Nethub.git
cd Nethub

pip install flask
```

**Key dependency:** `flask`

---

## 🚀 Usage

### 1. Start the Flask server

```bash
python app.py
# Server runs at http://127.0.0.1:5000
```

### 2. Open in your browser

Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) — you will land on the animated NETHUB welcome portal.

### 3. Use the Python Music Selector directly

```python
from p1 import MusicSelector

music_library = [
    {'title': 'Believer',   'artist': 'Imagine Dragons', 'genre': 'Rock'},
    {'title': 'Dandelions', 'artist': 'Ruth B.',         'genre': 'Pop'},
    {'title': 'Blue Bossa', 'artist': 'Bill Evans',      'genre': 'Jazz'},
]

selector = MusicSelector(music_library)

# Pick a random song from the full library
print(selector.select_random_music())

# Pick a random song from a specific genre
print(selector.select_by_genre('Rock'))
```

### 4. Submit the registration form

POST to `/submit` with `name` and `email` fields — returns a personalised thank-you page:

```bash
curl -X POST http://127.0.0.1:5000/submit \
  -d "name=Shravya&email=shravya@example.com"
```

**Sample response:**
```
Thank you, Shravya! Your email (shravya@example.com) has been submitted.
```

---

## 🔍 Pipeline Details

### Stage 1 — Welcome Portal (`index.html`)

The landing page uses **CSS keyframe animations** to render animated red smoke columns on both sides of the viewport. The smoke particles breathe via `scale` and `opacity` transitions, creating an atmospheric entrance before the user proceeds to the content hub.

- **Background:** Full-screen image (`1.jpg`) with `background-size: cover`
- **Effect:** Two `.red-smoke` divs with `::before` / `::after` particle pseudo-elements
- **CTA:** Link to `2.html` to proceed into the hub

### Stage 2 — Music Player (`m1.html / m2.html / m3.html`)

The music player renders a **dynamically built song list** from a JavaScript array. Each item displays cover art and title; clicking fires an `<audio>` play event.

- **Floating card:** Persists at the bottom of the viewport showing album art, title, and controls
- **Controls:** Play on click · Pause · Resume · Stop (resets `currentTime`)
- **Song catalogue:** 10 tracks including Believer, Dandelions, Dynasty, Senorita, Memories

### Stage 3 — Novels Library (`n1.html / n2.html / n3.html`)

Novels are stored as a JavaScript array of objects with `title`, `author`, `pdfLink`, and `image`. The DOM is built dynamically on `DOMContentLoaded`.

| File | Content |
|------|---------|
| `n1.html` | Pride and Prejudice, The Notebook, Jane Eyre, The Fault in Our Stars, and more |
| `n2.html` | Extended catalogue page |
| `n3.html` | Further catalogue page |

### Stage 4 — Movies, Form & Python Selector (`p1.html` / `2.html` / `app.py` / `p1.py`)

| Script | Task |
|--------|------|
| `p1.html` | English movies — Romeo and Juliet, Cinderella, Beauty and the Beast, and more |
| `2.html` | HTML form posting `name` + `email` to Flask `/submit` |
| `app.py` | Flask routes — `GET /` renders `index.html`; `POST /submit` returns thank-you string |
| `p1.py` | `MusicSelector` class — `select_random_music()` and `select_by_genre(genre)` |

---

## 📁 File Structure

```
Nethub/
├── app.py               # Flask application — routes & form handling
├── index.html           # Welcome page with animated red smoke effects
├── 2.html               # Email registration form (POST /submit)
├── m1.html              # English songs music player — page 1
├── m2.html              # English songs music player — page 2
├── m3.html              # English songs music player — page 3
├── n1.html              # Romance novels library — page 1
├── n2.html              # Romance novels library — page 2
├── n3.html              # Romance novels library — page 3
├── p1.html              # English movies viewer — page 1
├── p2.html              # English movies viewer — page 2
├── p3.html              # English movies viewer — page 3
├── p1.py                # Python MusicSelector class
├── MUSIC/               # Audio files (.mp3) and cover art (.webp / .jpg)
├── NOVELS/Romance/      # PDF novel files and cover images
├── 1.jpg / 2.jpg        # Background images
├── .gitignore
├── LICENSE
└── README.md
```

---

## 📜 License

MIT © 2026 ShettyShravya03
