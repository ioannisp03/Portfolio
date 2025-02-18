<template>
  <section id="resume" class="resume section">
    <div class="container section-title" data-aos="fade-up">
      <h2>{{ $t("resume.title") }}</h2>
      <div>
        <p>{{ $t('resume.downloadResume') }}</p>
        <button @click="downloadCV" class="download-btn">
          {{ $t('resume.downloadButton') }}
        </button>

      </div>
    </div>

    <div class="container">
      <div class="row">
        <div class="col-lg-6" data-aos="fade-up" data-aos-delay="100">
          <h3 class="resume-title">{{ $t("resume.summaryTitle") }}</h3>
          <div class="resume-item pb-0">
            <h4>Ioannis Panaritis</h4>
            <p><em>{{ $t("resume.summaryDescription") }}</em></p>
          </div>

          <h3 class="resume-title">{{ $t("resume.educationTitle") }}</h3>
          <div class="resume-item">
            <h4>{{ $t("resume.educationDegree") }}</h4>
            <h5>{{ $t("resume.educationDates") }}</h5>
            <p><em>Champlain College St-Lambert</em></p>
            <p>{{ $t("resume.educationDescription") }}</p>
          </div>

          <h3 class="resume-title">{{ $t("resume.certificationsTitle") }}</h3>
          <div class="resume-item">
            <h4>{{ $t("resume.certificationName") }}</h4>
            <h5>{{ $t("resume.certificationDates") }}</h5>
            <p><em>{{ $t("resume.certificationInstitution") }}</em></p>
            <ul>
              <li>{{ $t("resume.certificationDetail1") }}</li>
              <li>{{ $t("resume.certificationDetail2") }}</li>
            </ul>
          </div>
        </div>

        <div class="col-lg-6" data-aos="fade-up" data-aos-delay="200">
          <h3 class="resume-title">{{ $t("resume.experienceTitle") }}</h3>

          <div class="resume-item">
            <h4>{{ $t("resume.job1.title") }}</h4>
            <h5>{{ $t("resume.job1.dates") }}</h5>
            <p><em>{{ $t("resume.job1.company") }}</em></p>
            <ul>
              <li>{{ $t("resume.job1.detail1") }}</li>
              <li>{{ $t("resume.job1.detail2") }}</li>
              <li>{{ $t("resume.job1.detail3") }}</li>
            </ul>
          </div>

          <div class="resume-item">
            <h4>{{ $t("resume.job2.title") }}</h4>
            <h5>{{ $t("resume.job2.dates") }}</h5>
            <p><em>{{ $t("resume.job2.company") }}</em></p>
            <ul>
              <li>{{ $t("resume.job2.detail1") }}</li>
              <li>{{ $t("resume.job2.detail2") }}</li>
              <li>{{ $t("resume.job2.detail3") }}</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import api from '@/services/api';

const downloadCV = async () => {
  try {
    console.log("Attempting to fetch resume...");
    const response = await api.downloadResumeCv();
    const fileURL = window.URL.createObjectURL(response);
    window.open(fileURL, "_blank");

  } catch (error) {
    console.error("Error downloading resume:", error);
  }
};


</script>


<style>
#resumeLink {
  color: blue;
  text-decoration: none;

}
.download-btn {
  background: transparent;
  color: #0056b3;
  font-size: 0.875rem; 
  font-weight: 600;
  padding: 8px 16px; 
  margin: 20PX;
  border: 2px solid #0056b3;
  border-radius: 6px;
  transition: all 0.3s ease-in-out;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.download-btn:hover {
  background: #0056b3;
  color: white;
  transform: scale(1.05);
}

.download-btn:active {
  transform: scale(0.97);
}


</style>
