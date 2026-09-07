import re, json, os

# ROOT = the site's root directory (one level above this file, i.e. build/..).
# SHARED = build/shared, where the CSS/nav/footer/i18n/JS fragments that every
# generated page is assembled from live. Both are computed relative to this
# script's own location (not hardcoded) so the build system works no matter
# where the repo is cloned.
BUILD_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BUILD_DIR)
SHARED = os.path.join(BUILD_DIR, 'shared')

with open(os.path.join(SHARED, 'extracted_css.css'), encoding='utf-8') as f:
    CSS_RAW = f.read()

with open(os.path.join(SHARED, 'extracted_nav.html'), encoding='utf-8') as f:
    NAV_RAW = f.read()

with open(os.path.join(SHARED, 'shared_i18n.json'), encoding='utf-8') as f:
    SHARED_I18N = json.load(f)


def merge_i18n(page_specific):
    """page_specific: {'pt': {...}, 'en': {...}, 'es': {...}}"""
    out = {}
    for lang in ('pt', 'en', 'es'):
        out[lang] = {**SHARED_I18N[lang], **page_specific.get(lang, {})}
    return out

with open(os.path.join(SHARED, 'extracted_footer.html'), encoding='utf-8') as f:
    FOOTER_RAW = f.read()

with open(os.path.join(SHARED, 'js_part1_utils.js'), encoding='utf-8') as f:
    JS_UTILS = f.read()

APPLY_LANG_JS = """let currentLang = 'en';
function applyLang(lang){
  if(!I18N[lang]) return;
  currentLang = lang;
  document.documentElement.setAttribute('lang', lang === 'pt' ? 'pt-PT' : lang);
  document.querySelectorAll('[data-i18n]').forEach(el=>{
    const key = el.getAttribute('data-i18n');
    const val = I18N[lang][key];
    if(val === undefined) return;
    if(el.classList.contains('line')){
      /* Hero-title lines are split into <span class="word"> pieces by splitLines() right after
         load, purely for the one-off intro stagger animation (see HERO_SPLIT_JS below). Because of
         that split, this element has element children by the time a language switch happens — the
         "find the first text node" fallback below (meant for CTA buttons with a trailing icon)
         would instead grab a stray whitespace text node left over from the word-join and overwrite
         it with the WHOLE new sentence, while every stale <span class="word"> from the old language
         stayed in the DOM untouched. That produced duplicated/garbled hero-title text on language
         switch. Rebuilding the words from scratch keeps the DOM in sync with the new language; the
         intro stagger has already played by the time anyone switches language, so the rebuilt words
         are shown immediately at their final (visible) state instead of replaying the reveal. */
      const words = val.trim().split(/\\s+/);
      el.innerHTML = words.map(w=>`<span class="word">${w}</span>`).join(' ');
      el.querySelectorAll('.word').forEach(w=>{ w.style.opacity = '1'; w.style.transform = 'none'; });
    } else if(el.children.length){
      /* Some data-i18n elements (CTA buttons) carry a trailing <svg> icon child alongside their
         label text — el.textContent would wipe that icon out. Replace only the leading text node
         instead, leaving any element children (the icon) untouched. */
      let node = el.firstChild;
      while(node && node.nodeType !== Node.TEXT_NODE) node = node.nextSibling;
      if(node) node.textContent = val;
      else el.insertBefore(document.createTextNode(val), el.firstChild);
    } else {
      el.textContent = val;
    }
  });
  document.querySelectorAll('#langLabel').forEach(el=> el.textContent = lang.toUpperCase());
  document.querySelectorAll('.lang-menu button, .mobile-lang button').forEach(btn=>{
    btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
  });
  /* Remember the visitor's choice so it survives navigation to another page — every page on the
     site checks this before falling back to the English default (see below). */
  try{ localStorage.setItem('adpetrosLang', lang); }catch(e){}
  if(window.ScrollTrigger) ScrollTrigger.refresh();
}
document.querySelectorAll('.lang-menu button, .mobile-lang button').forEach(btn=>{
  btn.addEventListener('click', (e)=>{
    e.stopPropagation();
    applyLang(btn.getAttribute('data-lang'));
    langSwitch.classList.remove('open');
  });
});
/* The site's primary/default language is English — the HTML is authored with Portuguese as the
   baked-in fallback text (for no-JS / first-paint), but we immediately (synchronously, in this same
   parse/execute tick, before the browser gets a chance to paint) swap every [data-i18n] node over to
   whichever language the visitor last picked (persisted in localStorage so it holds across page
   navigation), or English by default if they haven't chosen one yet. PT/ES remain available via the
   switcher. */
let savedLang = 'en';
try{ const s = localStorage.getItem('adpetrosLang'); if(s && I18N[s]) savedLang = s; }catch(e){}
applyLang(savedLang);"""

