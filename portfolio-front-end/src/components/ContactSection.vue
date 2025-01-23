<template>
  <section id="contact" class="contact section">
    <div class="container">
      <div class="info-wrap">
        <div class="info-item">
          <i class="bi bi-geo-alt"></i>
          <div>
            <h3>Address</h3>
            <p>A108 Adam Street, New York, NY</p>
          </div>
        </div>
      </div>
      <form @submit.prevent="submitForm">
        <input type="text" v-model="form.name" placeholder="Your Name" required />
        <input type="email" v-model="form.email" placeholder="Your Email" required />
        <textarea v-model="form.message" placeholder="Message" required></textarea>
        <button type="submit">Send Message</button>
      </form>
    </div>
  </section>
</template>

<script setup>
import { reactive } from 'vue';

// Form data
const form = reactive({
  name: '',
  email: '',
  message: '',
});

// Form submission logic
function submitForm() {
  alert(`Form submitted: ${JSON.stringify(form)}`);
}
</script>

<style scoped>
/* Add styles for the contact form */
</style>
