import sys
sys.path.insert(0, '/home/claude/adpetros-site/build')
from sitegen import build_page, write_page, merge_i18n, sol_steps_html, check_list_html, photo_section_html, example_situation_html, inline_cta_html

P = "p"  # prefix

I18N = merge_i18n({
  'pt': {
    "p.hero.eyebrow": "PROCUREMENT GLOBAL E SOURCING DE SUPPLY CHAIN",
    "p.hero.title1": "Os fornecedores certos,",
    "p.hero.title2": "no local certo.",
    "p.hero.lead": "Garantir o equipamento, os componentes e os fornecedores certos é, muitas vezes, o maior obstáculo ao entrar num mercado novo. Combinamos capacidade de sourcing global com uma rede de fornecedores local já estabelecida para manter a cadeia de abastecimento do seu projeto em movimento — desde a primeira cotação até à entrega final.",
    "p.hero.cta1": "Falar sobre um projeto", "p.hero.cta2": "Ver todas as soluções",

    "p.prob.eyebrow": "O PROBLEMA",
    "p.prob.title1": "Comprar bem num mercado novo",
    "p.prob.title2": "é mais difícil sem uma rede de fornecedores já conhecida.",
    "p.prob.p1": "Encontrar fornecedores de confiança, negociar condições favoráveis e garantir prazos de entrega fiáveis é um processo lento e arriscado quando feito do zero, à distância, num mercado desconhecido.",
    "p.prob.p2": "Uma rede de procurement já testada localmente elimina essa incerteza e mantém o projeto a avançar ao ritmo necessário.",

    "p.help.eyebrow": "COMO A ADPETROS AJUDA",
    "p.help.title1": "Da identificação do fornecedor",
    "p.help.title2": "à entrega no terreno.",
    "p.help.s1t": "Identificação de fornecedores", "p.help.s1p": "Mapeamos fornecedores locais e internacionais capazes de responder às necessidades do projeto.",
    "p.help.s2t": "Seleção e qualificação", "p.help.s2p": "Avaliamos a capacidade técnica e a fiabilidade de cada fornecedor antes de o recomendar.",
    "p.help.s3t": "Aquisição e logística", "p.help.s3p": "Coordenamos a negociação, contratação e entrega dos equipamentos e componentes necessários.",

    "p.photo.eyebrow": "NO TERRENO, DESDE O INÍCIO",
    "p.photo.title1": "Décadas de operação nestes mercados",
    "p.photo.title2": "construíram uma rede de confiança que já conhece o terreno.",
    "p.photo.text": "Essa rede de fornecedores e parceiros locais trabalha para o seu projeto desde o primeiro dia, eliminando riscos de prazo antes de estes surgirem.",

    "p.inc.eyebrow": "PROCUREMENT E SOURCING DE PONTA A PONTA",
    "p.inc.title1": "Um processo de compra",
    "p.inc.title2": "coordenado do início ao fim.",
    "p.inc1": "Identificação de fornecedores locais e internacionais", "p.inc2": "Qualificação técnica rigorosa de fornecedores",
    "p.inc3": "Aquisição de equipamentos e materiais críticos", "p.inc4": "Sourcing de componentes especializados",
    "p.inc5": "Gestão da negociação, mitigação de risco e contratação", "p.inc6": "Supervisão da logística global e entrega no terreno",

    "p.ex.eyebrow": "EXEMPLO PRÁTICO", "p.ex.title": "Imagine a seguinte situação:",
    "p.ex.p": "Um projeto está parado à espera de um equipamento específico, e não há um fornecedor de confiança à vista no mercado local. Encontramos, negociamos e tratamos da logística — para o projeto não parar.",
    "p.cta.eyebrow": "FALE CONNOSCO",
    "p.cta.title1": "Precisa de equipamentos ou fornecedores",
    "p.cta.title2": "para um projeto na Venezuela?",
    "p.cta.p": "Fale com a nossa equipa sobre o que o seu projeto precisa de adquirir.",
    "p.cta.btn1": "Falar com a equipa", "p.cta.btn2": "Ver todas as soluções",
  },
  'en': {
    "p.hero.eyebrow": "GLOBAL PROCUREMENT & SUPPLY CHAIN SOURCING",
    "p.hero.title1": "The right suppliers,",
    "p.hero.title2": "in the right place.",
    "p.hero.lead": "Securing the right equipment, components, and suppliers is often the biggest bottleneck when entering a new market. We combine global sourcing capability with an established local supplier network to keep your project's supply chain moving — from first quote to final delivery.",
    "p.hero.cta1": "Talk about a project", "p.hero.cta2": "See all solutions",

    "p.prob.eyebrow": "THE PROBLEM",
    "p.prob.title1": "Buying well in a new market",
    "p.prob.title2": "is harder without an already-known supplier network.",
    "p.prob.p1": "Finding trustworthy suppliers, negotiating favorable terms, and securing reliable delivery timelines is slow and risky when it's done from scratch, from a distance, in an unfamiliar market.",
    "p.prob.p2": "An already-proven local procurement network removes that uncertainty and keeps the project moving at the pace it needs.",

    "p.help.eyebrow": "HOW ADPETROS HELPS",
    "p.help.title1": "From supplier identification",
    "p.help.title2": "to delivery on the ground.",
    "p.help.s1t": "Supplier identification", "p.help.s1p": "We map local and international suppliers able to meet the project's needs.",
    "p.help.s2t": "Selection and qualification", "p.help.s2p": "We assess each supplier's technical capacity and reliability before recommending them.",
    "p.help.s3t": "Acquisition and logistics", "p.help.s3p": "We coordinate negotiation, contracting and delivery of the equipment and components needed.",

    "p.photo.eyebrow": "ON THE GROUND, FROM DAY ONE",
    "p.photo.title1": "Decades of operations in these markets",
    "p.photo.title2": "built a trusted network that already knows the ground.",
    "p.photo.text": "That network of local suppliers and partners works for your project from day one, eliminating lead-time risks before they start.",

    "p.inc.eyebrow": "END-TO-END PROCUREMENT & SOURCING",
    "p.inc.title1": "A purchasing process",
    "p.ex.eyebrow": "PRACTICAL EXAMPLE", "p.ex.title": "Imagine the following situation:",
    "p.ex.p": "A project is stalled waiting for a specific piece of equipment, and there's no trusted supplier in sight on the local market. We find, negotiate and handle the logistics — so the project doesn't stop.",
    "p.inc.title2": "coordinated from start to finish.",
    "p.inc1": "Identifying local and international suppliers", "p.inc2": "Qualifying suppliers on strict technical standards",
    "p.inc3": "Procuring critical equipment and materials", "p.inc4": "Sourcing specialized components",
    "p.inc5": "Managing negotiation, risk mitigation, and contracting", "p.inc6": "Overseeing global logistics and field delivery",

    "p.cta.eyebrow": "GET IN TOUCH",
    "p.cta.title1": "Need equipment or suppliers",
    "p.cta.title2": "for a project in Venezuela?",
    "p.cta.p": "Talk to our team about what your project needs to acquire.",
    "p.cta.btn1": "Talk to the team", "p.cta.btn2": "See all solutions",
  },
  'es': {
    "p.hero.eyebrow": "PROCUREMENT GLOBAL Y SOURCING DE SUPPLY CHAIN",
    "p.hero.title1": "Los proveedores correctos,",
    "p.hero.title2": "en el lugar correcto.",
    "p.hero.lead": "Garantizar el equipo, los componentes y los proveedores adecuados es, a menudo, el mayor obstáculo al entrar en un mercado nuevo. Combinamos capacidad de sourcing global con una red de proveedores local ya establecida para mantener en movimiento la cadena de suministro de su proyecto — desde la primera cotización hasta la entrega final.",
    "p.hero.cta1": "Hablar sobre un proyecto", "p.hero.cta2": "Ver todas las soluciones",

    "p.prob.eyebrow": "EL PROBLEMA",
    "p.prob.title1": "Comprar bien en un mercado nuevo",
    "p.prob.title2": "es más difícil sin una red de proveedores ya conocida.",
    "p.prob.p1": "Encontrar proveedores de confianza, negociar condiciones favorables y garantizar plazos de entrega fiables es un proceso lento y arriesgado cuando se hace desde cero, a distancia, en un mercado desconocido.",
    "p.prob.p2": "Una red de procurement ya probada localmente elimina esa incertidumbre y mantiene el proyecto avanzando al ritmo necesario.",

    "p.help.eyebrow": "CÓMO AYUDA ADPETROS",
    "p.help.title1": "De la identificación del proveedor",
    "p.help.title2": "a la entrega en el terreno.",
    "p.help.s1t": "Identificación de proveedores", "p.help.s1p": "Mapeamos proveedores locales e internacionales capaces de responder a las necesidades del proyecto.",
    "p.help.s2t": "Selección y calificación", "p.help.s2p": "Evaluamos la capacidad técnica y la fiabilidad de cada proveedor antes de recomendarlo.",
    "p.help.s3t": "Adquisición y logística", "p.help.s3p": "Coordinamos la negociación, contratación y entrega de los equipos y componentes necesarios.",

    "p.photo.eyebrow": "EN EL TERRENO, DESDE EL PRINCIPIO",
    "p.photo.title1": "Décadas de operación en estos mercados",
    "p.ex.eyebrow": "EJEMPLO PRÁCTICO", "p.ex.title": "Imagine la siguiente situación:",
    "p.ex.p": "Un proyecto está parado esperando un equipo específico, y no hay un proveedor de confianza a la vista en el mercado local. Lo encontramos, lo negociamos y gestionamos la logística — para que el proyecto no se detenga.",
    "p.photo.title2": "crearon una red de confianza que ya conoce el terreno.",
    "p.photo.text": "Esa red de proveedores y socios locales trabaja para su proyecto desde el primer día, eliminando riesgos de plazo antes de que surjan.",

    "p.inc.eyebrow": "PROCUREMENT Y SOURCING DE EXTREMO A EXTREMO",
    "p.inc.title1": "Un proceso de compra",
    "p.inc.title2": "coordinado de principio a fin.",
    "p.inc1": "Identificación de proveedores locales e internacionales", "p.inc2": "Calificación técnica rigurosa de proveedores",
    "p.inc3": "Adquisición de equipos y materiales críticos", "p.inc4": "Sourcing de componentes especializados",
    "p.inc5": "Gestión de la negociación, mitigación de riesgos y contratación", "p.inc6": "Supervisión de la logística global y entrega en el terreno",

    "p.cta.eyebrow": "HABLEMOS",
    "p.cta.title1": "¿Necesita equipos o proveedores",
    "p.cta.title2": "para un proyecto en Venezuela?",
    "p.cta.p": "Hable con nuestro equipo sobre lo que su proyecto necesita adquirir.",
    "p.cta.btn1": "Hablar con el equipo", "p.cta.btn2": "Ver todas las soluciones",
  },
})