REVEAL_JS = """/* ---------- GSAP scroll storytelling ---------- */
gsap.registerPlugin(ScrollTrigger);
ScrollTrigger.config({ ignoreMobileResize: true });
const REDUCE_MOTION = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* .reveal elements. Big titles (which are the vast majority of .reveal usage across the site) get an
   extra clip-mask wipe layered on top of the fade+rise — a more architectural "reveal" than a plain
   fade, without requiring any markup changes since every .big-title already carries .reveal. */
gsap.utils.toArray('.reveal').forEach((el, i)=>{
  const isTitle = !el.closest('#heroTitle') && (el.classList.contains('big-title') || (el.tagName === 'H2' && el.closest('.cta-final')));
  if(isTitle && !REDUCE_MOTION) gsap.set(el, {clipPath:'inset(0 0 100% 0)'});
  gsap.fromTo(el, {opacity:0, y:34}, {
    opacity:1, y:0, duration:.9, ease:'power3.out', clearProps:'opacity,transform',
    onComplete:()=>el.classList.remove('reveal'),
    scrollTrigger:{trigger:el, start:'top 88%', once:true}
  });
  if(isTitle && !REDUCE_MOTION){
    gsap.to(el, {clipPath:'inset(0 0 0% 0)', duration:1.05, ease:'power3.out', clearProps:'clipPath',
      scrollTrigger:{trigger:el, start:'top 88%', once:true}});
  }
});

/* .reveal-img elements (images / visual blocks): clip-mask wipe + soft scale, more "reveal" than "fade" */
gsap.utils.toArray('.reveal-img').forEach(el=>{
  if(!REDUCE_MOTION) gsap.set(el, {clipPath:'inset(0 0 8% 0)'});
  gsap.fromTo(el, {opacity:0, y:26, scale:1.035}, {
    opacity:1, y:0, scale:1, duration:1.15, ease:'power3.out', clearProps:'opacity,transform,clipPath',
    onComplete:()=>el.classList.remove('reveal-img'),
    scrollTrigger:{trigger:el, start:'top 88%', once:true}
  });
  if(!REDUCE_MOTION){
    gsap.to(el, {clipPath:'inset(0 0 0% 0)', duration:1.15, ease:'power3.out',
      scrollTrigger:{trigger:el, start:'top 88%', once:true}});
  }
});

/* .stagger groups (children animate one after another). Optional data-stagger-dir="left|right" on the
   group gives the whole group a short diagonal entrance instead of the default straight rise — used
   sparingly so different sections have a slightly different rhythm without feeling random.
   once:true is important here: without it, a ScrollTrigger.refresh() after window 'load' (e.g. once
   late-loading photography settles the page's final height) can re-evaluate this trigger's position
   and — because clearProps already stripped the tween's inline styles — snap the group back to its
   "from" state and replay it, which reads as a jarring blink/flash on entrance. */
gsap.utils.toArray('.stagger').forEach(group=>{
  const dir = group.getAttribute('data-stagger-dir');
  const fromVars = dir === 'left' ? {opacity:0, x:-22, y:14} : dir === 'right' ? {opacity:0, x:22, y:14} : {opacity:0, y:28};
  const toVars = dir ? {opacity:1, x:0, y:0} : {opacity:1, y:0};
  gsap.fromTo(group.children, fromVars, {
    ...toVars, duration:.8, ease:'power3.out', stagger:0.09, clearProps:'opacity,transform',
    onComplete:()=>group.classList.remove('stagger'),
    scrollTrigger:{trigger:group, start:'top 90%', once:true}
  });
});

/* eyebrow tags fade-in */
gsap.utils.toArray('.eyebrow').forEach(el=>{
  gsap.fromTo(el, {opacity:0, x:-14}, {
    opacity:1, x:0, duration:.7, ease:'power3.out',
    scrollTrigger:{trigger:el, start:'top 92%', once:true}
  });
});

/* Count-up numbers (only used where a real, confirmed metric exists) */
gsap.utils.toArray('.count-num[data-count-to]').forEach(el=>{
  const target = parseFloat(el.getAttribute('data-count-to'));
  const decimals = (el.getAttribute('data-count-to').split('.')[1] || '').length;
  const proxy = {val:0};
  ScrollTrigger.create({
    trigger:el, start:'top 90%', once:true,
    onEnter:()=> gsap.to(proxy, {val:target, duration:1.6, ease:'power2.out',
      onUpdate:()=> el.textContent = proxy.val.toFixed(decimals)})
  });
});

/* Progressive SVG line-draw (used by diagram components, e.g. the comparison section) */
gsap.utils.toArray('.draw-path').forEach(path=>{
  if(typeof path.getTotalLength !== 'function') return;
  const len = path.getTotalLength();
  gsap.set(path, {strokeDasharray:len, strokeDashoffset:REDUCE_MOTION ? 0 : len});
  if(REDUCE_MOTION) return;
  gsap.to(path, {strokeDashoffset:0, duration:1.1, ease:'power2.inOut',
    scrollTrigger:{trigger:path.closest('.cmp2-canvas') || path, start:'top 82%', once:true}
  });
});

/* Subtle parallax for full-bleed photography (scroll-linked, not just entrance) */
if(!REDUCE_MOTION){
  gsap.utils.toArray('.photo-section-bg img').forEach(img=>{
    gsap.fromTo(img, {yPercent:-6}, {
      yPercent:6, ease:'none',
      scrollTrigger:{trigger:img.closest('.photo-section'), start:'top bottom', end:'bottom top', scrub:0.6}
    });
  });
}
"""

