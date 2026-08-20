import sys
sys.path.insert(0, '/home/claude/adpetros-site/build')
from sitegen import build_page, write_page, merge_i18n

I18N = merge_i18n({
    'pt': {
        "ct.eyebrow": "FALE CONNOSCO",
        "ct.title1": "Vamos falar", "ct.title2": "sobre o seu projeto.",
        "ct.lead": "Está a avaliar um investimento, uma operação ou uma oportunidade num dos mercados onde atuamos? Preencha o formulário ou utilize os contactos abaixo — a nossa equipa responde o mais brevemente possível.",
        "ct.form.name": "Nome", "ct.form.company": "Empresa",
        "ct.form.email": "E-mail", "ct.form.market": "Mercado de interesse",
        "ct.form.market.opt0": "Selecionar",
        "ct.form.market.opt1": "Venezuela", "ct.form.market.opt2": "América do Sul",
        "ct.form.market.opt3": "África", "ct.form.market.opt4": "Outro",
        "ct.form.message": "Descreva brevemente o projeto ou a oportunidade",
        "ct.form.submit": "Enviar mensagem",
        "ct.form.note": "Ao enviar, o seu cliente de e-mail abre com a mensagem pronta a enviar para a nossa equipa.",
        "ct.form.success": "Obrigado. A sua mensagem está pronta no seu cliente de e-mail — basta confirmar o envio.",
        "ct.info.email": "E-MAIL", "ct.info.phone": "TELEFONE", "ct.info.address": "MORADA",
        "ct.info.other": "OUTRAS FORMAS DE CONTACTO",
        "ct.info.phone.placeholder": "[a confirmar]",
        "ct.info.address.placeholder": "[a confirmar]",
        "ct.info.other.placeholder": "LinkedIn — [a confirmar]",
    },
    'en': {
        "ct.eyebrow": "GET IN TOUCH",
        "ct.title1": "Let's talk", "ct.title2": "about your project.",
        "ct.lead": "Are you assessing an investment, an operation or an opportunity in one of the markets where we operate? Fill in the form or use the contacts below — our team replies as soon as possible.",
        "ct.form.name": "Name", "ct.form.company": "Company",
        "ct.form.email": "Email", "ct.form.market": "Market of interest",
        "ct.form.market.opt0": "Select",
        "ct.form.market.opt1": "Venezuela", "ct.form.market.opt2": "South America",
        "ct.form.market.opt3": "Africa", "ct.form.market.opt4": "Other",
        "ct.form.message": "Briefly describe the project or opportunity",
        "ct.form.submit": "Send message",
        "ct.form.note": "On submit, your email client opens with the message ready to send to our team.",
        "ct.form.success": "Thank you. Your message is ready in your email client — just confirm sending.",
        "ct.info.email": "EMAIL", "ct.info.phone": "PHONE", "ct.info.address": "ADDRESS",
        "ct.info.other": "OTHER WAYS TO REACH US",
        "ct.info.phone.placeholder": "[to be confirmed]",
        "ct.info.address.placeholder": "[to be confirmed]",
        "ct.info.other.placeholder": "LinkedIn — [to be confirmed]",
    },
    'es': {
        "ct.eyebrow": "HABLEMOS",
        "ct.title1": "Hablemos", "ct.title2": "sobre su proyecto.",
        "ct.lead": "¿Está evaluando una inversión, una operación o una oportunidad en uno de los mercados donde operamos? Complete el formulario o utilice los contactos abajo — nuestro equipo responde lo antes posible.",
        "ct.form.name": "Nombre", "ct.form.company": "Empresa",
        "ct.form.email": "Correo electrónico", "ct.form.market": "Mercado de interés",
        "ct.form.market.opt0": "Seleccionar",
        "ct.form.market.opt1": "Venezuela", "ct.form.market.opt2": "América del Sur",
        "ct.form.market.opt3": "África", "ct.form.market.opt4": "Otro",
        "ct.form.message": "Describa brevemente el proyecto o la oportunidad",
        "ct.form.submit": "Enviar mensaje",
        "ct.form.note": "Al enviar, su cliente de correo se abrirá con el mensaje listo para enviar a nuestro equipo.",
        "ct.form.success": "Gracias. Su mensaje está listo en su cliente de correo — solo falta confirmar el envío.",
        "ct.info.email": "CORREO", "ct.info.phone": "TELÉFONO", "ct.info.address": "DIRECCIÓN",
        "ct.info.other": "OTRAS FORMAS DE CONTACTO",
        "ct.info.phone.placeholder": "[a confirmar]",
        "ct.info.address.placeholder": "[a confirmar]",
        "ct.info.other.placeholder": "LinkedIn — [a confirmar]",
    },
})

