from django.urls import path

from . import views

urlpatterns = [
    # ================== common ==================
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    # ================== Periemeter ==================
    path('peri/circle', views.circle, name='circleperi'),
    path('peri/circleres', views.circleres, name='circleperires'),
    path('peri/semicircle', views.semicircle, name='semicircleperi'),
    path('peri/semicircleres', views.semicircleres, name='semicircleperires'),
    # ================== Area ==================

    # ================== Volume ==================

    # ================== Total Surface Area ==================

    # ================== Curve Surface Area ==================

]