HERO_SPLIT_JS = """/* Hero title line reveal */
function splitLines(container){
  container.querySelectorAll('.line').forEach(line=>{
    const words = line.textContent.trim().split(/\\s+/);
    line.innerHTML = words.map(w=>`<span class="word">${w}</span>`).join(' ');
  });
}
const heroTitleEl = document.getElementById('heroTitle');
splitLines(heroTitleEl);
/* #heroTitle starts at opacity:0 in CSS (word spans don't exist until splitLines runs, so they
   can't be pre-hidden via CSS) — reveal the now-split container in this same synchronous tick,
   right before hiding the individual words below, so the browser never paints the old unsplit
   plain-text title at full opacity. */
heroTitleEl.style.opacity = '1';
gsap.set('#heroTitle .word', {y:'115%', opacity:0});
gsap.to('#heroTitle .word', {
  y:0, opacity:1, duration:1.1, ease:'power4.out', stagger:0.035, delay:.3
});
/* Scoped to ".hero" specifically — .hero-lead/.hero-ctas are reused outside the hero (e.g. the
   CTA-final section's button row) and must never be touched by this once-off page-load timeline;
   those reused instances are driven solely by the generic .reveal scroll system instead. */
gsap.set('.hero .hero-lead, .hero .hero-ctas', {opacity:0, y:24});
gsap.to('.hero .hero-lead', {opacity:1, y:0, duration:1, ease:'power3.out', delay:1});
gsap.to('.hero .hero-ctas', {opacity:1, y:0, duration:1, ease:'power3.out', delay:1.15});
"""

REFRESH_JS = """window.addEventListener('load', ()=> ScrollTrigger.refresh());
/* Web fonts can swap in slightly after 'load' (font-display:swap), reflowing text and
   shifting everything below it — refresh once more once they're actually ready so later
   (not-yet-fired) triggers keep accurate positions. Already-fired triggers are immune to
   this anyway (see once:true above), so this only helps triggers still waiting to fire. */
if(document.fonts && document.fonts.ready){
  document.fonts.ready.then(()=> ScrollTrigger.refresh());
}"""

