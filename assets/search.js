(() => {
  const input = document.getElementById('site-search-input');
  const form = document.getElementById('search-form');
  const results = document.getElementById('search-results');
  const status = document.getElementById('search-status');
  if (!input || !results) return;
  const cards = [...results.querySelectorAll('.search-result')];
  const filter = () => {
    const query = input.value.trim().toLocaleLowerCase();
    let visible = 0;
    cards.forEach(card => {
      const match = !query || (card.dataset.searchText || card.textContent.toLocaleLowerCase()).includes(query);
      card.hidden = !match;
      if (match) visible++;
    });
    if (status) status.textContent = query ? `${visible} result${visible === 1 ? '' : 's'} for “${input.value.trim()}”.` : `Showing all ${visible} pages.`;
  };
  input.addEventListener('input', filter);
  if (form) form.addEventListener('submit', event => { event.preventDefault(); filter(); });
  const params = new URLSearchParams(location.search);
  if (params.has('q')) input.value = params.get('q') || '';
  filter();
})();
