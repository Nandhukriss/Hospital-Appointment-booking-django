from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index )
    path('about/',views.about )
    path('booking/',views.booking )
    path('doctors/',views.doctors )
    path('contact/',views.contact)

]
