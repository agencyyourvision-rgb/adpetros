import sys
sys.path.insert(0, '/home/claude/adpetros-site/build')
from sitegen import build_page, write_page, merge_i18n, sol_steps_html, check_list_html, eng_cards_html, photo_section_html, example_situation_html, inline_cta_html

P = "e"  # prefix

ENG_ICONS = [
  '<svg viewBox="0 0 24 24" fill="none"><path d="M4 12h4l2-7 4 14 2-7h4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  '<svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="1.6"/><path d="M19 12a7 7 0 00-.13-1.36l2.03-1.58-2-3.46-2.39.96a7.03 7.03 0 00-2.36-1.36L13.8 3h-3.6l-.35 2.2a7.03 7.03 0 00-2.36 1.36l-2.39-.96-2 3.46 2.03 1.58A7 7 0 005 12c0 .46.04.9.13 1.36l-2.03 1.58 2 3.46 2.39-.96c.7.58 1.5 1.05 2.36 1.36l.35 2.2h3.6l.35-2.2a7.03 7.03 0 002.36-1.36l2.39.96 2-3.46-2.03-1.58c.09-.46.13-.9.13-1.36z" stroke="currentColor" stroke-width="1.3"/></svg>',
  '<svg viewBox="0 0 24 24" fill="none"><path d="M3 21h18M5 21V9l7-5 7 5v12M9 21v-6h6v6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  '<svg viewBox="0 0 24 24" fill="none"><path d="M13 2L4 14h7l-1 8 9-12h-7l1-8z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
  '<svg viewBox="0 0 24 24" fill="none"><path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6l8-4z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M9 12l2 2 4-4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  '<svg viewBox="0 0 24 24" fill="none"><rect x="4" y="4" width="16" height="16" rx="2" stroke="currentColor" stroke-width="1.6"/><path d="M9 4v16M4 9h5M4 15h5" stroke="currentColor" stroke-width="1.6"/></svg>',
]

