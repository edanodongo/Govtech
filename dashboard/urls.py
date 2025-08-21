
from django.urls import path

from .views import multi_step_registration, individual_reg, index, authlogout, \
    Myprofile, profileChange, saveEditProfile, mySupport, resetPassword, saveChangeMyPassword, dashboard_view, \
    notifications, markAsRead, viewMynotifications, application_status, startup_toolkit, legal_templates, \
    collaboration_board, events_view, dashboard_stats  # DashboardData

urlpatterns = [
    # path("", views.home, name="home"),
    path('SoftwareFirm/', multi_step_registration, name='multi_step'),
    path('step/<int:step>/', multi_step_registration, name='multi_step'),
    path('individual/', individual_reg, name='individual_reg'),
    path('', dashboard_view, name='dashboard_view'),
    path("index/", index, name="index"),
    path("authlogout/", authlogout, name="authlogout"),
    path('Myprofile/', Myprofile, name='Myprofile'),
    path('editProfile/', profileChange, name='editProfile'),
    path('saveEditProfile/', saveEditProfile, name='saveEditProfile'),
    path('mySupport/', mySupport, name='mySupport'),
    path('changeMyPassword/', resetPassword, name='changeMyPassword'),
    path('saveChangeMyPassword/', saveChangeMyPassword, name='saveChangeMyPassword'),
    path('notifications/', notifications, name='notifications'),
    path('markAsRead/<int:pk>/', markAsRead, name='markAsRead'),
    path('viewMynotifications/<int:pk>/', viewMynotifications, name='viewMynotifications'),
    path('application_status/', application_status, name='application_status'),
    path('startup-toolkit/', startup_toolkit, name='startup_toolkit'),
    path('legal-templates/', legal_templates, name='legal_templates'),
    path('collaboration-board/', collaboration_board, name='collaboration_board'),
    path('events/', events_view, name='events'),
    path('statistics/', dashboard_stats, name='dashboard_stats'),

]
