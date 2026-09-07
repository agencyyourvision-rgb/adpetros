import sys
sys.path.insert(0, '/home/claude/adpetros-site/build')
from sitegen import build_page, write_page, merge_i18n, sol_steps_html, check_list_html, why_mini_html, photo_section_html, example_situation_html, inline_cta_html

WHY_ICONS = [
  '<svg viewBox="0 0 24 24" fill="none"><path d="M13 3L4 14h7l-1 7 9-11h-7l1-7z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
  '<svg viewBox="0 0 24 24" fill="none"><path d="M5 13l4 4L19 7" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  '<svg viewBox="0 0 24 24" fill="none"><circle cx="6" cy="7" r="2.4" stroke="currentColor" stroke-width="1.6"/><circle cx="18" cy="7" r="2.4" stroke="currentColor" stroke-width="1.6"/><circle cx="12" cy="17" r="2.4" stroke="currentColor" stroke-width="1.6"/><path d="M7.6 9L10.5 15M16.4 9L13.5 15M8.4 7H15.6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
]

I18N = merge_i18n({
  'pt': {
    "i.hero.eyebrow": "SOLUÇÕES · IMPLEMENTAÇÃO DE PROJETOS",
    "i.hero.title1": "Do planeamento",
    "i.hero.title2": "à execução no terreno.",
    "i.hero.lead": "Ter um projeto de engenharia robusto é apenas o primeiro passo. Pô-lo em prática exige equipas no terreno, fornecedores validados, logística precisa e uma infraestrutura local capaz de transformar esse projeto técnico numa operação totalmente ativa.",
    "i.hero.cta1": "Falar sobre um projeto", "i.hero.cta2": "Ver todas as soluções",

    "i.prob.eyebrow": "O PROBLEMA",
    "i.prob.title1": "Muitos projetos estagnam",
    "i.prob.title2": "entre o design e a execução.",
    "i.prob.p1": "Depois de concluída a fase de engenharia, entrar num mercado desconhecido exige identificar fornecedores de confiança, mobilizar equipas, organizar logística e garantir recursos regionais — tudo isto exige um tempo considerável e um conhecimento local que muitas empresas não têm.",
    "i.prob.p2": "Esta é a fase crítica em que os projetos perdem impulso ou nunca chegam a arrancar.",

    "i.help.eyebrow": "COMO A ADPETROS AJUDA",
    "i.help.title1": "Uma estrutura pronta",
    "i.help.title2": "para colocar o projeto em movimento.",
    "i.help.s1t": "Estrutura e equipas", "i.help.s1p": "Ajudamos a montar as equipas técnicas e locais necessárias à operação.",
    "i.help.s2t": "Logística e mobilidade", "i.help.s2p": "Organizamos transporte, alojamento e mobilidade das equipas no terreno.",
    "i.help.s3t": "Fornecedores e supply chain", "i.help.s3p": "Selecionamos fornecedores locais de confiança para os materiais e serviços necessários.",
    "i.help.s4t": "Acompanhamento da implementação", "i.help.s4p": "Seguimos o projeto durante a fase de execução, ajustando o que for necessário.",

    "i.photo.eyebrow": "DO DESIGN À OPERAÇÃO",
    "i.photo.title1": "UM PLANO SÓ TEM VALOR",
    "i.photo.title2": "QUANDO ATINGE A OPERAÇÃO PLENA.",
    "i.photo.text": "Acompanhamos essa transição de perto, porque é nesta fase crítica que a maioria dos projetos sofre atrasos graves ou nunca chega a arrancar.",

    "i.inc.eyebrow": "O QUE ESTÁ INCLUÍDO",
    "i.inc.title1": "Tudo o que a operação",
    "i.inc.title2": "precisa para arrancar.",
    "i.inc1": "Apoio à instalação", "i.inc2": "Requisitos locais",
    "i.inc3": "Mobilidade", "i.inc4": "Logística",
    "i.inc5": "Segurança", "i.inc6": "Gestão de frotas",
    "i.inc7": "Supply chain", "i.inc8": "Acompanhamento da implementação",

    "i.ben.eyebrow": "BENEFÍCIOS",
    "i.ben.title1": "O que muda",
    "i.ben.title2": "ao ter um parceiro local.",
    "i.ben1.t": "Menos tempo perdido", "i.ben1.p": "Uma estrutura já preparada reduz o tempo entre decidir entrar num mercado e começar a operar.",
    "i.ben2.t": "Menos risco operacional", "i.ben2.p": "Conhecemos os fornecedores, os requisitos e as particularidades locais que normalmente atrasam um projeto.",
    "i.ben3.t": "Um único ponto de coordenação", "i.ben3.p": "Em vez de gerir várias empresas separadas, o cliente tem uma estrutura integrada a coordenar tudo.",

    "i.mk.text": "Esta solução apoia-se na experiência que construímos na Venezuela, América do Sul e África.",
    "i.mk.link": "Conhecer a nossa experiência local",

    "i.ex.eyebrow": "EXEMPLO PRÁTICO", "i.ex.title": "Imagine a seguinte situação:",
    "i.ex.p": "Uma empresa internacional quer entrar no mercado venezuelano, mas enfrenta uma teia complexa de documentação e logística: vistos, licenças, alojamento das equipas, segurança e transporte local. Tratamos destes requisitos como um único processo simplificado, garantindo que a sua equipa chega ao terreno em segurança, totalmente equipada e pronta para operar e viver nas melhores condições.",
    "i.cta.eyebrow": "FALE CONNOSCO",
    "i.cta.title1": "Precisa de apoio para implementar",
    "i.cta.title2": "um projeto de óleo e gás na Venezuela?",
    "i.cta.p": "Fale com a nossa equipa sobre a operação que pretende desenvolver.",
    "i.cta.btn1": "Falar com a equipa", "i.cta.btn2": "Ver todas as soluções",
  },
  'en': {
    "i.hero.eyebrow": "SOLUTIONS · PROJECT IMPLEMENTATION",
    "i.hero.title1": "From planning",
    "i.hero.title2": "to on-site execution.",
    "i.hero.lead": "Having a robust engineering design is only the first step. Bringing it to life requires field teams, vetted suppliers, precise logistics, and a local infrastructure capable of turning that technical blueprint into a fully active operation.",
    "i.hero.cta1": "Talk about a project", "i.hero.cta2": "See all solutions",

    "i.prob.eyebrow": "THE PROBLEM",
    "i.prob.title1": "Many projects stall",
    "i.prob.title2": "between design and execution.",
    "i.prob.p1": "Once the engineering phase is complete, entering an unfamiliar market means identifying trustworthy suppliers, mobilizing teams, organizing logistics, and securing regional resources — all of which take considerable time and local knowledge that many companies lack.",
    "i.prob.p2": "This is the critical phase where projects lose momentum or never get off the ground.",

    "i.help.eyebrow": "HOW ADPETROS HELPS",
    "i.help.title1": "A structure ready",
    "i.help.title2": "to put the project in motion.",
    "i.help.s1t": "Structure and teams", "i.help.s1p": "We help build the technical and local teams the operation needs.",
    "i.help.s2t": "Logistics and mobility", "i.help.s2p": "We organise transport, accommodation and mobility for teams on the ground.",
    "i.help.s3t": "Suppliers and supply chain", "i.help.s3p": "We select trustworthy local suppliers for the necessary materials and services.",
    "i.help.s4t": "Implementation support", "i.help.s4p": "We follow the project through execution, adjusting whatever is needed.",

    "i.photo.eyebrow": "FROM DESIGN TO OPERATION",
    "i.photo.title1": "A PLAN ONLY HAS VALUE",
    "i.photo.title2": "ONCE IT REACHES FULL OPERATION.",
    "i.photo.text": "We manage that transition closely, because that is the critical stage where most projects experience severe delays or fail to launch entirely.",

    "i.inc.eyebrow": "WHAT'S INCLUDED",
    "i.inc.title1": "Everything the operation",
    "i.inc.title2": "needs to get moving.",
    "i.inc1": "Installation support", "i.inc2": "Local requirements",
    "i.inc3": "Mobility", "i.inc4": "Logistics",
    "i.inc5": "Security", "i.inc6": "Fleet management",
    "i.inc7": "Supply chain", "i.inc8": "Implementation follow-up",

    "i.ben.eyebrow": "BENEFITS",
    "i.ben.title1": "What changes",
    "i.ben.title2": "with a local partner.",
    "i.ben1.t": "Less time lost", "i.ben1.p": "A structure that's already in place shortens the time between deciding to enter a market and starting to operate.",
    "i.ben2.t": "Less operational risk", "i.ben2.p": "We know the suppliers, requirements and local particularities that usually delay a project.",
    "i.ex.eyebrow": "PRACTICAL EXAMPLE", "i.ex.title": "Imagine the following situation:",
    "i.ex.p": "An international company wants to enter the Venezuelan market but faces a complex web of documentation and logistics: visas, permits, crew housing, security, and local transportation. We manage these requirements as a single, streamlined process, ensuring your team arrives on the ground safely, fully equipped and ready to operate and live in the best conditions.",
    "i.ben3.t": "A single point of coordination", "i.ben3.p": "Instead of managing several separate companies, the client has one integrated structure coordinating everything.",

    "i.mk.text": "This solution builds on the experience we've gained in Venezuela, South America and Africa.",
    "i.mk.link": "See our local experience",

    "i.cta.eyebrow": "GET IN TOUCH",
    "i.cta.title1": "Need support to implement",
    "i.cta.title2": "an oil & gas project in Venezuela?",
    "i.cta.p": "Talk to our team about the operation you want to develop.",
    "i.cta.btn1": "Talk to the team", "i.cta.btn2": "See all solutions",
  },
  'es': {
    "i.hero.eyebrow": "SOLUCIONES · IMPLEMENTACIÓN DE PROYECTOS",
    "i.hero.title1": "De la planificación",
    "i.hero.title2": "a la ejecución en el terreno.",
    "i.hero.lead": "Contar con un diseño de ingeniería robusto es solo el primer paso. Llevarlo a la práctica requiere equipos de campo, proveedores validados, logística precisa y una infraestructura local capaz de convertir ese proyecto técnico en una operación plenamente activa.",
    "i.hero.cta1": "Hablar sobre un proyecto", "i.hero.cta2": "Ver todas las soluciones",

    "i.prob.eyebrow": "EL PROBLEMA",
    "i.prob.title1": "Muchos proyectos se estancan",
    "i.prob.title2": "entre el diseño y la ejecución.",
    "i.prob.p1": "Una vez completada la fase de ingeniería, entrar en un mercado desconocido exige identificar proveedores de confianza, movilizar equipos, organizar la logística y asegurar recursos regionales — todo ello exige un tiempo considerable y un conocimiento local que muchas empresas no tienen.",
    "i.prob.p2": "Esta es la fase crítica en la que los proyectos pierden impulso o nunca llegan a arrancar.",

    "i.help.eyebrow": "CÓMO AYUDA ADPETROS",
    "i.help.title1": "Una estructura lista",
    "i.help.title2": "para poner el proyecto en marcha.",
    "i.help.s1t": "Estructura y equipos", "i.help.s1p": "Ayudamos a formar los equipos técnicos y locales necesarios para la operación.",
    "i.help.s2t": "Logística y movilidad", "i.help.s2p": "Organizamos el transporte, alojamiento y movilidad de los equipos en el terreno.",
    "i.help.s3t": "Proveedores y supply chain", "i.help.s3p": "Seleccionamos proveedores locales de confianza para los materiales y servicios necesarios.",
    "i.help.s4t": "Apoyo a la implementación", "i.help.s4p": "Seguimos el proyecto durante la fase de ejecución, ajustando lo que sea necesario.",

    "i.photo.eyebrow": "DEL DISEÑO A LA OPERACIÓN",
    "i.photo.title1": "UN PLAN SOLO TIENE VALOR",
    "i.photo.title2": "CUANDO ALCANZA LA OPERACIÓN PLENA.",
    "i.photo.text": "Gestionamos esa transición de cerca, porque es en esta fase crítica donde la mayoría de los proyectos sufre retrasos graves o nunca llega a arrancar.",

    "i.inc.eyebrow": "QUÉ INCLUYE",
    "i.inc.title1": "Todo lo que la operación",
    "i.inc.title2": "necesita para arrancar.",
    "i.inc1": "Apoyo a la instalación", "i.inc2": "Requisitos locales",
    "i.inc3": "Movilidad", "i.inc4": "Logística",
    "i.inc5": "Seguridad", "i.inc6": "Gestión de flotas",
    "i.inc7": "Supply chain", "i.inc8": "Seguimiento de la implementación",

    "i.ben.eyebrow": "BENEFICIOS",
    "i.ben.title1": "Qué cambia",
    "i.ben.title2": "al tener un socio local.",
    "i.ex.eyebrow": "EJEMPLO PRÁCTICO", "i.ex.title": "Imagine la siguiente situación:",
    "i.ex.p": "Una empresa internacional quiere entrar en el mercado venezolano, pero se enfrenta a una compleja red de documentación y logística: visados, permisos, alojamiento de los equipos, seguridad y transporte local. Gestionamos estos requisitos como un único proceso simplificado, garantizando que su equipo llegue al terreno con seguridad, totalmente equipado y listo para operar y vivir en las mejores condiciones.",
    "i.ben1.t": "Menos tiempo perdido", "i.ben1.p": "Una estructura ya preparada reduce el tiempo entre decidir entrar en un mercado y empezar a operar.",
    "i.ben2.t": "Menos riesgo operativo", "i.ben2.p": "Conocemos los proveedores, los requisitos y las particularidades locales que normalmente retrasan un proyecto.",
    "i.ben3.t": "Un único punto de coordinación", "i.ben3.p": "En lugar de gestionar varias empresas separadas, el cliente tiene una estructura integrada coordinándolo todo.",

    "i.mk.text": "Esta solución se apoya en la experiencia que hemos construido en Venezuela, Sudamérica y África.",
    "i.mk.link": "Conocer nuestra experiencia local",

    "i.cta.eyebrow": "HABLEMOS",
    "i.cta.title1": "¿Necesita apoyo para implementar",
    "i.cta.title2": "un proyecto de petróleo y gas en Venezuela?",
    "i.cta.p": "Hable con nuestro equipo sobre la operación que desea desarrollar.",
    "i.cta.btn1": "Hablar con el equipo", "i.cta.btn2": "Ver todas las soluciones",
  },
})

