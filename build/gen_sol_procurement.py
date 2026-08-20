import sys
sys.path.insert(0, '/home/claude/adpetros-site/build')
from sitegen import build_page, write_page, merge_i18n, sol_steps_html, check_list_html, photo_section_html

P = "p"  # prefix

I18N = merge_i18n({
  'pt': {
    "p.hero.eyebrow": "SOLUÇÕES · PROCUREMENT E SOURCING",
    "p.hero.title1": "Os fornecedores certos,",
    "p.hero.title2": "no local certo.",
    "p.hero.lead": "Identificamos, selecionamos e adquirimos os equipamentos, componentes, fornecedores e serviços necessários para o seu projeto avançar, com a rede de contactos que já construímos nos mercados onde atuamos.",
    "p.hero.cta1": "Falar sobre um projeto", "p.hero.cta2": "Ver todas as soluções",

    "p.prob.eyebrow": "O PROBLEMA",
    "p.prob.title1": "Comprar bem num mercado novo",
    "p.prob.title2": "é mais difícil sem uma rede de fornecedores já conhecida.",
    "p.prob.p1": "Encontrar fornecedores fiáveis, negociar condições e garantir prazos de entrega é um trabalho moroso e arriscado quando é feito do zero, à distância.",
    "p.prob.p2": "Uma rede de procurement já testada localmente reduz esse risco e acelera o projeto.",

    "p.help.eyebrow": "COMO A ADPETROS AJUDA",
    "p.help.title1": "Da identificação do fornecedor",
    "p.help.title2": "à entrega no terreno.",
    "p.help.s1t": "Identificação de fornecedores", "p.help.s1p": "Mapeamos fornecedores locais e internacionais capazes de responder às necessidades do projeto.",
    "p.help.s2t": "Seleção e qualificação", "p.help.s2p": "Avaliamos a capacidade técnica e a fiabilidade de cada fornecedor antes de o recomendar.",
    "p.help.s3t": "Aquisição e logística", "p.help.s3p": "Coordenamos a negociação, contratação e entrega dos equipamentos e componentes necessários.",

    "p.photo.eyebrow": "NO TERRENO, DESDE O INÍCIO",
    "p.photo.title1": "Décadas de operação nestes mercados",
    "p.photo.title2": "criaram uma rede que já conhece o terreno.",
    "p.photo.text": "Essa rede de fornecedores e parceiros locais está ao serviço do seu projeto, desde o primeiro pedido de cotação.",

    "p.inc.eyebrow": "O QUE ESTÁ INCLUÍDO",
    "p.inc.title1": "Um processo de compra",
    "p.inc.title2": "coordenado do início ao fim.",
    "p.inc1": "Identificação de fornecedores locais e internacionais", "p.inc2": "Qualificação técnica de fornecedores",
    "p.inc3": "Aquisição de equipamentos", "p.inc4": "Aquisição de componentes",
    "p.inc5": "Negociação e contratação", "p.inc6": "Logística e entrega",

    "p.cta.eyebrow": "FALE CONNOSCO",
    "p.cta.title1": "Precisa de equipamentos, componentes",
    "p.cta.title2": "ou fornecedores para o seu projeto?",
    "p.cta.p": "Fale com a nossa equipa sobre o que o seu projeto precisa de adquirir.",
    "p.cta.btn1": "Falar com a equipa", "p.cta.btn2": "Ver todas as soluções",
  },
  'en': {
    "p.hero.eyebrow": "SOLUTIONS · PROCUREMENT & SOURCING",
    "p.hero.title1": "The right suppliers,",
    "p.hero.title2": "in the right place.",
    "p.hero.lead": "We identify, select and acquire the equipment, components, suppliers and services your project needs to move forward, using the network we've already built in the markets where we operate.",
    "p.hero.cta1": "Talk about a project", "p.hero.cta2": "See all solutions",

    "p.prob.eyebrow": "THE PROBLEM",
    "p.prob.title1": "Buying well in a new market",
    "p.prob.title2": "is harder without an already-known supplier network.",
    "p.prob.p1": "Finding reliable suppliers, negotiating terms and securing delivery times is slow and risky when done from scratch, remotely.",
    "p.prob.p2": "An already-tested local procurement network reduces that risk and speeds up the project.",

    "p.help.eyebrow": "HOW ADPETROS HELPS",
    "p.help.title1": "From supplier identification",
    "p.help.title2": "to delivery on the ground.",
    "p.help.s1t": "Supplier identification", "p.help.s1p": "We map local and international suppliers able to meet the project's needs.",
    "p.help.s2t": "Selection and qualification", "p.help.s2p": "We assess each supplier's technical capacity and reliability before recommending them.",
    "p.help.s3t": "Acquisition and logistics", "p.help.s3p": "We coordinate negotiation, contracting and delivery of the equipment and components needed.",

    "p.photo.eyebrow": "ON THE GROUND, FROM DAY ONE",
    "p.photo.title1": "Decades operating in these markets",
    "p.photo.title2": "built a network that already knows the ground.",
    "p.photo.text": "That network of local suppliers and partners is at your project's service, from the very first quote request.",

    "p.inc.eyebrow": "WHAT'S INCLUDED",
    "p.inc.title1": "A purchasing process",
    "p.inc.title2": "coordinated from start to finish.",
    "p.inc1": "Identification of local and international suppliers", "p.inc2": "Technical qualification of suppliers",
    "p.inc3": "Equipment acquisition", "p.inc4": "Component acquisition",
    "p.inc5": "Negotiation and contracting", "p.inc6": "Logistics and delivery",

    "p.cta.eyebrow": "GET IN TOUCH",
    "p.cta.title1": "Do you need equipment, components",
    "p.cta.title2": "or suppliers for your project?",
    "p.cta.p": "Talk to our team about what your project needs to acquire.",
    "p.cta.btn1": "Talk to the team", "p.cta.btn2": "See all solutions",
  },
  'es': {
    "p.hero.eyebrow": "SOLUCIONES · PROCUREMENT Y SOURCING",
    "p.hero.title1": "Los proveedores correctos,",
    "p.hero.title2": "en el lugar correcto.",
    "p.hero.lead": "Identificamos, seleccionamos y adquirimos los equipos, componentes, proveedores y servicios que su proyecto necesita para avanzar, con la red de contactos que ya hemos construido en los mercados donde operamos.",
    "p.hero.cta1": "Hablar sobre un proyecto", "p.hero.cta2": "Ver todas las soluciones",

    "p.prob.eyebrow": "EL PROBLEMA",
    "p.prob.title1": "Comprar bien en un mercado nuevo",
    "p.prob.title2": "es más difícil sin una red de proveedores ya conocida.",
    "p.prob.p1": "Encontrar proveedores fiables, negociar condiciones y garantizar plazos de entrega es un trabajo lento y arriesgado cuando se hace desde cero, a distancia.",
    "p.prob.p2": "Una red de procurement ya probada localmente reduce ese riesgo y acelera el proyecto.",

    "p.help.eyebrow": "CÓMO AYUDA ADPETROS",
    "p.help.title1": "De la identificación del proveedor",
    "p.help.title2": "a la entrega en el terreno.",
    "p.help.s1t": "Identificación de proveedores", "p.help.s1p": "Mapeamos proveedores locales e internacionales capaces de responder a las necesidades del proyecto.",
    "p.help.s2t": "Selección y calificación", "p.help.s2p": "Evaluamos la capacidad técnica y la fiabilidad de cada proveedor antes de recomendarlo.",
    "p.help.s3t": "Adquisición y logística", "p.help.s3p": "Coordinamos la negociación, contratación y entrega de los equipos y componentes necesarios.",

    "p.photo.eyebrow": "EN EL TERRENO, DESDE EL PRINCIPIO",
    "p.photo.title1": "Décadas de operación en estos mercados",
    "p.photo.title2": "crearon una red que ya conoce el terreno.",
    "p.photo.text": "Esa red de proveedores y socios locales está al servicio de su proyecto, desde la primera solicitud de cotización.",

    "p.inc.eyebrow": "QUÉ INCLUYE",
    "p.inc.title1": "Un proceso de compra",
    "p.inc.title2": "coordinado de principio a fin.",
    "p.inc1": "Identificación de proveedores locales e internacionales", "p.inc2": "Calificación técnica de proveedores",
    "p.inc3": "Adquisición de equipos", "p.inc4": "Adquisición de componentes",
    "p.inc5": "Negociación y contratación", "p.inc6": "Logística y entrega",

    "p.cta.eyebrow": "HABLEMOS",
    "p.cta.title1": "¿Necesita equipos, componentes",
    "p.cta.title2": "o proveedores para su proyecto?",
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
    {'key': 'p.inc1', 'text': 'Identificação de fornecedores locais e internacionais'}, {'key': 'p.inc2', 'text': 'Qualificação técnica de fornecedores'},
    {'key': 'p.inc3', 'text': 'Aquisição de equipamentos'}, {'key': 'p.inc4', 'text': 'Aquisição de componentes'},
    {'key': 'p.inc5', 'text': 'Negociação e contratação'}, {'key': 'p.inc6', 'text': 'Logística e entrega'},
])

photo_section = photo_section_html(
    img='/assets/img/8-lg.jpg', alt='Poços de petróleo ao pôr-do-sol',
    eyebrow_key='p.photo.eyebrow', eyebrow_def='NO TERRENO, DESDE O INÍCIO',
    title1_key='p.photo.title1', title1_def='Décadas de operação nestes mercados',
    title2_key='p.photo.title2', title2_def='criaram uma rede que já conhece o terreno.',
    text_key='p.photo.text', text_def='Essa rede de fornecedores e parceiros locais está ao serviço do seu projeto, desde o primeiro pedido de cotação.',
)

BODY = f"""
<header class="hero" id="top" data-theme="dark" style="min-height:76vh">
  <div class="hero-bg"><div class="glow"></div><div class="hero-vignette"></div></div>
  <div class="hero-inner hero-inner-centered">
    <div class="eyebrow" data-i18n="p.hero.eyebrow">SOLUÇÕES · PROCUREMENT E SOURCING</div>
    <h1 id="heroTitle">
      <span class="line-mask"><span class="line" data-i18n="p.hero.title1">Os fornecedores certos,</span></span>
      <span class="line-mask"><span class="line sub" data-i18n="p.hero.title2">no local certo.</span></span>
    </h1>
    <p class="hero-lead reveal" data-i18n="p.hero.lead">Identificamos, selecionamos e adquirimos os equipamentos, componentes, fornecedores e serviços necessários para o seu projeto avançar, com a rede de contactos que já construímos nos mercados onde atuamos.</p>
    <div class="hero-ctas reveal">
      <a href="/contactos/" class="btn btn-primary" data-i18n="p.hero.cta1">Falar sobre um projeto
        <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      <a href="/solucoes/" class="btn btn-ghost" data-i18n="p.hero.cta2">Ver todas as soluções</a>
    </div>
  </div>
</header>

<section class="section" data-theme="white">
  <div class="container">
    <div class="sol-two-col">
      <div>
        <div class="eyebrow" data-i18n="p.prob.eyebrow">O PROBLEMA</div>
        <h2 class="big-title reveal"><span data-i18n="p.prob.title1">Comprar bem num mercado novo</span> <span class="title-dim" data-i18n="p.prob.title2">é mais difícil sem uma rede de fornecedores já conhecida.</span></h2>
      </div>
      <div>
        <p class="reveal dim" style="line-height:1.75;font-size:16px" data-i18n="p.prob.p1">Encontrar fornecedores fiáveis, negociar condições e garantir prazos de entrega é um trabalho moroso e arriscado quando é feito do zero, à distância.</p>
        <p class="reveal dim" style="line-height:1.75;font-size:16px;margin-top:16px" data-i18n="p.prob.p2">Uma rede de procurement já testada localmente reduz esse risco e acelera o projeto.</p>
      </div>
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
  </div>
</section>

{photo_section}

<section class="section" data-theme="white">
  <div class="container">
    <div class="header-row">
      <div>
        <div class="eyebrow" data-i18n="p.inc.eyebrow">O QUE ESTÁ INCLUÍDO</div>
        <h2 class="big-title reveal"><span data-i18n="p.inc.title1">Um processo de compra</span> <span class="title-dim" data-i18n="p.inc.title2">coordenado do início ao fim.</span></h2>
      </div>
    </div>
    {checklist}
  </div>
</section>

<section class="section cta-final" data-theme="dark">
  <div class="container">
    <div class="cf-card reveal-img">
      <div class="cf-card-bg" aria-hidden="true">
        <div class="cf-ridge cf-ridge-l"></div><div class="cf-ridge cf-ridge-r"></div>
        <div class="cf-glow"></div><div class="cf-vignette"></div>
      </div>
      <div class="cf-card-inner">
        <div class="eyebrow" data-i18n="p.cta.eyebrow">FALE CONNOSCO</div>
        <h2 class="big-title reveal"><span data-i18n="p.cta.title1">Precisa de equipamentos, componentes</span> <span class="title-dim" data-i18n="p.cta.title2">ou fornecedores para o seu projeto?</span></h2>
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
  "name": "Procurement e Sourcing — ADPetros",
  "url": "https://www.adpetros.com/solucoes/procurement-e-sourcing/",
  "provider": {"@type":"Organization","name":"ADPetros"}
}
</script>"""

html = build_page(
    title="Procurement e Sourcing — Soluções ADPetros",
    description="Identificação, seleção e aquisição de equipamentos, componentes, fornecedores e serviços para projetos industriais.",
    path="/solucoes/procurement-e-sourcing/",
    active_nav="solutions",
    body_html=BODY,
    i18n_dict=I18N,
    include_hero_split=True,
    extra_js="",
    ld_json=LD_JSON,
)

write_page('solucoes/procurement-e-sourcing/index.html', html)
