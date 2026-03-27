/**
 * SHARED SCRIPTS FOR PERSONAL WEBSITE
 */

// --- UTILS ---
function getAssetUrl(path) {
  if (!path) return '';
  if (path.startsWith('http') || path.startsWith('data:')) return path;
  return `https://raw.githubusercontent.com/Anand-Gautam/Personal-Website/main/${path.replace(/^\//, '')}`;
}

// --- CURSOR ---
const cur = document.getElementById('cur');
const curR = document.getElementById('cur-r');
if (cur && curR) {
  document.addEventListener('mousemove', (e) => {
    cur.style.left = e.clientX + 'px';
    cur.style.top = e.clientY + 'px';
    curR.style.left = e.clientX + 'px';
    curR.style.top = e.clientY + 'px';
  });
}

// --- REVEAL ON SCROLL ---
const revObs = new IntersectionObserver((entries) => {
  entries.forEach(en => {
    if (en.isIntersecting) {
      en.target.classList.add('on');
      revObs.unobserve(en.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.rev').forEach(el => revObs.observe(el));

// --- RUNE CANVAS ---
const runeCanvas = document.getElementById('rune-canvas');
if (runeCanvas) {
  const ctx = runeCanvas.getContext('2d');
  let w, h;
  const runes = "ΓÜ║ΓÜ╗ΓÜ╝ΓÜ╜ΓÜ╛ΓÜ┐ΓÜÇΓÜüΓÜéΓÜâΓÜäΓÜàΓÜåΓÜç";
  const activeRunes = [];

  function initRuneSize() {
    w = runeCanvas.width = window.innerWidth;
    h = runeCanvas.height = window.innerHeight;
  }
  window.addEventListener('resize', initRuneSize);
  initRuneSize();

  class Rune {
    constructor() {
      this.reset();
    }
    reset() {
      this.x = Math.random() * w;
      this.y = Math.random() * h;
      this.t = runes[Math.floor(Math.random() * runes.length)];
      this.s = 10 + Math.random() * 20;
      this.o = 0.1 + Math.random() * 0.3;
      this.v = 0.2 + Math.random() * 0.5;
    }
    draw() {
      ctx.globalAlpha = this.o;
      ctx.font = `${this.s}px serif`;
      ctx.fillStyle = "#d4a843";
      ctx.fillText(this.t, this.x, this.y);
      this.y -= this.v;
      if (this.y < -20) this.reset();
    }
  }

  for (let i = 0; i < 40; i++) activeRunes.push(new Rune());

  function animRunes() {
    ctx.clearRect(0, 0, w, h);
    activeRunes.forEach(r => r.draw());
    requestAnimationFrame(animRunes);
  }
  animRunes();
}

// --- PIXEL SPARKS ---
const pxCanvas = document.getElementById('px-canvas');
if (pxCanvas) {
  const pctx = pxCanvas.getContext('2d');
  let pw, ph;
  const particles = [];

  function initPxSize() {
    pw = pxCanvas.width = window.innerWidth / 2;
    ph = pxCanvas.height = window.innerHeight / 2;
  }
  window.addEventListener('resize', initPxSize);
  initPxSize();

  class Particle {
    constructor() { this.reset(); }
    reset() {
      this.x = Math.random() * pw;
      this.y = ph + 10;
      this.vx = (Math.random() - 0.5) * 0.5;
      this.vy = -(0.5 + Math.random() * 1.5);
      this.l = 50 + Math.random() * 100;
    }
    update() {
      this.x += this.vx;
      this.y += this.vy;
      this.l--;
      if (this.l <= 0) this.reset();
    }
    draw() {
      pctx.fillStyle = Math.random() > 0.5 ? '#d4a843' : '#7b4fc4';
      pctx.fillRect(Math.floor(this.x), Math.floor(this.y), 1, 1);
    }
  }

  for (let i = 0; i < 60; i++) particles.push(new Particle());

  function animPx() {
    pctx.clearRect(0, 0, pw, ph);
    particles.forEach(p => { p.update(); p.draw(); });
    requestAnimationFrame(animPx);
  }
  animPx();
}

// --- SCENE SWITCHER ---
function setScene(imgBase64, btn) {
  const bg = document.getElementById('scene-bg');
  if (!bg) return;
  bg.style.backgroundImage = `url(${imgBase64})`;
  document.querySelectorAll('.scene-btn').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');
}

// --- CMS CONTENT LOADER ---
async function fetchCMSContent(type, folder) {
  try {
    const response = await fetch(`https://api.github.com/repos/Anand-Gautam/Personal-Website/contents/content/${folder}`);
    const files = await response.json();
    
    for (const file of files) {
      if (file.name.endsWith('.md')) {
        const res = await fetch(file.download_url);
        const text = await res.text();
        const fm = text.match(/^---([\s\S]*?)---/);
        if (fm) {
          const data = jsyaml.load(fm[1]);
          data.body = text.replace(fm[0], '').trim();
          
          // Process asset URLs in data
          if (data.image) data.image = getAssetUrl(data.image);
          if (data.thumbnail) data.thumbnail = getAssetUrl(data.thumbnail);
          if (data.audio_file) data.audio_file = getAssetUrl(data.audio_file);
          
          renderItem(type, data);
        }
      }
    }
  } catch (err) {
    console.error(`Error loading ${type}:`, err);
  }
}

// MODAL (Generic)
function openModal(id) {
  const modal = document.getElementById(id);
  if (modal) modal.style.display = 'flex';
}
function closeModal(id) {
  const modal = document.getElementById(id);
  if (modal) modal.style.display = 'none';
}
