<template>
  <section id="testimonials" class="testimonials section accent-background">
    <!-- <div class="container section-title" data-aos="fade-up">
      <h2>Testimonials</h2>
      <p>Necessitatibus eius consequatur ex aliquid fuga eum quidem sint consectetur velit</p>
    </div> -->
    <div class="container">
      <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
        <!-- Indicators -->
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active"
            aria-current="true" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1"
            aria-label="Slide 2"></button>
          <button type="button " data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2"
            aria-label="Slide 3"></button>
        </div>

        <!-- Carousel Items -->
        <div class="carousel-inner">
          <div class="carousel-item active">
            <div class="testimonial-item">
              <img src="/img/testimonials/testimonials-1.jpg" alt="Saul Goodman" class="testimonial-img" />
              <h3>Saul Goodman</h3>
              <h4>CEO & Founder</h4>
              <div class="stars">
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-fill"></i>
              </div>
              <p>
                <i class="bi bi-quote quote-icon-left"></i>
                Proin iaculis purus consequat sem cure dignissim donec porttitora entum suscipit rhoncus.
                <i class="bi bi-quote quote-icon-right"></i>
              </p>
            </div>
          </div>

          <div class="carousel-item">
            <div class="testimonial-item">
              <img src="/img/testimonials/testimonials-2.jpg" alt="Sara Wilsson" class="testimonial-img" />
              <h3>Sara Wilsson</h3>
              <h4>Designer</h4>
              <div class="stars">
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-fill"></i>
              </div>
              <p>
                <i class="bi bi-quote quote-icon-left"></i>
                Export tempor illum tamen malis malis eram quae irure esse labore quem cillum.
                <i class="bi bi-quote quote-icon-right"></i>
              </p>
            </div>
          </div>

          <div class="carousel-item">
            <div class="testimonial-item">
              <img src="/img/testimonials/testimonials-3.jpg" alt="Jena Karlis" class="testimonial-img" />
              <h3>Jena Karlis</h3>
              <h4>Store Owner</h4>
              <div class="stars">
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-fill"></i>
              </div>
              <p>
                <i class="bi bi-quote quote-icon-left"></i>
                Enim nisi quem export duis labore cillum magna enim sint.
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
          <button class="btn btn-custom mt-5 ms-auto">Add testimonial</button>
        </div>
    </div>
  </section>
</template>

<script setup>
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
</script>

<style scoped>
.testimonials {
  padding: 40px 0;
  background-image: url("../.././../public/img/testimonials-bg.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  position: relative; /* Needed for the pseudo-element to position correctly */

}

.testimonials::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(59, 99, 209, 0.5); /* Blue overlay */
  z-index: 1; /* Ensures the overlay is above the image but below the content */
}

.testimonials .container {
  position: relative; /* Ensures content stays above the overlay */
  z-index: 2;
}


.btn-custom{
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
</style>
