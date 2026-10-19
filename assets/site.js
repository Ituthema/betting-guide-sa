(() => {
  const close = document.getElementById('age-close');
  const ageBar = document.getElementById('age-bar');
  if (close && ageBar) close.addEventListener('click', () => ageBar.hidden = true);
  const header = document.querySelector('.site-header');
  if (header) {
    const onScroll = () => header.classList.toggle('stuck', window.scrollY > 12);
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }
})();