sol_steps = sol_steps_html([
    {'n': '01', 'tkey': 'i.help.s1t', 'tdef': 'Estrutura e equipas', 'pkey': 'i.help.s1p', 'pdef': 'Ajudamos a montar as equipas técnicas e locais necessárias à operação.'},
    {'n': '02', 'tkey': 'i.help.s2t', 'tdef': 'Logística e mobilidade', 'pkey': 'i.help.s2p', 'pdef': 'Organizamos transporte, alojamento e mobilidade das equipas no terreno.'},
    {'n': '03', 'tkey': 'i.help.s3t', 'tdef': 'Fornecedores e supply chain', 'pkey': 'i.help.s3p', 'pdef': 'Selecionamos fornecedores locais de confiança para os materiais e serviços necessários.'},
    {'n': '04', 'tkey': 'i.help.s4t', 'tdef': 'Acompanhamento da implementação', 'pkey': 'i.help.s4p', 'pdef': 'Seguimos o projeto durante a fase de execução, ajustando o que for necessário.'},
], extra_style='margin-top:48px')

checklist = check_list_html([
    {'key': 'i.inc1', 'text': 'Apoio à instalação'}, {'key': 'i.inc2', 'text': 'Requisitos locais'},
    {'key': 'i.inc3', 'text': 'Mobilidade'}, {'key': 'i.inc4', 'text': 'Logística'},
    {'key': 'i.inc5', 'text': 'Segurança'}, {'key': 'i.inc6', 'text': 'Gestão de frotas'},
    {'key': 'i.inc7', 'text': 'Supply chain'}, {'key': 'i.inc8', 'text': 'Acompanhamento da implementação'},
])

