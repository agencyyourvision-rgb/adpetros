# ADPetros — site institucional

Site estático multi-página (HTML/CSS/JS autocontido, sem frameworks, GSAP + ScrollTrigger para as animações). Sem build step em produção — os ficheiros `index.html` de cada pasta já estão prontos a publicar tal como estão.

## Estrutura

```
/                                 Home (index.html — mantido à mão, não gerado)
/sobre-nos/                       Página "Sobre Nós"
/solucoes/                        Hub de soluções
/solucoes/engenharia/              
/solucoes/implementacao-de-projetos/
/solucoes/modernizacao-de-ativos/
/solucoes/energia-e-descarbonizacao/
/solucoes/procurement-e-sourcing/
/contactos/                       Página de contactos
/assets/                          Imagens, vídeos, ícones
/build/                           Scripts Python que geram as 8 páginas acima (exceto a Home)
```

A Home (`/index.html`) é o único ficheiro mantido diretamente — as outras 8 páginas são geradas pelos scripts em `/build` a partir de fragmentos partilhados em `/build/shared` (CSS, nav, footer, i18n, JS). Isto garante que uma alteração ao design system (cores, espaçamentos, animações, footer, botão de WhatsApp, etc.) feita em `/build/shared` se propaga a todas as páginas geradas de uma só vez.

## Pré-visualizar localmente

**Importante:** não abrir os ficheiros `.html` diretamente a fazer duplo-clique (protocolo `file://`). As páginas fora da Home usam caminhos absolutos a partir da raiz do site (ex: `/assets/img/...`), que só resolvem corretamente quando servidos por um servidor web — em `file://` aparecem como imagem quebrada. Isto é normal e não acontece depois de publicado (Vercel, Netlify, GitHub Pages, etc. servem sempre a partir da raiz do domínio).

Para testar localmente, a partir da pasta do projeto:

```bash
python3 -m http.server 8080
# ou
npx serve .
```

e abrir `http://localhost:8080/`.

## Regenerar as páginas (depois de editar `/build/shared`)

```bash
cd build
python3 gen_contactos.py
python3 gen_sobrenos.py
python3 gen_solucoes.py
python3 gen_sol_engenharia.py
python3 gen_sol_implementacao.py
python3 gen_sol_modernizacao.py
python3 gen_sol_energia.py
python3 gen_sol_procurement.py
```

Cada script escreve diretamente para a respetiva pasta na raiz do site. A Home não é afetada por estes scripts — as alterações ao design system que também devam aplicar-se à Home têm de ser replicadas manualmente no `<style>`/`<script>` do `index.html`.

## Deploy (GitHub + Vercel)

Site 100% estático — sem "Build Command" nem "Output Directory" a configurar no Vercel (deixar em branco / "Other"). O Vercel serve `/solucoes/index.html` automaticamente em `/solucoes/`, tal como as outras subpastas.

## Contactos confirmados

- **E-mail**: `info@adpetros.com` — usado no rodapé, na página de Contactos e como destino do formulário (abre o cliente de e-mail do visitante com a mensagem pronta a enviar).
- **WhatsApp / telefone**: `+971 52 433 1781`, confirmado pelo cliente. O botão flutuante de WhatsApp está ativo em todas as páginas (`WHATSAPP_NUMBER` em cada `<script>`, ou em `build/sitegen.py` para as páginas geradas) e o mesmo número está visível na página de Contactos.

## Por confirmar

- **Morada**: continua sem ser fornecida — aparece como "[a confirmar]" na página de Contactos até ser recebida.
- **LinkedIn**: idem, "[a confirmar]" na página de Contactos.