BODY = """
<section class="section page-hero" id="top" data-theme="dark">
  <div class="container">
    <div class="eyebrow" data-i18n="ct.eyebrow">FALE CONNOSCO</div>
    <h1 class="big-title reveal"><span data-i18n="ct.title1">Vamos falar</span> <span class="title-dim" data-i18n="ct.title2">sobre o seu projeto.</span></h1>
    <p class="page-hero-lead reveal" data-i18n="ct.lead">Está a avaliar um investimento, uma operação ou uma oportunidade num dos mercados onde atuamos? Preencha o formulário ou utilize os contactos abaixo — a nossa equipa responde o mais brevemente possível.</p>
  </div>

  <div class="container" style="margin-top:clamp(48px,6vw,72px)">
    <div class="contact-grid">
      <div class="glass contact-form-card reveal-img">
        <form id="contactForm">
          <div class="form-row">
            <div class="form-field">
              <label for="ctName" data-i18n="ct.form.name">Nome</label>
              <input type="text" id="ctName" name="name" required>
            </div>
            <div class="form-field">
              <label for="ctCompany" data-i18n="ct.form.company">Empresa</label>
              <input type="text" id="ctCompany" name="company">
            </div>
          </div>
          <div class="form-row">
            <div class="form-field">
              <label for="ctEmail" data-i18n="ct.form.email">E-mail</label>
              <input type="email" id="ctEmail" name="email" required>
            </div>
            <div class="form-field">
              <label for="ctMarket" data-i18n="ct.form.market">Mercado de interesse</label>
              <select id="ctMarket" name="market">
                <option value="" data-i18n="ct.form.market.opt0">Selecionar</option>
                <option value="Venezuela" data-i18n="ct.form.market.opt1">Venezuela</option>
                <option value="América do Sul" data-i18n="ct.form.market.opt2">América do Sul</option>
                <option value="África" data-i18n="ct.form.market.opt3">África</option>
                <option value="Outro" data-i18n="ct.form.market.opt4">Outro</option>
              </select>
            </div>
          </div>
          <div class="form-field">
            <label for="ctMessage" data-i18n="ct.form.message">Descreva brevemente o projeto ou a oportunidade</label>
            <textarea id="ctMessage" name="message" required></textarea>
          </div>
          <div class="form-submit-row">
            <button type="submit" class="btn btn-primary">
              <span data-i18n="ct.form.submit">Enviar mensagem</span>
              <svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </button>
            <span class="form-note" data-i18n="ct.form.note">Ao enviar, o seu cliente de e-mail abre com a mensagem pronta a enviar para a nossa equipa.</span>
          </div>
          <div class="form-success" id="ctSuccess" data-i18n="ct.form.success">Obrigado. A sua mensagem está pronta no seu cliente de e-mail — basta confirmar o envio.</div>
        </form>
      </div>

      <div class="glass contact-info-card reveal-img">
        <div class="contact-info-group">
          <h4 data-i18n="ct.info.email">E-MAIL</h4>
          <a href="mailto:geral@adpetros.com">geral@adpetros.com</a>
        </div>
        <div class="contact-info-divider"></div>
        <div class="contact-info-group">
          <h4 data-i18n="ct.info.phone">TELEFONE</h4>
          <p class="placeholder" data-i18n="ct.info.phone.placeholder">[a confirmar]</p>
        </div>
        <div class="contact-info-divider"></div>
        <div class="contact-info-group">
          <h4 data-i18n="ct.info.address">MORADA</h4>
          <p class="placeholder" data-i18n="ct.info.address.placeholder">[a confirmar]</p>
        </div>
        <div class="contact-info-divider"></div>
        <div class="contact-info-group">
          <h4 data-i18n="ct.info.other">OUTRAS FORMAS DE CONTACTO</h4>
          <p class="placeholder" data-i18n="ct.info.other.placeholder">LinkedIn — [a confirmar]</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""

EXTRA_JS = """/* ---------- Contact form: mailto passthrough (no backend yet) ---------- */
const contactForm = document.getElementById('contactForm');
if(contactForm){
  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('ctName').value;
    const company = document.getElementById('ctCompany').value;
    const email = document.getElementById('ctEmail').value;
    const market = document.getElementById('ctMarket').value;
    const message = document.getElementById('ctMessage').value;
    const subject = encodeURIComponent('Novo contacto via site — ' + name);
    const bodyLines = [
      'Nome: ' + name,
      'Empresa: ' + company,
      'E-mail: ' + email,
      'Mercado de interesse: ' + market,
      '',
      message
    ];
    const body = encodeURIComponent(bodyLines.join('\\n'));
    window.location.href = 'mailto:geral@adpetros.com?subject=' + subject + '&body=' + body;
    document.getElementById('ctSuccess').classList.add('show');
  });
}
"""

LD_JSON = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "name": "Contactos — ADPetros",
  "url": "https://www.adpetros.com/contactos/"
}
</script>"""

html = build_page(
    title="Contactos — ADPetros",
    description="Fale com a equipa da ADPetros sobre um projeto, uma operação ou uma oportunidade nos mercados onde atuamos.",
    path="/contactos/",
    active_nav="contact",
    body_html=BODY,
    i18n_dict=I18N,
    include_hero_split=False,
    extra_js=EXTRA_JS,
    ld_json=LD_JSON,
)

write_page('contactos/index.html', html)
