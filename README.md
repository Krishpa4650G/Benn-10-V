# ⚡ Ben 10 Video Transmission Portal (ASP.NET Core MVC)

A dedicated, high-tech video streaming & download portal for the Ben 10 Multiverse, matching the exact dark sci-fi aesthetic, neon green glow, and Omnitrix branding of your main website ([https://benn-10.onrender.com/](https://benn-10.onrender.com/)).

---

## 🌟 Key Features

1. **Exact Visual Theme Matching**:
   - Galvan dark space background with dot grid matrix pattern.
   - Neon green glow accents (`#00ff41`), sleek glassmorphism cards, and Space Grotesk/Outfit typography.
   - Authentic interactive Omnitrix cursor with rotating ring, glowing core, and canvas particle spark trail.
   - Omnitrix Navigation bar with brand emblem, sub-space beacon, and links back to the main site.

2. **Multi-Level Selection Flow**:
   - **Step 1: Select Universe**: Ben 10 Classic, Alien Force, Ultimate Alien, Omniverse, and Reboot.
   - **Step 2: Select Season**: Interactive season pill selector showing episode counts and air years.
   - **Step 3: Select Episode**: Grid of episode cards with episode numbers (e.g. S01E01), titles, descriptions, runtimes, and featured alien tags.
   - **Step 4: Transfer to TeraBox**: Stream/download button linking directly to your custom TeraBox links, plus an animated Galvan Sub-Space Gateway countdown screen.

3. **Instant Search & Filter**:
   - Real-time client-side episode search filtering by episode title, number, or featured alien (e.g. "Heatblast", "Malware", "Alien X").

4. **Easy TeraBox Link Management**:
   - **Option A (In-Browser Admin)**: Navigate to `/Watch/Admin` to view all episodes across all universes in one table and paste/save your TeraBox links with 1 click.
   - **Option B (Episode Modal)**: Click the eye or gear icon on any episode card to paste a new TeraBox link on the fly.
   - **Option C (JSON File)**: Open `Data/episodes.json` and replace any `TeraBoxUrl` value with your actual links!

---

## 🚀 How to Run Locally

From this directory (`c:\Users\patel\OneDrive\Desktop\Benn 10 Vidoes`):

```powershell
# Restore & build
dotnet build

# Run the app
dotnet run
```

Then open your browser to the URL shown (e.g., `http://localhost:5055` or `http://localhost:5000`).

---

## 🔗 How to Add the Button to Your Main Website (`https://benn-10.onrender.com/`)

Whenever you are ready to link your main site to this video website, you can add this button:

### 1. Navigation Link (Add inside `<div class="nav-links">` on your main site):
```html
<a class="nav-link" href="https://your-video-site.onrender.com" target="_blank" style="color: #00ff41; font-weight: 600;">
    🎬 Watch Episodes
</a>
```

### 2. Standalone Glowing Omnitrix Button (Add anywhere on your landing page):
```html
<!-- Glowing Ben 10 Watch Button -->
<a href="https://your-video-site.onrender.com" target="_blank" class="omni-watch-btn">
    <span class="omni-btn-glow"></span>
    <span class="omni-btn-icon">⚡</span>
    <span class="omni-btn-text">
        <strong>WATCH EPISODES</strong>
        <small>Select Universe &bull; Season &bull; TeraBox Stream</small>
    </span>
    <span class="omni-btn-arrow">→</span>
</a>

<style>
.omni-watch-btn {
    display: inline-flex;
    align-items: center;
    gap: 1rem;
    background: linear-gradient(135deg, rgba(0, 255, 65, 0.15) 0%, rgba(0, 0, 0, 0.8) 100%);
    border: 1.5px solid #00ff41;
    border-radius: 50px;
    padding: 0.85rem 1.8rem;
    color: #ffffff;
    text-decoration: none;
    font-family: 'Space Grotesk', sans-serif;
    box-shadow: 0 0 25px rgba(0, 255, 65, 0.35);
    transition: all 0.35s ease;
    margin: 1.5rem 0;
}
.omni-watch-btn:hover {
    background: #00ff41;
    color: #000000;
    box-shadow: 0 0 40px rgba(0, 255, 65, 0.7);
    transform: translateY(-3px) scale(1.03);
}
.omni-watch-btn:hover .omni-btn-text small {
    color: #1a1a1a;
}
.omni-btn-icon {
    font-size: 1.3rem;
}
.omni-btn-text {
    display: flex;
    flex-direction: column;
    text-align: left;
}
.omni-btn-text strong {
    font-size: 1rem;
    letter-spacing: 1px;
}
.omni-btn-text small {
    font-size: 0.72rem;
    color: #00ff41;
    font-family: 'Outfit', sans-serif;
}
.omni-btn-arrow {
    font-size: 1.2rem;
    transition: transform 0.3s ease;
}
.omni-watch-btn:hover .omni-btn-arrow {
    transform: translateX(4px);
}
</style>
```

---

## ☁️ Deploying to Render (Same as your main website)

Since your current website runs on Render, deploying this app to Render is simple:
1. Create a GitHub repository and push this folder.
2. Go to [Render Dashboard](https://dashboard.render.com/) -> **New Web Service**.
3. Select your repository.
4. Set:
   - **Environment**: `.NET` / `Docker`
   - **Build Command**: `dotnet publish -c Release -o out`
   - **Start Command**: `dotnet out/Ben10Videos.dll`
5. Click **Deploy Web Service**!