I18N = merge_i18n({
  'pt': {
    "e.hero.eyebrow": "SOLUÇÕES · ENGENHARIA",
    "e.hero.title1": "Engenharia que transforma conceitos",
    "e.hero.title2": "em realidades construíveis.",
    "e.hero.lead": "Antes de qualquer operação no terreno, um ativo precisa de uma base técnica sólida. A nossa equipa de engenharia estuda, desenha e prepara o seu projeto para a fase mais crítica: a IMPLEMENTAÇÃO.",
    "e.hero.cta1": "Falar sobre um projeto", "e.hero.cta2": "Ver todas as soluções",

    "e.prob.eyebrow": "O PROBLEMA",
    "e.prob.title1": "Um projeto mal preparado",
    "e.prob.title2": "tecnicamente implica atrasos graves e custos inflacionados mais à frente.",
    "e.prob.p1": "Decisões de engenharia tomadas sem rigor técnico, ou sem um conhecimento profundo do ambiente operacional, geram retrabalho dispendioso, atrasos no projeto e despesas imprevistas que só surgem mais tarde — muitas vezes já durante a implementação ativa.",
    "e.prob.p2": "Um projeto de engenharia excecional elimina estes riscos ao identificar e mitigar problemas muito antes de estes afetarem o seu resultado final.",

    "e.help.eyebrow": "COMO A ADPETROS AJUDA",
    "e.help.title1": "Da análise técnica",
    "e.help.title2": "à documentação pronta para executar.",
    "e.help.s1t": "Estudo e avaliação técnica", "e.help.s1p": "Analisamos o projeto e as condições existentes para identificar a solução técnica mais adequada.",
    "e.help.s2t": "Engenharia de detalhe", "e.help.s2p": "Desenvolvemos os desenhos, especificações e documentação técnica necessários à execução.",
    "e.help.s3t": "Coordenação multidisciplinar", "e.help.s3p": "Integramos as diferentes especialidades de engenharia numa mesma equipa e num mesmo cronograma.",
    "e.help.s4t": "Apoio à implementação", "e.help.s4p": "Acompanhamos a transição do projeto técnico para a fase de execução no terreno.",

    "e.photo.eyebrow": "NO TERRENO",
    "e.photo.title1": "Engenharia pensada",
    "e.photo.title2": "para o contexto onde vai operar.",
    "e.photo.text": "Cada estudo tem em conta as condições reais do terreno — do clima às particularidades logísticas de cada mercado — e não apenas a folha de cálculo.",

    "e.inc.eyebrow": "O QUE ESTÁ INCLUÍDO",
    "e.inc.title1": "Especialidades de engenharia",
    "e.inc.title2": "organizadas numa só equipa.",
    "e.inc1": "Engenharia de processo", "e.inc2": "Engenharia mecânica",
    "e.inc3": "Engenharia civil e estrutural", "e.inc4": "Engenharia elétrica e instrumentação",
    "e.inc5": "Integridade e inspeção de ativos", "e.inc6": "Automação e controlo de processo",
    "e.inc7": "Especificação técnica e documentação de projeto", "e.inc8": "Apoio técnico durante a implementação",

    "e.cap.eyebrow": "CAPACIDADES TÉCNICAS",
    "e.cap.title1": "Especialidades que sustentam",
    "e.cap.title2": "cada fase do projeto.",
    "e.cap1": "Engenharia de processo", "e.cap2": "Engenharia mecânica", "e.cap3": "Engenharia civil e estrutural",
    "e.cap4": "Engenharia elétrica e instrumentação", "e.cap5": "Integridade e inspeção de ativos", "e.cap6": "Automação e controlo de processo",

    "e.ex.eyebrow": "EXEMPLO PRÁTICO", "e.ex.title": "Imagine a seguinte situação:",
    "e.ex.p": "Identificou um ativo estratégico, mas precisa de uma avaliação de risco rigorosa para apresentar à administração da sua empresa. A nossa equipa de engenharia entra em ação para analisar a viabilidade técnica, as projeções de CAPEX e as restrições operacionais ocultas, garantindo total clareza antes de finalizar o seu investimento.",
    "e.cta.eyebrow": "FALE CONNOSCO",
    "e.cta.title1": "Quer avançar com um projeto de engenharia",
    "e.cta.title2": "de óleo e gás na Venezuela?",
    "e.cta.p": "Fale com a nossa equipa técnica sobre as necessidades do seu projeto.",
    "e.cta.btn1": "Falar com a equipa", "e.cta.btn2": "Ver todas as soluções",
  },
  'en': {
    "e.hero.eyebrow": "SOLUTIONS · ENGINEERING",
    "e.hero.title1": "Engineering that turns concepts",
    "e.hero.title2": "into buildable realities.",
    "e.hero.lead": "Before any field operations can begin, an asset requires a solid technical foundation. Our engineering team studies, designs, and prepares your project for its most critical next phase: IMPLEMENTATION.",
    "e.hero.cta1": "Talk about a project", "e.hero.cta2": "See all solutions",

    "e.prob.eyebrow": "THE PROBLEM",
    "e.prob.title1": "A technically unprepared project",
    "e.prob.title2": "incurs severe delays and inflated costs down the line.",
    "e.prob.p1": "Engineering decisions made without technical rigor, or without a deep understanding of the operating environment, generate costly rework, project delays, and unforeseen expenses that surface late—often during active implementation.",
    "e.prob.p2": "Exceptional engineering design eliminates these liabilities by identifying and mitigating risks long before they impact your bottom line.",

    "e.help.eyebrow": "HOW ADPETROS HELPS",
    "e.help.title1": "From technical analysis",
    "e.help.title2": "to documentation ready for execution.",
    "e.help.s1t": "Technical study and assessment", "e.help.s1p": "We analyse the project and existing conditions to identify the most suitable technical solution.",
    "e.help.s2t": "Detailed engineering", "e.help.s2p": "We develop the drawings, specifications and technical documentation needed for execution.",
    "e.help.s3t": "Multidisciplinary coordination", "e.help.s3p": "We integrate the different engineering specialities into one team and one schedule.",
    "e.help.s4t": "Implementation support", "e.help.s4p": "We follow the transition from the technical project to on-the-ground execution.",

    "e.photo.eyebrow": "ON THE GROUND",
    "e.photo.title1": "Engineering designed",
    "e.photo.title2": "for the context where it will operate.",
    "e.photo.text": "Every study takes into account real ground conditions — from climate to the logistical particularities of each market — not just the spreadsheet.",

    "e.inc.eyebrow": "WHAT'S INCLUDED",
    "e.inc.title1": "Engineering specialities",
    "e.inc.title2": "organised in a single team.",
    "e.inc1": "Process engineering", "e.inc2": "Mechanical engineering",
    "e.inc3": "Civil and structural engineering", "e.inc4": "Electrical engineering and instrumentation",
    "e.inc5": "Asset integrity and inspection", "e.inc6": "Automation and process control",
    "e.inc7": "Technical specification and project documentation", "e.inc8": "Technical support during implementation",

    "e.cap.eyebrow": "TECHNICAL CAPABILITIES",
    "e.ex.eyebrow": "PRACTICAL EXAMPLE", "e.ex.title": "Imagine the following situation:",
    "e.ex.p": "You've identified a strategic asset, but you need a thorough risk evaluation to present to the board executives of your firm. Our engineering team steps in to analyze technical viability, CAPEX projections, and hidden operational constraints, ensuring total clarity before you finalize your investment.",
    "e.cap.title1": "Specialities that support",
    "e.cap.title2": "every phase of the project.",
    "e.cap1": "Process engineering", "e.cap2": "Mechanical engineering", "e.cap3": "Civil and structural engineering",
    "e.cap4": "Electrical engineering and instrumentation", "e.cap5": "Asset integrity and inspection", "e.cap6": "Automation and process control",

    "e.cta.eyebrow": "GET IN TOUCH",
    "e.cta.title1": "Want to move forward with an oil & gas",
    "e.cta.title2": "engineering project in Venezuela?",
    "e.cta.p": "Talk to our technical team about your project's needs.",
    "e.cta.btn1": "Talk to the team", "e.cta.btn2": "See all solutions",
  },
  'es': {
    "e.hero.eyebrow": "SOLUCIONES · INGENIERÍA",
    "e.hero.title1": "Ingeniería que convierte conceptos",
    "e.hero.title2": "en realidades construibles.",
    "e.hero.lead": "Antes de cualquier operación en el terreno, un activo necesita una base técnica sólida. Nuestro equipo de ingeniería estudia, diseña y prepara su proyecto para la fase más crítica: la IMPLEMENTACIÓN.",
    "e.hero.cta1": "Hablar sobre un proyecto", "e.hero.cta2": "Ver todas las soluciones",

    "e.prob.eyebrow": "EL PROBLEMA",
    "e.prob.title1": "Un proyecto mal preparado",
    "e.prob.title2": "técnicamente implica retrasos graves y costes inflados más adelante.",
    "e.prob.p1": "Las decisiones de ingeniería tomadas sin rigor técnico, o sin un conocimiento profundo del entorno operativo, generan retrabajo costoso, retrasos en el proyecto y gastos imprevistos que solo aparecen más tarde — a menudo ya durante la implementación activa.",
    "e.prob.p2": "Un proyecto de ingeniería excepcional elimina estos riesgos al identificar y mitigar problemas mucho antes de que afecten su resultado final.",

    "e.help.eyebrow": "CÓMO AYUDA ADPETROS",
    "e.help.title1": "Del análisis técnico",
    "e.help.title2": "a la documentación lista para ejecutar.",
    "e.help.s1t": "Estudio y evaluación técnica", "e.help.s1p": "Analizamos el proyecto y las condiciones existentes para identificar la solución técnica más adecuada.",
    "e.help.s2t": "Ingeniería de detalle", "e.help.s2p": "Desarrollamos los planos, especificaciones y documentación técnica necesarios para la ejecución.",
    "e.help.s3t": "Coordinación multidisciplinar", "e.help.s3p": "Integramos las diferentes especialidades de ingeniería en un mismo equipo y un mismo cronograma.",
    "e.help.s4t": "Apoyo a la implementación", "e.help.s4p": "Acompañamos la transición del proyecto técnico a la fase de ejecución en el terreno.",

    "e.photo.eyebrow": "EN EL TERRENO",
    "e.photo.title1": "Ingeniería pensada",
    "e.photo.title2": "para el contexto donde va a operar.",
    "e.photo.text": "Cada estudio tiene en cuenta las condiciones reales del terreno — desde el clima hasta las particularidades logísticas de cada mercado — no solo la hoja de cálculo.",

    "e.inc.eyebrow": "QUÉ INCLUYE",
    "e.inc.title1": "Especialidades de ingeniería",
    "e.inc.title2": "organizadas en un solo equipo.",
    "e.inc1": "Ingeniería de procesos", "e.inc2": "Ingeniería mecánica",
    "e.ex.eyebrow": "EJEMPLO PRÁCTICO", "e.ex.title": "Imagine la siguiente situación:",
    "e.ex.p": "Ha identificado un activo estratégico, pero necesita una evaluación de riesgo rigurosa para presentar a la dirección de su empresa. Nuestro equipo de ingeniería interviene para analizar la viabilidad técnica, las proyecciones de CAPEX y las restricciones operativas ocultas, garantizando total claridad antes de finalizar su inversión.",
    "e.inc3": "Ingeniería civil y estructural", "e.inc4": "Ingeniería eléctrica e instrumentación",
    "e.inc5": "Integridad e inspección de activos", "e.inc6": "Automatización y control de procesos",
    "e.inc7": "Especificación técnica y documentación de proyecto", "e.inc8": "Apoyo técnico durante la implementación",

    "e.cap.eyebrow": "CAPACIDADES TÉCNICAS",
    "e.cap.title1": "Especialidades que sostienen",
    "e.cap.title2": "cada fase del proyecto.",
    "e.cap1": "Ingeniería de procesos", "e.cap2": "Ingeniería mecánica", "e.cap3": "Ingeniería civil y estructural",
    "e.cap4": "Ingeniería eléctrica e instrumentación", "e.cap5": "Integridad e inspección de activos", "e.cap6": "Automatización y control de procesos",

    "e.cta.eyebrow": "HABLEMOS",
    "e.cta.title1": "¿Quiere avanzar con un proyecto de ingeniería",
    "e.cta.title2": "de petróleo y gas en Venezuela?",
    "e.cta.p": "Hable con nuestro equipo técnico sobre las necesidades de su proyecto.",
    "e.cta.btn1": "Hablar con el equipo", "e.cta.btn2": "Ver todas las soluciones",
  },
})

