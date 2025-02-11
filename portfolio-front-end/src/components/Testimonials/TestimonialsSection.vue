<template>
  <section id="testimonials" class="testimonials section accent-background">
    <div class="container">
      <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
        <!-- Indicators -->
        <div class="carousel-indicators">
          <button v-for="(testimonial, index) in testimonials" :key="index" type="button"
            :data-bs-target="'#carouselExampleIndicators'" :data-bs-slide-to="index" :class="{ active: index === 0 }"
            :aria-label="'Slide ' + (index + 1)"></button>
        </div>

        <!-- Carousel Items -->
        <div class="carousel-inner">
          <div v-for="(testimonial, index) in filteredTestimonials" :key="testimonial._id"
            :class="['carousel-item', { active: index === 0 }]">
            <div class="testimonial-item">
              <h3>{{ testimonial.name }}</h3>
              <h4>{{ testimonial.title }}</h4>
              <!-- <div class="stars">
                <i class="bi bi-star-fill" v-for="star in 5" :key="star"></i>
              </div> -->
              <p>
                <i class="bi bi-quote quote-icon-left"></i>
                {{ testimonial.message }}
                <i class="bi bi-quote quote-icon-right"></i>
              </p>
            </div>
          </div>
        </div>

        <!-- Controls -->
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators"
          data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators"
          data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
      <div class="d-flex">
        <button class="btn btn-custom mt-5 ms-auto" @click="showAddTestimonialModal">Add testimonial</button>
      </div>
    </div>
  </section>


  <!-- Modal for adding a testimonial -->
  <div class="modal fade" id="addTestimonialModal" tabindex="-1" aria-labelledby="addTestimonialModalLabel"
    aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="addTestimonialModalLabel">Add Testimonial</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="addTestimonial">
            <div class="mb-3">
              <label for="testimonialName" class="form-label">Name</label>
              <input type="text" class="form-control" id="testimonialName" v-model="newTestimonial.name" required>
            </div>
            <div class="mb-3">
              <label for="testimonialTitle" class="form-label">Title</label>
              <input type="text" class="form-control" id="testimonialTitle" v-model="newTestimonial.title" required>
            </div>
            <div class="mb-3">
              <label for="testimonialMessage" class="form-label">Message</label>
              <textarea class="form-control" id="testimonialMessage" required
                v-model="newTestimonial.message"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Add Testimonial</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import api from '@/services/api';
import "bootstrap/dist/css/bootstrap.min.css";
import * as bootstrap from 'bootstrap';

const testimonials = ref([]);
const newTestimonial = ref({
  name: '',
  title: '',
  message: ''
});

const showAddTestimonialModal = () => {
  newTestimonial.value = {}; // reset the new testimonial data
  const addTestimonialModal = new bootstrap.Modal(document.getElementById('addTestimonialModal'));
  addTestimonialModal.show();
};


onMounted(async () => {
  try {
    const response = await api.getAllTestimonials();
    testimonials.value = response.filter(testimonial => testimonial.status === 'shown');
  } catch (error) {
    console.error("Error fetching testimonials: ", error);
  }
});

const addTestimonial = async () => {
  try {
    await api.addTestimonial(newTestimonial.value);

    // Fetch updated testimonial list
    const updatedTestimonials = await api.getAllTestimonials();
    testimonials.value = updatedTestimonials;

    newTestimonial.value = {
      name: '',
      title: '',
      message: ''
    };

    // Close modal
    bootstrap.Modal.getInstance(document.getElementById('addTestimonialModal')).hide();
  } catch (error) {
    console.error("Error adding testimonial: ", error);
  }
};
const filteredTestimonials = computed(() => {
  return testimonials.value.filter(testimonial => testimonial.status === 'shown')
})
</script>

<style scoped>
.testimonials {
  padding: 100px 0;
  background-image: url("../.././../public/img/testimonials-bg.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  position: relative;
  /* Needed for the pseudo-element to position correctly */

}

.testimonials::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(59, 99, 209, 0.5);
  /* Blue overlay */
  z-index: 1;
  /* Ensures the overlay is above the image but below the content */
}

.testimonials .container {
  position: relative;
  /* Ensures content stays above the overlay */
  z-index: 2;
}


.btn-custom {
  color: gre;
  background-color: rgb(190, 190, 190);

}

#testimonials {
  color: black;
}

#testimonials h4 {
  font-size: small;
}


.testimonial-item {
  text-align: center;
  padding: 30px;
  border-radius: 10px;
  /* box-shadow: 0px 0 30px rgba(0, 0, 0, 0.1); */
  /* background: rgba(59, 99, 209, 0.8); */

  color: white;
  font-style: italic;


}

.testimonial-img {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin: 0 auto 15px;
}

.popup-form {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  z-index: 1000;
}
</style>
