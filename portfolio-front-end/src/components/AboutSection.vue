<template>
  <!-- About Section -->
  <section id="about" class="about section">
    <div class="container" data-aos="fade-up" data-aos-delay="100">

      <div class="row gy-4">
        <div class="col-md-6">
          <div class="row justify-content-between gy-4">
            <div class="col-lg-5">
              <img src="../assets/images/profile.png" class="img-fluid" alt="">
            </div>
            <div class="col-lg-7 about-info">
              <p><strong>{{ $t("about.name") }}: </strong> <span>Ioannis Panaritis</span></p>
              <p><strong>{{ $t("about.profile") }}: </strong> <span>{{ $t("about.fullStackDeveloper") }}</span></p>
              <p><strong>{{ $t("about.email") }}: </strong> <span>{{ $t("about.emailPlaceholder") }}</span></p>
            </div>
          </div>
        </div>

        <div class="col-md-6">
          <div class="about-me">
            <h4>{{ $t("about.title") }}</h4>
            <p>{{ $t("about.description1") }}</p>
            <p>{{ $t("about.description2") }}</p>
            <p>{{ $t("about.description3") }}</p>
          </div>
        </div>
      </div>

    </div>
  </section>
</template>


<script setup>


</script>
