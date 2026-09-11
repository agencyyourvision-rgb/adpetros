import sys
sys.path.insert(0, '/home/claude/adpetros-site/build')
from sitegen import build_page, write_page, merge_i18n, sol_steps_html, check_list_html, eng_cards_html, photo_section_html, example_situation_html, inline_cta_html

P = "m"  # prefix

MOD_ICONS = [
  '<svg viewBox="0 0 24 24" fill="none"><path d="M9 3v4M15 3v4M4 8h16M6 8v11a2 2 0 002 2h8a2 2 0 002-2V8" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M9.5 13l2 2 3-3.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  '<svg viewBox="0 0 24 24" fill="none"><path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6l8-4z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M9 12l2 2 4-4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  '<svg viewBox="0 0 24 24" fill="none"><circle cx="11" cy="11" r="7" stroke="currentColor" stroke-width="1.6"/><path d="M21 21l-4.3-4.3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><path d="M8 11h6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
  '<svg viewBox="0 0 24 24" fill="none"><path d="M4 20V10M10 20V4M16 20v-7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M2 20h20" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><path d="M13 4l5-2v6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  '<svg viewBox="0 0 24 24" fill="none"><path d="M13 3L4 14h7l-1 7 9-11h-7l1-7z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
  '<svg viewBox="0 0 24 24" fill="none"><path d="M12 9v4M12 17h.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M10.3 3.9L2.6 17.5A1.8 1.8 0 004.2 20h15.6a1.8 1.8 0 001.6-2.5L13.7 3.9a1.8 1.8 0 00-3.4 0z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
]