sol_steps = sol_steps_html([
    {'n': '01', 'tkey': 'e.help.s1t', 'tdef': 'Estudo e avaliação técnica', 'pkey': 'e.help.s1p', 'pdef': 'Analisamos o projeto e as condições existentes para identificar a solução técnica mais adequada.'},
    {'n': '02', 'tkey': 'e.help.s2t', 'tdef': 'Engenharia de detalhe', 'pkey': 'e.help.s2p', 'pdef': 'Desenvolvemos os desenhos, especificações e documentação técnica necessários à execução.'},
    {'n': '03', 'tkey': 'e.help.s3t', 'tdef': 'Coordenação multidisciplinar', 'pkey': 'e.help.s3p', 'pdef': 'Integramos as diferentes especialidades de engenharia numa mesma equipa e num mesmo cronograma.'},
    {'n': '04', 'tkey': 'e.help.s4t', 'tdef': 'Apoio à implementação', 'pkey': 'e.help.s4p', 'pdef': 'Acompanhamos a transição do projeto técnico para a fase de execução no terreno.'},
], extra_style='margin-top:48px')

checklist = check_list_html([
    {'key': 'e.inc1', 'text': 'Engenharia de processo'}, {'key': 'e.inc2', 'text': 'Engenharia mecânica'},
    {'key': 'e.inc3', 'text': 'Engenharia civil e estrutural'}, {'key': 'e.inc4', 'text': 'Engenharia elétrica e instrumentação'},
    {'key': 'e.inc5', 'text': 'Integridade e inspeção de ativos'}, {'key': 'e.inc6', 'text': 'Automação e controlo de processo'},
    {'key': 'e.inc7', 'text': 'Especificação técnica e documentação de projeto'}, {'key': 'e.inc8', 'text': 'Apoio técnico durante a implementação'},
])

