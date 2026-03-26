# Rae Martin Aneron — Personal Website

A dark, fantasy-themed personal portfolio website with an integrated CMS dashboard.

## 🛠️ Tech Stack
- **Frontend**: Pure HTML/CSS/JavaScript (no framework needed!)
- **CMS**: [Decap CMS](https://decapcms.org/) (formerly Netlify CMS)
- **Auth**: Netlify Identity
- **Hosting**: Netlify (free tier)

## 📂 Project Structure
```
Personal Website/
├── index.html          # Main portfolio site
├── admin/
│   ├── index.html      # CMS dashboard entry
│   └── config.yml      # CMS content configuration
├── content/
│   ├── blog/           # Blog posts (Markdown)
│   ├── photos/         # Photo entries
│   ├── videos/         # Video entries
│   └── settings/       # Site settings (JSON)
├── uploads/            # Media uploads (managed by CMS)
├── netlify.toml        # Netlify deployment config
└── .gitignore
```

## 🚀 Deployment Steps

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit with CMS"
git remote add origin https://github.com/YOUR-USERNAME/personal-website.git
git push -u origin main
```

### 2. Deploy on Netlify
1. Go to [netlify.com](https://netlify.com) and sign in with GitHub
2. Click **"Add new site"** → **"Import an existing project"**
3. Select your GitHub repo
4. Leave build settings empty (static site, no build needed!)
5. Click **Deploy**

### 3. Enable Netlify Identity (for CMS login)
1. In your Netlify dashboard, go to **Site settings** → **Identity**
2. Click **Enable Identity**
3. Under **Registration**, set to **Invite only**
4. Go to **Identity** tab → **Invite users** → Enter your email
5. Check your email and accept the invitation

### 4. Enable Git Gateway
1. Go to **Site settings** → **Identity** → **Services**
2. Click **Enable Git Gateway**

### 5. Access the CMS
- Go to `https://your-site.netlify.app/admin/`
- Log in with your Netlify Identity credentials
- Start creating blog posts, uploading photos, and adding videos! 🎉

## 📝 Content Management
Once deployed, visit `/admin/` to:
- ✍️ Write and publish blog posts
- 📸 Upload and categorize photos
- 🎬 Add video links with thumbnails
- ⚙️ Update site settings (title, contact info, etc.)

## 🎨 Design
The site features a dark, dungeon-themed RPG aesthetic with:
- Custom cursor effects
- Torch-light animations
- Rune canvas backgrounds
- Pixel-art character selector
- Scene background switcher