sol_steps = sol_steps_html([
    {'n': '01', 'tkey': 'p.help.s1t', 'tdef': 'Identificação de fornecedores', 'pkey': 'p.help.s1p', 'pdef': 'Mapeamos fornecedores locais e internacionais capazes de responder às necessidades do projeto.'},
    {'n': '02', 'tkey': 'p.help.s2t', 'tdef': 'Seleção e qualificação', 'pkey': 'p.help.s2p', 'pdef': 'Avaliamos a capacidade técnica e a fiabilidade de cada fornecedor antes de o recomendar.'},
    {'n': '03', 'tkey': 'p.help.s3t', 'tdef': 'Aquisição e logística', 'pkey': 'p.help.s3p', 'pdef': 'Coordenamos a negociação, contratação e entrega dos equipamentos e componentes necessários.'},
], extra_style='margin-top:48px')

checklist = check_list_html([
    {'key': 'p.inc1', 'text': 'Identificação de fornecedores locais e internacionais'}, {'key': 'p.inc2', 'text': 'Qualificação técnica rigorosa de fornecedores'},
    {'key': 'p.inc3', 'text': 'Aquisição de equipamentos e materiais críticos'}, {'key': 'p.inc4', 'text': 'Sourcing de componentes especializados'},
    {'key': 'p.inc5', 'text': 'Gestão da negociação, mitigação de risco e contratação'}, {'key': 'p.inc6', 'text': 'Supervisão da logística global e entrega no terreno'},
])