BGVIDEOS_JS = """/* ---------- Background videos: play only while visible ---------- */
(function bgVideos(){
  const reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const videos = document.querySelectorAll('.hero-video, .why-hero-video, .section-visual-video');
  if(!videos.length) return;
  if(reduceMotion){
    videos.forEach(v => v.pause());
    return;
  }
  if('IntersectionObserver' in window){
    const io = new IntersectionObserver((entries)=>{
      entries.forEach(entry=>{
        const v = entry.target;
        if(entry.isIntersecting) v.play().catch(()=>{});
        else v.pause();
      });
    }, {threshold:0.15});
    videos.forEach(v => io.observe(v));
  }
})();
"""


WHATSAPP_HTML = """<a href="#" id="waFloat" class="wa-float" aria-label="Falar no WhatsApp" target="_blank" rel="noopener">
  <svg viewBox="0 0 32 32" fill="none" aria-hidden="true">
    <path d="M16.02 3C9.4 3 4 8.37 4 14.98c0 2.2.6 4.26 1.63 6.04L4 29l8.2-1.58a12.9 12.9 0 003.82.58h.01c6.62 0 12.02-5.37 12.02-11.98C28.05 8.37 22.65 3 16.02 3z" fill="#fff"/>
    <path d="M16.02 3C9.4 3 4 8.37 4 14.98c0 2.2.6 4.26 1.63 6.04L4 29l8.2-1.58a12.9 12.9 0 003.82.58h.01c6.62 0 12.02-5.37 12.02-11.98C28.05 8.37 22.65 3 16.02 3zm7.02 17.03c-.3.83-1.72 1.58-2.38 1.66-.61.08-1.38.11-2.23-.14-.51-.15-1.17-.37-2.02-.73-3.55-1.53-5.87-5.1-6.05-5.34-.18-.24-1.45-1.93-1.45-3.68 0-1.75.92-2.6 1.24-2.96.33-.36.71-.44.95-.44.24 0 .47.002.68.012.22.01.51-.08.8.61.3.7 1.02 2.44 1.11 2.62.09.18.15.4.03.64-.12.24-.18.4-.36.61-.18.21-.38.47-.55.63-.18.18-.37.37-.16.73.21.36.94 1.55 2.02 2.51 1.39 1.24 2.56 1.62 2.92 1.8.36.18.57.15.78-.09.21-.24.9-1.05 1.14-1.41.24-.36.48-.3.81-.18.33.12 2.08.98 2.44 1.16.36.18.6.27.68.42.09.15.09.85-.21 1.68z" fill="#25D366"/>
  </svg>
</a>"""

WHATSAPP_JS = """/* ---------- WhatsApp floating button ---------- */
const WHATSAPP_NUMBER = ''; /* TODO(cliente): número em formato internacional sem espaços, ex: '351912345678'. Deixar vazio até ser confirmado — nao inventar um contacto. */
(function initWhatsApp(){
  const btn = document.getElementById('waFloat');
  if(!btn) return;
  if(WHATSAPP_NUMBER){
    btn.href = 'https://wa.me/' + WHATSAPP_NUMBER;
  } else {
    btn.removeAttribute('target');
    btn.setAttribute('aria-disabled', 'true');
    console.warn('[ADPETROS] Número de WhatsApp por configurar — ver WHATSAPP_NUMBER no script da página.');
  }
})();
"""


