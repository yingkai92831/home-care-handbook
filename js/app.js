/* ===== State ===== */
let rulings = [];
let scenarios = [];
let favorites = JSON.parse(localStorage.getItem('ltc_favorites') || '[]');
let activeFilters = { source: null, category: null };
let sortOrder = 'newest';
let searchQuery = '';

/* ===== Init ===== */
document.addEventListener('DOMContentLoaded', async () => {
  await loadData();
  renderRulings();
  renderScenarios();
  bindEvents();
  updateFavCount();
});

/* ===== Load JSON ===== */
async function loadData() {
  try {
    const [rulingsRes, scenariosRes] = await Promise.all([
      fetch('data/rulings.json'),
      fetch('data/scenarios.json')
    ]);
    rulings = await rulingsRes.json();
    scenarios = await scenariosRes.json();
  } catch (e) {
    console.error('Failed to load data:', e);
  }
}

/* ===== Card Accordion ===== */
function bindEvents() {
  // Manual card toggles
  document.querySelectorAll('.card-header').forEach(h => {
    h.addEventListener('click', () => {
      h.closest('.card').classList.toggle('open');
    });
  });

  // Sub-tab toggles
  document.querySelectorAll('.sub-tabs').forEach(tabs => {
    tabs.querySelectorAll('.sub-tab').forEach(btn => {
      btn.addEventListener('click', () => {
        const parent = btn.closest('.card-body');
        const target = btn.dataset.target;
        // Toggle: if already active, deactivate
        if (btn.classList.contains('active')) {
          btn.classList.remove('active');
          parent.querySelector(`.sub-content.${target}`).classList.remove('active');
          return;
        }
        // Deactivate siblings
        tabs.querySelectorAll('.sub-tab').forEach(b => b.classList.remove('active'));
        parent.querySelectorAll('.sub-content').forEach(c => c.classList.remove('active'));
        // Activate clicked
        btn.classList.add('active');
        parent.querySelector(`.sub-content.${target}`).classList.add('active');
      });
    });
  });

  // Search
  const searchInput = document.getElementById('ruling-search');
  if (searchInput) {
    searchInput.addEventListener('input', debounce(e => {
      searchQuery = e.target.value.trim();
      renderRulings();
    }, 250));
  }

  // Filter buttons
  document.querySelectorAll('.filter-btn[data-source]').forEach(btn => {
    btn.addEventListener('click', () => {
      const val = btn.dataset.source;
      if (activeFilters.source === val) {
        activeFilters.source = null;
        btn.classList.remove('active');
      } else {
        document.querySelectorAll('.filter-btn[data-source]').forEach(b => b.classList.remove('active'));
        activeFilters.source = val;
        btn.classList.add('active');
      }
      renderRulings();
    });
  });

  document.querySelectorAll('.filter-btn[data-category]').forEach(btn => {
    btn.addEventListener('click', () => {
      const val = btn.dataset.category;
      if (activeFilters.category === val) {
        activeFilters.category = null;
        btn.classList.remove('active');
      } else {
        document.querySelectorAll('.filter-btn[data-category]').forEach(b => b.classList.remove('active'));
        activeFilters.category = val;
        btn.classList.add('active');
      }
      renderRulings();
    });
  });

  // Sort
  const sortBtn = document.getElementById('sort-btn');
  if (sortBtn) {
    sortBtn.addEventListener('click', () => {
      sortOrder = sortOrder === 'newest' ? 'oldest' : 'newest';
      sortBtn.textContent = sortOrder === 'newest' ? '最新 ↓' : '最舊 ↑';
      renderRulings();
    });
  }

  // Clear filters
  const clearBtn = document.getElementById('clear-filters');
  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      searchQuery = '';
      activeFilters = { source: null, category: null };
      document.getElementById('ruling-search').value = '';
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      renderRulings();
    });
  }

  // Show only favorites
  const favFilterBtn = document.getElementById('fav-filter');
  if (favFilterBtn) {
    favFilterBtn.addEventListener('click', () => {
      favFilterBtn.classList.toggle('active');
      renderRulings();
    });
  }

  // Expand all manual cards
  document.getElementById('expand-all')?.addEventListener('click', () => {
    const cards = document.querySelectorAll('#manual-section .card');
    const allOpen = [...cards].every(c => c.classList.contains('open'));
    cards.forEach(c => c.classList.toggle('open', !allOpen));
  });

  // Back to top
  const topBtn = document.querySelector('.back-top');
  window.addEventListener('scroll', () => {
    topBtn.classList.toggle('show', window.scrollY > 400);
  });
  topBtn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
}