I18N = merge_i18n({
  'pt': {
    "m.hero.eyebrow": "SOLUÇÕES · RECUPERAÇÃO E MODERNIZAÇÃO DE ATIVOS",
    "m.hero.title1": "Recuperar e otimizar",
    "m.hero.title2": "instalações e equipamentos já existentes.",
    "m.hero.lead": "Nem todos os ativos precisam de ser substituídos. Muitas vezes, o maior retorno vem de prolongar a vida útil do que já opera — através de um diagnóstico técnico rigoroso e de um plano de modernização direcionado, construído em torno do seu equipamento e das suas restrições específicas.",
    "m.hero.cta1": "Falar sobre um ativo", "m.hero.cta2": "Ver todas as soluções",

    "m.prob.eyebrow": "O PROBLEMA",
    "m.prob.title1": "Refinarias e instalações industriais",
    "m.prob.title2": "perdem eficiência ao longo do tempo, muitas vezes sem visibilidade imediata.",
    "m.prob.p1": "Os equipamentos envelhecem, os processos desviam-se do seu ponto ótimo de funcionamento e pequenas falhas acumulam-se até se tornarem grandes problemas — de produção, de segurança ou de custo.",
    "m.prob.p2": "Sem um diagnóstico técnico independente, é difícil saber onde investir primeiro.",

    "m.help.eyebrow": "COMO A ADPETROS AJUDA",
    "m.help.title1": "Do diagnóstico",
    "m.help.title2": "à implementação da melhoria.",
    "m.help.s1t": "Diagnóstico técnico", "m.help.s1p": "Avaliamos o estado atual dos ativos e identificamos as causas reais dos problemas.",
    "m.help.s2t": "Integridade e inspeção", "m.help.s2p": "Verificamos a integridade estrutural e operacional de equipamentos e instalações.",
    "m.help.s3t": "Modernização e resolução de estrangulamentos operacionais", "m.help.s3p": "Desenvolvemos soluções técnicas para aumentar capacidade, eficiência e fiabilidade.",
    "m.help.s4t": "Acompanhamento da implementação", "m.help.s4p": "Apoiamos a execução das melhorias definidas, até estarem em operação.",

    "m.photo.eyebrow": "ATIVOS EXISTENTES",
    "m.photo.title1": "Cada instalação tem",
    "m.photo.title2": "uma história e um potencial por explorar.",
    "m.photo.text": "O diagnóstico certo revela onde investir primeiro — antes de qualquer decisão de modernização.",

    "m.inc.eyebrow": "O QUE ESTÁ INCLUÍDO",
    "m.inc.title1": "Um processo completo",
    "m.inc.title2": "de recuperação de ativos.",
    "m.inc1": "Diagnóstico técnico", "m.inc2": "Integridade de ativos",
    "m.inc3": "Identificação de falhas", "m.inc4": "Inspeção de equipamentos",
    "m.inc5": "Modernização de instalações", "m.inc6": "Resolução de estrangulamentos operacionais",
    "m.inc7": "Melhoria de eficiência operacional", "m.inc8": "Acompanhamento da implementação",

    "m.cap.eyebrow": "CAPACIDADES TÉCNICAS",
    "m.cap.title1": "Competências que sustentam",
    "m.cap.title2": "um bom diagnóstico e uma boa modernização.",
    "m.cap1": "Diagnóstico técnico", "m.cap2": "Integridade e inspeção de ativos", "m.cap3": "Identificação de falhas",
    "m.cap4": "Modernização de instalações", "m.cap5": "Resolução de estrangulamentos operacionais", "m.cap6": "Prevenção e gestão de riscos",

    "m.ex.eyebrow": "EXEMPLO PRÁTICO", "m.ex.title": "Imagine a seguinte situação:",
    "m.ex.p": "Quando um ativo-chave tem um desempenho abaixo do esperado, decidir entre recuperá-lo ou substituí-lo é uma escolha financeira de grande impacto. Realizamos o diagnóstico técnico que fornece essa resposta definitiva, sustentado por dados quantificáveis, não suposições.",
    "m.cta.eyebrow": "FALE CONNOSCO",
    "m.cta.title1": "Tem um ativo de óleo e gás na Venezuela",
    "m.cta.title2": "que precisa de diagnóstico ou modernização?",
    "m.cta.p": "Fale com a nossa equipa técnica sobre a instalação ou o equipamento em questão.",
    "m.cta.btn1": "Falar com a equipa", "m.cta.btn2": "Ver todas as soluções",
  },
  'en': {
    "m.hero.eyebrow": "SOLUTIONS · ASSET RECOVERY & MODERNISATION",
    "m.hero.title1": "Recovering and optimising",
    "m.hero.title2": "already existing installations and equipment.",
    "m.hero.lead": "Building from scratch is no longer the only path to progress. We help operators extract the maximum ROI from existing facilities through rigorous diagnoses and targeted modernization framework.",
    "m.hero.cta1": "Talk about an asset", "m.hero.cta2": "See all solutions",

    "m.prob.eyebrow": "THE PROBLEM",
    "m.prob.title1": "Refineries and industrial facilities",
    "m.prob.title2": "lose efficiency over time, often without immediate visibility.",
    "m.prob.p1": "Equipment ages, processes lose optimization, and minor faults accumulate until they escalate into major production, safety, or financial risks.",
    "m.prob.p2": "Without an independent technical diagnosis, it is difficult to determine exactly where capital should be allocated first.",

    "m.help.eyebrow": "HOW ADPETROS HELPS",
    "m.help.title1": "From diagnosis",
    "m.help.title2": "to implementing the improvement.",
    "m.help.s1t": "Technical diagnosis", "m.help.s1p": "We assess the current state of assets and identify the real causes of the problems.",
    "m.help.s2t": "Integrity and inspection", "m.help.s2p": "We verify the structural and operational integrity of equipment and facilities.",
    "m.help.s3t": "Modernisation and operational bottleneck resolution", "m.help.s3p": "We develop technical solutions to increase capacity, efficiency and reliability.",
    "m.help.s4t": "Implementation support", "m.help.s4p": "We support the execution of the defined improvements, until they are in operation.",

    "m.photo.eyebrow": "EXISTING ASSETS",
    "m.photo.title1": "Every facility has",
    "m.photo.title2": "a history and untapped potential.",
    "m.photo.text": "The right diagnosis reveals where to invest first — before any modernisation decision.",

    "m.inc.eyebrow": "WHAT'S INCLUDED",
    "m.inc.title1": "A complete",
    "m.inc.title2": "asset recovery process.",
    "m.inc1": "Technical diagnosis", "m.inc2": "Asset integrity",
    "m.inc3": "Fault identification", "m.inc4": "Equipment inspection",
    "m.inc5": "Facility modernisation", "m.inc6": "Operational bottleneck resolution",
    "m.inc7": "Operational efficiency improvement", "m.inc8": "Implementation support",

    "m.cap.eyebrow": "TECHNICAL CAPABILITIES",
    "m.cap.title1": "Competencies behind",
    "m.ex.eyebrow": "PRACTICAL EXAMPLE", "m.ex.title": "Imagine the following situation:",
    "m.ex.p": "When a key asset underperforms, deciding whether to overhaul or replace it is a high-stakes financial choice. We conduct the technical diagnosis that provides that definitive answer, backed by quantifiable data, not assumptions.",
    "m.cap.title2": "a good diagnosis and a good modernisation.",
    "m.cap1": "Technical diagnosis", "m.cap2": "Asset integrity and inspection", "m.cap3": "Fault identification",
    "m.cap4": "Facility modernisation", "m.cap5": "Operational bottleneck resolution", "m.cap6": "Risk prevention and management",

    "m.cta.eyebrow": "GET IN TOUCH",
    "m.cta.title1": "Do you have an oil & gas asset in Venezuela",
    "m.cta.title2": "that needs diagnosis or modernisation?",
    "m.cta.p": "Talk to our technical team about the facility or equipment in question.",
    "m.cta.btn1": "Talk to the team", "m.cta.btn2": "See all solutions",
  },
  'es': {
    "m.hero.eyebrow": "SOLUCIONES · RECUPERACIÓN Y MODERNIZACIÓN DE ACTIVOS",
    "m.hero.title1": "Recuperar y optimizar",
    "m.hero.title2": "instalaciones y equipos ya existentes.",
    "m.hero.lead": "No todos los activos necesitan ser sustituidos. A menudo, el mayor retorno proviene de prolongar la vida útil de lo que ya opera — mediante un diagnóstico técnico riguroso y un plan de modernización específico, diseñado en torno a su equipo y sus restricciones particulares.",
    "m.hero.cta1": "Hablar sobre un activo", "m.hero.cta2": "Ver todas las soluciones",

    "m.prob.eyebrow": "EL PROBLEMA",
    "m.prob.title1": "Las refinerías e instalaciones industriales",
    "m.prob.title2": "pierden eficiencia con el tiempo, muchas veces sin visibilidad inmediata.",
    "m.prob.p1": "Los equipos envejecen, los procesos se desvían de su punto óptimo de funcionamiento y los pequeños fallos se acumulan hasta convertirse en grandes problemas — de producción, seguridad o coste.",
    "m.prob.p2": "Sin un diagnóstico técnico independiente, es difícil saber dónde invertir primero.",

    "m.help.eyebrow": "CÓMO AYUDA ADPETROS",
    "m.help.title1": "Del diagnóstico",
    "m.help.title2": "a la implementación de la mejora.",
    "m.help.s1t": "Diagnóstico técnico", "m.help.s1p": "Evaluamos el estado actual de los activos e identificamos las causas reales de los problemas.",
    "m.help.s2t": "Integridad e inspección", "m.help.s2p": "Verificamos la integridad estructural y operativa de equipos e instalaciones.",
    "m.help.s3t": "Modernización y resolución de estrangulamientos operativos", "m.help.s3p": "Desarrollamos soluciones técnicas para aumentar capacidad, eficiencia y fiabilidad.",
    "m.help.s4t": "Apoyo a la implementación", "m.help.s4p": "Apoyamos la ejecución de las mejoras definidas, hasta que estén en operación.",

    "m.photo.eyebrow": "ACTIVOS EXISTENTES",
    "m.photo.title1": "Cada instalación tiene",
    "m.photo.title2": "una historia y un potencial por explorar.",
    "m.photo.text": "El diagnóstico correcto revela dónde invertir primero — antes de cualquier decisión de modernización.",

    "m.inc.eyebrow": "QUÉ INCLUYE",
    "m.inc.title1": "Un proceso completo",
    "m.inc.title2": "de recuperación de activos.",
    "m.inc1": "Diagnóstico técnico", "m.inc2": "Integridad de activos",
    "m.inc3": "Identificación de fallos", "m.inc4": "Inspección de equipos",
    "m.ex.eyebrow": "EJEMPLO PRÁCTICO", "m.ex.title": "Imagine la siguiente situación:",
    "m.ex.p": "Cuando un activo clave tiene un rendimiento inferior al esperado, decidir entre recuperarlo o sustituirlo es una decisión financiera de gran impacto. Realizamos el diagnóstico técnico que ofrece esa respuesta definitiva, respaldada por datos cuantificables, no suposiciones.",
    "m.inc5": "Modernización de instalaciones", "m.inc6": "Resolución de estrangulamientos operativos",
    "m.inc7": "Mejora de la eficiencia operativa", "m.inc8": "Apoyo a la implementación",

    "m.cap.eyebrow": "CAPACIDADES TÉCNICAS",
    "m.cap.title1": "Competencias que sostienen",
    "m.cap.title2": "un buen diagnóstico y una buena modernización.",
    "m.cap1": "Diagnóstico técnico", "m.cap2": "Integridad e inspección de activos", "m.cap3": "Identificación de fallos",
    "m.cap4": "Modernización de instalaciones", "m.cap5": "Resolución de estrangulamientos operativos", "m.cap6": "Prevención y gestión de riesgos",

    "m.cta.eyebrow": "HABLEMOS",
    "m.cta.title1": "¿Tiene un activo de petróleo y gas en Venezuela",
    "m.cta.title2": "que necesita diagnóstico o modernización?",
    "m.cta.p": "Hable con nuestro equipo técnico sobre la instalación o el equipo en cuestión.",
    "m.cta.btn1": "Hablar con el equipo", "m.cta.btn2": "Ver todas las soluciones",
  },
})

