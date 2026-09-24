// Clean and Fast Watch & Filter Engine

document.addEventListener('DOMContentLoaded', () => {
    // Mobile navigation toggle
    const toggleBtn = document.getElementById('nav-toggle');
    const navLinks = document.getElementById('nav-links');
    if (toggleBtn && navLinks) {
        toggleBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            navLinks.classList.toggle('mobile-open');
        });

        document.addEventListener('click', (e) => {
            if (!navLinks.contains(e.target) && e.target !== toggleBtn) {
                navLinks.classList.remove('mobile-open');
            }
        });

        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('mobile-open');
            });
        });
    }

    // Client-side quick filter for episodes
    const searchInput = document.getElementById('episode-search');
    const episodeCards = document.querySelectorAll('.episode-card');

    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase().trim();
            let visibleCount = 0;

            episodeCards.forEach(card => {
                const title = card.getAttribute('data-title')?.toLowerCase() || '';
                const epNum = card.getAttribute('data-ep')?.toLowerCase() || '';
                const desc = card.getAttribute('data-desc')?.toLowerCase() || '';
                const aliens = card.getAttribute('data-aliens')?.toLowerCase() || '';

                const matches = title.includes(query) || 
                                epNum.includes(query) || 
                                desc.includes(query) || 
                                aliens.includes(query);

                if (matches) {
                    card.style.display = 'flex';
                    visibleCount++;
                } else {
                    card.style.display = 'none';
                }
            });

            const emptyState = document.getElementById('search-empty-state');
            if (emptyState) {
                emptyState.style.display = (visibleCount === 0 && query.length > 0) ? 'block' : 'none';
            }
        });
    }
});
