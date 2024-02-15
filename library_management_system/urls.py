
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path,  re_path
from django.views.generic.base import RedirectView


from core.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('library/', include('library.urls')),
    path('transaction/', include('transaction.urls', namespace='transaction')),
    re_path(r'^accounts/profile/$', RedirectView.as_view(url='/account/profile/', permanent=True)),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
