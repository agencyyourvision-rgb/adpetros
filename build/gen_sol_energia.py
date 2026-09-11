import sys
sys.path.insert(0, '/home/claude/adpetros-site/build')
from sitegen import build_page, write_page, merge_i18n, sol_steps_html, check_list_html, photo_section_html, example_situation_html, inline_cta_html

P = "en"  # prefix

I18N = merge_i18n({
  'pt': {
    "en.hero.eyebrow": "SOLUÇÕES · ENERGIA E DESCARBONIZAÇÃO",
    "en.hero.title1": "TRANSFORMAR GÁS DESPERDIÇADO",
    "en.hero.title2": "NUM RECURSO ESTRATÉGICO.",
    "en.hero.lead": "Queimar gás associado em flare não é apenas um passivo ambiental — é uma perda contínua de valor comercial. Os nossos Flare Gas Recovery Systems (FGRS) captam esse gás antes de chegar à tocha, tratando-o para que possa ser reintroduzido num uso produtivo em vez de ser queimado.",
    "en.hero.lead2": "Da avaliação de viabilidade ao desenho e implementação do sistema, ajudamos os operadores a transformar um encargo regulatório e ambiental numa fonte funcional de energia e receita.",
    "en.hero.cta1": "Falar sobre um projeto", "en.hero.cta2": "Ver todas as soluções",

    "en.prob.eyebrow": "O PROBLEMA",
    "en.prob.title1": "Queimar gás em flare",
    "en.prob.title2": "desperdiça energia e aumenta as emissões de gases com efeito de estufa.",
    "en.prob.p1": "Quando o gás associado não tem um destino definido, a solução mais simples é queimá-lo em flare. Isso significa perder um recurso com valor comercial real e aumentar a pegada de emissões de CO₂ e metano da operação.",
    "en.prob.p2": "Cada vez mais, reguladores, investidores e parceiros esperam planos mensuráveis de redução de flaring e descarbonização — não apenas intenções declaradas.",

    "en.visual.eyebrow": "VALORIZAÇÃO DE GÁS",
    "en.visual.title1": "Quando o gás é desperdiçado,",
    "en.visual.title2": "perde-se muito mais do que energia.",
    "en.visual.p1": "A ADPETROS desenvolve soluções para recuperar e valorizar gás associado que, de outra forma, seria queimado ou libertado durante a operação.",
    "en.visual.sub": "Onde o gás recuperado pode ser aproveitado:",
    "en.visual.li1": "Sistemas de geração de energia no local",
    "en.visual.li2": "Redes locais de distribuição por gasoduto",
    "en.visual.li3": "Matérias-primas petroquímicas comerciais",
    "en.visual.p2": "Transformar esse gás numa destas soluções cria valor a partir de um recurso que antes era desperdiçado, ao mesmo tempo que reduz diretamente as emissões associadas ao flaring.",
    "en.visual.tag1": "GERAÇÃO NO LOCAL", "en.visual.tag2": "REDE DE DISTRIBUIÇÃO",
    "en.visual.caption": "Exemplo ilustrativo de um sistema de geração e distribuição de energia no local.",

    "en.help.eyebrow": "COMO A ADPETROS AJUDA",
    "en.help.title1": "Da avaliação do potencial",
    "en.help.title2": "à operação em contínuo.",
    "en.help.s1t": "Avaliação do potencial de gás", "en.help.s1p": "Estudamos os volumes de gás associado disponíveis e o seu potencial de aproveitamento.",
    "en.help.s2t": "Tratamento e valorização", "en.help.s2p": "Desenhamos as soluções técnicas de tratamento necessárias para tornar o gás utilizável.",
    "en.help.s3t": "Produção de energia", "en.help.s3p": "Desenvolvemos soluções para converter o gás recuperado em energia ou outros produtos de valor.",
    "en.help.s4t": "Redução de flaring e descarbonização", "en.help.s4p": "Acompanhamos a implementação e a medição da redução de emissões ao longo do tempo.",

    "en.photo.eyebrow": "UM RECURSO POR APROVEITAR",
    "en.photo.title1": "A energia já está lá.",
    "en.photo.title2": "Falta a estrutura para a aproveitar.",
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

    "en.ex.eyebrow": "EXEMPLO PRÁTICO", "en.ex.title": "Imagine a seguinte situação:",
    "en.ex.p": "Há gás a ser queimado numa operação, e ninguém quantificou com precisão quanto valor está a perder-se. Ajudamos a medir com precisão esse potencial latente, transformando um dispendioso fluxo de resíduo ambiental numa fonte de receita estável.",
    "en.cta.eyebrow": "FALE CONNOSCO",
    "en.cta.title1": "Tem gás associado num projeto na Venezuela",
    "en.cta.title2": "que pode estar a perder valor?",
    "en.cta.p": "Fale com a nossa equipa técnica sobre o potencial energético da sua operação.",
    "en.cta.btn1": "Falar com a equipa", "en.cta.btn2": "Ver todas as soluções",
  },
  'en': {
    "en.hero.eyebrow": "SOLUTIONS · ENERGY & DECARBONISATION",
    "en.hero.title1": "TURNING WASTED GAS",
    "en.hero.title2": "INTO A STRATEGIC RESOURCE.",
    "en.hero.lead": "Flaring associated gas isn't just an environmental liability — it's a continuous loss of commercial value. Our Flare Gas Recovery Systems (FGRS) capture that gas before it reaches the flare, treating it so it can be reintroduced into productive use instead of being burned off.",
    "en.hero.lead2": "From feasibility assessment to system design and implementation, we help operators turn a regulatory and environmental burden into a functioning source of energy and revenue.",
    "en.hero.cta1": "Talk about a project", "en.hero.cta2": "See all solutions",

    "en.prob.eyebrow": "THE PROBLEM",
    "en.prob.title1": "Flaring gas",
    "en.prob.title2": "wastes energy and increases greenhouse gas emissions.",
    "en.prob.p1": "When associated gas has no defined destination, flaring becomes the default choice. That means losing a resource with real commercial value while adding to the operation's CO₂ and methane emissions footprint.",
    "en.prob.p2": "Increasingly, regulators, investors and partners expect measurable flaring-reduction and decarbonisation plans — not just stated intentions.",

    "en.visual.eyebrow": "GAS VALORISATION",
    "en.visual.title1": "Capturing lost energy &",
    "en.visual.title2": "generating new revenue.",
    "en.visual.p1": "Routine flaring and venting throw away valuable market assets. We design turnkey systems to recover associated gas directly at the source.",
    "en.visual.sub": "Treating it for immediate integration into:",
    "en.visual.li1": "On-site power generation systems",
    "en.visual.li2": "Local pipeline distribution networks",
    "en.visual.li3": "Commercial petrochemical feedstocks",
    "en.visual.p2": "Our engineered solutions simultaneously mitigate your carbon footprint and recover trapped asset value while protecting the environment and people's health.",
    "en.visual.tag1": "ON-SITE GENERATION", "en.visual.tag2": "DISTRIBUTION NETWORK",
    "en.visual.caption": "Illustrative example of an on-site power generation and distribution system.",

    "en.help.eyebrow": "HOW ADPETROS HELPS",
    "en.help.title1": "From potential assessment",
    "en.help.title2": "to ongoing operation.",
    "en.help.s1t": "Gas potential assessment", "en.help.s1p": "We study the volumes of associated gas available and their recovery potential.",
    "en.help.s2t": "Treatment and valorisation", "en.help.s2p": "We design the technical treatment solutions needed to make the gas usable.",
    "en.help.s3t": "Energy production", "en.help.s3p": "We develop solutions to convert recovered gas into energy or other value products.",
    "en.help.s4t": "Flaring reduction and decarbonisation", "en.help.s4p": "We follow implementation and measure emissions reduction over time.",

    "en.photo.eyebrow": "AN UNTAPPED RESOURCE",
    "en.photo.title1": "The energy is already there.",
    "en.photo.title2": "What's missing is the structure to capture it.",
    "en.photo.text": "That structure — technical and operational — is what we help build, market by market.",

    "en.inc.eyebrow": "WHAT'S INCLUDED",
    "en.inc.title1": "Technical solutions",
    "en.inc.title2": "for energy and decarbonisation.",
    "en.inc1": "Associated gas valorisation", "en.inc2": "Associated gas treatment",
    "en.inc3": "Energy production", "en.inc4": "Flaring reduction",
    "en.inc5": "Operations decarbonisation", "en.inc6": "Carbon credits",
    "en.ex.eyebrow": "PRACTICAL EXAMPLE", "en.ex.title": "Consider this scenario:",
    "en.ex.p": "Gas is actively being flared during your operations. We step in to precisely measure that latent potential, turning a costly environmental waste stream into a steady revenue source.",
    "en.inc7": "Technical feasibility studies", "en.inc8": "Technical operations follow-up",

    "en.mk.text": "This is one of the areas where our local experience — especially in Venezuela and Africa — adds the most value to a gas valorisation project.",
    "en.mk.link": "Learn about our local experience",

    "en.cta.eyebrow": "GET IN TOUCH",
    "en.cta.title1": "Do you have associated gas on a project in Venezuela",
    "en.cta.title2": "that could be losing value?",
    "en.cta.p": "Talk to our technical team about your operation's energy potential.",
    "en.cta.btn1": "Talk to the team", "en.cta.btn2": "See all solutions",
  },
  'es': {
    "en.hero.eyebrow": "SOLUCIONES · ENERGÍA Y DESCARBONIZACIÓN",
    "en.hero.title1": "TRANSFORMAR GAS DESPERDICIADO",
    "en.hero.title2": "EN UN RECURSO ESTRATÉGICO.",
    "en.hero.lead": "Quemar gas asociado en flare no es solo un pasivo ambiental — es una pérdida continua de valor comercial. Nuestros Flare Gas Recovery Systems (FGRS) captan ese gas antes de que llegue a la antorcha, tratándolo para que pueda reintroducirse en un uso productivo en lugar de ser quemado.",
    "en.hero.lead2": "Desde la evaluación de viabilidad hasta el diseño e implementación del sistema, ayudamos a los operadores a transformar una carga regulatoria y ambiental en una fuente funcional de energía e ingresos.",
    "en.hero.cta1": "Hablar sobre un proyecto", "en.hero.cta2": "Ver todas las soluciones",

    "en.prob.eyebrow": "EL PROBLEMA",
    "en.prob.title1": "Quemar gas en flare",
    "en.prob.title2": "desperdicia energía y aumenta las emisiones de gases de efecto invernadero.",
    "en.prob.p1": "Cuando el gas asociado no tiene un destino definido, la solución más simple es quemarlo en flare. Esto significa perder un recurso con valor comercial real y aumentar la huella de emisiones de CO₂ y metano de la operación.",
    "en.prob.p2": "Cada vez más, reguladores, inversores y socios esperan planes medibles de reducción de flaring y descarbonización — no solo intenciones declaradas.",

    "en.visual.eyebrow": "VALORIZACIÓN DE GAS",
    "en.visual.title1": "Cuando el gas se desperdicia,",
    "en.visual.title2": "se pierde mucho más que energía.",
    "en.visual.p1": "ADPETROS desarrolla soluciones para recuperar y dar valor al gas asociado que, de otro modo, sería quemado o liberado durante la operación.",
    "en.visual.sub": "Dónde puede aprovecharse el gas recuperado:",
    "en.visual.li1": "Sistemas de generación de energía in situ",
    "en.visual.li2": "Redes locales de distribución por gasoducto",
    "en.visual.li3": "Materias primas petroquímicas comerciales",
    "en.visual.p2": "Convertir ese gas en una de estas soluciones crea valor a partir de un recurso antes desperdiciado, a la vez que reduce directamente las emisiones asociadas al flaring.",
    "en.visual.tag1": "GENERACIÓN EN SITIO", "en.visual.tag2": "RED DE DISTRIBUCIÓN",
    "en.visual.caption": "Ejemplo ilustrativo de un sistema de generación y distribución de energía en sitio.",

    "en.help.eyebrow": "CÓMO AYUDA ADPETROS",
    "en.help.title1": "De la evaluación del potencial",
    "en.help.title2": "a la operación continua.",
    "en.help.s1t": "Evaluación del potencial de gas", "en.help.s1p": "Estudiamos los volúmenes de gas asociado disponibles y su potencial de aprovechamiento.",
    "en.help.s2t": "Tratamiento y valorización", "en.help.s2p": "Diseñamos las soluciones técnicas de tratamiento necesarias para hacer el gas utilizable.",
    "en.help.s3t": "Producción de energía", "en.help.s3p": "Desarrollamos soluciones para convertir el gas recuperado en energía u otros productos de valor.",
    "en.help.s4t": "Reducción de flaring y descarbonización", "en.help.s4p": "Acompañamos la implementación y la medición de la reducción de emisiones a lo largo del tiempo.",

    "en.photo.eyebrow": "UN RECURSO POR APROVECHAR",
    "en.photo.title1": "La energía ya está ahí.",
    "en.photo.title2": "Falta la estructura para aprovecharla.",
    "en.photo.text": "Esa estructura — técnica y operativa — es la que ayudamos a construir, mercado a mercado.",

    "en.inc.eyebrow": "QUÉ INCLUYE",
    "en.inc.title1": "Soluciones técnicas",
    "en.inc.title2": "para energía y descarbonización.",
    "en.ex.eyebrow": "EJEMPLO PRÁCTICO", "en.ex.title": "Imagine la siguiente situación:",
    "en.ex.p": "Hay gas que se está quemando en una operación, y nadie ha cuantificado con precisión cuánto valor se está perdiendo. Ayudamos a medir con precisión ese potencial latente, transformando un costoso flujo de residuo ambiental en una fuente de ingresos estable.",
    "en.inc1": "Valorización de gas asociado", "en.inc2": "Tratamiento de gas asociado",
    "en.inc3": "Producción de energía", "en.inc4": "Reducción de flaring",
    "en.inc5": "Descarbonización de operaciones", "en.inc6": "Créditos de carbono",
    "en.inc7": "Estudios de viabilidad técnica", "en.inc8": "Seguimiento técnico de la operación",

    "en.mk.text": "Esta es una de las áreas donde nuestra experiencia local — sobre todo en Venezuela y África — más valor añade a un proyecto de valorización de gas.",
    "en.mk.link": "Conocer nuestra experiencia local",

    "en.cta.eyebrow": "HABLEMOS",
    "en.cta.title1": "¿Tiene gas asociado en un proyecto en Venezuela",
    "en.cta.title2": "que podría estar perdiendo valor?",
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
    img='/assets/img/new/h2.jpg', alt='Plataforma offshore com tocha de flare, vista aérea',
    eyebrow_key='en.photo.eyebrow', eyebrow_def='UM RECURSO POR APROVEITAR',
    title1_key='en.photo.title1', title1_def='A energia já está lá.',
    title2_key='en.photo.title2', title2_def='Falta a estrutura para a aproveitar.',
    text_key='en.photo.text', text_def='É essa estrutura — técnica e operacional — que ajudamos a construir, mercado a mercado.',
)

example_html = example_situation_html(
    prefix='en', eyebrow_def='EXEMPLO PRÁTICO', title_def='Imagine a seguinte situação:',
    text_def='Há gás a ser queimado numa operação, e ninguém quantificou com precisão quanto valor está a perder-se. Ajudamos a medir com precisão esse potencial latente, transformando um dispendioso fluxo de resíduo ambiental numa fonte de receita estável.',
    img='/assets/img/12-lg.jpg', alt='Chama de flare a queimar gás associado',
    cta_href='/contactos/', cta_key='cta.project', cta_def='Falar sobre o meu projeto',
)
BODY = f"""
<header class="hero" id="top" data-theme="dark">
  <div class="hero-bg"><img src="/assets/img/new/v13.jpg" alt="Tocha de flare gas em operação contra céu azul" loading="eager"><div class="glow"></div><div class="hero-vignette"></div></div>
  <div class="hero-inner hero-inner-centered">
    <div class="eyebrow" data-i18n="en.hero.eyebrow">SOLUÇÕES · ENERGIA E DESCARBONIZAÇÃO</div>
    <h1 id="heroTitle">
      <span class="line-mask"><span class="line" data-i18n="en.hero.title1">TRANSFORMAR GÁS DESPERDIÇADO</span></span>
      <span class="line-mask"><span class="line sub" data-i18n="en.hero.title2">NUM RECURSO ESTRATÉGICO.</span></span>
    </h1>
    <p class="hero-lead" data-i18n="en.hero.lead">Queimar gás associado em flare não é apenas um passivo ambiental — é uma perda contínua de valor comercial. Os nossos Flare Gas Recovery Systems (FGRS) captam esse gás antes de chegar à tocha, tratando-o para que possa ser reintroduzido num uso produtivo em vez de ser queimado.</p>
    <p class="hero-lead" data-i18n="en.hero.lead2">Da avaliação de viabilidade ao desenho e implementação do sistema, ajudamos os operadores a transformar um encargo regulatório e ambiental numa fonte funcional de energia e receita.</p>
    <div class="hero-ctas">
      <a href="/contactos/" class="btn btn-primary" data-i18n="en.hero.cta1">Falar sobre um projeto
        <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      <a href="/solucoes/" class="btn btn-ghost" data-i18n="en.hero.cta2">Ver todas as soluções</a>
    </div>
  </div>
</header>

<section class="section" data-theme="white">
  <div class="container">
    <div class="prob-grid">
      <div class="prob-copy">
        <div class="eyebrow" data-i18n="en.prob.eyebrow">O PROBLEMA</div>
        <h2 class="big-title reveal"><span data-i18n="en.prob.title1">Queimar gás em flare</span> <span class="title-dim" data-i18n="en.prob.title2">desperdiça energia e aumenta as emissões de gases com efeito de estufa.</span></h2>
        <p class="reveal dim prob-p" data-i18n="en.prob.p1">Quando o gás associado não tem um destino definido, a solução mais simples é queimá-lo em flare. Isso significa perder um recurso com valor comercial real e aumentar a pegada de emissões de CO₂ e metano da operação.</p>
        <p class="reveal dim prob-p" data-i18n="en.prob.p2">Cada vez mais, reguladores, investidores e parceiros esperam planos mensuráveis de redução de flaring e descarbonização — não apenas intenções declaradas.</p>
      </div>
      <div class="prob-photo reveal-img"><img src="/assets/img/new/v3.jpg" alt="Bomba de extração em silhueta ao entardecer" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="section flare-section" data-theme="white">
  <div class="container">
    <div class="flare-grid">
      <div class="flare-visual is-diagram reveal-img">
        <div class="flare-metrics">
          <span class="m-tag" data-i18n="en.visual.tag1">GERAÇÃO NO LOCAL</span>
          <span class="m-tag" data-i18n="en.visual.tag2">REDE DE DISTRIBUIÇÃO</span>
        </div>
        <div class="flare-diagram-plate">
          <img src="/assets/img/new/v14.png" alt="Diagrama de um sistema elétrico de geração e distribuição de energia no local" loading="lazy">
        </div>
        <p class="flare-diagram-caption" data-i18n="en.visual.caption">Exemplo ilustrativo de um sistema de geração e distribuição de energia no local.</p>
      </div>

      <div class="flare-copy">
        <div class="eyebrow" data-i18n="en.visual.eyebrow">VALORIZAÇÃO DE GÁS</div>
        <h2 class="big-title reveal"><span data-i18n="en.visual.title1">Quando o gás é desperdiçado,</span> <span class="title-dim" data-i18n="en.visual.title2">perde-se muito mais do que energia.</span></h2>
        <p class="reveal" data-i18n="en.visual.p1">A ADPETROS desenvolve soluções para recuperar e valorizar gás associado que, de outra forma, seria queimado ou libertado durante a operação.</p>
        <p class="reveal flare-sub" data-i18n="en.visual.sub">Onde o gás recuperado pode ser aproveitado:</p>
        <ul class="flare-list reveal">
          <li data-i18n="en.visual.li1">Sistemas de geração de energia no local</li>
          <li data-i18n="en.visual.li2">Redes locais de distribuição por gasoduto</li>
          <li data-i18n="en.visual.li3">Matérias-primas petroquímicas comerciais</li>
        </ul>
        <p class="reveal" data-i18n="en.visual.p2">Transformar esse gás numa destas soluções cria valor a partir de um recurso que antes era desperdiçado, ao mesmo tempo que reduz diretamente as emissões associadas ao flaring.</p>
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
{inline_cta_html()}
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
        <div class="eyebrow" data-i18n="en.cta.eyebrow">FALE CONNOSCO</div>
        <h2 class="big-title reveal"><span data-i18n="en.cta.title1">Tem gás associado num projeto na Venezuela</span> <span class="title-dim" data-i18n="en.cta.title2">que pode estar a perder valor?</span></h2>
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

EXTRA_JS = ""

LD_JSON = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Energy & Decarbonization — ADPETROS",
  "url": "https://www.adpetros.com/solucoes/energia-e-descarbonizacao/",
  "provider": {"@type":"Organization","name":"ADPETROS"}
}
</script>"""

html = build_page(
    title="Energy & Decarbonization — ADPETROS Solutions",
    description="Associated gas valorization, gas treatment, energy production, flaring reduction, decarbonization and carbon credits.",
    path="/solucoes/energia-e-descarbonizacao/",
    active_nav="solutions",
    body_html=BODY,
    i18n_dict=I18N,
    include_hero_split=True,
    extra_js=EXTRA_JS,
    ld_json=LD_JSON,
)

write_page('solucoes/energia-e-descarbonizacao/index.html', html)