photo_section = photo_section_html(
    img='/assets/img/new/h3.jpg', alt='Plataforma de perfuração offshore com embarcação de apoio',
    eyebrow_key='i.photo.eyebrow', eyebrow_def='DO DESIGN À OPERAÇÃO',
    title1_key='i.photo.title1', title1_def='UM PLANO SÓ TEM VALOR',
    title2_key='i.photo.title2', title2_def='QUANDO ATINGE A OPERAÇÃO PLENA.',
    text_key='i.photo.text', text_def='Acompanhamos essa transição de perto, porque é nesta fase crítica que a maioria dos projetos sofre atrasos graves ou nunca chega a arrancar.',
    extra_class='photo-section-strong',
)

benefits = why_mini_html([
    {'icon': WHY_ICONS[0], 'tkey': 'i.ben1.t', 'tdef': 'Menos tempo perdido', 'pkey': 'i.ben1.p', 'pdef': 'Uma estrutura já preparada reduz o tempo entre decidir entrar num mercado e começar a operar.'},
    {'icon': WHY_ICONS[1], 'tkey': 'i.ben2.t', 'tdef': 'Menos risco operacional', 'pkey': 'i.ben2.p', 'pdef': 'Conhecemos os fornecedores, os requisitos e as particularidades locais que normalmente atrasam um projeto.'},
    {'icon': WHY_ICONS[2], 'tkey': 'i.ben3.t', 'tdef': 'Um único ponto de coordenação', 'pkey': 'i.ben3.p', 'pdef': 'Em vez de gerir várias empresas separadas, o cliente tem uma estrutura integrada a coordenar tudo.'},
])

