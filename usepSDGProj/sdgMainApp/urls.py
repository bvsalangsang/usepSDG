from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
        path('',views.index,name="Home"),
        path('commitment',views.commitment, name="commitment"),
        path('strategy',views.strategy, name="strategy"),
        path("sdg-initiatives/sustainability-ppa",views.sustainPPA,name="sustainability-ppa"),
        path("sdg-initiatives/sustainability-ppa/goal-4",views.goal4, name="goal-4"),
        path("sdg-initiatives/sustainability-ppa/goal-4/goal-topic",views.goalTopic, name="goal-topic"),
        path("contact-us",views.contact,name="contact"),
        path('sub/test',views.test,name="Home"),
    ]