/* ===== Render Rulings ===== */
function renderRulings() {
  const container = document.getElementById('rulings-list');
  if (!container) return;

  let filtered = [...rulings];

  // Favorites filter
  const favActive = document.getElementById('fav-filter')?.classList.contains('active');
  if (favActive) {
    filtered = filtered.filter(r => favorites.includes(r.id));
  }

  // Source filter
  if (activeFilters.source) {
    filtered = filtered.filter(r =>
      activeFilters.source === '中央' ? r.source === '中央' : r.source !== '中央'
    );
  }

  // Category filter
  if (activeFilters.category) {
    filtered = filtered.filter(r => r.category === activeFilters.category);
  }

  // Search
  if (searchQuery) {
    const q = searchQuery.toLowerCase();
    filtered = filtered.filter(r =>
      r.number.toLowerCase().includes(q) ||
      r.subject.toLowerCase().includes(q) ||
      r.summary.toLowerCase().includes(q) ||
      r.category.toLowerCase().includes(q)
    );
  }

  // Sort
  filtered.sort((a, b) => {
    return sortOrder === 'newest'
      ? b.date.localeCompare(a.date)
      : a.date.localeCompare(b.date);
  });

  if (filtered.length === 0) {
    container.innerHTML = '<div class="no-results">🔍 沒有找到符合條件的函釋</div>';
    return;
  }

  container.innerHTML = filtered.map(r => {
    const isFav = favorites.includes(r.id);
    const sourceClass = r.source === '中央' ? 'source-central' : 'source-local';
    const catClass = r.category.startsWith('BA') ? 'cat-ba'
      : r.category.startsWith('AA') ? 'cat-aa'
      : r.category.startsWith('GA') ? 'cat-ga' : 'cat-other';

    return `
      <div class="ruling-card" data-id="${r.id}">
        <div class="ruling-header" onclick="toggleRuling(this)">
          <div style="flex:1">
            <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap">
              <span class="ruling-num">${r.number}</span>
              <span class="ruling-date">${r.date}</span>
            </div>
            <div class="ruling-subject">${r.subject}</div>
            <div class="ruling-meta">
              <span class="tag ${sourceClass}">${r.source}</span>
              <span class="tag ${catClass}">${r.category}</span>
            </div>
          </div>
          <span class="arrow">▶</span>
        </div>
        <div class="ruling-body">
          <p>${r.summary}</p>
          <div class="ruling-actions">
            <button class="ruling-action-btn fav ${isFav ? 'active' : ''}" onclick="toggleFav('${r.id}', this)">
              ${isFav ? '★ 已收藏' : '☆ 收藏'}
            </button>
            <button class="ruling-action-btn" onclick="copyRuling('${r.id}')">📋 複製引用</button>
            <button class="ruling-action-btn" onclick="shareRuling('${r.id}')">🔗 分享</button>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

function toggleRuling(el) {
  el.closest('.ruling-card').classList.toggle('open');
}

/* ===== Favorites ===== */
function toggleFav(id, btn) {
  event.stopPropagation();
  const idx = favorites.indexOf(id);
  if (idx > -1) {
    favorites.splice(idx, 1);
    btn.classList.remove('active');
    btn.innerHTML = '☆ 收藏';
  } else {
    favorites.push(id);
    btn.classList.add('active');
    btn.innerHTML = '★ 已收藏';
  }
  localStorage.setItem('ltc_favorites', JSON.stringify(favorites));
  updateFavCount();
  showToast(idx > -1 ? '已取消收藏' : '已加入收藏');
}

function updateFavCount() {
  const el = document.getElementById('fav-count');
  if (el) el.textContent = favorites.length;
}

/* ===== Copy / Share ===== */
function copyRuling(id) {
  event.stopPropagation();
  const r = rulings.find(x => x.id === id);
  if (!r) return;
  const text = `${r.number}（${r.date}）\n${r.subject}\n來源：${r.source}`;
  navigator.clipboard.writeText(text).then(() => showToast('已複製引用格式'));
}

function shareRuling(id) {
  event.stopPropagation();
  const url = `${location.href.split('#')[0]}#ruling-${id}`;
  navigator.clipboard.writeText(url).then(() => showToast('已複製分享連結'));
}

/* ===== Render Scenarios ===== */
function renderScenarios() {
  const container = document.getElementById('scenarios-list');
  if (!container) return;

  const grouped = {};
  scenarios.forEach(s => {
    if (!grouped[s.category]) grouped[s.category] = [];
    grouped[s.category].push(s);
  });

  let html = '';
  for (const [cat, items] of Object.entries(grouped)) {
    html += `<div style="margin-bottom:8px;font-size:13px;font-weight:700;color:var(--gray-500);text-transform:uppercase;letter-spacing:.03em">${cat}</div>`;
    items.forEach(s => {
      html += `
        <div class="card">
          <div class="card-header" onclick="this.closest('.card').classList.toggle('open')">
            <span class="arrow">▶</span>
            <span class="title">❓ ${s.question}</span>
          </div>
          <div class="card-body">
            <p style="line-height:1.9">${s.answer}</p>
          </div>
        </div>
      `;
    });
  }
  container.innerHTML = html;
}

/* ===== Utils ===== */
function debounce(fn, ms) {
  let t;
  return (...args) => { clearTimeout(t); t = setTimeout(() => fn(...args), ms); };
}

function showToast(msg) {
  const el = document.getElementById('toast');
  if (!el) return;
  el.textContent = msg;
  el.classList.add('show');
  setTimeout(() => el.classList.remove('show'), 2000);
}