example_html = example_situation_html(
    prefix='i', eyebrow_def='EXEMPLO PRÁTICO', title_def='Imagine a seguinte situação:',
    text_def='Uma empresa internacional quer entrar no mercado venezuelano, mas enfrenta uma teia complexa de documentação e logística: vistos, licenças, alojamento das equipas, segurança e transporte local. Tratamos destes requisitos como um único processo simplificado, garantindo que a sua equipa chega ao terreno em segurança, totalmente equipada e pronta para operar e viver nas melhores condições.',
    img='/assets/img/new/v10.jpg', alt='Equipa satisfeita a comemorar com o polegar em riste após o trabalho estar tratado',
    cta_href='/contactos/', cta_key='cta.project', cta_def='Falar sobre o meu projeto',
)
BODY = f"""
<header class="hero" id="top" data-theme="dark">
  <div class="hero-bg"><img src="/assets/img/13-lg.jpg" alt="Equipa técnica em campo numa instalação industrial" loading="eager"><div class="glow"></div><div class="hero-vignette"></div></div>
  <div class="hero-inner hero-inner-centered">
    <div class="eyebrow" data-i18n="i.hero.eyebrow">SOLUÇÕES · IMPLEMENTAÇÃO DE PROJETOS</div>
    <h1 id="heroTitle">
      <span class="line-mask"><span class="line" data-i18n="i.hero.title1">Do planeamento</span></span>
      <span class="line-mask"><span class="line sub" data-i18n="i.hero.title2">à execução no terreno.</span></span>
    </h1>
    <p class="hero-lead" data-i18n="i.hero.lead">Ter um projeto de engenharia robusto é apenas o primeiro passo. Pô-lo em prática exige equipas no terreno, fornecedores validados, logística precisa e uma infraestrutura local capaz de transformar esse projeto técnico numa operação totalmente ativa.</p>
    <div class="hero-ctas">
      <a href="/contactos/" class="btn btn-primary" data-i18n="i.hero.cta1">Falar sobre um projeto
        <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      <a href="/solucoes/" class="btn btn-ghost" data-i18n="i.hero.cta2">Ver todas as soluções</a>
    </div>
  </div>
</header>

<section class="section" data-theme="white">
  <div class="container">
    <div class="prob-grid">
      <div class="prob-copy">
        <div class="eyebrow" data-i18n="i.prob.eyebrow">O PROBLEMA</div>
        <h2 class="big-title reveal"><span data-i18n="i.prob.title1">Muitos projetos estagnam</span> <span class="title-dim" data-i18n="i.prob.title2">entre o design e a execução.</span></h2>
        <p class="reveal dim prob-p" data-i18n="i.prob.p1">Depois de concluída a fase de engenharia, entrar num mercado desconhecido exige identificar fornecedores de confiança, mobilizar equipas, organizar logística e garantir recursos regionais — tudo isto exige um tempo considerável e um conhecimento local que muitas empresas não têm.</p>
        <p class="reveal dim prob-p" data-i18n="i.prob.p2">Esta é a fase crítica em que os projetos perdem impulso ou nunca chegam a arrancar.</p>
      </div>
      <div class="prob-photo reveal-img"><img src="/assets/img/new/v5.jpg" alt="Plataforma de perfuração offshore, vista aérea" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="section" data-theme="dark">
  <div class="container">
    <div class="header-row">
      <div>
        <div class="eyebrow" data-i18n="i.help.eyebrow">COMO A ADPETROS AJUDA</div>
        <h2 class="big-title reveal"><span data-i18n="i.help.title1">Uma estrutura pronta</span> <span class="title-dim" data-i18n="i.help.title2">para colocar o projeto em movimento.</span></h2>
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
        <div class="eyebrow" data-i18n="i.inc.eyebrow">O QUE ESTÁ INCLUÍDO</div>
        <h2 class="big-title reveal"><span data-i18n="i.inc.title1">Tudo o que a operação</span> <span class="title-dim" data-i18n="i.inc.title2">precisa para arrancar.</span></h2>
      </div>
    </div>
    {checklist}
  </div>
</section>

<section class="section" data-theme="dark">
  <div class="container">
    <div class="header-row">
      <div>
        <div class="eyebrow" data-i18n="i.ben.eyebrow">BENEFÍCIOS</div>
        <h2 class="big-title reveal"><span data-i18n="i.ben.title1">O que muda</span> <span class="title-dim" data-i18n="i.ben.title2">ao ter um parceiro local.</span></h2>
      </div>
    </div>
    {benefits}
    <div class="sol-markets-note reveal" style="margin-top:40px">
      <svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="8.5" stroke="currentColor" stroke-width="1.6"/><path d="M3.5 12h17M12 3.5c2.2 2.3 3.3 5.1 3.3 8.5s-1.1 6.2-3.3 8.5c-2.2-2.3-3.3-5.1-3.3-8.5s1.1-6.2 3.3-8.5z" stroke="currentColor" stroke-width="1.6"/></svg>
      <p><span data-i18n="i.mk.text">Esta solução apoia-se na experiência que construímos na Venezuela, América do Sul e África.</span> <a href="/sobre-nos/" style="color:var(--accent);font-weight:600" data-i18n="i.mk.link">Conhecer a nossa experiência local</a></p>
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
        <div class="eyebrow" data-i18n="i.cta.eyebrow">FALE CONNOSCO</div>
        <h2 class="big-title reveal"><span data-i18n="i.cta.title1">Precisa de apoio para implementar</span> <span class="title-dim" data-i18n="i.cta.title2">um projeto de óleo e gás na Venezuela?</span></h2>
        <p class="reveal" data-i18n="i.cta.p">Fale com a nossa equipa sobre a operação que pretende desenvolver.</p>
        <div class="hero-ctas reveal">
          <a href="/contactos/" class="btn btn-primary" data-i18n="i.cta.btn1">Falar com a equipa
            <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <a href="/solucoes/" class="btn btn-ghost" data-i18n="i.cta.btn2">Ver todas as soluções</a>
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
  "name": "Project Implementation — ADPETROS",
  "url": "https://www.adpetros.com/solucoes/implementacao-de-projetos/",
  "provider": {"@type":"Organization","name":"ADPETROS"}
}
</script>"""

html = build_page(
    title="Project Implementation — ADPETROS Solutions",
    description="Teams, local structure, logistics, suppliers, mobility and supply chain to put projects into execution in the market.",
    path="/solucoes/implementacao-de-projetos/",
    active_nav="solutions",
    body_html=BODY,
    i18n_dict=I18N,
    include_hero_split=True,
    extra_js="",
    ld_json=LD_JSON,
)

write_page('solucoes/implementacao-de-projetos/index.html', html)
