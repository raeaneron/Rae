with open(r'd:\web apps\Personal Website\index.html', 'r', encoding='utf-8') as f:
    current = f.read()

# --- 1. Inject Music section before Skills ---
music_section = (
    '\n<div class="div"></div>\n\n'
    '<!-- MUSIC PORTFOLIO -->\n'
    '<section id="music">\n'
    '  <div class="s-eye">Melodic Spells</div>\n'
    '  <h2>Bardic <em>Inspirations</em></h2>\n'
    '  <div class="music-grid rev" id="musicGrid" '
    'style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">\n'
    '    <!-- Populated by CMS -->\n'
    '  </div>\n'
    '</section>\n'
)

skills_marker = '<div class="div"></div>\n\n<!-- SKILLS'
if '<!-- MUSIC PORTFOLIO -->' not in current and skills_marker in current:
    current = current.replace(skills_marker, music_section + skills_marker, 1)
    print('Music section injected')
else:
    print('Music already present or marker not found')

# --- 2. Inject CMS loader script before Netlify identity script ---
cms_script = r"""
<!-- UNIVERSAL CMS CONTENT LOADER -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/js-yaml/4.1.0/js-yaml.min.js"></script>
<script>
  const GITHUB_USER = 'raeaneron';
  const GITHUB_REPO = 'Rae';
  const BRANCH = 'main';

  async function fetchCMSContent(folder, type) {
    const url = `https://api.github.com/repos/${GITHUB_USER}/${GITHUB_REPO}/contents/content/${folder}?ref=${BRANCH}`;
    try {
      const resp = await fetch(url);
      if (!resp.ok) return;
      const files = await resp.json();
      for (const file of files) {
        if (file.name.endsWith('.md') || file.name.endsWith('.json')) {
          const fileResp = await fetch(file.download_url);
          const rawText = await fileResp.text();
          let data = {};
          if (file.name.endsWith('.md')) {
            const fmMatch = rawText.match(/^---([\s\S]*?)---/);
            if (fmMatch) {
              data = jsyaml.load(fmMatch[1]);
              data.content = rawText.replace(fmMatch[0], '').trim();
            }
          } else {
            data = JSON.parse(rawText);
          }
          renderItem(data, type);
        }
      }
    } catch (e) { console.error("CMS Loader Error:", e); }
  }

  function renderItem(data, type) {
    if (type === 'blog') {
      const container = document.getElementById('quest-log-container');
      const item = document.createElement('div');
      item.className = 'tl-item';
      item.innerHTML = `
        <div class="tl-dot"></div>
        <div class="tl-date">${new Date(data.date).toLocaleDateString('en-US', {month:'short', year:'numeric'})}</div>
        <div class="tl-role">${data.title}</div>
        <div class="tl-co">${data.description || ''}</div>
        <p style="font-size:0.85rem; color:var(--dim); margin-top:0.5rem;">${data.content ? data.content.substring(0, 150) + '...' : ''}</p>
      `;
      container.prepend(item);
    }
    else if (type === 'music') {
      const container = document.getElementById('musicGrid');
      const item = document.createElement('div');
      item.className = 'sk-card';
      item.style.padding = '0';
      item.style.overflow = 'hidden';
      item.innerHTML = `
        <div style="height:140px; background:url(${data.cover || '#111'}); background-size:cover;"></div>
        <div style="padding:1rem;">
          <div class="sk-title">${data.title}</div>
          <p style="font-size:0.6rem; color:var(--amber); margin-bottom:0.5rem;">BY ${data.artist || 'Rae'}</p>
          <audio controls style="width:100%; height:30px; filter: invert(1);">
            <source src="${data.audio_file}" type="audio/mpeg">
          </audio>
        </div>
      `;
      container.appendChild(item);
    }
    else if (type === 'games') {
      const container = document.getElementById('worksGrid');
      const item = document.createElement('div');
      item.className = 'work-card';
      item.onclick = () => window.open(data.url, '_blank');
      item.innerHTML = `
        <div class="work-thumb">
          <img src="${data.thumbnail}" alt="${data.title}">
          <div class="work-overlay"><div class="work-ot">PLAY PROJECT</div></div>
        </div>
        <div class="work-info">
          <div class="work-cat">${data.type}</div>
          <div class="work-title">${data.title}</div>
        </div>
      `;
      container.prepend(item);
    }
  }

  document.addEventListener('DOMContentLoaded', () => {
    fetchCMSContent('blog', 'blog');
    fetchCMSContent('music', 'music');
    fetchCMSContent('games', 'games');
  });
</script>
"""

netlify_marker = '<script>\n  if (window.netlifyIdentity)'
if 'fetchCMSContent' not in current:
    if netlify_marker in current:
        current = current.replace(netlify_marker, cms_script + '\n' + netlify_marker, 1)
        print('CMS script injected before Netlify identity block')
    else:
        current = current.replace('</body>', cms_script + '\n</body>', 1)
        print('CMS script injected before </body>')
else:
    print('CMS script already present')

with open(r'd:\web apps\Personal Website\index.html', 'w', encoding='utf-8') as f:
    f.write(current)

print('Done. Lines:', current.count('\n'))
