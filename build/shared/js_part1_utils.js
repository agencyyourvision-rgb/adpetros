/* ---------- Scroll lock utility (shared by mobile menu) ---------- */
let _scrollLockCount = 0, _scrollLockY = 0;
function lockScroll(){
  if(_scrollLockCount++ === 0){
    _scrollLockY = window.scrollY;
    document.body.style.position = 'fixed';
    document.body.style.top = -_scrollLockY + 'px';
    document.body.style.width = '100%';
    document.body.classList.add('no-scroll');
  }
}
function unlockScroll(){
  if(--_scrollLockCount <= 0){
    _scrollLockCount = 0;
    document.body.style.position = '';
    document.body.style.top = '';
    document.body.style.width = '';
    document.body.classList.remove('no-scroll');
    window.scrollTo(0, _scrollLockY);
  }
}

/* ---------- Nav solid on scroll + progress bar ---------- */
const nav = document.getElementById('nav');
const progress = document.getElementById('progress');
function onScroll(){
  nav.classList.toggle('solid', window.scrollY > 40);
  const h = document.documentElement;
  const scrollPct = (h.scrollTop || document.body.scrollTop) / ((h.scrollHeight || document.body.scrollHeight) - h.clientHeight) * 100;
  progress.style.width = (isFinite(scrollPct) ? scrollPct : 0) + '%';
}
window.addEventListener('scroll', onScroll, {passive:true});
onScroll();

/* ---------- Mobile menu ---------- */
const burger = document.getElementById('burger');
const mobileMenu = document.getElementById('mobileMenu');
burger.addEventListener('click', () => {
  const open = burger.classList.toggle('open');
  mobileMenu.classList.toggle('open', open);
  if(open) lockScroll(); else unlockScroll();
});
mobileMenu.querySelectorAll('a.m-link, .mobile-sub a').forEach(a=>{
  a.addEventListener('click', () => {
    burger.classList.remove('open');
    mobileMenu.classList.remove('open');
    unlockScroll();
  });
});
const mToggleSolutions = document.getElementById('mToggleSolutions');
const mItemSolutions = document.getElementById('mItemSolutions');
if(mToggleSolutions && mItemSolutions){
  mToggleSolutions.addEventListener('click', (e) => {
    e.preventDefault();
    e.stopPropagation();
    const open = mItemSolutions.classList.toggle('open');
    mToggleSolutions.setAttribute('aria-expanded', open);
  });
}

/* ---------- Language switch (desktop dropdown) ---------- */
const langSwitch = document.getElementById('langSwitch');
const langBtn = document.getElementById('langBtn');
langBtn.addEventListener('click', (e) => {
  e.stopPropagation();
  langSwitch.classList.toggle('open');
  langBtn.setAttribute('aria-expanded', langSwitch.classList.contains('open'));
});
document.addEventListener('click', () => langSwitch.classList.remove('open'));