cap_cards = eng_cards_html([
    {'icon': ENG_ICONS[0], 'key': 'e.cap1', 'text': 'Engenharia de processo'},
    {'icon': ENG_ICONS[1], 'key': 'e.cap2', 'text': 'Engenharia mecânica'},
    {'icon': ENG_ICONS[2], 'key': 'e.cap3', 'text': 'Engenharia civil e estrutural'},
    {'icon': ENG_ICONS[3], 'key': 'e.cap4', 'text': 'Engenharia elétrica e instrumentação'},
    {'icon': ENG_ICONS[4], 'key': 'e.cap5', 'text': 'Integridade e inspeção de ativos'},
    {'icon': ENG_ICONS[5], 'key': 'e.cap6', 'text': 'Automação e controlo de processo'},
])

photo_section = photo_section_html(
    img='/assets/img/new/h4.jpg', alt='Plataforma offshore ao pôr-do-sol, vista aérea',
    eyebrow_key='e.photo.eyebrow', eyebrow_def='NO TERRENO',
    title1_key='e.photo.title1', title1_def='Engenharia pensada',
    title2_key='e.photo.title2', title2_def='para o contexto onde vai operar.',
    text_key='e.photo.text', text_def='Cada estudo tem em conta as condições reais do terreno — do clima às particularidades logísticas de cada mercado — e não apenas a folha de cálculo.',
    extra_class='photo-section-strong',
)

