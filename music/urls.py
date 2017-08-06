from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^profile/', views.ProfileView.as_view(),
        name="ProfilePage"),
    url(r'^feeds/', views.FeedsView.as_view(),
        name="FeedsPage")
]