import sys
sys.path.insert(0, '/home/claude/adpetros-site/build')
from sitegen import build_page, write_page, merge_i18n, sol_steps_html, check_list_html, photo_section_html

P = "en"  # prefix

I18N = merge_i18n({
  'pt': {
    "en.hero.eyebrow": "SOLUÇÕES · ENERGIA E DESCARBONIZAÇÃO",
    "en.hero.title1": "Transformar gás",
    "en.hero.title2": "desperdiçado em recurso.",
    "en.hero.lead": "Grande parte do gás associado à produção de petróleo é queimado em flare — uma perda de energia e um fator relevante de emissões. A ADPetros desenvolve soluções técnicas para recuperar, tratar e valorizar esse gás.",
    "en.hero.cta1": "Falar sobre um projeto", "en.hero.cta2": "Ver todas as soluções",

    "en.prob.eyebrow": "O PROBLEMA",
    "en.prob.title1": "Queimar gás em flare",
    "en.prob.title2": "desperdiça energia e agrava as emissões.",
    "en.prob.p1": "Quando o gás associado não tem destino definido, a solução mais simples é queimá-lo. Isso significa perder um recurso energético com valor comercial e aumentar as emissões de CO₂ e metano da operação.",
    "en.prob.p2": "Cada vez mais, reguladores, investidores e parceiros esperam planos concretos de redução de flaring e descarbonização — não apenas intenções.",

    "en.visual.eyebrow": "VALORIZAÇÃO DE GÁS",
    "en.visual.title1": "Quando o gás é desperdiçado,",
    "en.visual.title2": "perde-se muito mais do que energia.",
    "en.visual.p1": "A ADPetros desenvolve soluções para recuperar e valorizar gás associado que seria queimado ou libertado durante a operação.",
    "en.visual.p2": "O gás recuperado pode ser tratado e utilizado para produção de energia ou outros produtos, criando valor a partir de um recurso que antes era desperdiçado e contribuindo para a redução das emissões associadas ao flaring.",
    "en.visual.tag1": "GÁS ASSOCIADO", "en.visual.tag2": "VALORIZAÇÃO",

    "en.help.eyebrow": "COMO A ADPETROS AJUDA",
    "en.help.title1": "Da avaliação do potencial",
    "en.help.title2": "à operação em contínuo.",
    "en.help.s1t": "Avaliação do potencial de gás", "en.help.s1p": "Estudamos os volumes de gás associado disponíveis e o seu potencial de aproveitamento.",
    "en.help.s2t": "Tratamento e valorização", "en.help.s2p": "Desenhamos as soluções técnicas de tratamento necessárias para tornar o gás utilizável.",
    "en.help.s3t": "Produção de energia", "en.help.s3p": "Desenvolvemos soluções para converter o gás recuperado em energia ou outros produtos de valor.",
    "en.help.s4t": "Redução de flaring e descarbonização", "en.help.s4p": "Acompanhamos a implementação e a medição da redução de emissões ao longo do tempo.",

    "en.photo.eyebrow": "UM RECURSO POR APROVEITAR",
    "en.photo.title1": "A energia já está lá",
    "en.photo.title2": "falta a estrutura para a aproveitar.",
    "en.photo.text": "É essa estrutura — técnica e operacional — que ajudamos a construir, mercado a mercado.",

    "en.inc.eyebrow": "O QUE ESTÁ INCLUÍDO",
    "en.inc.title1": "Soluções técnicas",
    "en.inc.title2": "para energia e descarbonização.",
    "en.inc1": "Valorização de gás associado", "en.inc2": "Tratamento de gás associado",
    "en.inc3": "Produção de energia", "en.inc4": "Redução de flaring",
    "en.inc5": "Descarbonização de operações", "en.inc6": "Créditos de carbono",
    "en.inc7": "Estudos de viabilidade técnica", "en.inc8": "Acompanhamento técnico da operação",

    "en.mk.text": "Esta é uma das áreas onde a nossa experiência local — sobretudo na Venezuela e em África — mais valor acrescenta a um projeto de valorização de gás.",
    "en.mk.link": "Conhecer a nossa experiência local",

    "en.cta.eyebrow": "FALE CONNOSCO",
    "en.cta.title1": "Tem gás associado ou emissões",
    "en.cta.title2": "que podem ser valorizadas?",
    "en.cta.p": "Fale com a nossa equipa técnica sobre o potencial energético da sua operação.",
    "en.cta.btn1": "Falar com a equipa", "en.cta.btn2": "Ver todas as soluções",
  },
  'en': {
    "en.hero.eyebrow": "SOLUTIONS · ENERGY & DECARBONISATION",
    "en.hero.title1": "Turning wasted gas",
    "en.hero.title2": "into a resource.",
    "en.hero.lead": "Much of the gas associated with oil production is burned in flares — a waste of energy and a significant source of emissions. ADPetros develops technical solutions to recover, treat and add value to that gas.",
    "en.hero.cta1": "Talk about a project", "en.hero.cta2": "See all solutions",

    "en.prob.eyebrow": "THE PROBLEM",
    "en.prob.title1": "Flaring gas",
    "en.prob.title2": "wastes energy and worsens emissions.",
    "en.prob.p1": "When associated gas has no defined use, the simplest solution is to burn it. That means losing an energy resource with commercial value and increasing the operation's CO₂ and methane emissions.",
    "en.prob.p2": "Increasingly, regulators, investors and partners expect concrete flaring reduction and decarbonisation plans — not just intentions.",

    "en.visual.eyebrow": "GAS VALORISATION",
    "en.visual.title1": "When gas is wasted,",
    "en.visual.title2": "much more than energy is lost.",
    "en.visual.p1": "ADPetros develops solutions to recover and add value to associated gas that would otherwise be flared or released during operations.",
    "en.visual.p2": "Recovered gas can be treated and used for energy production or other products, creating value from a resource that was previously wasted and helping reduce flaring-related emissions.",
    "en.visual.tag1": "ASSOCIATED GAS", "en.visual.tag2": "VALORISATION",

    "en.help.eyebrow": "HOW ADPETROS HELPS",
    "en.help.title1": "From potential assessment",
    "en.help.title2": "to ongoing operation.",
    "en.help.s1t": "Gas potential assessment", "en.help.s1p": "We study the volumes of associated gas available and their recovery potential.",
    "en.help.s2t": "Treatment and valorisation", "en.help.s2p": "We design the technical treatment solutions needed to make the gas usable.",
    "en.help.s3t": "Energy production", "en.help.s3p": "We develop solutions to convert recovered gas into energy or other value products.",
    "en.help.s4t": "Flaring reduction and decarbonisation", "en.help.s4p": "We follow implementation and measure emissions reduction over time.",

    "en.photo.eyebrow": "AN UNTAPPED RESOURCE",
    "en.photo.title1": "The energy is already there",
    "en.photo.title2": "what's missing is the structure to capture it.",
    "en.photo.text": "That structure — technical and operational — is what we help build, market by market.",

    "en.inc.eyebrow": "WHAT'S INCLUDED",
    "en.inc.title1": "Technical solutions",
    "en.inc.title2": "for energy and decarbonisation.",
    "en.inc1": "Associated gas valorisation", "en.inc2": "Associated gas treatment",
    "en.inc3": "Energy production", "en.inc4": "Flaring reduction",
    "en.inc5": "Operations decarbonisation", "en.inc6": "Carbon credits",
    "en.inc7": "Technical feasibility studies", "en.inc8": "Technical operations follow-up",

    "en.mk.text": "This is one of the areas where our local experience — especially in Venezuela and Africa — adds the most value to a gas valorisation project.",
    "en.mk.link": "Learn about our local experience",

    "en.cta.eyebrow": "GET IN TOUCH",
    "en.cta.title1": "Do you have associated gas or emissions",
    "en.cta.title2": "that could be valorised?",
    "en.cta.p": "Talk to our technical team about your operation's energy potential.",
    "en.cta.btn1": "Talk to the team", "en.cta.btn2": "See all solutions",
  },
  'es': {
    "en.hero.eyebrow": "SOLUCIONES · ENERGÍA Y DESCARBONIZACIÓN",
    "en.hero.title1": "Transformar gas",
    "en.hero.title2": "desperdiciado en recurso.",
    "en.hero.lead": "Gran parte del gas asociado a la producción de petróleo se quema en flare — una pérdida de energía y un factor relevante de emisiones. ADPetros desarrolla soluciones técnicas para recuperar, tratar y dar valor a ese gas.",
    "en.hero.cta1": "Hablar sobre un proyecto", "en.hero.cta2": "Ver todas las soluciones",

    "en.prob.eyebrow": "EL PROBLEMA",
    "en.prob.title1": "Quemar gas en flare",
    "en.prob.title2": "desperdicia energía y agrava las emisiones.",
    "en.prob.p1": "Cuando el gas asociado no tiene un destino definido, la solución más simple es quemarlo. Esto significa perder un recurso energético con valor comercial y aumentar las emisiones de CO₂ y metano de la operación.",
    "en.prob.p2": "Cada vez más, reguladores, inversores y socios esperan planes concretos de reducción de flaring y descarbonización — no solo intenciones.",

    "en.visual.eyebrow": "VALORIZACIÓN DE GAS",
    "en.visual.title1": "Cuando el gas se desperdicia,",
    "en.visual.title2": "se pierde mucho más que energía.",
    "en.visual.p1": "ADPetros desarrolla soluciones para recuperar y dar valor al gas asociado que sería quemado o liberado durante la operación.",
    "en.visual.p2": "El gas recuperado puede tratarse y utilizarse para producción de energía u otros productos, creando valor a partir de un recurso antes desperdiciado y contribuyendo a reducir las emisiones asociadas al flaring.",
    "en.visual.tag1": "GAS ASOCIADO", "en.visual.tag2": "VALORIZACIÓN",

    "en.help.eyebrow": "CÓMO AYUDA ADPETROS",
    "en.help.title1": "De la evaluación del potencial",
    "en.help.title2": "a la operación continua.",
    "en.help.s1t": "Evaluación del potencial de gas", "en.help.s1p": "Estudiamos los volúmenes de gas asociado disponibles y su potencial de aprovechamiento.",
    "en.help.s2t": "Tratamiento y valorización", "en.help.s2p": "Diseñamos las soluciones técnicas de tratamiento necesarias para hacer el gas utilizable.",
    "en.help.s3t": "Producción de energía", "en.help.s3p": "Desarrollamos soluciones para convertir el gas recuperado en energía u otros productos de valor.",
    "en.help.s4t": "Reducción de flaring y descarbonización", "en.help.s4p": "Acompañamos la implementación y la medición de la reducción de emisiones a lo largo del tiempo.",

    "en.photo.eyebrow": "UN RECURSO POR APROVECHAR",
    "en.photo.title1": "La energía ya está ahí",
    "en.photo.title2": "falta la estructura para aprovecharla.",
    "en.photo.text": "Esa estructura — técnica y operativa — es la que ayudamos a construir, mercado a mercado.",

    "en.inc.eyebrow": "QUÉ INCLUYE",
    "en.inc.title1": "Soluciones técnicas",
    "en.inc.title2": "para energía y descarbonización.",
    "en.inc1": "Valorización de gas asociado", "en.inc2": "Tratamiento de gas asociado",
    "en.inc3": "Producción de energía", "en.inc4": "Reducción de flaring",
    "en.inc5": "Descarbonización de operaciones", "en.inc6": "Créditos de carbono",
    "en.inc7": "Estudios de viabilidad técnica", "en.inc8": "Seguimiento técnico de la operación",

    "en.mk.text": "Esta es una de las áreas donde nuestra experiencia local — sobre todo en Venezuela y África — más valor añade a un proyecto de valorización de gas.",
    "en.mk.link": "Conocer nuestra experiencia local",

    "en.cta.eyebrow": "HABLEMOS",
    "en.cta.title1": "¿Tiene gas asociado o emisiones",
    "en.cta.title2": "que puedan valorizarse?",
    "en.cta.p": "Hable con nuestro equipo técnico sobre el potencial energético de su operación.",
    "en.cta.btn1": "Hablar con el equipo", "en.cta.btn2": "Ver todas las soluciones",
  },
})

