import { createI18n } from "vue-i18n";
import en from '@/locale/en.json'
import fr from '@/locale/fr.json'


const i18n = createI18n({
    legacy: false, // Required for Vue 3 composition API
    locale: 'en', // Default language
    fallbackLocale: 'fr', // If a key is missing, fallback to French
    messages: { en, fr } // Load translations
  });
  
  export default i18n;