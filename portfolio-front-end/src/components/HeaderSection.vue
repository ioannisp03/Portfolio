<template>
  <header id="header" class="header d-flex align-items-center sticky-top">
    <div class="container-fluid container-xl position-relative d-flex align-items-center justify-content-between">

      <!-- Brand/Username Section -->
      <a href="/#hero" class="logo d-flex align-items-center text-decoration-none">
        <h1 v-if="!user" class="sitename">Ioannis Panaritis</h1>

        <!-- Dropdown replaces logo when logged in -->
        <div v-if="user" class="dropdown user-dropdown-container">
          <a href="#" class="nav-link user-dropdown">
            <span>{{ $t("navigation.hello") }}, <strong>{{ user.username }}</strong></span>
            <i class="bi bi-chevron-down toggle-dropdown" style="color: orange; padding-left: .2vw;"></i>
          </a>

          <ul class="dropdown-menu user-menu">
            <li v-if="user.role === 'admin'">
              <router-link to="/admin-panel">{{ $t("navigation.adminPanel") }}</router-link>
            </li>
            <li>
              <a href="#" @click.prevent="logout">{{ $t("navigation.logout") }}</a>
            </li>
          </ul>
        </div>
      </a>

      <nav id="navmenu" class="navmenu" :class="{ 'navmenu-mobile': isMobileMenuOpen }">
        <ul>
          <li><a href="/#hero">{{ $t("navigation.home") }}</a></li>
          <li><a href="/#about">{{ $t("navigation.about") }}</a></li>
          <li><a href="/#resume">{{ $t("navigation.resume") }}</a></li>
          <li><a href="/#portfolio">{{ $t("navigation.portfolio") }}</a></li>
          <li><a href="/#testimonials">{{ $t("navigation.testimonials") }}</a></li>
          <li><a href="/#contact">{{ $t("navigation.contact") }}</a></li>

          <!-- Register & Login (Visible for Guests) -->
          <li v-if="!user" style="color: #f39c12;"><router-link to="/register">{{ $t("navigation.registerLogin") }}</router-link></li>

          <li class="language-toggle">
            <button @click="toggleLanguage" class="btn btn-outline-light">
              {{ locale === 'en' ? 'EN' : 'FR' }}
            </button>
          </li>
        </ul>

        <i class="mobile-nav-toggle bi" :class="{ 'bi-list': !isMobileMenuOpen, 'bi-x': isMobileMenuOpen }"
          @click="toggleMobileMenu"></i>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, watchEffect } from "vue";
import { useRouter } from "vue-router";
import authService from "@/services/authService";
import { useI18n } from "vue-i18n";
import "bootstrap/dist/js/bootstrap.bundle.min.js";

const router = useRouter();
const user = ref(null);
const isMobileMenuOpen = ref(false);
const { locale } = useI18n();

const updateUser = async () => {
  user.value = await authService.getUser();
};

onMounted(() => {
  const storedLocale = localStorage.getItem('locale');
  if (storedLocale) {
    locale.value = storedLocale;
  }
  updateUser();
  window.addEventListener("auth-change", updateUser);

  document.addEventListener('click', (e) => {
    const navmenu = document.querySelector("#navmenu");
    const toggle = document.querySelector(".mobile-nav-toggle");
    if (!navmenu?.contains(e.target) && !toggle?.contains(e.target) && isMobileMenuOpen.value) {
      isMobileMenuOpen.value = false;
    }
  });
});

watchEffect(() => {
  if (localStorage.getItem("token")) {
    updateUser();
  } else {
    user.value = null;
  }
});

const logout = () => {
  authService.logout();
  user.value = null;
  router.push("/");
};

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
};

const toggleLanguage = () => {
  locale.value = locale.value === 'en' ? 'fr' : 'en';
  localStorage.setItem('locale', locale.value)
};
</script>

<style scoped>
.header {
  background-color: #000;
  padding: 12px 16px;
}

.sitename {
  font-size: 1.6rem;
  font-weight: bold;
  color: white;
  transition: color 0.3s ease-in-out;
}