def make_nav(active, is_home=False):
    """active in {'home','about','solutions','contact', None}"""
    nav = NAV_RAW
    if not is_home:
        # point logo + Início to root
        nav = nav.replace('<a href="#top" class="logo">', '<a href="/" class="logo">')
        nav = nav.replace(
            '<li><a href="#top" class="nav-link active" data-i18n="nav.home">Início</a></li>',
            '<li><a href="/" class="nav-link" data-i18n="nav.home">Início</a></li>'
        )
        nav = nav.replace(
            '<li><a href="#top" class="m-link" data-i18n="nav.home">Início</a></li>',
            '<li><a href="/" class="m-link" data-i18n="nav.home">Início</a></li>'
        )
    else:
        active = active or 'home'

    # remove default active class from home link if a different page is active
    if active != 'home':
        nav = nav.replace(
            'class="nav-link active" data-i18n="nav.home"',
            'class="nav-link" data-i18n="nav.home"'
        )

    targets = {
        'about': '<a href="/sobre-nos/" class="nav-link" data-i18n="nav.about">',
        'solutions': '<a href="/solucoes/" class="nav-link" data-i18n="nav.solutions">',
        'contact': '<a href="/contactos/" class="nav-link" data-i18n="nav.contact">',
    }
    if active in targets:
        old = targets[active]
        new = old.replace('class="nav-link"', 'class="nav-link active"')
        nav = nav.replace(old, new, 1)

    return nav


def make_footer():
    return FOOTER_RAW


def head_meta(title, description, path, og_image='og-image.jpg'):
    canonical = f"https://www.adpetros.com{path}"
    return f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">

<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="https://www.adpetros.com/{og_image}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="https://www.adpetros.com/{og_image}">

<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">"""


def build_js(i18n_dict, extra_css_only_js='', include_hero_split=True, extra_js=''):
    i18n_js = "const I18N = " + json.dumps(i18n_dict, ensure_ascii=False, indent=2) + ";\n"
    parts = [
        "/* =========================================================",
        "   ADPETROS — page.js (shared utilities, generated)",
        "   ========================================================= */",
        JS_UTILS,
        "",
        "/* ---------- i18n ---------- */",
        i18n_js,
        APPLY_LANG_JS,
        "",
        BGVIDEOS_JS,
        REVEAL_JS,
    ]
    if include_hero_split:
        parts.append(HERO_SPLIT_JS)
    if extra_js:
        parts.append(extra_js)
    parts.append(WHATSAPP_JS)
    parts.append(REFRESH_JS)
    return "\n".join(parts)


def build_page(*, title, description, path, active_nav, body_html, i18n_dict,
                include_hero_split=True, extra_js='', is_home=False, lang_attr='en',
                ld_json=None):
    nav_html = make_nav(active_nav, is_home=is_home)
    footer_html = make_footer()
    js = build_js(i18n_dict, include_hero_split=include_hero_split, extra_js=extra_js)
    ld = ld_json or ""
    html = f"""<!DOCTYPE html>
<html lang="{lang_attr}">
<head>
{head_meta(title, description, path)}
{ld}
<style>
{CSS_RAW}
</style>
</head>
<body>

<div class="progress" id="progress"></div>

{nav_html}

{body_html}

{footer_html}

{WHATSAPP_HTML}

<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script>
{js}
</script>
</body>
</html>
"""
    return html


CHECK_ICON = '<svg class="ico" viewBox="0 0 16 16" fill="none"><path d="M3 8.5l3.2 3L13 4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

GENERIC_ENG_ICON = '<svg viewBox="0 0 24 24" fill="none"><path d="M13 3L4 14h7l-1 7 9-11h-7l1-7z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>'

GENERIC_WHY_ICON = '<svg viewBox="0 0 24 24" fill="none"><path d="M5 13l4 4L19 7" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def sol_steps_html(items, extra_style=''):
    """items: list of dicts {n, tkey, tdef, pkey, pdef}
    The grid's column count on desktop (>=760px) tracks the real number of items via the
    --sol-steps-cols custom property, so a 3-item page gets 3 equal columns filling the full
    width instead of the CSS assuming 4 and leaving an empty trailing slot."""
    style = f'--sol-steps-cols:{len(items)};{extra_style}'
    out = [f'<div class="sol-steps" style="{style}">']
    for it in items:
        out.append(f'''      <div class="sol-step flip-card reveal">
        <div class="n">{it['n']}</div>
        <h4 data-i18n="{it['tkey']}">{it['tdef']}</h4>
        <p data-i18n="{it['pkey']}">{it['pdef']}</p>
      </div>''')
    out.append('    </div>')
    return '\n'.join(out)


