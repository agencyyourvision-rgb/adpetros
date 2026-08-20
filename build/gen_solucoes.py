import sys
sys.path.insert(0, '/home/claude/adpetros-site/build')
from sitegen import build_page, write_page, merge_i18n

I18N = merge_i18n({
  'pt': {
    "sh.eyebrow": "SOLUÇÕES",
    "sh.title1": "O que podemos fazer",
    "sh.title2": "pelo seu projeto.",
    "sh.lead": "Cada projeto tem necessidades diferentes. Estas são as grandes áreas onde a ADPetros pode ajudar — da avaliação inicial à operação no terreno.",
    "sh.c1.t": "Engenharia",
    "sh.c1.p": "Engenharia e desenvolvimento técnico para projetos e operações industriais.",
    "sh.c2.t": "Implementação de Projetos",
    "sh.c2.p": "Apoio necessário para preparar e colocar projetos em execução no mercado.",
    "sh.c3.t": "Recuperação e Modernização de Ativos",
    "sh.c3.p": "Diagnóstico, recuperação, modernização e melhoria de refinarias e instalações existentes.",
    "sh.c4.t": "Energia e Descarbonização",
    "sh.c4.p": "Soluções para aproveitamento energético, gás associado e redução de emissões.",
    "sh.c5.t": "Procurement e Sourcing",
    "sh.c5.p": "Identificação, seleção e aquisição de equipamentos, componentes e fornecedores.",
    "sh.cta": "Saber mais",
    "sh.cta.eyebrow": "NÃO SABE POR ONDE COMEÇAR?",
    "sh.cta.title1": "Fale connosco",
    "sh.cta.title2": "e ajudamo-lo a encontrar a solução certa.",
    "sh.cta.btn": "Falar com a equipa",
  },
  'en': {
    "sh.eyebrow": "SOLUTIONS",
    "sh.title1": "What we can do",
    "sh.title2": "for your project.",
    "sh.lead": "Every project has different needs. These are the main areas where ADPetros can help — from the initial assessment to operating on the ground.",
    "sh.c1.t": "Engineering",
    "sh.c1.p": "Engineering and technical development for industrial projects and operations.",
    "sh.c2.t": "Project Implementation",
    "sh.c2.p": "The support needed to prepare and put projects into execution in the market.",
    "sh.c3.t": "Asset Recovery & Modernisation",
    "sh.c3.p": "Diagnosis, recovery, modernisation and improvement of refineries and existing facilities.",
    "sh.c4.t": "Energy & Decarbonisation",
    "sh.c4.p": "Solutions for energy recovery, associated gas and emissions reduction.",
    "sh.c5.t": "Procurement & Sourcing",
    "sh.c5.p": "Identifying, selecting and acquiring equipment, components and suppliers.",
    "sh.cta": "Learn more",
    "sh.cta.eyebrow": "NOT SURE WHERE TO START?",
    "sh.cta.title1": "Talk to us",
    "sh.cta.title2": "and we'll help you find the right solution.",
    "sh.cta.btn": "Talk to the team",
  },
  'es': {
    "sh.eyebrow": "SOLUCIONES",
    "sh.title1": "Qué podemos hacer",
    "sh.title2": "por su proyecto.",
    "sh.lead": "Cada proyecto tiene necesidades diferentes. Estas son las grandes áreas donde ADPetros puede ayudar — desde la evaluación inicial hasta la operación en el terreno.",
    "sh.c1.t": "Ingeniería",
    "sh.c1.p": "Ingeniería y desarrollo técnico para proyectos y operaciones industriales.",
    "sh.c2.t": "Implementación de Proyectos",
    "sh.c2.p": "El apoyo necesario para preparar y poner en ejecución proyectos en el mercado.",
    "sh.c3.t": "Recuperación y Modernización de Activos",
    "sh.c3.p": "Diagnóstico, recuperación, modernización y mejora de refinerías e instalaciones existentes.",
    "sh.c4.t": "Energía y Descarbonización",
    "sh.c4.p": "Soluciones para el aprovechamiento energético, gas asociado y reducción de emisiones.",
    "sh.c5.t": "Procurement y Sourcing",
    "sh.c5.p": "Identificación, selección y adquisición de equipos, componentes y proveedores.",
    "sh.cta": "Saber más",
    "sh.cta.eyebrow": "¿NO SABE POR DÓNDE EMPEZAR?",
    "sh.cta.title1": "Hable con nosotros",
    "sh.cta.title2": "y le ayudamos a encontrar la solución adecuada.",
    "sh.cta.btn": "Hablar con el equipo",
  },
})

