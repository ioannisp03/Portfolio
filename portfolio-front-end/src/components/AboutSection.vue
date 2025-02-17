<template>
  <!-- About Section -->
  <section id="about" class="about section">
    <div class="container" data-aos="fade-up" data-aos-delay="100">
      <div class="row gy-4">
        <div class="col-md-6">
          <div class="row justify-content-between gy-4">
            <div class="col-lg-5">
              <img src="../assets/images/profile.png" class="img-fluid" alt="Profile Picture">
            </div>
            <div class="col-lg-7 about-info">
              <p>
                <strong>{{ $t("about.name") }}: </strong>
                <span>Ioannis Panaritis</span>
              </p>
              <p>
                <strong>{{ $t("about.profile") }}: </strong>
                <span>{{ $t("about.fullStackDeveloper") }}</span>
              </p>
              <p>
                <strong>{{ $t("about.email") }}: </strong>
                <span>{{ $t("about.emailPlaceholder") }}</span>
              </p>
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

      <!-- Skills Horizontal Scroll Section -->
      <div class="skills-scroll mt-5">
        <h4 class="text-center mb-4">{{ $t("about.skillsTitle") }}</h4>
        <div class="skills-container">
          <div
            v-for="(skill, index) in techStack"
            :key="index"
            class="skill-item text-center p-3"
          >
            <Icon :icon="skill.icon" class="skill-icon" />
            <p class="skill-name mt-3">{{ skill.name }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';
import { Icon } from '@iconify/vue';

// Full Tech Stack using Iconify icons
const techStack = ref([
  { name: 'Java', icon: 'devicon:java' },
  { name: 'Python', icon: 'logos:python' },
  { name: 'C#', icon: 'devicon:csharp' },
  { name: 'Kotlin', icon: 'devicon:kotlin' },
  { name: 'TypeScript', icon: 'logos:typescript-icon' },
  { name: 'JavaScript', icon: 'logos:javascript' },
  { name: 'PHP', icon: 'logos:php' },
  { name: 'Spring Boot', icon: 'devicon:spring' },
  { name: 'Docker', icon: 'logos:docker-icon' },
  { name: 'Git', icon: 'devicon:git' },
  { name: 'MySQL', icon: 'logos:mysql' },
  { name: 'MongoDB', icon: 'devicon:mongodb' },
  { name: 'React.js', icon: 'logos:react' },
  { name: 'HTML5', icon: 'logos:html-5' },
  { name: 'CSS3', icon: 'logos:css-3' },
  { name: 'Bootstrap', icon: 'logos:bootstrap' },
  { name: 'Laravel', icon: 'logos:laravel' },
  { name: 'ASP.NET', icon: 'logos:dotnet' },
  { name: 'Jira', icon: 'logos:jira' },
  { name: 'Pandas', icon: 'logos:pandas' },
]);
</script>

<style scoped>
/* Horizontal Scroll Container */
.skills-scroll {
  padding: 50px 0;
}

.skills-container {
  display: flex;
  overflow-x: auto;
  scroll-behavior: smooth;
  padding: 20px 0;
}

/* Individual Skill Items */
.skill-item {
  flex: 0 0 auto;
  width: 150px;
  margin-right: 20px;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  background-color: #fff;
  transition: transform 0.3s, box-shadow 0.3s;
}

/* Hover effect for desktop users */
.skill-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

/* Skill Icon */
.skill-icon {
  width: 50px;
  height: 50px;
}

/* Skill Name */
.skill-name {
  font-size: 1.1rem;
  font-weight: bold;
  margin-top: 15px;
}
</style>