photo_section = photo_section_html(
    img='/assets/img/new/h5.jpg', alt='Equipa técnica a inspecionar equipamento industrial de perto',
    eyebrow_key='p.photo.eyebrow', eyebrow_def='NO TERRENO, DESDE O INÍCIO',
    title1_key='p.photo.title1', title1_def='Décadas de operação nestes mercados',
    title2_key='p.photo.title2', title2_def='construíram uma rede de confiança que já conhece o terreno.',
    text_key='p.photo.text', text_def='Essa rede de fornecedores e parceiros locais trabalha para o seu projeto desde o primeiro dia, eliminando riscos de prazo antes de estes surgirem.',
)

example_html = example_situation_html(
    prefix='p', eyebrow_def='EXEMPLO PRÁTICO', title_def='Imagine a seguinte situação:',
    text_def='Um projeto está parado à espera de um equipamento específico, e não há um fornecedor de confiança à vista no mercado local. Encontramos, negociamos e tratamos da logística — para o projeto não parar.',
    img='/assets/img/14-lg.jpg', alt='Plataforma industrial à espera de equipamento',
    cta_href='/contactos/', cta_key='cta.project', cta_def='Falar sobre o meu projeto',
)
BODY = f"""
<header class="hero" id="top" data-theme="dark">
  <div class="hero-bg"><img src="/assets/img/19-lg.jpg" alt="Tubagens e válvulas industriais" loading="eager"><div class="glow"></div><div class="hero-vignette"></div></div>
  <div class="hero-inner hero-inner-centered">
    <div class="eyebrow" data-i18n="p.hero.eyebrow">PROCUREMENT GLOBAL E SOURCING DE SUPPLY CHAIN</div>
    <h1 id="heroTitle">
      <span class="line-mask"><span class="line" data-i18n="p.hero.title1">Os fornecedores certos,</span></span>
      <span class="line-mask"><span class="line sub" data-i18n="p.hero.title2">no local certo.</span></span>
    </h1>
    <p class="hero-lead" data-i18n="p.hero.lead">Garantir o equipamento, os componentes e os fornecedores certos é, muitas vezes, o maior obstáculo ao entrar num mercado novo. Combinamos capacidade de sourcing global com uma rede de fornecedores local já estabelecida para manter a cadeia de abastecimento do seu projeto em movimento — desde a primeira cotação até à entrega final.</p>
    <div class="hero-ctas">
      <a href="/contactos/" class="btn btn-primary" data-i18n="p.hero.cta1">Falar sobre um projeto
        <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      <a href="/solucoes/" class="btn btn-ghost" data-i18n="p.hero.cta2">Ver todas as soluções</a>
    </div>
  </div>
</header>

<section class="section" data-theme="white">
  <div class="container">
    <div class="prob-grid">
      <div class="prob-copy">
        <div class="eyebrow" data-i18n="p.prob.eyebrow">O PROBLEMA</div>
        <h2 class="big-title reveal"><span data-i18n="p.prob.title1">Comprar bem num mercado novo</span> <span class="title-dim" data-i18n="p.prob.title2">é mais difícil sem uma rede de fornecedores já conhecida.</span></h2>
        <p class="reveal dim prob-p" data-i18n="p.prob.p1">Encontrar fornecedores de confiança, negociar condições favoráveis e garantir prazos de entrega fiáveis é um processo lento e arriscado quando feito do zero, à distância, num mercado desconhecido.</p>
        <p class="reveal dim prob-p" data-i18n="p.prob.p2">Uma rede de procurement já testada localmente elimina essa incerteza e mantém o projeto a avançar ao ritmo necessário.</p>
      </div>
      <div class="prob-photo reveal-img"><img src="/assets/img/new/v11.jpg" alt="Dois técnicos sobre carris a apontar para uma refinaria ao entardecer" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="section" data-theme="dark">
  <div class="container">
    <div class="header-row">
      <div>
        <div class="eyebrow" data-i18n="p.help.eyebrow">COMO A ADPETROS AJUDA</div>
        <h2 class="big-title reveal"><span data-i18n="p.help.title1">Da identificação do fornecedor</span> <span class="title-dim" data-i18n="p.help.title2">à entrega no terreno.</span></h2>
      </div>
    </div>
{sol_steps}
{inline_cta_html()}
  </div>
</section>

{photo_section}

<section class="section" data-theme="white">
  <div class="container">
    <div class="header-row">
      <div>
        <div class="eyebrow" data-i18n="p.inc.eyebrow">PROCUREMENT E SOURCING DE PONTA A PONTA</div>
        <h2 class="big-title reveal"><span data-i18n="p.inc.title1">Um processo de compra</span> <span class="title-dim" data-i18n="p.inc.title2">coordenado do início ao fim.</span></h2>
      </div>
    </div>
    {checklist}
{inline_cta_html(key='cta.talk', default='Fale connosco')}
  </div>
</section>

{example_html}

<section class="section cta-final" data-theme="dark">
  <div class="container">
    <div class="cf-card reveal-img">
      <div class="cf-card-bg" aria-hidden="true">
        <div class="cf-ridge cf-ridge-l"></div><div class="cf-ridge cf-ridge-r"></div>
        <div class="cf-glow"></div><div class="cf-vignette"></div>
      </div>
      <div class="cf-card-inner">
        <div class="eyebrow" data-i18n="p.cta.eyebrow">FALE CONNOSCO</div>
        <h2 class="big-title reveal"><span data-i18n="p.cta.title1">Precisa de equipamentos ou fornecedores</span> <span class="title-dim" data-i18n="p.cta.title2">para um projeto na Venezuela?</span></h2>
        <p class="reveal" data-i18n="p.cta.p">Fale com a nossa equipa sobre o que o seu projeto precisa de adquirir.</p>
        <div class="hero-ctas reveal">
          <a href="/contactos/" class="btn btn-primary" data-i18n="p.cta.btn1">Falar com a equipa
            <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <a href="/solucoes/" class="btn btn-ghost" data-i18n="p.cta.btn2">Ver todas as soluções</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""

LD_JSON = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Procurement & Sourcing — ADPETROS",
  "url": "https://www.adpetros.com/solucoes/procurement-e-sourcing/",
  "provider": {"@type":"Organization","name":"ADPETROS"}
}
</script>"""

html = build_page(
    title="Procurement & Sourcing — ADPETROS Solutions",
    description="Identification, selection and acquisition of equipment, components, suppliers and services for industrial projects.",
    path="/solucoes/procurement-e-sourcing/",
    active_nav="solutions",
    body_html=BODY,
    i18n_dict=I18N,
    include_hero_split=True,
    extra_js="",
    ld_json=LD_JSON,
)

write_page('solucoes/procurement-e-sourcing/index.html', html)
