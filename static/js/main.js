/**
 * DA FRAN PRA VOCÊ — INTERAÇÕES, HEADER SCROLL, MENU MOBILE & FAQ ACCORDION
 */

document.addEventListener('DOMContentLoaded', () => {

  // ===================================================================
  // 1. CABEÇALHO COM EFEITO DE SCROLL
  // ===================================================================
  const siteHeader = document.getElementById('siteHeader');
  function handleHeaderScroll() {
    if (window.scrollY > 30) {
      siteHeader?.classList.add('scrolled');
    } else {
      siteHeader?.classList.remove('scrolled');
    }
  }
  window.addEventListener('scroll', handleHeaderScroll, { passive: true });
  handleHeaderScroll();

  // ===================================================================
  // 2. MENU MOBILE DROPDOWN LIMPO
  // ===================================================================
  const mobileMenuToggle = document.getElementById('mobileMenuToggle');
  const mobileNavMenu = document.getElementById('mobileNavMenu');
  const menuIconOpen = document.getElementById('menuIconOpen');
  const menuIconClose = document.getElementById('menuIconClose');
  const mobileNavItems = document.querySelectorAll('.mobile-nav-item');

  if (mobileMenuToggle && mobileNavMenu) {
    mobileMenuToggle.addEventListener('click', () => {
      const isExpanded = mobileMenuToggle.getAttribute('aria-expanded') === 'true';
      mobileMenuToggle.setAttribute('aria-expanded', !isExpanded);
      
      if (!isExpanded) {
        mobileNavMenu.classList.remove('hidden');
        menuIconOpen?.classList.add('hidden');
        menuIconClose?.classList.remove('hidden');
      } else {
        mobileNavMenu.classList.add('hidden');
        menuIconOpen?.classList.remove('hidden');
        menuIconClose?.classList.add('hidden');
      }
    });

    mobileNavItems.forEach(item => {
      item.addEventListener('click', () => {
        mobileNavMenu.classList.add('hidden');
        mobileMenuToggle.setAttribute('aria-expanded', 'false');
        menuIconOpen?.classList.remove('hidden');
        menuIconClose?.classList.add('hidden');
      });
    });
  }

  // ===================================================================
  // 3. FAQ ACCORDION SUAVE
  // ===================================================================
  const faqButtons = document.querySelectorAll('#faq button[aria-controls]');

  faqButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const panelId = btn.getAttribute('aria-controls');
      const panel = document.getElementById(panelId);
      const isExpanded = btn.getAttribute('aria-expanded') === 'true';
      const chevron = btn.querySelector('.lucide-chevron-down');
      const iconBadge = btn.querySelector('span.grid');

      // Fecha todos os outros
      faqButtons.forEach(otherBtn => {
        if (otherBtn !== btn) {
          otherBtn.setAttribute('aria-expanded', 'false');
          const otherPanelId = otherBtn.getAttribute('aria-controls');
          const otherPanel = document.getElementById(otherPanelId);
          const otherChevron = otherBtn.querySelector('.lucide-chevron-down');
          const otherBadge = otherBtn.querySelector('span.grid');

          if (otherPanel) {
            otherPanel.classList.remove('grid-rows-[1fr]', 'opacity-100');
            otherPanel.classList.add('grid-rows-[0fr]', 'opacity-0');
          }
          if (otherChevron) {
            otherChevron.style.transform = 'rotate(0deg)';
          }
          if (otherBadge) {
            otherBadge.style.background = 'var(--surface-soft)';
            otherBadge.style.color = 'var(--pink-dark)';
          }
        }
      });

      // Alterna o atual
      if (!isExpanded) {
        btn.setAttribute('aria-expanded', 'true');
        if (panel) {
          panel.classList.remove('grid-rows-[0fr]', 'opacity-0');
          panel.classList.add('grid-rows-[1fr]', 'opacity-100');
        }
        if (chevron) {
          chevron.style.transform = 'rotate(180deg)';
        }
        if (iconBadge) {
          iconBadge.style.background = 'linear-gradient(135deg, var(--pink), var(--pink-dark))';
          iconBadge.style.color = '#ffffff';
        }
      } else {
        btn.setAttribute('aria-expanded', 'false');
        if (panel) {
          panel.classList.remove('grid-rows-[1fr]', 'opacity-100');
          panel.classList.add('grid-rows-[0fr]', 'opacity-0');
        }
        if (chevron) {
          chevron.style.transform = 'rotate(0deg)';
        }
        if (iconBadge) {
          iconBadge.style.background = 'var(--surface-soft)';
          iconBadge.style.color = 'var(--pink-dark)';
        }
      }
    });
  });

});
