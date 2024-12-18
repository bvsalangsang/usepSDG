from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
        path('logView/',views.logView, name="logView"),
        path('login/',views.login, name="login"),
        path('set_session_auth/',views.set_session_auth,name="set-session-auth"),
        path('logout/', views.session_flush, name="logout"),
        path('dash-admin/',views.dashboard,name="Home"),
        

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
         
        #sustain strat
        path('dash-admin/sustain-strat',views.susStratView,name="susStratView"),
        path('susStratJsonList/',views.susStratJsonList,name="susStratJsonList"),
        path('susStratSaveUpdateParams', views.susStratSaveUpdateParams, name="susStratSaveUpdateParams"),
        path('susStratDeleteParams/<int:id>', views.susStratDeleteParams, name="susStratDeleteParams"),

        #Green Metric
        path('dash-admin/green-metric',views.uiGreenMetView,name="uiGreenMetView"),
        path('uiGreenMetJsonList/',views.uiGreenMetJsonList,name="uiGreenMetJsonList"),
        path('uiGreenMetSaveUpdateParams', views.uiGreenMetSaveUpdateParams, name="uiGreenMetSaveUpdateParams"),
        path('uiGreenMetDeleteParams/<int:id>', views.uiGreenMetDeleteParams, name="uiGreenMetDeleteParams"),

        #sdg scorecard
        path('dash-admin/sdg-scorecard',views.sdgScorecardView,name="sdgScorecardView"),
        path('sdgScorecardJsonList/',views.sdgScorecardJsonList,name="sdgScorecardJsonList"),
        path('fetchTarget/', views.fetchTarget, name="fetchTarget"),
        path('fetchIndicator/', views.fetchIndicator, name="fetchIndicator"),
        path('sdgSaveUpdateParams/',views.sdgSaveUpdateParams,name="sdgSaveUpdateParams"),
        path('sdgDeleteParams/<int:id>', views.sdgDeleteParams, name="sdgDeleteParams"),

        #Vegetation Map
        path('dash-admin/vegetation-map',views.vegMapView,name="vegMapView"),
        path('vegMapJsonList/',views.vegMapJsonList,name="vegMapJsonList"),

        #policy 
        path('dash-admin/sdg-policy',views.sdgPolicyView,name="sdgPolicyView"),
        path('sdgPolicyJsonList/',views.sdgPolicyJsonList,name="sdgPolicyJsonList"),
        path('sdgPolicySaveUpdateParams/',views.sdgPolicySaveUpdateParams,name="sdgPolicySaveUpdateParams"),

        path('testpage/', views.testPage,name="testpage")

        # path('fetchTarget/<int:id>', views.fetchTarget, name="fetchTarget"),

   
   ]   