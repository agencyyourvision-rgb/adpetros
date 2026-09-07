import sys
sys.path.insert(0, '/home/claude/adpetros-site/build')
from sitegen import build_page, write_page, merge_i18n, why_bento_html, WHY_BENTO_I18N

I18N = merge_i18n({
  'pt': {
    "an.hero.eyebrow": "SOBRE A ADPETROS",
    "an.hero.title1": "Uma empresa de engenharia",
    "an.hero.title2": "pensada para operar para além da engenharia.",
    "an.hero.lead": "A ADPETROS é uma empresa europeia de engenharia de petróleo e gás, com profunda experiência nos setores do petróleo, gás e petroquímico. Possuímos um conhecimento alargado e anos de experiência local dos mercados onde atuamos, da Venezuela à restante América do Sul e África.",
    "an.hero.cta1": "Falar com a equipa",
    "an.hero.cta2": "Conhecer as soluções",

    "an.who.eyebrow": "QUEM SOMOS",
    "an.who.title1": "Engenharia europeia.",
    "an.who.title2": "Presença onde o projeto acontece.",
    "an.who.lead": "A ADPETROS foi fundada para resolver um desafio específico: excelentes projetos de engenharia falham quando faltam as condições para os executar no terreno. Combinamos rigor técnico europeu com experiência profunda construída diretamente nos mercados onde atuamos. Como resultado, o seu projeto tem sucesso não só no papel, através de um estudo de viabilidade sólido, mas também através da capacidade prática de o executar no terreno.",
    "an.who.s1t": "Engenharia europeia",
    "an.who.s1p": "Conhecimento técnico aplicado a projetos e operações industriais complexas.",
    "an.who.s2t": "Experiência local",
    "an.who.s2p": "Conhecimento dos mercados e do contexto onde desenvolvemos os projetos.",
    "an.who.s3t": "Rede no terreno",
    "an.who.s3p": "Profissionais, fornecedores e parceiros que conhecemos e em quem confiamos.",
    "an.who.s4t": "Capacidade de execução",
    "an.who.s4p": "Estrutura preparada para transformar planeamento em operação real.",

    "an.why2.eyebrow": "O DESAFIO",
    "an.why2.title1": "Um projeto internacional exige",
    "an.why2.title2": "mais do que um estudo de engenharia sólido.",
    "an.why2.p1": "Quando uma empresa decide implementar um ativo num mercado que não conhece, a engenharia costuma ser o elemento mais previsível do processo. O que normalmente atrasa ou compromete um projeto é tudo o resto: compreender o contexto local, encontrar fornecedores de confiança, organizar equipas, coordenar a logística e estabelecer as condições práticas necessárias para executar.",
    "an.why2.p2": "É por isso que a ADPETROS combina engenharia disciplinada com experiência profunda, garantindo que o seu projeto nunca tem de enfrentar esses obstáculos sozinho.",


    "an.mk.eyebrow": "MERCADOS",
    "an.mk.title1": "Conhecer o terreno",
    "an.mk.title2": "faz a diferença.",
    "an.mk.lead": "A experiência local não é um discurso — é o que nos permite antecipar problemas que só aparecem depois de um projeto já estar em curso.",
    "an.mk.ve.tag": "MERCADO PRINCIPAL",
    "an.mk.ve.title": "Venezuela",
    "an.mk.ve.p1": "A Venezuela é o mercado onde a ADPETROS construiu a sua experiência mais profunda, trabalhando ao mais alto nível junto da PDVSA e de outras entidades-chave do setor. Compreendemos profundamente o setor petrolífero e de gás do país, incluindo os seus parâmetros regulatórios e operacionais distintos. Além disso, mantemos relações próximas com empresas, entidades e profissionais locais.",
    "an.mk.ve.p2": "Este conhecimento acumulado permite-nos apoiar empresas internacionais que procuram avaliar oportunidades, investir ou desenvolver projetos no país sobre uma base de confiança já estabelecida, em vez de partirem do zero.",
    "an.mk.sa.tag": "AMÉRICA DO SUL",
    "an.mk.sa.title": "América do Sul",
    "an.mk.sa.p1": "A experiência adquirida na Venezuela e a proximidade cultural e operacional da região permitem à ADPETROS avaliar e apoiar projetos noutros mercados sul-americanos, de acordo com as necessidades específicas de cada operação.",
    "an.mk.af.tag": "ÁFRICA",
    "an.mk.af.title": "África",
    "an.mk.af.p1": "Trabalhamos ao mais alto nível com as entidades de cada mercado — GEPETROL na Guiné Equatorial, SNPC no Congo Brazzaville, o Ministério dos Hidrocarbonetos na República Democrática do Congo, e ADNOC nos Emirados Árabes Unidos — com destaque também para Angola, aplicando a mesma lógica de combinar engenharia com conhecimento do contexto local em cada um destes mercados.",

    "an.eng.eyebrow": "A BASE TÉCNICA",
    "an.eng.title1": "Engenharia que sustenta",
    "an.eng.title2": "tudo o resto.",
    "an.eng.lead": "A capacidade de execução da ADPETROS assenta em conhecimento técnico sólido, organizado nas seguintes especialidades.",
    "an.eng.c1": "Engenharia de processo",
    "an.eng.c2": "Engenharia mecânica",
    "an.eng.c3": "Engenharia civil e estrutural",
    "an.eng.c4": "Engenharia elétrica e instrumentação",
    "an.eng.c5": "Integridade e inspeção de ativos",
    "an.eng.c6": "Automação e controlo de processo",
    "an.eng.cta": "Conhecer a nossa engenharia",

    "an.work.eyebrow": "EXPERIÊNCIA LOCAL. OPORTUNIDADES GLOBAIS.",
    "an.work.title1": "Quer investir em óleo e gás?",
    "an.work.title2": "Comece pelo parceiro certo.",
    "an.work.p1": "A ADPETROS conhece o mercado venezuelano, os seus principais operadores e as estruturas necessárias para desenvolver novos negócios no setor.",
    "an.work.p2": "Com relações construídas junto de entidades governamentais, instituições, operadores e parceiros locais, ajudamos empresas internacionais a compreender o mercado, identificar oportunidades e criar as condições necessárias para avançar.",
    "an.work.p3": "Da oportunidade à operação, somos a ligação entre o investimento internacional e o mercado local.",

    "an.cta.eyebrow": "FALE CONNOSCO",
    "an.cta.title1": "Quer avaliar um projeto de óleo e gás",
    "an.cta.title2": "na Venezuela? Somos os parceiros certos.",
    "an.cta.p": "Fale com a nossa equipa ou explore as soluções que oferecemos para cada fase do projeto.",
    "an.cta.cta1": "Falar com a equipa",
    "an.cta.cta2": "Conhecer as soluções",
  },
  'en': {
    "an.hero.eyebrow": "ABOUT ADPETROS",
    "an.hero.title1": "An engineering company",
    "an.hero.title2": "built to operate beyond engineering.",
    "an.hero.lead": "ADPETROS is a European oil & gas engineering company with deep expertise across the oil, gas, and petrochemical sectors. We possess extensive knowledge and years of local experience of the markets where we operate, spanning from Venezuela, wider South America, and Africa.",
    "an.hero.cta1": "Talk to the team",
    "an.hero.cta2": "See our solutions",

    "an.who.eyebrow": "WHO WE ARE",
    "an.who.title1": "European engineering.",
    "an.who.title2": "Presence where the project happens.",
    "an.who.lead": "ADPETROS was founded to solve a specific challenge: excellent engineering projects fail when the conditions to execute them on the ground are missing. We combine European technical rigor with deep experience built directly within the markets where we operate. As a result, your project succeeds not only on paper through a strong feasibility study, but through the practical capability to execute it in the field.",
    "an.who.s1t": "European engineering",
    "an.who.s1p": "Technical knowledge applied to complex industrial projects and operations.",
    "an.who.s2t": "Local experience",
    "an.who.s2p": "Knowledge of the markets and the context where we develop projects.",
    "an.who.s3t": "Network on the ground",
    "an.who.s3p": "Professionals, suppliers and partners we know and trust.",
    "an.who.s4t": "Execution capability",
    "an.who.s4p": "A structure built to turn planning into a real operation.",

    "an.why2.eyebrow": "THE CHALLENGE",
    "an.why2.title1": "An international project requires",
    "an.why2.title2": "more than a strong engineering study.",
    "an.why2.p1": "When a company decides to deploy an asset in an unfamiliar market, engineering is usually the most predictable element of the process. What typically delays or compromises a project is everything else: understanding the local context, finding trustworthy suppliers, organizing teams, coordinating logistics, and establishing the practical conditions required to execute.",
    "an.why2.p2": "That's why ADPETROS combines disciplined engineering with deep experience, ensuring your project never has to navigate those hurdles alone.",


    "an.mk.eyebrow": "MARKETS",
    "an.mk.title1": "Knowing the ground",
    "an.mk.title2": "makes the difference.",
    "an.mk.lead": "Local experience isn't a talking point — it's what lets us anticipate problems that only appear once a project is already underway.",
    "an.mk.ve.tag": "PRIMARY MARKET",
    "an.mk.ve.title": "Venezuela",
    "an.mk.ve.p1": "Venezuela is the market where ADPETROS has built its deepest experience, working at the highest level alongside PDVSA and other key sector entities. We thoroughly understand the country's oil and gas sector, including its distinct regulatory and operational parameters. Furthermore, we maintain close relationships with local companies, entities, and industry professionals.",
    "an.mk.ve.p2": "This accumulated knowledge enables us to support international companies looking to assess opportunities, invest, or develop projects in the country on an already established foundation of trust, rather than starting from zero.",
    "an.mk.sa.tag": "SOUTH AMERICA",
    "an.mk.sa.title": "South America",
    "an.mk.sa.p1": "The experience gained in Venezuela, together with the region's cultural and operational proximity, allows ADPETROS to assess and support projects in other South American markets, according to the specific needs of each operation.",
    "an.mk.af.tag": "AFRICA",
    "an.mk.af.title": "Africa",
    "an.mk.af.p1": "We work at the highest level with the entities in each market — GEPETROL in Equatorial Guinea, SNPC in Congo Brazzaville, the Ministry of Hydrocarbons in the Democratic Republic of Congo, and ADNOC in the United Arab Emirates — with particular focus also on Angola, applying the same logic of combining engineering with knowledge of the local context in each of these markets.",

    "an.eng.eyebrow": "THE TECHNICAL BASE",
    "an.eng.title1": "Engineering that supports",
    "an.eng.title2": "everything else.",
    "an.eng.lead": "ADPETROS' execution capability rests on solid technical knowledge, organised across the following specialities.",
    "an.eng.c1": "Process engineering",
    "an.eng.c2": "Mechanical engineering",
    "an.eng.c3": "Civil and structural engineering",
    "an.eng.c4": "Electrical engineering and instrumentation",
    "an.eng.c5": "Asset integrity and inspection",
    "an.eng.c6": "Automation and process control",
    "an.eng.cta": "See our engineering",

    "an.work.eyebrow": "LOCAL EXPERIENCE. GLOBAL OPPORTUNITIES.",
    "an.work.title1": "Want to invest in oil and gas?",
    "an.work.title2": "Start with the right partner.",
    "an.work.p1": "ADPETROS knows the Venezuelan market, its main operators and the structures needed to develop new business in the sector.",
    "an.work.p2": "With relationships built with government entities, institutions, operators and local partners, we help international companies understand the market, identify opportunities and create the conditions needed to move forward.",
    "an.work.p3": "From opportunity to operation, we are the link between international investment and the local market.",

    "an.cta.eyebrow": "GET IN TOUCH",
    "an.cta.title1": "Want to evaluate an oil & gas project",
    "an.cta.title2": "in Venezuela? We're the right partner.",
    "an.cta.p": "Talk to our team or explore the solutions we offer for each phase of a project.",
    "an.cta.cta1": "Talk to the team",
    "an.cta.cta2": "See our solutions",
  },
  'es': {
    "an.hero.eyebrow": "SOBRE ADPETROS",
    "an.hero.title1": "Una empresa de ingeniería",
    "an.hero.title2": "pensada para operar más allá de la ingeniería.",
    "an.hero.lead": "ADPETROS es una empresa europea de ingeniería de petróleo y gas, con amplia experiencia en los sectores de petróleo, gas y petroquímico. Poseemos un conocimiento extenso y años de experiencia local en los mercados donde operamos, desde Venezuela hasta el resto de Sudamérica y África.",
    "an.hero.cta1": "Hablar con el equipo",
    "an.hero.cta2": "Conocer las soluciones",

    "an.who.eyebrow": "QUIÉNES SOMOS",
    "an.who.title1": "Ingeniería europea.",
    "an.who.title2": "Presencia donde el proyecto ocurre.",
    "an.who.lead": "ADPETROS fue fundada para resolver un desafío específico: los excelentes proyectos de ingeniería fracasan cuando faltan las condiciones para ejecutarlos en el terreno. Combinamos el rigor técnico europeo con una experiencia profunda construida directamente en los mercados donde operamos. Como resultado, su proyecto tiene éxito no solo sobre el papel, mediante un sólido estudio de viabilidad, sino también gracias a la capacidad práctica de ejecutarlo en el terreno.",
    "an.who.s1t": "Ingeniería europea",
    "an.who.s1p": "Conocimiento técnico aplicado a proyectos y operaciones industriales complejas.",
    "an.who.s2t": "Experiencia local",
    "an.who.s2p": "Conocimiento de los mercados y del contexto donde desarrollamos los proyectos.",
    "an.who.s3t": "Red en el terreno",
    "an.who.s3p": "Profesionales, proveedores y socios que conocemos y en quienes confiamos.",
    "an.who.s4t": "Capacidad de ejecución",
    "an.who.s4p": "Estructura preparada para transformar la planificación en una operación real.",

    "an.why2.eyebrow": "EL DESAFÍO",
    "an.why2.title1": "Un proyecto internacional exige",
    "an.why2.title2": "más que un sólido estudio de ingeniería.",
    "an.why2.p1": "Cuando una empresa decide desplegar un activo en un mercado que no conoce, la ingeniería suele ser el elemento más previsible del proceso. Lo que normalmente retrasa o compromete un proyecto es todo lo demás: comprender el contexto local, encontrar proveedores de confianza, organizar equipos, coordinar la logística y establecer las condiciones prácticas necesarias para ejecutar.",
    "an.why2.p2": "Por eso ADPETROS combina ingeniería disciplinada con experiencia profunda, garantizando que su proyecto nunca tenga que enfrentar esos obstáculos solo.",


    "an.mk.eyebrow": "MERCADOS",
    "an.mk.title1": "Conocer el terreno",
    "an.mk.title2": "marca la diferencia.",
    "an.mk.lead": "La experiencia local no es un discurso — es lo que nos permite anticipar problemas que solo aparecen cuando un proyecto ya está en marcha.",
    "an.mk.ve.tag": "MERCADO PRINCIPAL",
    "an.mk.ve.title": "Venezuela",
    "an.mk.ve.p1": "Venezuela es el mercado donde ADPETROS ha construido su experiencia más profunda, trabajando al más alto nivel junto a PDVSA y otras entidades clave del sector. Comprendemos profundamente el sector petrolero y de gas del país, incluyendo sus parámetros regulatorios y operativos distintivos. Además, mantenemos relaciones cercanas con empresas, entidades y profesionales locales.",
    "an.mk.ve.p2": "Este conocimiento acumulado nos permite apoyar a empresas internacionales que buscan evaluar oportunidades, invertir o desarrollar proyectos en el país sobre una base de confianza ya establecida, en lugar de partir de cero.",
    "an.mk.sa.tag": "SUDAMÉRICA",
    "an.mk.sa.title": "Sudamérica",
    "an.mk.sa.p1": "La experiencia adquirida en Venezuela, junto con la proximidad cultural y operativa de la región, permite a ADPETROS evaluar y apoyar proyectos en otros mercados sudamericanos, según las necesidades específicas de cada operación.",
    "an.mk.af.tag": "ÁFRICA",
    "an.mk.af.title": "África",
    "an.mk.af.p1": "Trabajamos al más alto nivel con las entidades de cada mercado — GEPETROL en Guinea Ecuatorial, SNPC en Congo Brazzaville, el Ministerio de Hidrocarburos en la República Democrática del Congo, y ADNOC en los Emiratos Árabes Unidos — con especial atención también a Angola, aplicando la misma lógica de combinar ingeniería con conocimiento del contexto local en cada uno de estos mercados.",

    "an.eng.eyebrow": "LA BASE TÉCNICA",
    "an.eng.title1": "Ingeniería que sostiene",
    "an.eng.title2": "todo lo demás.",
    "an.eng.lead": "La capacidad de ejecución de ADPETROS se apoya en un conocimiento técnico sólido, organizado en las siguientes especialidades.",
    "an.eng.c1": "Ingeniería de procesos",
    "an.eng.c2": "Ingeniería mecánica",
    "an.eng.c3": "Ingeniería civil y estructural",
    "an.eng.c4": "Ingeniería eléctrica e instrumentación",
    "an.eng.c5": "Integridad e inspección de activos",
    "an.eng.c6": "Automatización y control de procesos",
    "an.eng.cta": "Conocer nuestra ingeniería",

    "an.work.eyebrow": "EXPERIENCIA LOCAL. OPORTUNIDADES GLOBALES.",
    "an.work.title1": "¿Quiere invertir en petróleo y gas?",
    "an.work.title2": "Empiece por el socio adecuado.",
    "an.work.p1": "ADPETROS conoce el mercado venezolano, sus principales operadores y las estructuras necesarias para desarrollar nuevos negocios en el sector.",
    "an.work.p2": "Con relaciones construidas junto a entidades gubernamentales, instituciones, operadores y socios locales, ayudamos a empresas internacionales a comprender el mercado, identificar oportunidades y crear las condiciones necesarias para avanzar.",
    "an.work.p3": "De la oportunidad a la operación, somos el vínculo entre la inversión internacional y el mercado local.",

    "an.cta.eyebrow": "HABLEMOS",
    "an.cta.title1": "¿Quiere evaluar un proyecto de petróleo y gas",
    "an.cta.title2": "en Venezuela? Somos el socio adecuado.",
    "an.cta.p": "Hable con nuestro equipo o explore las soluciones que ofrecemos para cada fase del proyecto.",
    "an.cta.cta1": "Hablar con el equipo",
    "an.cta.cta2": "Conocer las soluciones",
  },
})
for _lang in ('pt', 'en', 'es'):
    I18N[_lang].update(WHY_BENTO_I18N[_lang])

