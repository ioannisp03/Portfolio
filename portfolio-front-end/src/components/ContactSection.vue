<script setup>
import { ref } from 'vue';
import { useI18n } from 'vue-i18n';
import Toastify from 'toastify-js';
import api from '@/services/api';

const { t } = useI18n(); // Get translation function

const form = ref({
  sender_email: '',
  subject: '',
  message: '',
});

async function submitForm() {
  try {
    const response = await api.sendEmail(form.value);
    Toastify({
      text: t('contact.successMessage'),
      duration: 3000,
      close: true,
      gravity: 'top',
      position: 'right',
      backgroundColor: '#4caf50',
    }).showToast();
    console.log(response.data);
  } catch (error) {
    Toastify({
      text: `${t('contact.errorMessage')}: ${error.message}`,
      duration: 3000,
      close: true,
      gravity: 'top',
      position: 'right',
      backgroundColor: '#f44336',
    }).showToast();
  }
}
</script>

<template>
  <section id="contact" class="contact section">
    <div class="container section-title" data-aos="fade-up">
      <h2>{{ $t("contact.title") }}</h2>
      <p>{{ $t("contact.subtitle") }}</p>
    </div>

    <div class="container" data-aos="fade-up" data-aos-delay="100">
      <form @submit.prevent="submitForm" method="post" class="php-email-form" data-aos="fade-up" data-aos-delay="300">
        <div class="row gy-4">
          <div class="col-md-12">
            <input type="email" class="form-control" v-model="form.sender_email" :placeholder="$t('contact.emailPlaceholder')" required>
          </div>

          <div class="col-md-12">
            <input type="text" class="form-control" v-model="form.subject" :placeholder="$t('contact.subjectPlaceholder')" required>
          </div>

          <div class="col-md-12">
            <textarea class="form-control" v-model="form.message" rows="6" :placeholder="$t('contact.messagePlaceholder')" required></textarea>
          </div>

          <button type="submit">{{ $t("contact.sendButton") }}</button>
        </div>
      </form>
    </div>
  </section>
</template>
