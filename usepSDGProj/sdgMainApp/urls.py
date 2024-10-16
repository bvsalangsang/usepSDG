from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
        path('',views.index,name="home"),
        path('commitment',views.commitment, name="commitment"),
        path('strategy',views.strategy, name="strategy"),
        path("sdg-initiatives/sustainability-ppa",views.sustainPPA,name="sustainability-ppa"),
        path("sdg-initiatives/sustainability-ppa/goal-1",views.goal1, name="goal-1"),
        path("sdg-initiatives/sustainability-ppa/goal-2",views.goal2, name="goal-2"),
        path("sdg-initiatives/sustainability-ppa/goal-3",views.goal3, name="goal-3"),
        path("sdg-initiatives/sustainability-ppa/goal-4",views.goal4, name="goal-4"),
        path("sdg-initiatives/sustainability-ppa/goal-5",views.goal5, name="goal-5"),
        path("sdg-initiatives/sustainability-ppa/goal-6",views.goal6, name="goal-6"),
        path("sdg-initiatives/sustainability-ppa/goal-7",views.goal7, name="goal-7"),
        path("sdg-initiatives/sustainability-ppa/goal-8",views.goal8, name="goal-8"),
        path("sdg-initiatives/sustainability-ppa/goal-9",views.goal9, name="goal-9"),
        path("sdg-initiatives/sustainability-ppa/goal-10",views.goal10, name="goal-10"),
        path("sdg-initiatives/sustainability-ppa/goal-11",views.goal11, name="goal-11"),
        path("sdg-initiatives/sustainability-ppa/goal-12",views.goal12, name="goal-12"),
        path("sdg-initiatives/sustainability-ppa/goal-13",views.goal13, name="goal-13"),
        path("sdg-initiatives/sustainability-ppa/goal-14",views.goal14, name="goal-14"),
        path("sdg-initiatives/sustainability-ppa/goal-15",views.goal15, name="goal-15"),
        path("sdg-initiatives/sustainability-ppa/goal-16",views.goal16, name="goal-16"),
        path("sdg-initiatives/sustainability-ppa/goal-17",views.goal17, name="goal-17"),
        path("sdg-initiatives/sustainability-ppa/goal-4/goal-topic",views.goalTopic, name="goal-topic"),
        path("contact-us",views.contact,name="contact"),
        path("goalJsonFetchPerId/<int:id>",views.goalJsonFetchPerId,name="goalJsonFetchPerId"),
        path('sub/test',views.test,name="Home"),
    ]