example_html = example_situation_html(
    prefix='e', eyebrow_def='EXEMPLO PRÁTICO', title_def='Imagine a seguinte situação:',
    text_def='Identificou um ativo estratégico, mas precisa de uma avaliação de risco rigorosa para apresentar à administração da sua empresa. A nossa equipa de engenharia entra em ação para analisar a viabilidade técnica, as projeções de CAPEX e as restrições operacionais ocultas, garantindo total clareza antes de finalizar o seu investimento.',
    img='/assets/img/new/v12.jpg', alt='Dois colegas de equipa com capacetes na mão, prontos para colaborar num projeto',
    cta_href='/contactos/', cta_key='cta.project', cta_def='Falar sobre o meu projeto',
)
BODY = f"""
<header class="hero" id="top" data-theme="dark">
  <div class="hero-bg"><img src="/assets/img/11-lg.jpg" alt="Engenheiro a apontar para uma instalação industrial ao entardecer" loading="eager"><div class="glow"></div><div class="hero-vignette"></div></div>
  <div class="hero-inner hero-inner-centered">
    <div class="eyebrow" data-i18n="e.hero.eyebrow">SOLUÇÕES · ENGENHARIA</div>
    <h1 id="heroTitle">
      <span class="line-mask"><span class="line" data-i18n="e.hero.title1">Engenharia que transforma conceitos</span></span>
      <span class="line-mask"><span class="line sub" data-i18n="e.hero.title2">em realidades construíveis.</span></span>
    </h1>
    <p class="hero-lead" data-i18n="e.hero.lead">Antes de qualquer operação no terreno, um ativo precisa de uma base técnica sólida. A nossa equipa de engenharia estuda, desenha e prepara o seu projeto para a fase mais crítica: a IMPLEMENTAÇÃO.</p>
    <div class="hero-ctas">
      <a href="/contactos/" class="btn btn-primary" data-i18n="e.hero.cta1">Falar sobre um projeto
        <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      <a href="/solucoes/" class="btn btn-ghost" data-i18n="e.hero.cta2">Ver todas as soluções</a>
    </div>
  </div>
</header>

<section class="section" data-theme="white">
  <div class="container">
    <div class="prob-grid">
      <div class="prob-copy">
        <div class="eyebrow" data-i18n="e.prob.eyebrow">O PROBLEMA</div>
        <h2 class="big-title reveal"><span data-i18n="e.prob.title1">Um projeto mal preparado</span> <span class="title-dim" data-i18n="e.prob.title2">tecnicamente implica atrasos graves e custos inflacionados mais à frente.</span></h2>
        <p class="reveal dim prob-p" data-i18n="e.prob.p1">Decisões de engenharia tomadas sem rigor técnico, ou sem um conhecimento profundo do ambiente operacional, geram retrabalho dispendioso, atrasos no projeto e despesas imprevistas que só surgem mais tarde — muitas vezes já durante a implementação ativa.</p>
        <p class="reveal dim prob-p" data-i18n="e.prob.p2">Um projeto de engenharia excecional elimina estes riscos ao identificar e mitigar problemas muito antes de estes afetarem o seu resultado final.</p>
      </div>
      <div class="prob-photo reveal-img"><img src="/assets/img/new/v8.jpg" alt="Técnico com rádio a observar uma instalação industrial ao entardecer" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="section" data-theme="dark">
  <div class="container">
    <div class="header-row">
      <div>
        <div class="eyebrow" data-i18n="e.help.eyebrow">COMO A ADPETROS AJUDA</div>
        <h2 class="big-title reveal"><span data-i18n="e.help.title1">Da análise técnica</span> <span class="title-dim" data-i18n="e.help.title2">à documentação pronta para executar.</span></h2>
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
        <div class="eyebrow" data-i18n="e.inc.eyebrow">O QUE ESTÁ INCLUÍDO</div>
        <h2 class="big-title reveal"><span data-i18n="e.inc.title1">Especialidades de engenharia</span> <span class="title-dim" data-i18n="e.inc.title2">organizadas numa só equipa.</span></h2>
      </div>
    </div>
    {checklist}
  </div>
</section>

<section class="section" data-theme="dark">
  <div class="container">
    <div class="header-row">
      <div>
        <div class="eyebrow" data-i18n="e.cap.eyebrow">CAPACIDADES TÉCNICAS</div>
        <h2 class="big-title reveal"><span data-i18n="e.cap.title1">Especialidades que sustentam</span> <span class="title-dim" data-i18n="e.cap.title2">cada fase do projeto.</span></h2>
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
        <div class="eyebrow" data-i18n="e.cta.eyebrow">FALE CONNOSCO</div>
        <h2 class="big-title reveal"><span data-i18n="e.cta.title1">Quer avançar com um projeto de engenharia</span> <span class="title-dim" data-i18n="e.cta.title2">de óleo e gás na Venezuela?</span></h2>
        <p class="reveal" data-i18n="e.cta.p">Fale com a nossa equipa técnica sobre as necessidades do seu projeto.</p>
        <div class="hero-ctas reveal">
          <a href="/contactos/" class="btn btn-primary" data-i18n="e.cta.btn1">Falar com a equipa
            <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <a href="/solucoes/" class="btn btn-ghost" data-i18n="e.cta.btn2">Ver todas as soluções</a>
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
  "name": "Engineering — ADPETROS",
  "url": "https://www.adpetros.com/solucoes/engenharia/",
  "provider": {"@type":"Organization","name":"ADPETROS"}
}
</script>"""

html = build_page(
    title="Engineering — ADPETROS Solutions",
    description="Process, mechanical, civil, electrical, asset integrity and automation engineering for industrial projects and operations.",
    path="/solucoes/engenharia/",
    active_nav="solutions",
    body_html=BODY,
    i18n_dict=I18N,
    include_hero_split=True,
    extra_js="",
    ld_json=LD_JSON,
)

write_page('solucoes/engenharia/index.html', html)
