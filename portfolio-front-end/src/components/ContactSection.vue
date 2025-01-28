<script setup>
import { ref } from 'vue';

import api from '@/services/api'

const form = ref({
  sender_email: '',
  subject: '',
  message: '',
});

async function submitForm() {
  try {
    const response = await api.sendEmail(form.value);
    alert('Email sent successfully')
    console.log(response.data)
  } catch (error) {
    alert("Failed to send email", error)
  }
}

</script>

<template>
  <section id="contact" class="contact section">

    <!-- Section Title -->
    <div class="container section-title" data-aos="fade-up">
      <h2>Contact</h2>
      <p>Necessitatibus eius consequatur ex aliquid fuga eum quidem sint consectetur velit</p>
    </div><!-- End Section Title -->

    <div class="container" data-aos="fade-up" data-aos-delay="100">

      <div class="info-wrap" data-aos="fade-up" data-aos-delay="200">
        <div class="row gy-5">

          <div class="col-lg-4">
            <div class="info-item d-flex align-items-center">
              <i class="bi bi-geo-alt flex-shrink-0"></i>
              <div>
                <h3>Address</h3>
                <p>Montreal, Quebec</p>
              </div>
            </div>
          </div><!-- End Info Item -->

          <div class="col-lg-4">
            <div class="info-item d-flex align-items-center">
              <i class="bi bi-telephone flex-shrink-0"></i>
              <div>
                <h3>Call me</h3>
                <p>+1 5589 55488 55</p>
              </div>
            </div>
          </div><!-- End Info Item -->

          <div class="col-lg-4">
            <div class="info-item d-flex align-items-center">
              <i class="bi bi-envelope flex-shrink-0"></i>
              <div>
                <h3>Email Me</h3>
                <p>ioannis.panaritis03@gmail.com</p>
              </div>
            </div>
          </div><!-- End Info Item -->

        </div>
      </div>

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

          <div class="col-md-12 text-center">
            <div class="loading">Loading</div>
            <div class="error-message"></div>
            <div class="sent-message">Your message has been sent. Thank you!</div>

            <button type="submit">Send Message</button>
          </div>
        </div>
      </form>
    </div>
  </section>
</template>