BODY = """
<section class="section page-hero" id="top" data-theme="dark">
  <div class="container">
    <div class="eyebrow" data-i18n="sh.eyebrow">SOLUÇÕES</div>
    <h1 class="big-title reveal"><span data-i18n="sh.title1">O que podemos fazer</span> <span class="title-dim" data-i18n="sh.title2">pelo seu projeto.</span></h1>
    <p class="page-hero-lead reveal" data-i18n="sh.lead">Cada projeto tem necessidades diferentes. Estas são as grandes áreas onde a ADPetros pode ajudar — da avaliação inicial à operação no terreno.</p>
  </div>

  <div class="container" style="margin-top:clamp(48px,6vw,72px)">
    <div class="sol-hub-grid stagger">
      <a href="/solucoes/engenharia/" class="ch2-card reveal">
        <div class="ch2-card-img has-photo" aria-hidden="true"><img src="/assets/img/9-card.jpg" alt="" loading="lazy"><div class="layer"></div><div class="vignette"></div></div>
        <div class="ch2-card-body">
          <h3 data-i18n="sh.c1.t">Engenharia</h3>
          <p data-i18n="sh.c1.p">Engenharia e desenvolvimento técnico para projetos e operações industriais.</p>
          <span class="ch2-card-cta"><span data-i18n="sh.cta">Saber mais</span><svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </div>
      </a>
      <a href="/solucoes/implementacao-de-projetos/" class="ch2-card reveal">
        <div class="ch2-card-img has-photo" aria-hidden="true"><img src="/assets/img/14-card.jpg" alt="" loading="lazy"><div class="layer"></div><div class="vignette"></div></div>
        <div class="ch2-card-body">
          <h3 data-i18n="sh.c2.t">Implementação de Projetos</h3>
          <p data-i18n="sh.c2.p">Apoio necessário para preparar e colocar projetos em execução no mercado.</p>
          <span class="ch2-card-cta"><span data-i18n="sh.cta">Saber mais</span><svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </div>
      </a>
      <a href="/solucoes/modernizacao-de-ativos/" class="ch2-card reveal">
        <div class="ch2-card-img has-photo" aria-hidden="true"><img src="/assets/img/17-card.jpg" alt="" loading="lazy"><div class="layer"></div><div class="vignette"></div></div>
        <div class="ch2-card-body">
          <h3 data-i18n="sh.c3.t">Recuperação e Modernização de Ativos</h3>
          <p data-i18n="sh.c3.p">Diagnóstico, recuperação, modernização e melhoria de refinarias e instalações existentes.</p>
          <span class="ch2-card-cta"><span data-i18n="sh.cta">Saber mais</span><svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </div>
      </a>
      <a href="/solucoes/energia-e-descarbonizacao/" class="ch2-card reveal">
        <div class="ch2-card-img has-photo" aria-hidden="true"><img src="/assets/img/12-card.jpg" alt="" loading="lazy"><div class="layer"></div><div class="vignette"></div></div>
        <div class="ch2-card-body">
          <h3 data-i18n="sh.c4.t">Energia e Descarbonização</h3>
          <p data-i18n="sh.c4.p">Soluções para aproveitamento energético, gás associado e redução de emissões.</p>
          <span class="ch2-card-cta"><span data-i18n="sh.cta">Saber mais</span><svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </div>
      </a>
      <a href="/solucoes/procurement-e-sourcing/" class="ch2-card reveal">
        <div class="ch2-card-img has-photo" aria-hidden="true"><img src="/assets/img/19-card.jpg" alt="" loading="lazy"><div class="layer"></div><div class="vignette"></div></div>
        <div class="ch2-card-body">
          <h3 data-i18n="sh.c5.t">Procurement e Sourcing</h3>
          <p data-i18n="sh.c5.p">Identificação, seleção e aquisição de equipamentos, componentes e fornecedores.</p>
          <span class="ch2-card-cta"><span data-i18n="sh.cta">Saber mais</span><svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="section cta-final" data-theme="dark">
  <div class="container">
    <div class="cf-card reveal-img">
      <div class="cf-card-bg" aria-hidden="true">
        <div class="cf-ridge cf-ridge-l"></div>
        <div class="cf-ridge cf-ridge-r"></div>
        <div class="cf-glow"></div>
        <div class="cf-vignette"></div>
      </div>
      <div class="cf-card-inner">
        <div class="eyebrow" data-i18n="sh.cta.eyebrow">NÃO SABE POR ONDE COMEÇAR?</div>
        <h2 class="big-title reveal"><span data-i18n="sh.cta.title1">Fale connosco</span> <span class="title-dim" data-i18n="sh.cta.title2">e ajudamo-lo a encontrar a solução certa.</span></h2>
        <div class="hero-ctas reveal">
          <a href="/contactos/" class="btn btn-primary" data-i18n="sh.cta.btn">Falar com a equipa
            <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
        </div>
      </div>
    </div>
  </div>
</section>
"""

LD_JSON = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Soluções — ADPetros",
  "url": "https://www.adpetros.com/solucoes/",
  "itemListElement": [
    {"@type":"ListItem","position":1,"name":"Engenharia","url":"https://www.adpetros.com/solucoes/engenharia/"},
    {"@type":"ListItem","position":2,"name":"Implementação de Projetos","url":"https://www.adpetros.com/solucoes/implementacao-de-projetos/"},
    {"@type":"ListItem","position":3,"name":"Recuperação e Modernização de Ativos","url":"https://www.adpetros.com/solucoes/modernizacao-de-ativos/"},
    {"@type":"ListItem","position":4,"name":"Energia e Descarbonização","url":"https://www.adpetros.com/solucoes/energia-e-descarbonizacao/"},
    {"@type":"ListItem","position":5,"name":"Procurement e Sourcing","url":"https://www.adpetros.com/solucoes/procurement-e-sourcing/"}
  ]
}
</script>"""

html = build_page(
    title="Soluções — ADPetros",
    description="Conheça as soluções da ADPetros: engenharia, implementação de projetos, recuperação e modernização de ativos, energia e descarbonização, procurement e sourcing.",
    path="/solucoes/",
    active_nav="solutions",
    body_html=BODY,
    i18n_dict=I18N,
    include_hero_split=False,
    extra_js="",
    ld_json=LD_JSON,
)

write_page('solucoes/index.html', html)
