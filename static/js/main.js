/* ShopEase — Custom JavaScript */

document.addEventListener('DOMContentLoaded', function () {

  // ── Auto-dismiss alerts after 4 seconds ──────────────────────────────────
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(function (alert) {
    setTimeout(function () {
      const bsAlert = new bootstrap.Alert(alert);
      if (bsAlert) bsAlert.close();
    }, 4000);
  });

  // ── Quantity input: prevent negatives & enforce min=1 ────────────────────
  const qtyInputs = document.querySelectorAll('.qty-input');
  qtyInputs.forEach(function (input) {
    input.addEventListener('change', function () {
      const val = parseInt(this.value, 10);
      if (isNaN(val) || val < 1) {
        this.value = 1;
      }
    });
  });

  // ── Navbar scroll effect ──────────────────────────────────────────────────
  const navbar = document.getElementById('main-navbar');
  if (navbar) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 20) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    });
  }

  // ── Add to cart button loading state ─────────────────────────────────────
  const cartForms = document.querySelectorAll('.add-to-cart-form');
  cartForms.forEach(function (form) {
    form.addEventListener('submit', function () {
      const btn = form.querySelector('button[type="submit"]');
      if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status"></span>Adding...';
      }
    });
  });

  // ── Product image fallback ────────────────────────────────────────────────
  const productImages = document.querySelectorAll('.product-img');
  productImages.forEach(function (img) {
    img.addEventListener('error', function () {
      this.style.display = 'none';
      const placeholder = this.nextElementSibling;
      if (placeholder) placeholder.style.display = 'flex';
    });
  });

});
