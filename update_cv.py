import re
import markdown
import sys

# Read the markdown
with open('/tmp/workspace/ItsManikantaGopi/ItsManikantaGopi.github.io/resume.md', 'r') as f:
    md_content = f.read()

# Convert to HTML
html_content = markdown.markdown(md_content, extensions=['tables'])

# Read the current cv.html
with open('/tmp/workspace/ItsManikantaGopi/ItsManikantaGopi.github.io/cv.html', 'r') as f:
    cv_content = f.read()

# Extract the header/CSS part and the footer part
# We assume the content is inside <div class="container">
match = re.search(r'(<div class="container">).*?(</div>\s*</body>\s*</html>)', cv_content, re.DOTALL)
if match:
    # but the current cv.html might have some specific custom classes. Let's look at the cv.html fully.
    pass