def check_list_html(items):
    """items: list of dicts {key, text}"""
    out = ['<ul class="check-list stagger">']
    for it in items:
        out.append(f'      <li>{CHECK_ICON}<span data-i18n="{it["key"]}">{it["text"]}</span></li>')
    out.append('    </ul>')
    return '\n'.join(out)


def eng_cards_html(items):
    """items: list of dicts {icon, key, text}"""
    out = ['<div class="grid eng-grid stagger">']
    for it in items:
        icon = it.get('icon', GENERIC_ENG_ICON)
        out.append(f'''      <div class="eng-card">
        {icon}
        <h4 data-i18n="{it['key']}">{it['text']}</h4>
      </div>''')
    out.append('    </div>')
    return '\n'.join(out)


def why_mini_html(items):
    """items: list of dicts {icon, tkey, tdef, pkey, pdef}"""
    out = ['<div class="why-mini-grid stagger">']
    for it in items:
        icon = it.get('icon', GENERIC_WHY_ICON)
        out.append(f'''      <article class="why-mini">
        <div class="why-mini-ic">{icon}</div>
        <h4 data-i18n="{it['tkey']}">{it['tdef']}</h4>
        <p data-i18n="{it['pkey']}">{it['pdef']}</p>
      </article>''')
    out.append('    </div>')
    return '\n'.join(out)


def inline_cta_html(href='/contactos/', key='nav.cta', default='Falar com a equipa', style='primary', margin_top=36):
    """A lightweight, in-flow conversion CTA — reuses the site's existing .btn style/arrow icon
    exactly as-is (no new button style). Meant to sit inside an existing section, right below its
    content, so solution pages offer a few natural chances to convert along the way instead of
    saving the only CTA for the very end of the page."""
    return f'''<div class="reveal" style="margin-top:{margin_top}px">
      <a href="{href}" class="btn btn-{style}" data-i18n="{key}">{default}
        <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
    </div>'''


def photo_section_html(*, img, alt, eyebrow_key, eyebrow_def, title1_key, title1_def, title2_key, title2_def,
                        text_key=None, text_def=None, cta_href=None, cta_key=None, cta_def=None, extra_class=''):
    """A full-bleed photography section with a petrol overlay, used on solution detail pages.
    img: root-relative path to the -lg.jpg variant (e.g. '/assets/img/12-lg.jpg')."""
    cta_html = ''
    if cta_href and cta_key:
        cta_html = f'''
        <div class="hero-ctas reveal" style="margin-top:8px">
          <a href="{cta_href}" class="btn btn-primary" data-i18n="{cta_key}">{cta_def}
            <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
        </div>'''
    text_html = ''
    if text_key and text_def:
        text_html = f'\n        <p class="reveal" style="max-width:560px;margin-top:18px;font-size:16px;line-height:1.75" data-i18n="{text_key}">{text_def}</p>'
    return f'''<section class="section photo-section {extra_class}" data-theme="dark">
  <div class="photo-section-bg"><img src="{img}" alt="{alt}" loading="lazy"></div>
  <div class="container photo-section-content">
    <div class="eyebrow" data-i18n="{eyebrow_key}">{eyebrow_def}</div>
    <h2 class="big-title reveal"><span data-i18n="{title1_key}">{title1_def}</span> <span class="title-dim" data-i18n="{title2_key}">{title2_def}</span></h2>{text_html}{cta_html}
  </div>
</section>'''


def example_situation_html(*, prefix, eyebrow_def, title_def, text_def, img, alt, img_first=False,
                            cta_href=None, cta_key=None, cta_def=None):
    """'Imagine a seguinte situação' — a light, easy-to-scan two-column example
    (text + real photo) used on solution detail pages to make the service concrete."""
    order_style = ' style="order:2"' if img_first else ''
    cta_html = ''
    if cta_href and cta_key:
        cta_html = f'''
        <div class="reveal" style="margin-top:28px">
          <a href="{cta_href}" class="btn btn-primary" data-i18n="{cta_key}">{cta_def}
            <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
        </div>'''
    text_block = f'''
      <div class="example-text"{order_style}>
        <div class="example-badge"><svg viewBox="0 0 24 24" fill="none"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.4.3.6.8.6 1.3V16h5.8v-.8c0-.5.2-1 .6-1.3A6 6 0 0 0 12 3Z" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg><span data-i18n="{prefix}.ex.eyebrow">{eyebrow_def}</span></div>
        <h2 class="big-title reveal" data-i18n="{prefix}.ex.title">{title_def}</h2>
        <p class="reveal example-p" data-i18n="{prefix}.ex.p">{text_def}</p>{cta_html}
      </div>'''
    photo_block = f'''
      <div class="example-photo reveal-img"><img src="{img}" alt="{alt}" loading="lazy"></div>'''
    inner = (photo_block + text_block) if img_first else (text_block + photo_block)
    return f'''<section class="section example-section" data-theme="white">
  <div class="container">
    <div class="example-grid">{inner}
    </div>
  </div>
</section>'''