sol_steps = sol_steps_html([
    {'n': '01', 'tkey': 'en.help.s1t', 'tdef': 'Avaliação do potencial de gás', 'pkey': 'en.help.s1p', 'pdef': 'Estudamos os volumes de gás associado disponíveis e o seu potencial de aproveitamento.'},
    {'n': '02', 'tkey': 'en.help.s2t', 'tdef': 'Tratamento e valorização', 'pkey': 'en.help.s2p', 'pdef': 'Desenhamos as soluções técnicas de tratamento necessárias para tornar o gás utilizável.'},
    {'n': '03', 'tkey': 'en.help.s3t', 'tdef': 'Produção de energia', 'pkey': 'en.help.s3p', 'pdef': 'Desenvolvemos soluções para converter o gás recuperado em energia ou outros produtos de valor.'},
    {'n': '04', 'tkey': 'en.help.s4t', 'tdef': 'Redução de flaring e descarbonização', 'pkey': 'en.help.s4p', 'pdef': 'Acompanhamos a implementação e a medição da redução de emissões ao longo do tempo.'},
], extra_style='margin-top:48px')

checklist = check_list_html([
    {'key': 'en.inc1', 'text': 'Valorização de gás associado'}, {'key': 'en.inc2', 'text': 'Tratamento de gás associado'},
    {'key': 'en.inc3', 'text': 'Produção de energia'}, {'key': 'en.inc4', 'text': 'Redução de flaring'},
    {'key': 'en.inc5', 'text': 'Descarbonização de operações'}, {'key': 'en.inc6', 'text': 'Créditos de carbono'},
    {'key': 'en.inc7', 'text': 'Estudos de viabilidade técnica'}, {'key': 'en.inc8', 'text': 'Acompanhamento técnico da operação'},
])