sol_steps = sol_steps_html([
    {'n': '01', 'tkey': 'm.help.s1t', 'tdef': 'Diagnóstico técnico', 'pkey': 'm.help.s1p', 'pdef': 'Avaliamos o estado atual dos ativos e identificamos as causas reais dos problemas.'},
    {'n': '02', 'tkey': 'm.help.s2t', 'tdef': 'Integridade e inspeção', 'pkey': 'm.help.s2p', 'pdef': 'Verificamos a integridade estrutural e operacional de equipamentos e instalações.'},
    {'n': '03', 'tkey': 'm.help.s3t', 'tdef': 'Modernização e resolução de estrangulamentos operacionais', 'pkey': 'm.help.s3p', 'pdef': 'Desenvolvemos soluções técnicas para aumentar capacidade, eficiência e fiabilidade.'},
    {'n': '04', 'tkey': 'm.help.s4t', 'tdef': 'Acompanhamento da implementação', 'pkey': 'm.help.s4p', 'pdef': 'Apoiamos a execução das melhorias definidas, até estarem em operação.'},
], extra_style='margin-top:48px')

checklist = check_list_html([
    {'key': 'm.inc1', 'text': 'Diagnóstico técnico'}, {'key': 'm.inc2', 'text': 'Integridade de ativos'},
    {'key': 'm.inc3', 'text': 'Identificação de falhas'}, {'key': 'm.inc4', 'text': 'Inspeção de equipamentos'},
    {'key': 'm.inc5', 'text': 'Modernização de instalações'}, {'key': 'm.inc6', 'text': 'Resolução de estrangulamentos operacionais'},
    {'key': 'm.inc7', 'text': 'Melhoria de eficiência operacional'}, {'key': 'm.inc8', 'text': 'Acompanhamento da implementação'},
])

