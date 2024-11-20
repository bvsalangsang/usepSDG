
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
        path('',views.index,name="home"),
        path('commitment',views.commitment, name="commitment"),
        path('strategy',views.strategy, name="strategy"),
        path("sdg-initiatives/sustainability-ppa",views.sustainPPA,name="sustainability-ppa"),
        path("sdg-initiatives/sustainability-ppa/goal-<int:goal_id>/", views.goal, name="goal"),
        path("sdg-initiatives/sustainability-ppa/goal-<int:goal_id>/goal-topic/<int:sdgScoreId>", views.goalTopic, name="goal-topic"),
        # path("sdg-initiatives/sustainability-ppa/goal-1",views.goal1, name="goal-1"),
        path("scorecard",views.scorecard,name="scorecard"),
        path("goalJsonFetchPerId/<int:id>",views.goalJsonFetchPerId,name="goalJsonFetchPerId"),
        path("getGoalListJsonList/<int:id>",views.getGoalListJsonList,name="getGoalListJsonList"),
        path("getSdgScorecardJsonList/<int:id>",views.getSdgScorecardJsonList,name="getSdgScorecardJsonList"),
        path("green-campus",views.greenCampus,name="greenCampus"),
            
        path('sub/test',views.test,name="Home"),
    ]
