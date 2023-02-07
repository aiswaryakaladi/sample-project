from django.urls import path
from .views import *

urlpatterns=[
    path('index/',index),
    path('register/',register),
    path('login/',login),
    path('profile/',profile),

    path('formpage/<int:id>',formpage),
    path('jobdisplay/',jobdisplay),
    path('editcard/<int:id>',editcard),
    path('deletecard/<int:id>',deletecard),

    path('regclass/',regclass),
    path('logclass/',logclass),

    path('userupload/',userupload),
    path('apply/<int:id>',apply),
    path('applieddisplay/',applieddisplay),
    path('emailalert/',emailalert),

    path('wishlist/<int:id>',wishlist),
    path('wish/',wish),
    path('remove/<int:id>',remove),

    path('appliedview/',appliedview),
    path('sendmail/<int:id>',sendmail),
    path('remov/<int:id>',remov),
    path('userapplied/',userapplied),
    ]