WHY_BENTO_I18N = {
  'pt': {
    "why.eyebrow": "O VALOR DA EXPERIÊNCIA LOCAL",
    "why.title1": "Menos complexidade,", "why.title2": "mais possibilidades.",
    "why.cardtitle": "Simplifique com a ADPETROS", "why.cta": "Fale connosco",
    "why1.t": "Conhecimento técnico", "why1.p": "Experiência de engenharia aplicada a projetos e operações industriais.",
    "why2.t": "Conhecimento local", "why2.p": "Conhecimento dos mercados e das particularidades de cada país.",
    "why3.t": "Rede no terreno", "why3.p": "Rede de empresas, profissionais e fornecedores locais.",
    "why4.t": "Eficiência operacional", "why4.p": "Estrutura local que reduz deslocações e simplifica a operação.",
    "why5.t": "Capacidade de execução", "why5.p": "Criamos as condições necessárias para o projeto avançar.",
    "why6.t": "Relação de longo prazo", "why6.p": "Acompanhamos o projeto como parceiro em todas as fases.",
  },
  'en': {
    "why.eyebrow": "THE VALUE OF LOCAL EXPERIENCE",
    "why.title1": "Less complexity,", "why.title2": "more possibilities.",
    "why.cardtitle": "Simplify with ADPETROS", "why.cta": "Contact us",
    "why1.t": "Technical knowledge", "why1.p": "Engineering experience applied to industrial projects and operations.",
    "why2.t": "Local knowledge", "why2.p": "Knowledge of markets and the particularities of each country.",
    "why3.t": "Network on the ground", "why3.p": "A network of companies, professionals and local suppliers.",
    "why4.t": "Operational efficiency", "why4.p": "A local structure that reduces travel and simplifies operations.",
    "why5.t": "Execution capability", "why5.p": "We create the conditions the project needs to move forward.",
    "why6.t": "Long-term relationship", "why6.p": "We follow the project as a partner across every phase.",
  },
  'es': {
    "why.eyebrow": "EL VALOR DE LA EXPERIENCIA LOCAL",
    "why.title1": "Menos complejidad,", "why.title2": "más posibilidades.",
    "why.cardtitle": "Simplifique con ADPETROS", "why.cta": "Contáctenos",
    "why1.t": "Conocimiento técnico", "why1.p": "Experiencia de ingeniería aplicada a proyectos y operaciones industriales.",
    "why2.t": "Conocimiento local", "why2.p": "Conocimiento de los mercados y de las particularidades de cada país.",
    "why3.t": "Red en el terreno", "why3.p": "Red de empresas, profesionales y proveedores locales.",
    "why4.t": "Eficiencia operativa", "why4.p": "Estructura local que reduce desplazamientos y simplifica la operación.",
    "why5.t": "Capacidad de ejecución", "why5.p": "Creamos las condiciones necesarias para que el proyecto avance.",
    "why6.t": "Relación a largo plazo", "why6.p": "Acompañamos el proyecto como socio en todas sus fases.",
  },
}


