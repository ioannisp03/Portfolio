<script setup>
import { ref } from 'vue';
import Toastify from 'toastify-js'
import api from '@/services/api'

const form = ref({
  sender_email: '',
  subject: '',
  message: '',
});

async function submitForm() {
  try {
    const response = await api.sendEmail(form.value);
    Toastify({
      text: 'Email sent successfully',
      duration: 3000,
      close: true,
      gravity: 'top',
      position: 'right',
      backgroundColor: '#4caf50',
    }).showToast();
    console.log(response.data);
  } catch (error) {
    Toastify({
      text: `Failed to send email: ${error.message}`,
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
      <h2>Contact</h2>
      <p>Fill out the form to send me an email</p>
    </div>

    <div class="container" data-aos="fade-up" data-aos-delay="100">
      <form @submit.prevent="submitForm" method="post" class="php-email-form" data-aos="fade-up" data-aos-delay="300">
        <div class="row gy-4">

          <div class="col-md-12 ">
            <input type="email" class="form-control" v-model="form.sender_email" placeholder="Your Email" required="">
          </div>

          <div class="col-md-12">
            <input type="text" class="form-control" v-model="form.subject" placeholder="Subject" required="">
          </div>

          <div class="col-md-12">
            <textarea class="form-control" v-model="form.message" rows="6" placeholder="Message" required=""></textarea>

          </div>
          <button type="submit">Send Message</button>
        </div>
      </form>
    </div>
  </section>
</template>
