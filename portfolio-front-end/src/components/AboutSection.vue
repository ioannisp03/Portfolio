<template>
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

const techStack = ref([
  { name: 'Java', icon: 'devicon:java' },
  { name: 'Python', icon: 'logos:python' },
  { name: 'C#', icon: 'devicon:csharp' },
  { name: 'Kotlin', icon: 'devicon:kotlin' },
  { name: 'JavaScript', icon: 'logos:javascript' },
  { name: 'TypeScript', icon: 'logos:typescript-icon' },
  { name: 'PHP', icon: 'logos:php' },
  { name: 'HTML5', icon: 'logos:html-5' },
  { name: 'CSS3', icon: 'logos:css-3' },
  { name: 'Bootstrap', icon: 'logos:bootstrap' },
  { name: 'React.js', icon: 'logos:react' },
  { name: 'Spring Boot', icon: 'devicon:spring' },
  { name: 'Laravel', icon: 'logos:laravel' },
  { name: 'ASP.NET', icon: 'logos:dotnet' },
  { name: 'MySQL', icon: 'logos:mysql' },
  { name: 'MongoDB', icon: 'devicon:mongodb' },
  { name: 'Docker', icon: 'logos:docker-icon' },
  { name: 'Git', icon: 'devicon:git' },
  { name: 'Jira', icon: 'logos:jira' },
  { name: 'Pandas', icon: 'logos:pandas' },
]);
</script>

<style scoped>
.skills-scroll {
  padding: 50px 0;
}

.skills-container {
  display: flex;
  overflow-x: auto;
  scroll-behavior: smooth;
  padding: 20px 0;
}

.skill-item {
  flex: 0 0 auto;
  width: 150px;
  margin-right: 20px;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  background-color: #fff;
  transition: transform 0.3s, box-shadow 0.3s;
}

.skill-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.skill-icon {
  width: 50px;
  height: 50px;
}

.skill-name {
  font-size: 1.1rem;
  font-weight: bold;
  margin-top: 15px;
}
</style>
