import re

with open('/tmp/workspace/ItsManikantaGopi/ItsManikantaGopi.github.io/README.md', 'r') as f:
    readme_content = f.read()

# Update email
readme_content = re.sub(
    r'manikantagopiw@gmail\.com',
    'gopimanikanta50@gmail.com',
    readme_content
)

# Replace "Reduced API response times by **200ms** through CDN optimization" to cost optimization
# Or I can just update the Highlights and Achievements.
readme_content = readme_content.replace(
    'Reduced API response times by **200ms** through CDN optimization',
    'Optimized cloud costs and reduced Lambda service bills significantly'
)
readme_content = readme_content.replace(
    '10,000+ concurrent users',
    '20,000+ concurrent users'
)

# Key Achievements
old_achievements = """### 🏆 Key Achievements

✨ Reduced API response times by 200ms through strategic optimizations  
✨ Built messaging infrastructure with sub-100ms latency for 10K+ users  
✨ Reduced deployment time by 60% with automated CI/CD pipelines  
✨ Implemented multi-cloud architecture across AWS, GCP, and Azure  
✨ Reduced database load by 40% through Redis caching strategies"""

new_achievements = """### 🏆 Key Achievements

✨ **Cost Optimizations:** Moved logs to self-hosted service reducing $1k+ monthly bill, and optimized video processing reducing Lambda bill by 80%.  
✨ **Performance:** Reduced API response times by 200ms through strategic optimizations.  
✨ **High-Scale:** Built messaging infrastructure with sub-100ms latency for 20K+ users.  
✨ **Efficiency:** Reduced deployment time by 60% with GitOps and Kubernetes orchestration.  
✨ **Reliability:** Achieved 99.9% uptime and reduced database load by 40% via Redis caching."""

readme_content = readme_content.replace(old_achievements, new_achievements)

with open('/tmp/workspace/ItsManikantaGopi/ItsManikantaGopi.github.io/README.md', 'w') as f:
    f.write(readme_content)

