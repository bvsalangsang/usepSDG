from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
        path('logView/',views.logView, name="logView"),
        path('login/',views.login, name="Login"),
        path('dash-admin',views.dashboard,name="Home"),
      

        #SDG
        path('dash-admin/goals',views.sdgView,name="goals"),
        path('sdgJsonList/',views.sdgJsonList,name="sdgJsonList"),
        path('sdgSaveUpdateParams', views.sdgSaveUpdateParams, name="sdgSaveUpdateParams"),
        path('sdgDeleteParams/<int:id>', views.sdgDeleteParams, name="sdgDeleteParams"),
       
       #SDG Target
        path('dash-admin/targets',views.sdgTargetView,name="target"),
        path('sdgTargetJsonList/',views.sdgTargetJsonList,name="sdgTargetJsonList"),
        path('sdgTargetSaveUpdateParams', views.sdgTargetSaveUpdateParams, name="sdgTargetSaveUpdateParams"),
        path('sdgTargetDeleteParams/<int:id>', views.sdgTargetDeleteParams, name="sdgTargetDeleteParams"),
      
       #SDG Indicator
        path('dash-admin/indicator',views.sdgIndicatorView,name="indicator"),
        path('sdgIndicatorJsonList/',views.sdgIndicatorJsonList,name="sdgIndicatorJsonList"),
        path('sdgIndicatorSaveUpdateParams', views.sdgIndicatorSaveUpdateParams, name="sdgIndicatorSaveUpdateParams"),
        path('sdgIndicatorDeleteParams/<int:id>', views.sdgIndicatorDeleteParams, name="sdgIndicatorDeleteParams"),
      
        #SDG treeview
        path('dash-admin/goals-tree',views.sdgTreeView,name="sdgTreeView"),
        path('sdgTreeJsonList/',views.sdgTreeJsonList,name="sdgTreeJsonList"),
         
          
    ]   