cap_cards = eng_cards_html([
    {'icon': MOD_ICONS[0], 'key': 'm.cap1', 'text': 'Diagnóstico técnico'},
    {'icon': MOD_ICONS[1], 'key': 'm.cap2', 'text': 'Integridade e inspeção de ativos'},
    {'icon': MOD_ICONS[2], 'key': 'm.cap3', 'text': 'Identificação de falhas'},
    {'icon': MOD_ICONS[3], 'key': 'm.cap4', 'text': 'Modernização de instalações'},
    {'icon': MOD_ICONS[4], 'key': 'm.cap5', 'text': 'Resolução de estrangulamentos operacionais'},
    {'icon': MOD_ICONS[5], 'key': 'm.cap6', 'text': 'Prevenção e gestão de riscos'},
])

photo_section = photo_section_html(
    img='/assets/img/new/h7.jpg', alt='Bombas de extração em silhueta ao pôr-do-sol',
    eyebrow_key='m.photo.eyebrow', eyebrow_def='ATIVOS EXISTENTES',
    title1_key='m.photo.title1', title1_def='Cada instalação tem',
    title2_key='m.photo.title2', title2_def='uma história e um potencial por explorar.',
    text_key='m.photo.text', text_def='O diagnóstico certo revela onde investir primeiro — antes de qualquer decisão de modernização.',
)

