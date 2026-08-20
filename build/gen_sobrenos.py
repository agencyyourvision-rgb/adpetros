import sys
sys.path.insert(0, '/home/claude/adpetros-site/build')
from sitegen import build_page, write_page, merge_i18n, why_bento_html, WHY_BENTO_I18N

I18N = merge_i18n({
  'pt': {
    "an.hero.eyebrow": "SOBRE A ADPETROS",
    "an.hero.title1": "Uma empresa de engenharia",
    "an.hero.title2": "pensada para operar para além da engenharia.",
    "an.hero.lead": "A ADPetros é uma empresa europeia de engenharia industrial, com experiência nos setores do petróleo, gás e indústria petroquímica e conhecimento dos mercados onde atua — da Venezuela à América do Sul e África.",
    "an.hero.cta1": "Falar com a equipa",
    "an.hero.cta2": "Conhecer as soluções",

    "an.who.eyebrow": "QUEM SOMOS",
    "an.who.title1": "Engenharia europeia.",
    "an.who.title2": "Presença onde o projeto acontece.",
    "an.who.lead": "A ADPetros nasceu para responder a um problema concreto: bons projetos de engenharia perdem-se quando faltam as condições para os executar no terreno. Combinamos rigor técnico europeu com experiência acumulada nos mercados onde atuamos, para que um projeto não dependa apenas de um bom estudo, mas também da capacidade real de o pôr em prática.",
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
    "an.why2.title2": "mais do que um bom estudo de engenharia.",
    "an.why2.p1": "Quando uma empresa decide desenvolver um projeto num mercado que não conhece bem, a engenharia costuma ser a parte mais previsível do processo. O que normalmente atrasa ou compromete um projeto é tudo o resto: compreender o contexto local, encontrar fornecedores de confiança, organizar equipas, coordenar logística e criar as condições práticas para executar.",
    "an.why2.p2": "É por isso que a ADPetros combina engenharia com experiência local — para que um projeto não tenha de resolver esse caminho sozinho.",


    "an.mk.eyebrow": "MERCADOS",
    "an.mk.title1": "Conhecer o terreno",
    "an.mk.title2": "faz a diferença.",
    "an.mk.lead": "A experiência local não é um discurso — é o que nos permite antecipar problemas que só aparecem depois de um projeto já estar em curso.",
    "an.mk.ve.tag": "MERCADO PRINCIPAL",
    "an.mk.ve.title": "Venezuela",
    "an.mk.ve.p1": "A Venezuela é o mercado onde a ADPetros construiu a sua experiência mais profunda. Conhecemos o setor do petróleo e gás do país, as suas particularidades regulatórias e operacionais, e mantemos relações próximas com empresas, entidades e profissionais locais.",
    "an.mk.ve.p2": "Esse conhecimento acumulado permite-nos apoiar empresas internacionais que queiram avaliar oportunidades, investir ou desenvolver projetos no país com uma base de confiança já construída — em vez de partirem do zero.",
    "an.mk.sa.tag": "AMÉRICA DO SUL",
    "an.mk.sa.title": "América do Sul",
    "an.mk.sa.p1": "A experiência adquirida na Venezuela e a proximidade cultural e operacional da região permitem à ADPetros avaliar e apoiar projetos noutros mercados sul-americanos, de acordo com as necessidades específicas de cada operação.",
    "an.mk.af.tag": "ÁFRICA",
    "an.mk.af.title": "África",
    "an.mk.af.p1": "Com destaque para Angola e a Guiné Equatorial, a ADPetros acompanha também mercados na África Central, aplicando a mesma lógica de combinar engenharia com conhecimento do contexto local.",

    "an.eng.eyebrow": "A BASE TÉCNICA",
    "an.eng.title1": "Engenharia que sustenta",
    "an.eng.title2": "tudo o resto.",
    "an.eng.lead": "A capacidade de execução da ADPetros assenta em conhecimento técnico sólido, organizado nas seguintes especialidades.",
    "an.eng.c1": "Engenharia de processo",
    "an.eng.c2": "Engenharia mecânica",
    "an.eng.c3": "Engenharia civil e estrutural",
    "an.eng.c4": "Engenharia elétrica e instrumentação",
    "an.eng.c5": "Integridade e inspeção de ativos",
    "an.eng.c6": "Automação e controlo de processo",
    "an.eng.cta": "Conhecer a nossa engenharia",

    "an.work.eyebrow": "A NOSSA FORMA DE TRABALHAR",
    "an.work.title1": "O projeto não termina",
    "an.work.title2": "na engenharia.",
    "an.work.p1": "A ADPetros procura construir relações de longo prazo com os seus clientes, acompanhando não apenas o desenvolvimento técnico, mas também os desafios necessários para colocar cada projeto em funcionamento.",
    "an.work.p2": "Honestidade, conhecimento técnico, experiência local e capacidade de execução orientam a forma como trabalhamos. O nosso objetivo é simples: criar as condições para o projeto avançar.",

    "an.cta.eyebrow": "FALE CONNOSCO",
    "an.cta.title1": "Quer perceber como podemos",
    "an.cta.title2": "ajudar o seu projeto?",
    "an.cta.p": "Fale com a nossa equipa ou explore as soluções que oferecemos para cada fase do projeto.",
    "an.cta.cta1": "Falar com a equipa",
    "an.cta.cta2": "Conhecer as soluções",
  },
  'en': {
    "an.hero.eyebrow": "ABOUT ADPETROS",
    "an.hero.title1": "An engineering company",
    "an.hero.title2": "built to operate beyond engineering.",
    "an.hero.lead": "ADPetros is a European industrial engineering company with experience in the oil, gas and petrochemical sectors and knowledge of the markets where it operates — from Venezuela to South America and Africa.",
    "an.hero.cta1": "Talk to the team",
    "an.hero.cta2": "See our solutions",

    "an.who.eyebrow": "WHO WE ARE",
    "an.who.title1": "European engineering.",
    "an.who.title2": "Presence where the project happens.",
    "an.who.lead": "ADPetros was created to answer a concrete problem: good engineering projects get lost when the conditions to execute them on the ground are missing. We combine European technical rigour with experience built in the markets where we operate, so a project doesn't depend only on a good study, but also on the real capacity to put it into practice.",
    "an.who.s1t": "European engineering",
    "an.who.s1p": "Technical knowledge applied to complex industrial projects and operations.",
    "an.who.s2t": "Local experience",
    "an.who.s2p": "Knowledge of the markets and the context where we develop projects.",
    "an.who.s3t": "Network on the ground",
    "an.who.s3p": "Professionals, suppliers and partners we know and trust.",
    "an.who.s4t": "Execution capability",
    "an.who.s4p": "A structure built to turn planning into a real operation.",

    "an.why2.eyebrow": "THE CHALLENGE",
    "an.why2.title1": "An international project needs",
    "an.why2.title2": "more than a good engineering study.",
    "an.why2.p1": "When a company decides to develop a project in a market it doesn't know well, engineering is usually the most predictable part of the process. What normally delays or compromises a project is everything else: understanding the local context, finding trustworthy suppliers, organising teams, coordinating logistics and creating the practical conditions to execute.",
    "an.why2.p2": "That's why ADPetros combines engineering with local experience — so a project doesn't have to figure that path out alone.",


    "an.mk.eyebrow": "MARKETS",
    "an.mk.title1": "Knowing the ground",
    "an.mk.title2": "makes the difference.",
    "an.mk.lead": "Local experience isn't a talking point — it's what lets us anticipate problems that only appear once a project is already underway.",
    "an.mk.ve.tag": "PRIMARY MARKET",
    "an.mk.ve.title": "Venezuela",
    "an.mk.ve.p1": "Venezuela is the market where ADPetros has built its deepest experience. We know the country's oil and gas sector, its regulatory and operational particularities, and we maintain close relationships with local companies, entities and professionals.",
    "an.mk.ve.p2": "That accumulated knowledge lets us support international companies looking to assess opportunities, invest or develop projects in the country on an already-built foundation of trust — instead of starting from zero.",
    "an.mk.sa.tag": "SOUTH AMERICA",
    "an.mk.sa.title": "South America",
    "an.mk.sa.p1": "The experience gained in Venezuela, together with the region's cultural and operational proximity, allows ADPetros to assess and support projects in other South American markets, according to the specific needs of each operation.",
    "an.mk.af.tag": "AFRICA",
    "an.mk.af.title": "Africa",
    "an.mk.af.p1": "With particular focus on Angola and Equatorial Guinea, ADPetros also follows markets in Central Africa, applying the same logic of combining engineering with knowledge of the local context.",

    "an.eng.eyebrow": "THE TECHNICAL BASE",
    "an.eng.title1": "Engineering that supports",
    "an.eng.title2": "everything else.",
    "an.eng.lead": "ADPetros' execution capability rests on solid technical knowledge, organised across the following specialities.",
    "an.eng.c1": "Process engineering",
    "an.eng.c2": "Mechanical engineering",
    "an.eng.c3": "Civil and structural engineering",
    "an.eng.c4": "Electrical engineering and instrumentation",
    "an.eng.c5": "Asset integrity and inspection",
    "an.eng.c6": "Automation and process control",
    "an.eng.cta": "See our engineering",

    "an.work.eyebrow": "HOW WE WORK",
    "an.work.title1": "The project doesn't end",
    "an.work.title2": "at engineering.",
    "an.work.p1": "ADPetros looks to build long-term relationships with its clients, following not only the technical development but also the challenges needed to put each project into operation.",
    "an.work.p2": "Honesty, technical knowledge, local experience and execution capability guide how we work. Our goal is simple: create the conditions for the project to move forward.",

    "an.cta.eyebrow": "GET IN TOUCH",
    "an.cta.title1": "Want to see how we can",
    "an.cta.title2": "help your project?",
    "an.cta.p": "Talk to our team or explore the solutions we offer for each phase of a project.",
    "an.cta.cta1": "Talk to the team",
    "an.cta.cta2": "See our solutions",
  },
  'es': {
    "an.hero.eyebrow": "SOBRE ADPETROS",
    "an.hero.title1": "Una empresa de ingeniería",
    "an.hero.title2": "pensada para operar más allá de la ingeniería.",
    "an.hero.lead": "ADPetros es una empresa europea de ingeniería industrial, con experiencia en los sectores de petróleo, gas e industria petroquímica y conocimiento de los mercados donde opera — desde Venezuela hasta Sudamérica y África.",
    "an.hero.cta1": "Hablar con el equipo",
    "an.hero.cta2": "Conocer las soluciones",

    "an.who.eyebrow": "QUIÉNES SOMOS",
    "an.who.title1": "Ingeniería europea.",
    "an.who.title2": "Presencia donde el proyecto ocurre.",
    "an.who.lead": "ADPetros nació para responder a un problema concreto: los buenos proyectos de ingeniería se pierden cuando faltan las condiciones para ejecutarlos en el terreno. Combinamos el rigor técnico europeo con la experiencia acumulada en los mercados donde operamos, para que un proyecto no dependa solo de un buen estudio, sino también de la capacidad real de llevarlo a cabo.",
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
    "an.why2.title2": "más que un buen estudio de ingeniería.",
    "an.why2.p1": "Cuando una empresa decide desarrollar un proyecto en un mercado que no conoce bien, la ingeniería suele ser la parte más previsible del proceso. Lo que normalmente retrasa o compromete un proyecto es todo lo demás: comprender el contexto local, encontrar proveedores de confianza, organizar equipos, coordinar la logística y crear las condiciones prácticas para ejecutar.",
    "an.why2.p2": "Por eso ADPetros combina ingeniería con experiencia local — para que un proyecto no tenga que resolver ese camino solo.",


    "an.mk.eyebrow": "MERCADOS",
    "an.mk.title1": "Conocer el terreno",
    "an.mk.title2": "marca la diferencia.",
    "an.mk.lead": "La experiencia local no es un discurso — es lo que nos permite anticipar problemas que solo aparecen cuando un proyecto ya está en marcha.",
    "an.mk.ve.tag": "MERCADO PRINCIPAL",
    "an.mk.ve.title": "Venezuela",
    "an.mk.ve.p1": "Venezuela es el mercado donde ADPetros ha construido su experiencia más profunda. Conocemos el sector de petróleo y gas del país, sus particularidades regulatorias y operativas, y mantenemos relaciones cercanas con empresas, entidades y profesionales locales.",
    "an.mk.ve.p2": "Ese conocimiento acumulado nos permite apoyar a empresas internacionales que deseen evaluar oportunidades, invertir o desarrollar proyectos en el país sobre una base de confianza ya construida — en lugar de partir de cero.",
    "an.mk.sa.tag": "SUDAMÉRICA",
    "an.mk.sa.title": "Sudamérica",
    "an.mk.sa.p1": "La experiencia adquirida en Venezuela, junto con la proximidad cultural y operativa de la región, permite a ADPetros evaluar y apoyar proyectos en otros mercados sudamericanos, según las necesidades específicas de cada operación.",
    "an.mk.af.tag": "ÁFRICA",
    "an.mk.af.title": "África",
    "an.mk.af.p1": "Con especial atención a Angola y Guinea Ecuatorial, ADPetros también sigue mercados en África Central, aplicando la misma lógica de combinar ingeniería con conocimiento del contexto local.",

    "an.eng.eyebrow": "LA BASE TÉCNICA",
    "an.eng.title1": "Ingeniería que sostiene",
    "an.eng.title2": "todo lo demás.",
    "an.eng.lead": "La capacidad de ejecución de ADPetros se apoya en un conocimiento técnico sólido, organizado en las siguientes especialidades.",
    "an.eng.c1": "Ingeniería de procesos",
    "an.eng.c2": "Ingeniería mecánica",
    "an.eng.c3": "Ingeniería civil y estructural",
    "an.eng.c4": "Ingeniería eléctrica e instrumentación",
    "an.eng.c5": "Integridad e inspección de activos",
    "an.eng.c6": "Automatización y control de procesos",
    "an.eng.cta": "Conocer nuestra ingeniería",

    "an.work.eyebrow": "NUESTRA FORMA DE TRABAJAR",
    "an.work.title1": "El proyecto no termina",
    "an.work.title2": "en la ingeniería.",
    "an.work.p1": "ADPetros busca construir relaciones a largo plazo con sus clientes, acompañando no solo el desarrollo técnico, sino también los desafíos necesarios para poner en marcha cada proyecto.",
    "an.work.p2": "Honestidad, conocimiento técnico, experiencia local y capacidad de ejecución guían nuestra forma de trabajar. Nuestro objetivo es simple: crear las condiciones para que el proyecto avance.",

    "an.cta.eyebrow": "HABLEMOS",
    "an.cta.title1": "¿Quiere entender cómo podemos",
    "an.cta.title2": "ayudar a su proyecto?",
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
    <div class="glow"></div>
    <div class="hero-vignette"></div>
  </div>
  <div class="hero-inner hero-inner-centered">
    <div class="eyebrow" data-i18n="an.hero.eyebrow">SOBRE A ADPETROS</div>
    <h1 id="heroTitle">
      <span class="line-mask"><span class="line" data-i18n="an.hero.title1">Uma empresa de engenharia</span></span>
      <span class="line-mask"><span class="line sub" data-i18n="an.hero.title2">pensada para operar para além da engenharia.</span></span>
    </h1>
    <p class="hero-lead reveal" data-i18n="an.hero.lead">A ADPetros é uma empresa europeia de engenharia industrial, com experiência nos setores do petróleo, gás e indústria petroquímica e conhecimento dos mercados onde atua — da Venezuela à América do Sul e África.</p>
    <div class="hero-ctas reveal">
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
      <p class="lead dim reveal" data-i18n="an.who.lead">A ADPetros nasceu para responder a um problema concreto: bons projetos de engenharia perdem-se quando faltam as condições para os executar no terreno. Combinamos rigor técnico europeu com experiência acumulada nos mercados onde atuamos, para que um projeto não dependa apenas de um bom estudo, mas também da capacidade real de o pôr em prática.</p>
    </div>

    <div class="sol-steps" style="margin-top:56px">
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
  </div>
</section>

<!-- 03 PORQUE ESTE MODELO EXISTE -->
<section class="section" data-theme="white">
  <div class="container">
    <div class="sol-top">
      <div>
        <div class="eyebrow" data-i18n="an.why2.eyebrow">O DESAFIO</div>
        <h2 class="big-title reveal"><span data-i18n="an.why2.title1">Um projeto internacional exige</span> <span class="title-dim" data-i18n="an.why2.title2">mais do que um bom estudo de engenharia.</span></h2>
      </div>
      <div style="max-width:520px">
        <p class="reveal dim" data-i18n="an.why2.p1" style="line-height:1.75;font-size:16px">Quando uma empresa decide desenvolver um projeto num mercado que não conhece bem, a engenharia costuma ser a parte mais previsível do processo. O que normalmente atrasa ou compromete um projeto é tudo o resto: compreender o contexto local, encontrar fornecedores de confiança, organizar equipas, coordenar logística e criar as condições práticas para executar.</p>
        <p class="reveal dim" data-i18n="an.why2.p2" style="line-height:1.75;font-size:16px;margin-top:16px">É por isso que a ADPetros combina engenharia com experiência local — para que um projeto não tenha de resolver esse caminho sozinho.</p>
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
        <p style="margin-top:16px;line-height:1.7;color:var(--ink-dim)" data-i18n="an.mk.ve.p1">A Venezuela é o mercado onde a ADPetros construiu a sua experiência mais profunda. Conhecemos o setor do petróleo e gás do país, as suas particularidades regulatórias e operacionais, e mantemos relações próximas com empresas, entidades e profissionais locais.</p>
        <p style="margin-top:14px;line-height:1.7;color:var(--ink-dim)" data-i18n="an.mk.ve.p2">Esse conhecimento acumulado permite-nos apoiar empresas internacionais que queiram avaliar oportunidades, investir ou desenvolver projetos no país com uma base de confiança já construída — em vez de partirem do zero.</p>
      </div>
      <div style="display:flex;flex-direction:column;gap:24px">
        <div class="glass contact-info-card reveal-img" style="flex:1;justify-content:center">
          <span class="m-tag" data-i18n="an.mk.sa.tag">AMÉRICA DO SUL</span>
          <h3 style="font-family:var(--ff-display);font-size:clamp(20px,2vw,25px);font-weight:500;color:#fff;margin-top:12px" data-i18n="an.mk.sa.title">América do Sul</h3>
          <p style="margin-top:12px;line-height:1.7;color:var(--ink-dim);font-size:14.5px" data-i18n="an.mk.sa.p1">A experiência adquirida na Venezuela e a proximidade cultural e operacional da região permitem à ADPetros avaliar e apoiar projetos noutros mercados sul-americanos, de acordo com as necessidades específicas de cada operação.</p>
        </div>
        <div class="glass contact-info-card reveal-img" style="flex:1;justify-content:center">
          <span class="m-tag" data-i18n="an.mk.af.tag">ÁFRICA</span>
          <h3 style="font-family:var(--ff-display);font-size:clamp(20px,2vw,25px);font-weight:500;color:#fff;margin-top:12px" data-i18n="an.mk.af.title">África</h3>
          <p style="margin-top:12px;line-height:1.7;color:var(--ink-dim);font-size:14.5px" data-i18n="an.mk.af.p1">Com destaque para Angola e a Guiné Equatorial, a ADPetros acompanha também mercados na África Central, aplicando a mesma lógica de combinar engenharia com conhecimento do contexto local.</p>
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
        <p class="lead dim reveal" style="margin-top:20px" data-i18n="an.eng.lead">A capacidade de execução da ADPetros assenta em conhecimento técnico sólido, organizado nas seguintes especialidades.</p>
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
<section class="section" data-theme="dark">
  <div class="container">
    <div class="sol-top">
      <div>
        <div class="eyebrow" data-i18n="an.work.eyebrow">A NOSSA FORMA DE TRABALHAR</div>
        <h2 class="big-title reveal"><span data-i18n="an.work.title1">O projeto não termina</span> <span class="title-dim" data-i18n="an.work.title2">na engenharia.</span></h2>
      </div>
      <div style="max-width:520px">
        <p class="reveal dim" style="line-height:1.75;font-size:16px" data-i18n="an.work.p1">A ADPetros procura construir relações de longo prazo com os seus clientes, acompanhando não apenas o desenvolvimento técnico, mas também os desafios necessários para colocar cada projeto em funcionamento.</p>
        <p class="reveal dim" style="line-height:1.75;font-size:16px;margin-top:16px" data-i18n="an.work.p2">Honestidade, conhecimento técnico, experiência local e capacidade de execução orientam a forma como trabalhamos. O nosso objetivo é simples: criar as condições para o projeto avançar.</p>
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
  "name": "Sobre Nós — ADPetros",
  "url": "https://www.adpetros.com/sobre-nos/"
}
</script>"""

html = build_page(
    title="Sobre Nós — ADPetros",
    description="A ADPetros é uma empresa europeia de engenharia industrial que combina engenharia europeia, experiência local e capacidade de execução para desenvolver projetos na Venezuela, América do Sul e África.",
    path="/sobre-nos/",
    active_nav="about",
    body_html=BODY,
    i18n_dict=I18N,
    include_hero_split=True,
    extra_js="",
    ld_json=LD_JSON,
)

write_page('sobre-nos/index.html', html)