.navmenu ul {
  list-style: none;
  display: flex;
  align-items: center;

}


.navmenu ul li a {
  text-decoration: none;
  color: white;
  font-size: 1rem;
  font-weight: bold;
  transition: color 0.3s ease-in-out;
}

.navmenu ul li a:hover {
  color: #f39c12;
}



.user-dropdown {
  font-size: 1.1rem;
  font-weight: bold;
  color: #f39c12 !important;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 5px;
  cursor: pointer;
}

.user-menu {
  position: absolute;
  top: 100%;
  left: 0;
  width: 160px;
  background: white;
  border-radius: 5px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  padding: 8px;
  margin-top: 8px;
  z-index: 1000;
  display: flex;
  flex-direction: column;
  opacity: 0;
  visibility: hidden;
  transform: translateY(-10px);
  transition: all 0.3s ease-in-out;
}

.user-dropdown-container:hover .user-menu {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

.user-menu li {
  padding: 6px 8px;
  border-bottom: 1px solid #f0f0f0;
}

.user-menu li:last-child {
  border-bottom: none;
}

.user-menu li a {
  color: black;
  font-size: 0.95rem;
  font-weight: normal;
  text-decoration: none;
  transition: background 0.3s ease-in-out, color 0.3s ease-in-out;
}

.user-menu li a:hover {
  color: #f39c12;
  ;
  padding: 4px;
  border-radius: 4px;
}

/* Mobile Navigation Toggle */
.mobile-nav-toggle {
  display: none;
  font-size: 1.75rem;
  color: white;
  cursor: pointer;
  transition: transform 0.3s ease;
}

/* Large Screens (Desktop) */
@media (min-width: 1200px) {
  .mobile-nav-toggle {
    display: none;
  }

  .navmenu ul {
    display: flex !important;
    position: static;
    width: auto;
    background: none;
    height: auto;
    padding: 0;
    border: none;
  }
}

/* Medium Screens (Tablet) */
@media (min-width: 768px) and (max-width: 1199px) {
  .mobile-nav-toggle {
    display: block;
  }

  .navmenu ul {
    display: none;
    flex-direction: column;
    position: fixed;
    top: 60px;
    right: -100%;
    background: rgba(0, 0, 0, 0.95);
    width: 250px;
    height: auto;
    max-height: calc(100vh - 60px);
    padding: 15px 0;
    z-index: 1000;
    transition: right 0.3s ease-in-out;
    border-left: 1px solid rgba(255, 255, 255, 0.1);
  }

  .navmenu.navmenu-mobile ul {
    display: flex;
    right: 0;
  }
}

/* Small Screens (Mobile) */
@media (max-width: 767px) {
  .mobile-nav-toggle {
    display: block;
  }

  .navmenu ul {
    display: none;
    flex-direction: column;
    position: fixed;
    top: 60px;
    right: -100%;
    background: rgba(0, 0, 0, 0.95);
    width: 200px;
    height: auto;
    max-height: calc(100vh - 60px);
    padding: 10px 0;
    z-index: 1000;
    transition: right 0.3s ease-in-out;
    border-left: 1px solid rgba(255, 255, 255, 0.1);
  }

  .navmenu.navmenu-mobile ul {
    display: flex;
    right: 0;
  }
}

/* Shared Mobile & Tablet Styles */
@media (max-width: 1199px) {
  .navmenu ul li {
    width: 100%;
    padding: 8px 16px;
    text-align: left;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  }

  .navmenu ul li:last-child {
    border-bottom: none;
  }

  .navmenu ul li a {
    display: block;
    width: 100%;
    font-size: 1rem;
  }

  .navmenu-mobile .mobile-nav-toggle {
    transform: rotate(180deg);
  }

  .language-toggle button {
    color: white;
    font-size: 1rem;
    padding: 5px 10px;
    cursor: pointer;
    border-radius: 5px;
    background: none;
  }

  .language-toggle button:hover {
    background: white;
    color: black;
  }

}
</style>