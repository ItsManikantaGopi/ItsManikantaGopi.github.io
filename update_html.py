import re

with open('/tmp/workspace/ItsManikantaGopi/ItsManikantaGopi.github.io/cv.html', 'r') as f:
    cv_content = f.read()

# Update email
cv_content = re.sub(
    r'manikantagopiw@gmail\.com',
    'gopimanikanta50@gmail.com',
    cv_content
)

# Update Summary
new_summary = """Software Engineer II with 5+ years of experience building scalable systems that handle high-volume traffic while optimizing for performance and reliability. Expert in multi-cloud architecture (AWS, GCP, Azure), real-time messaging systems, and DevOps practices. Proven track record of optimizing cloud costs, building systems supporting 10,000+ concurrent users, and implementing robust CI/CD pipelines that reduced deployment time by 60%. Strong foundation in microservices designing and maintenance."""

cv_content = re.sub(
    r'<section id="summary">\s*<h2>Summary</h2>\s*<p>.*?</p>\s*</section>',
    f'<section id="summary">\n            <h2>Summary</h2>\n            <p>\n                {new_summary}\n            </p>\n        </section>',
    cv_content,
    flags=re.DOTALL
)

# Update SE II Experience
new_se2 = """<div class="job">
                <div class="job-header">
                    <h3>Software Engineer II</h3>
                    <span class="period">April 2025 – Present</span>
                </div>
                <div class="company">Circleapp Online Services</div>
                <ul>
                    <li>Managing company Infrastructure and cloud services as a sole responsible person.</li>
                    <li>Managing production Kubernetes cluster across multiple environments with disaster recovery mechanisms.</li>
                    <li>Deploying self hosted services to avoid unwanted billing from cloud services like loki for logs.</li>
                    <li>Optimizing costs related to cloud services, by observing patterns of usage.</li>
                    <li>Architecting microservices for PrajaApp social media platform handling high-volume traffic.</li>
                    <li>Building infrastructure-as-code solutions with Terraform for reproducible deployments.</li>
                    <li>Implementing hybrid cloud solutions across AWS, GCP, and Azure for optimal cost and performance.</li>
                </ul>
            </div>"""
cv_content = re.sub(
    r'<div class="job">\s*<div class="job-header">\s*<h3>Software Engineer II</h3>.*?</ul>\s*</div>',
    new_se2,
    cv_content,
    flags=re.DOTALL
)

# Update SE Experience (change 10,000 to 20,000 concurrent users for messaging)
cv_content = re.sub(
    r'10,000\+ concurrent users\.',
    '20,000+ concurrent users.',
    cv_content
)

# Update skills
new_skills = """<section id="skills">
            <h2>Technical Skills</h2>
            <table class="skills-table">
                <tr>
                    <td>Languages</td>
                    <td>Ruby, Python, TypeScript, JavaScript, Dart</td>
                </tr>
                <tr>
                    <td>Backend</td>
                    <td>Ruby on Rails, NestJS, Node.js, Express.js, Socket.io, BullMq</td>
                </tr>
                <tr>
                    <td>Cloud & DevOps</td>
                    <td>AWS, GCP, Azure, Docker, Kubernetes, Terraform, GitHub Actions, GitLab CI, FluxCD</td>
                </tr>
                <tr>
                    <td>Databases</td>
                    <td>MySQL, MongoDB, Redis, OpenSearch</td>
                </tr>
                <tr>
                    <td>Observability</td>
                    <td>Grafana, Prometheus, New Relic</td>
                </tr>
                <tr>
                    <td>AI / ML</td>
                    <td>PyTorch, TensorFlow, NumPy, Pandas</td>
                </tr>
                <tr>
                    <td>Mobile</td>
                    <td>Flutter (iOS & Android), View Model</td>
                </tr>
            </table>
        </section>"""
cv_content = re.sub(
    r'<section id="skills">.*?</section>',
    new_skills,
    cv_content,
    flags=re.DOTALL
)

with open('/tmp/workspace/ItsManikantaGopi/ItsManikantaGopi.github.io/cv.html', 'w') as f:
    f.write(cv_content)

