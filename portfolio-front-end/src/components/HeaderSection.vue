<template>
  <header id="header" class="header d-flex align-items-center sticky-top">
    <div class="container-fluid container-xl position-relative d-flex align-items-center justify-content-between">
      <a href="#hero" class="logo d-flex align-items-center" style="text-decoration: none;">
        <h1 class="sitename">Ioannis Panaritis</h1>
      </a>

      <nav id="navmenu" class="navmenu">
        <ul>
          <li><a href="/#hero" style="text-decoration: none;">Home</a></li>
          <li><a href="/#about" style="text-decoration: none;">About</a></li>
          <li><a href="/#portfolio" style="text-decoration: none;">Portfolio</a></li>
          <li><a href="/#contact" style="text-decoration: none;">Contact</a></li>
          <!-- Only logged in admin should be able to see this -->
          <li> <router-link to="/admin-panel" style="text-decoration: none;">admin (login)</router-link></li>
        </ul>
        <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
      </nav>
    </div>
  </header>
</template>

<script setup>

</script>

<style scoped></style>