def why_bento_html(cta_href='/contactos/'):
    """The exact 'Menos complexidade, mais possibilidades' component from Home — same structure, text,
    video, cards and animations. Reused verbatim (not recreated) wherever this section appears, so the
    two only ever diverge in the CTA link target."""
    return f'''<section class="section" data-theme="dark">
  <div class="container">
    <div class="header-row">
      <div>
        <div class="eyebrow" data-i18n="why.eyebrow">O VALOR DA EXPERIÊNCIA LOCAL</div>
        <h2 class="big-title reveal"><span data-i18n="why.title1">Menos complexidade,</span> <span class="title-dim" data-i18n="why.title2">mais possibilidades.</span></h2>
      </div>
    </div>

    <div class="why-bento">
      <article class="why-hero reveal-img">
        <div class="why-hero-img" aria-hidden="true">
          <video class="why-hero-video" muted loop playsinline preload="metadata" poster="/assets/video/videocard-poster.jpg">
            <source src="/assets/video/videocard.mp4" type="video/mp4">
          </video>
        </div>
        <div class="why-hero-body">
          <h3 data-i18n="why.cardtitle">Simplifique com a ADPETROS</h3>
          <a href="{cta_href}" class="why-hero-btn"><span data-i18n="why.cta">Fale connosco</span></a>
        </div>
      </article>

      <div class="why-mini-grid stagger">
        <article class="why-mini">
          <div class="why-mini-ic"><svg viewBox="0 0 24 24" fill="none"><path d="M4 20V10l8-6 8 6v10M9 20v-6h6v6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
          <h4 data-i18n="why1.t">Conhecimento técnico</h4>
          <p data-i18n="why1.p">Experiência de engenharia aplicada a projetos e operações industriais.</p>
        </article>
        <article class="why-mini">
          <div class="why-mini-ic"><svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="8.5" stroke="currentColor" stroke-width="1.6"/><path d="M3.5 12h17M12 3.5c2.2 2.3 3.3 5.1 3.3 8.5s-1.1 6.2-3.3 8.5c-2.2-2.3-3.3-5.1-3.3-8.5s1.1-6.2 3.3-8.5z" stroke="currentColor" stroke-width="1.6"/></svg></div>
          <h4 data-i18n="why2.t">Conhecimento local</h4>
          <p data-i18n="why2.p">Conhecimento dos mercados e das particularidades de cada país.</p>
        </article>
        <article class="why-mini">
          <div class="why-mini-ic"><svg viewBox="0 0 24 24" fill="none"><circle cx="6" cy="7" r="2.4" stroke="currentColor" stroke-width="1.6"/><circle cx="18" cy="7" r="2.4" stroke="currentColor" stroke-width="1.6"/><circle cx="12" cy="17" r="2.4" stroke="currentColor" stroke-width="1.6"/><path d="M7.6 9L10.5 15M16.4 9L13.5 15M8.4 7H15.6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></div>
          <h4 data-i18n="why3.t">Rede no terreno</h4>
          <p data-i18n="why3.p">Rede de empresas, profissionais e fornecedores locais.</p>
        </article>
        <article class="why-mini">
          <div class="why-mini-ic"><svg viewBox="0 0 24 24" fill="none"><path d="M13 3L4 14h7l-1 7 9-11h-7l1-7z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg></div>
          <h4 data-i18n="why4.t">Eficiência operacional</h4>
          <p data-i18n="why4.p">Estrutura local que reduz deslocações e simplifica a operação.</p>
        </article>
        <article class="why-mini">
          <div class="why-mini-ic"><svg viewBox="0 0 24 24" fill="none"><path d="M5 13l4 4L19 7" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
          <h4 data-i18n="why5.t">Capacidade de execução</h4>
          <p data-i18n="why5.p">Criamos as condições necessárias para o projeto avançar.</p>
        </article>
        <article class="why-mini">
          <div class="why-mini-ic"><svg viewBox="0 0 24 24" fill="none"><path d="M4 12a8 8 0 0114-5.3M20 12a8 8 0 01-14 5.3M14 4h4V0M10 20H6v4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
          <h4 data-i18n="why6.t">Relação de longo prazo</h4>
          <p data-i18n="why6.p">Acompanhamos o projeto como parceiro em todas as fases.</p>
        </article>
      </div>
    </div>
  </div>
</section>'''


def write_page(rel_path, html):
    full = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(html)
    print('wrote', full, len(html), 'bytes')