photo_section = photo_section_html(
    img='/assets/img/16-lg.jpg', alt='Poço de petróleo ao amanhecer, com halo solar',
    eyebrow_key='en.photo.eyebrow', eyebrow_def='UM RECURSO POR APROVEITAR',
    title1_key='en.photo.title1', title1_def='A energia já está lá',
    title2_key='en.photo.title2', title2_def='falta a estrutura para a aproveitar.',
    text_key='en.photo.text', text_def='É essa estrutura — técnica e operacional — que ajudamos a construir, mercado a mercado.',
)

BODY = f"""
<header class="hero" id="top" data-theme="dark" style="min-height:76vh">
  <div class="hero-bg"><div class="glow"></div><div class="hero-vignette"></div></div>
  <div class="hero-inner hero-inner-centered">
    <div class="eyebrow" data-i18n="en.hero.eyebrow">SOLUÇÕES · ENERGIA E DESCARBONIZAÇÃO</div>
    <h1 id="heroTitle">
      <span class="line-mask"><span class="line" data-i18n="en.hero.title1">Transformar gás</span></span>
      <span class="line-mask"><span class="line sub" data-i18n="en.hero.title2">desperdiçado em recurso.</span></span>
    </h1>
    <p class="hero-lead reveal" data-i18n="en.hero.lead">Grande parte do gás associado à produção de petróleo é queimado em flare — uma perda de energia e um fator relevante de emissões. A ADPetros desenvolve soluções técnicas para recuperar, tratar e valorizar esse gás.</p>
    <div class="hero-ctas reveal">
      <a href="/contactos/" class="btn btn-primary" data-i18n="en.hero.cta1">Falar sobre um projeto
        <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      <a href="/solucoes/" class="btn btn-ghost" data-i18n="en.hero.cta2">Ver todas as soluções</a>
    </div>
  </div>
</header>

<section class="section" data-theme="white">
  <div class="container">
    <div class="sol-two-col">
      <div>
        <div class="eyebrow" data-i18n="en.prob.eyebrow">O PROBLEMA</div>
        <h2 class="big-title reveal"><span data-i18n="en.prob.title1">Queimar gás em flare</span> <span class="title-dim" data-i18n="en.prob.title2">desperdiça energia e agrava as emissões.</span></h2>
      </div>
      <div>
        <p class="reveal dim" style="line-height:1.75;font-size:16px" data-i18n="en.prob.p1">Quando o gás associado não tem destino definido, a solução mais simples é queimá-lo. Isso significa perder um recurso energético com valor comercial e aumentar as emissões de CO₂ e metano da operação.</p>
        <p class="reveal dim" style="line-height:1.75;font-size:16px;margin-top:16px" data-i18n="en.prob.p2">Cada vez mais, reguladores, investidores e parceiros esperam planos concretos de redução de flaring e descarbonização — não apenas intenções.</p>
      </div>
    </div>
  </div>
</section>

<section class="section flare-section" data-theme="white">
  <div class="container">
    <div class="flare-grid">
      <div class="flare-visual reveal-img">
        <div class="ring r1"></div>
        <div class="ring r2"></div>
        <div class="stack"></div>
        <div class="flame-wrap">
          <div class="flame" id="flameSvg">
            <svg viewBox="0 0 120 160" fill="none">
              <path id="flamePath" d="M60 10 C30 55 20 85 35 115 C42 132 58 140 62 150 C90 140 100 112 92 85 C100 90 105 100 103 112 C118 90 112 55 92 35 C90 55 80 62 75 55 C82 40 72 18 60 10Z" fill="url(#flameGrad)"/>
              <defs>
                <linearGradient id="flameGrad" x1="60" y1="10" x2="60" y2="150" gradientUnits="userSpaceOnUse">
                  <stop offset="0" stop-color="#7395c6"/>
                  <stop offset="0.5" stop-color="#5d7391"/>
                  <stop offset="1" stop-color="#e7b84f"/>
                </linearGradient>
              </defs>
            </svg>
          </div>
        </div>
        <div class="flare-metrics">
          <span class="m-tag" data-i18n="en.visual.tag1">GÁS ASSOCIADO</span>
          <span class="m-tag" data-i18n="en.visual.tag2">VALORIZAÇÃO</span>
        </div>
      </div>

      <div class="flare-copy">
        <div class="eyebrow" data-i18n="en.visual.eyebrow">VALORIZAÇÃO DE GÁS</div>
        <h2 class="big-title reveal"><span data-i18n="en.visual.title1">Quando o gás é desperdiçado,</span> <span class="title-dim" data-i18n="en.visual.title2">perde-se muito mais do que energia.</span></h2>
        <p class="reveal" data-i18n="en.visual.p1">A ADPetros desenvolve soluções para recuperar e valorizar gás associado que seria queimado ou libertado durante a operação.</p>
        <p class="reveal" data-i18n="en.visual.p2">O gás recuperado pode ser tratado e utilizado para produção de energia ou outros produtos, criando valor a partir de um recurso que antes era desperdiçado e contribuindo para a redução das emissões associadas ao flaring.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" data-theme="dark">
  <div class="container">
    <div class="header-row">
      <div>
        <div class="eyebrow" data-i18n="en.help.eyebrow">COMO A ADPETROS AJUDA</div>
        <h2 class="big-title reveal"><span data-i18n="en.help.title1">Da avaliação do potencial</span> <span class="title-dim" data-i18n="en.help.title2">à operação em contínuo.</span></h2>
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
        <div class="eyebrow" data-i18n="en.inc.eyebrow">O QUE ESTÁ INCLUÍDO</div>
        <h2 class="big-title reveal"><span data-i18n="en.inc.title1">Soluções técnicas</span> <span class="title-dim" data-i18n="en.inc.title2">para energia e descarbonização.</span></h2>
      </div>
    </div>
    {checklist}
    <div class="sol-markets-note reveal" style="margin-top:40px">
      <svg viewBox="0 0 24 24" fill="none"><path d="M12 21s7-7.58 7-12a7 7 0 1 0-14 0c0 4.42 7 12 7 12z" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="12" cy="9" r="2.4" stroke="currentColor" stroke-width="1.6"/></svg>
      <p><span data-i18n="en.mk.text">Esta é uma das áreas onde a nossa experiência local — sobretudo na Venezuela e em África — mais valor acrescenta a um projeto de valorização de gás.</span> <a href="/sobre-nos/" data-i18n="en.mk.link" style="color:var(--accent);font-weight:600">Conhecer a nossa experiência local</a></p>
    </div>
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
        <div class="eyebrow" data-i18n="en.cta.eyebrow">FALE CONNOSCO</div>
        <h2 class="big-title reveal"><span data-i18n="en.cta.title1">Tem gás associado ou emissões</span> <span class="title-dim" data-i18n="en.cta.title2">que podem ser valorizadas?</span></h2>
        <p class="reveal" data-i18n="en.cta.p">Fale com a nossa equipa técnica sobre o potencial energético da sua operação.</p>
        <div class="hero-ctas reveal">
          <a href="/contactos/" class="btn btn-primary" data-i18n="en.cta.btn1">Falar com a equipa
            <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <a href="/solucoes/" class="btn btn-ghost" data-i18n="en.cta.btn2">Ver todas as soluções</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""

EXTRA_JS = """/* Flare flame gentle animation loop (reused from Home) */
if(document.getElementById('flamePath')){
  gsap.to('#flamePath', {
    attr:{ d:"M60 14 C34 55 22 88 34 116 C42 130 58 138 62 148 C88 138 100 110 90 84 C99 90 104 100 101 111 C118 88 110 54 90 34 C89 55 78 60 74 53 C82 38 71 20 60 14Z" },
    duration:2.6, ease:'sine.inOut', yoyo:true, repeat:-1
  });
  gsap.to('.flare-visual .ring', {
    scale:1.06, opacity:.6, duration:3, ease:'sine.inOut', yoyo:true, repeat:-1, stagger:0.4, transformOrigin:'50% 50%'
  });
}
"""

LD_JSON = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Energia e Descarbonização — ADPetros",
  "url": "https://www.adpetros.com/solucoes/energia-e-descarbonizacao/",
  "provider": {"@type":"Organization","name":"ADPetros"}
}
</script>"""

html = build_page(
    title="Energia e Descarbonização — Soluções ADPetros",
    description="Valorização de gás associado, tratamento de gás, produção de energia, redução de flaring, descarbonização e créditos de carbono.",
    path="/solucoes/energia-e-descarbonizacao/",
    active_nav="solutions",
    body_html=BODY,
    i18n_dict=I18N,
    include_hero_split=True,
    extra_js=EXTRA_JS,
    ld_json=LD_JSON,
)

write_page('solucoes/energia-e-descarbonizacao/index.html', html)