example_html = example_situation_html(
    prefix='m', eyebrow_def='EXEMPLO PRÁTICO', title_def='Imagine a seguinte situação:',
    text_def='Quando um ativo-chave tem um desempenho abaixo do esperado, decidir entre recuperá-lo ou substituí-lo é uma escolha financeira de grande impacto. Realizamos o diagnóstico técnico que fornece essa resposta definitiva, sustentado por dados quantificáveis, não suposições.',
    img='/assets/img/17-lg.jpg', alt='Técnico a inspecionar um ativo industrial',
    cta_href='/contactos/', cta_key='cta.project', cta_def='Falar sobre o meu projeto',
)
BODY = f"""
<header class="hero" id="top" data-theme="dark">
  <div class="hero-bg"><img src="/assets/img/8-lg.jpg" alt="Poços de petróleo ao pôr do sol" loading="eager"><div class="glow"></div><div class="hero-vignette"></div></div>
  <div class="hero-inner hero-inner-centered">
    <div class="eyebrow" data-i18n="m.hero.eyebrow">SOLUÇÕES · RECUPERAÇÃO E MODERNIZAÇÃO DE ATIVOS</div>
    <h1 id="heroTitle">
      <span class="line-mask"><span class="line" data-i18n="m.hero.title1">Recuperar e otimizar</span></span>
      <span class="line-mask"><span class="line sub" data-i18n="m.hero.title2">instalações e equipamentos já existentes.</span></span>
    </h1>
    <p class="hero-lead" data-i18n="m.hero.lead">Nem todos os ativos precisam de ser substituídos. Muitas vezes, o maior retorno vem de prolongar a vida útil do que já opera — através de um diagnóstico técnico rigoroso e de um plano de modernização direcionado, construído em torno do seu equipamento e das suas restrições específicas.</p>
    <div class="hero-ctas">
      <a href="/contactos/" class="btn btn-primary" data-i18n="m.hero.cta1">Falar sobre um ativo
        <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      <a href="/solucoes/" class="btn btn-ghost" data-i18n="m.hero.cta2">Ver todas as soluções</a>
    </div>
  </div>
</header>

<section class="section" data-theme="white">
  <div class="container">
    <div class="prob-grid">
      <div class="prob-copy">
        <div class="eyebrow" data-i18n="m.prob.eyebrow">O PROBLEMA</div>
        <h2 class="big-title reveal"><span data-i18n="m.prob.title1">Refinarias e instalações industriais</span> <span class="title-dim" data-i18n="m.prob.title2">perdem eficiência ao longo do tempo, muitas vezes sem visibilidade imediata.</span></h2>
        <p class="reveal dim prob-p" data-i18n="m.prob.p1">Os equipamentos envelhecem, os processos desviam-se do seu ponto ótimo de funcionamento e pequenas falhas acumulam-se até se tornarem grandes problemas — de produção, de segurança ou de custo.</p>
        <p class="reveal dim prob-p" data-i18n="m.prob.p2">Sem um diagnóstico técnico independente, é difícil saber onde investir primeiro.</p>
      </div>
      <div class="prob-photo reveal-img"><img src="/assets/img/new/v9.jpg" alt="Tubagem industrial antiga e enferrujada numa refinaria" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="section" data-theme="dark">
  <div class="container">
    <div class="header-row">
      <div>
        <div class="eyebrow" data-i18n="m.help.eyebrow">COMO A ADPETROS AJUDA</div>
        <h2 class="big-title reveal"><span data-i18n="m.help.title1">Do diagnóstico</span> <span class="title-dim" data-i18n="m.help.title2">à implementação da melhoria.</span></h2>
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
        <div class="eyebrow" data-i18n="m.inc.eyebrow">O QUE ESTÁ INCLUÍDO</div>
        <h2 class="big-title reveal"><span data-i18n="m.inc.title1">Um processo completo</span> <span class="title-dim" data-i18n="m.inc.title2">de recuperação de ativos.</span></h2>
      </div>
    </div>
    {checklist}
  </div>
</section>

<section class="section" data-theme="dark">
  <div class="container">
    <div class="header-row">
      <div>
        <div class="eyebrow" data-i18n="m.cap.eyebrow">CAPACIDADES TÉCNICAS</div>
        <h2 class="big-title reveal"><span data-i18n="m.cap.title1">Competências que sustentam</span> <span class="title-dim" data-i18n="m.cap.title2">um bom diagnóstico e uma boa modernização.</span></h2>
      </div>
    </div>
    {cap_cards}
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
        <div class="eyebrow" data-i18n="m.cta.eyebrow">FALE CONNOSCO</div>
        <h2 class="big-title reveal"><span data-i18n="m.cta.title1">Tem um ativo de óleo e gás na Venezuela</span> <span class="title-dim" data-i18n="m.cta.title2">que precisa de diagnóstico ou modernização?</span></h2>
        <p class="reveal" data-i18n="m.cta.p">Fale com a nossa equipa técnica sobre a instalação ou o equipamento em questão.</p>
        <div class="hero-ctas reveal">
          <a href="/contactos/" class="btn btn-primary" data-i18n="m.cta.btn1">Falar com a equipa
            <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <a href="/solucoes/" class="btn btn-ghost" data-i18n="m.cta.btn2">Ver todas as soluções</a>
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
  "name": "Asset Recovery & Modernization — ADPETROS",
  "url": "https://www.adpetros.com/solucoes/modernizacao-de-ativos/",
  "provider": {"@type":"Organization","name":"ADPETROS"}
}
</script>"""

html = build_page(
    title="Asset Recovery & Modernization — ADPETROS Solutions",
    description="Technical diagnosis, asset integrity, modernization and resolution of operational bottlenecks for existing refineries and industrial facilities.",
    path="/solucoes/modernizacao-de-ativos/",
    active_nav="solutions",
    body_html=BODY,
    i18n_dict=I18N,
    include_hero_split=True,
    extra_js="",
    ld_json=LD_JSON,
)

write_page('solucoes/modernizacao-de-ativos/index.html', html)
