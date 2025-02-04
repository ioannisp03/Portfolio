<template>
    <section id="resume" class="resume section">
        <div class="container section-title" data-aos="fade-up">
            <h2>Resume</h2>
            <p>Download <a id="resumeLink" href="#" @click.prevent="downloadCV">my resume</a> if you want to see more!
            </p>
        </div>
        <div class="container">
            <div class="row">
                <div class="col-lg-6" data-aos="fade-up" data-aos-delay="100">
                    <h3 class="resume-title">Sumary</h3>

                    <div class="resume-item pb-0">
                        <h4>Ioannis Panaritis</h4>
                        <p><em>Innovative and deadline-driven Software developer with 2+ years of experience in
                                developing and
                                user-centered digital/print marketing material from initial concept to final,
                                polished deliverable.</em></p>
                    </div>

                    <h3 class="resume-title">Education</h3>
                    <div class="resume-item">
                        <h4>Diploma of College Studies (DEC) - Computer Science Technology</h4>
                        <h5>September 2022 - May 2025</h5>
                        <p><em>Champlain College St-Lambert</em></p>
                        <p>Comprehensive program focused on software development, networking, and IT systems, preparing
                            students for careers in the tech industry.</p>
                    </div>
                    <h3 class="resume-title">Certifications</h3>
                    <div class="resume-item">
                        <h4>AI Accelerator Program</h4>
                        <h5>September 2024 - December 2024</h5>
                        <p><em>Dawson College AI Launch Lab, in partnership with Mitacs</em></p>
                        <ul>
                            <li>
                                Developed Python and machine learning skills through interactive workshops and a team
                                project
                            </li>
                            <li>
                                Engaged with AI experts on ethics and advanced machine learning techniques
                            </li>
                        </ul>
                    </div>
                </div>

                <div class="col-lg-6" data-aos="fade-up" data-aos-delay="200">
                    <h3 class="resume-title">Professional Experience</h3>
                    <div class="resume-item">
                        <h4>Data Analyst</h4>
                        <h5>April 2024 - September 2024</h5>
                        <p><em>Telus International AI Data Solutions, Montreal, QC</em></p>
                        <ul>
                            <li>Assessed AI-generated responses for accuracy and relevance according to strict
                                guidelines</li>
                            <li>Evaluated diverse data inputs like Google Maps, audio, and images for accuracy</li>
                            <li>Conducted research to resolve data inconsistencies, improving report precision</li>
                        </ul>
                    </div>
                    <div class="resume-item">
                        <h4>Tutor/Teacher Assistant for Computer Science</h4>
                        <h5>September 2024 - Present</h5>
                        <p><em>Champlain College St-Lambert, St-Lambert, QC</em></p>
                        <ul>
                            <li>Provided guidance to first and second year students on Python programming, focusing on
                                automation scripts and data processing using Pandas, Openpyxl, and Matplotlib</li>
                            <li>Assisted students in leveraging Python for Excel-based tasks, enhancing their
                                problem-solving and automation skills</li>
                            <li>Facilitated hands-on coding workshops and debugging sessions, helping students
                                understand core programming concepts and improve their ability to write efficient,
                                maintainable code.</li>
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
        const response = await api.downloadResumeCv();
        const fileURL = window.URL.createObjectURL(response); // creates a url
        window.open(fileURL, "_blank"); // Opens the PDF in a new tab
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
</style>
