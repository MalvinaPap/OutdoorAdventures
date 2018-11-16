
from django.contrib import admin
from django.urls import include, path
from django.http.response import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('outdooradventures/', include('outdooradventures.urls')),
]
