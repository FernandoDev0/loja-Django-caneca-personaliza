import os
import shutil
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.test import RequestFactory
from core.views import index

public_dir = 'public'
os.makedirs(public_dir, exist_ok=True)

# 1. Render homepage directly using Django view
rf = RequestFactory()
request = rf.get('/')
response = index(request)
html = response.content.decode('utf-8')

# Write index.html
with open(os.path.join(public_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Directly generated {public_dir}/index.html ({len(html)} bytes)")

# 2. Copy static files into public/static
dst_static = os.path.join(public_dir, 'static')
if os.path.exists(dst_static):
    shutil.rmtree(dst_static)
shutil.copytree('static', dst_static)
print(f"Copied static/ to {dst_static}")

# 3. Copy media files into public/media
if os.path.exists('media'):
    dst_media = os.path.join(public_dir, 'media')
    if os.path.exists(dst_media):
        shutil.rmtree(dst_media)
    shutil.copytree('media', dst_media)
    print(f"Copied media/ to {dst_media}")

print("Export completed successfully!")