BODY = f"""
<header class="hero hero-breathe" id="top" data-theme="dark" style="min-height:90vh">
  <div class="hero-bg">
    <img src="/assets/img/18-lg.jpg" alt="Instalações industriais ao entardecer">
    <div class="glow"></div>
    <div class="hero-vignette"></div>
  </div>
  <div class="hero-inner hero-inner-centered">
    <div class="eyebrow" data-i18n="an.hero.eyebrow">SOBRE A ADPETROS</div>
    <h1 id="heroTitle">
      <span class="line-mask"><span class="line" data-i18n="an.hero.title1">Uma empresa de engenharia</span></span>
      <span class="line-mask"><span class="line sub" data-i18n="an.hero.title2">pensada para operar para além da engenharia.</span></span>
    </h1>
    <p class="hero-lead" data-i18n="an.hero.lead">A ADPETROS é uma empresa europeia de engenharia de petróleo e gás, com profunda experiência nos setores do petróleo, gás e petroquímico. Possuímos um conhecimento alargado e anos de experiência local dos mercados onde atuamos, da Venezuela à restante América do Sul e África.</p>
    <div class="hero-ctas">
      <a href="/contactos/" class="btn btn-primary" data-i18n="an.hero.cta1">Falar com a equipa
        <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      <a href="/solucoes/" class="btn btn-ghost" data-i18n="an.hero.cta2">Conhecer as soluções</a>
    </div>
  </div>
</header>

<!-- 02 QUEM SOMOS -->
<section class="section" data-theme="dark">
  <div class="container">
    <div class="sol-top">
      <div>
        <div class="eyebrow" data-i18n="an.who.eyebrow">QUEM SOMOS</div>
        <h2 class="big-title reveal"><span data-i18n="an.who.title1">Engenharia europeia.</span> <span class="title-dim" data-i18n="an.who.title2">Presença onde o projeto acontece.</span></h2>
      </div>
      <p class="lead dim reveal" data-i18n="an.who.lead">A ADPETROS foi fundada para resolver um desafio específico: excelentes projetos de engenharia falham quando faltam as condições para os executar no terreno. Combinamos rigor técnico europeu com experiência profunda construída diretamente nos mercados onde atuamos. Como resultado, o seu projeto tem sucesso não só no papel, através de um estudo de viabilidade sólido, mas também através da capacidade prática de o executar no terreno.</p>
    </div>

    <div class="an-who-grid">
      <div class="sol-steps">
        <div class="sol-step flip-card reveal">
          <div class="n">01</div>
          <h4 data-i18n="an.who.s1t">Engenharia europeia</h4>
          <p data-i18n="an.who.s1p">Conhecimento técnico aplicado a projetos e operações industriais complexas.</p>
        </div>
        <div class="sol-step flip-card reveal">
          <div class="n">02</div>
          <h4 data-i18n="an.who.s2t">Experiência local</h4>
          <p data-i18n="an.who.s2p">Conhecimento dos mercados e do contexto onde desenvolvemos os projetos.</p>
        </div>
        <div class="sol-step flip-card reveal">
          <div class="n">03</div>
          <h4 data-i18n="an.who.s3t">Rede no terreno</h4>
          <p data-i18n="an.who.s3p">Profissionais, fornecedores e parceiros que conhecemos e em quem confiamos.</p>
        </div>
        <div class="sol-step flip-card reveal">
          <div class="n">04</div>
          <h4 data-i18n="an.who.s4t">Capacidade de execução</h4>
          <p data-i18n="an.who.s4p">Estrutura preparada para transformar planeamento em operação real.</p>
        </div>
      </div>
      <div class="an-float-wrap reveal-img">
        <div class="an-float-photo"><img src="/assets/img/11-lg.jpg" alt="Engenheiro da ADPETROS no terreno junto a uma instalação industrial" loading="lazy"></div>
      </div>
    </div>
  </div>
</section>

<!-- 03 PORQUE ESTE MODELO EXISTE -->
<section class="section" data-theme="white">
  <div class="container">
    <div class="sol-top">
      <div>
        <div class="eyebrow" data-i18n="an.why2.eyebrow">O DESAFIO</div>
        <h2 class="big-title reveal"><span data-i18n="an.why2.title1">Um projeto internacional exige</span> <span class="title-dim" data-i18n="an.why2.title2">mais do que um estudo de engenharia sólido.</span></h2>
      </div>
      <div style="max-width:520px">
        <p class="reveal dim" data-i18n="an.why2.p1" style="line-height:1.75;font-size:16px">Quando uma empresa decide implementar um ativo num mercado que não conhece, a engenharia costuma ser o elemento mais previsível do processo. O que normalmente atrasa ou compromete um projeto é tudo o resto: compreender o contexto local, encontrar fornecedores de confiança, organizar equipas, coordenar a logística e estabelecer as condições práticas necessárias para executar.</p>
        <p class="reveal dim" data-i18n="an.why2.p2" style="line-height:1.75;font-size:16px;margin-top:16px">É por isso que a ADPETROS combina engenharia disciplinada com experiência profunda, garantindo que o seu projeto nunca tem de enfrentar esses obstáculos sozinho.</p>
      </div>
    </div>
  </div>
</section>

<!-- 04 MENOS COMPLEXIDADE, MAIS POSSIBILIDADES (componente reutilizado da Home, sem alterações) -->
{why_bento_html(cta_href='/contactos/')}

<!-- 05 MERCADOS -->
<section class="section" data-theme="dark">
  <div class="container">
    <div class="header-row">
      <div>
        <div class="eyebrow" data-i18n="an.mk.eyebrow">MERCADOS</div>
        <h2 class="big-title reveal"><span data-i18n="an.mk.title1">Conhecer o terreno</span> <span class="title-dim" data-i18n="an.mk.title2">faz a diferença.</span></h2>
      </div>
      <p class="lead dim reveal" data-i18n="an.mk.lead">A experiência local não é um discurso — é o que nos permite antecipar problemas que só aparecem depois de um projeto já estar em curso.</p>
    </div>

    <div class="contact-grid" style="margin-top:48px;align-items:stretch">
      <div class="glass contact-info-card reveal-img" style="padding:clamp(32px,4vw,48px)">
        <span class="m-tag" data-i18n="an.mk.ve.tag">MERCADO PRINCIPAL</span>
        <h3 style="font-family:var(--ff-display);font-size:clamp(24px,2.6vw,32px);font-weight:500;color:#fff;margin-top:14px" data-i18n="an.mk.ve.title">Venezuela</h3>
        <p style="margin-top:16px;line-height:1.7;color:var(--ink-dim)" data-i18n="an.mk.ve.p1">A Venezuela é o mercado onde a ADPETROS construiu a sua experiência mais profunda, trabalhando ao mais alto nível junto da PDVSA e de outras entidades-chave do setor. Compreendemos profundamente o setor petrolífero e de gás do país, incluindo os seus parâmetros regulatórios e operacionais distintos. Além disso, mantemos relações próximas com empresas, entidades e profissionais locais.</p>
        <p style="margin-top:14px;line-height:1.7;color:var(--ink-dim)" data-i18n="an.mk.ve.p2">Este conhecimento acumulado permite-nos apoiar empresas internacionais que procuram avaliar oportunidades, investir ou desenvolver projetos no país sobre uma base de confiança já estabelecida, em vez de partirem do zero.</p>
      </div>
      <div style="display:flex;flex-direction:column;gap:24px">
        <div class="glass contact-info-card reveal-img" style="flex:1;justify-content:center">
          <span class="m-tag" data-i18n="an.mk.sa.tag">AMÉRICA DO SUL</span>
          <h3 style="font-family:var(--ff-display);font-size:clamp(20px,2vw,25px);font-weight:500;color:#fff;margin-top:12px" data-i18n="an.mk.sa.title">América do Sul</h3>
          <p style="margin-top:12px;line-height:1.7;color:var(--ink-dim);font-size:14.5px" data-i18n="an.mk.sa.p1">A experiência adquirida na Venezuela e a proximidade cultural e operacional da região permitem à ADPETROS avaliar e apoiar projetos noutros mercados sul-americanos, de acordo com as necessidades específicas de cada operação.</p>
        </div>
        <div class="glass contact-info-card reveal-img" style="flex:1;justify-content:center">
          <span class="m-tag" data-i18n="an.mk.af.tag">ÁFRICA</span>
          <h3 style="font-family:var(--ff-display);font-size:clamp(20px,2vw,25px);font-weight:500;color:#fff;margin-top:12px" data-i18n="an.mk.af.title">África</h3>
          <p style="margin-top:12px;line-height:1.7;color:var(--ink-dim);font-size:14.5px" data-i18n="an.mk.af.p1">Trabalhamos ao mais alto nível com as entidades de cada mercado — GEPETROL na Guiné Equatorial, SNPC no Congo Brazzaville, o Ministério dos Hidrocarbonetos na República Democrática do Congo, e ADNOC nos Emirados Árabes Unidos — com destaque também para Angola, aplicando a mesma lógica de combinar engenharia com conhecimento do contexto local em cada um destes mercados.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 06 ENGENHARIA -->
<section class="section" data-theme="white">
  <div class="container">
    <div class="header-row">
      <div>
        <div class="eyebrow" data-i18n="an.eng.eyebrow">A BASE TÉCNICA</div>
        <h2 class="big-title reveal"><span data-i18n="an.eng.title1">Engenharia que sustenta</span> <span class="title-dim" data-i18n="an.eng.title2">tudo o resto.</span></h2>
        <p class="lead dim reveal" style="margin-top:20px" data-i18n="an.eng.lead">A capacidade de execução da ADPETROS assenta em conhecimento técnico sólido, organizado nas seguintes especialidades.</p>
      </div>
    </div>

    <div class="grid eng-grid stagger" style="margin-top:44px">
      <div class="eng-card">
        <svg viewBox="0 0 24 24" fill="none"><path d="M4 12h4l2-7 4 14 2-7h4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <h4 data-i18n="an.eng.c1">Engenharia de processo</h4>
      </div>
      <div class="eng-card">
        <svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="1.6"/><path d="M19 12a7 7 0 00-.13-1.36l2.03-1.58-2-3.46-2.39.96a7.03 7.03 0 00-2.36-1.36L13.8 3h-3.6l-.35 2.2a7.03 7.03 0 00-2.36 1.36l-2.39-.96-2 3.46 2.03 1.58A7 7 0 005 12c0 .46.04.9.13 1.36l-2.03 1.58 2 3.46 2.39-.96c.7.58 1.5 1.05 2.36 1.36l.35 2.2h3.6l.35-2.2a7.03 7.03 0 002.36-1.36l2.39.96 2-3.46-2.03-1.58c.09-.46.13-.9.13-1.36z" stroke="currentColor" stroke-width="1.3"/></svg>
        <h4 data-i18n="an.eng.c2">Engenharia mecânica</h4>
      </div>
      <div class="eng-card">
        <svg viewBox="0 0 24 24" fill="none"><path d="M3 21h18M5 21V9l7-5 7 5v12M9 21v-6h6v6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <h4 data-i18n="an.eng.c3">Engenharia civil e estrutural</h4>
      </div>
      <div class="eng-card">
        <svg viewBox="0 0 24 24" fill="none"><path d="M13 2L4 14h7l-1 8 9-12h-7l1-8z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
        <h4 data-i18n="an.eng.c4">Engenharia elétrica e instrumentação</h4>
      </div>
      <div class="eng-card">
        <svg viewBox="0 0 24 24" fill="none"><path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6l8-4z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M9 12l2 2 4-4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <h4 data-i18n="an.eng.c5">Integridade e inspeção de ativos</h4>
      </div>
      <div class="eng-card">
        <svg viewBox="0 0 24 24" fill="none"><rect x="4" y="4" width="16" height="16" rx="2" stroke="currentColor" stroke-width="1.6"/><path d="M9 4v16M4 9h5M4 15h5" stroke="currentColor" stroke-width="1.6"/></svg>
        <h4 data-i18n="an.eng.c6">Automação e controlo de processo</h4>
      </div>
    </div>

    <div style="margin-top:44px" class="reveal">
      <a href="/solucoes/engenharia/" class="btn btn-ghost" data-i18n="an.eng.cta">Conhecer a nossa engenharia
        <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
    </div>
  </div>
</section>

<!-- 07 A NOSSA FORMA DE TRABALHAR -->
<section class="section photo-section photo-section-strong" data-theme="dark">
  <div class="photo-section-bg"><img src="/assets/img/new/h1.jpg" alt="Equipa da ADPETROS a analisar um projeto junto a uma instalação industrial" loading="lazy"></div>
  <div class="container photo-section-content">
    <div class="sol-top">
      <div>
        <div class="eyebrow" data-i18n="an.work.eyebrow">EXPERIÊNCIA LOCAL. OPORTUNIDADES GLOBAIS.</div>
        <h2 class="big-title reveal"><span data-i18n="an.work.title1">Quer investir em óleo e gás?</span> <span class="title-dim" data-i18n="an.work.title2">Comece pelo parceiro certo.</span></h2>
      </div>
      <div style="max-width:520px">
        <p class="reveal dim" style="line-height:1.75;font-size:16px" data-i18n="an.work.p1">A ADPETROS conhece o mercado venezuelano, os seus principais operadores e as estruturas necessárias para desenvolver novos negócios no setor.</p>
        <p class="reveal dim" style="line-height:1.75;font-size:16px;margin-top:16px" data-i18n="an.work.p2">Com relações construídas junto de entidades governamentais, instituições, operadores e parceiros locais, ajudamos empresas internacionais a compreender o mercado, identificar oportunidades e criar as condições necessárias para avançar.</p>
        <p class="reveal" style="line-height:1.6;font-size:18px;font-weight:500;color:#fff;margin-top:24px;padding-top:22px;border-top:1px solid var(--line-dark)" data-i18n="an.work.p3">Da oportunidade à operação, somos a ligação entre o investimento internacional e o mercado local.</p>
      </div>
    </div>
  </div>
</section>

<!-- 08 CTA FINAL -->
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
        <div class="eyebrow" data-i18n="an.cta.eyebrow">FALE CONNOSCO</div>
        <h2 class="big-title reveal"><span data-i18n="an.cta.title1">Quer perceber como podemos</span> <span class="title-dim" data-i18n="an.cta.title2">ajudar o seu projeto?</span></h2>
        <p class="reveal" data-i18n="an.cta.p">Fale com a nossa equipa ou explore as soluções que oferecemos para cada fase do projeto.</p>
        <div class="hero-ctas reveal">
          <a href="/contactos/" class="btn btn-primary" data-i18n="an.cta.cta1">Falar com a equipa
            <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <a href="/solucoes/" class="btn btn-ghost" data-i18n="an.cta.cta2">Conhecer as soluções</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""

LD_JSON = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "name": "About Us — ADPETROS",
  "url": "https://www.adpetros.com/sobre-nos/"
}
</script>"""

html = build_page(
    title="About Us — ADPETROS",
    description="ADPETROS is a European oil & gas engineering company that combines European engineering, local experience and execution capability to develop projects in Venezuela, South America and Africa.",
    path="/sobre-nos/",
    active_nav="about",
    body_html=BODY,
    i18n_dict=I18N,
    include_hero_split=True,
    extra_js="",
    ld_json=LD_JSON,
)

write_page('sobre-nos/index.html', html)
