# core/urls.py

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

import resume.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/', resume.views.sample_resume, name='sample_resume')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]