
from django.urls import path

from . import views

urlpatterns = [
    # path("", views.home, name="home"),
    path('SoftwareFirm/', views.multi_step_registration, name='multi_step'),
    path('step/<int:step>/', views.multi_step_registration, name='multi_step'),
    path('individual/', views.individual_reg, name='individual_reg'),
    path('', views.dashboard_data, name='dashboard_view'),
    path("index/", views.index, name="index"),
    path("authlogout/", views.authlogout, name="authlogout"),
    path('Myprofile/', views.Myprofile, name='Myprofile'),
    path('editProfile/', views.profileChange, name='editProfile'),
    path('saveEditProfile/', views.saveEditProfile, name='saveEditProfile'),
    path('mySupport/', views.mySupport, name='mySupport'),
    path('changeMyPassword/', views.resetPassword, name='changeMyPassword'),
    path('saveChangeMyPassword/', views.saveChangeMyPassword, name='saveChangeMyPassword'),
    path('notifications/', views.notifications, name='notifications'),
    path('markAsRead/<int:pk>/', views.markAsRead, name='markAsRead'),
    path('viewMynotifications/<int:pk>/', views.viewMynotifications, name='viewMynotifications'),
    path('application_status/', views.application_status, name='application_status'),
    path('startup-toolkit/', views.startup_toolkit, name='startup_toolkit'),
    path('legal-templates/', views.legal_templates, name='legal_templates'),
    path('collaboration-board/', views.collaboration_board, name='collaboration_board'),
    path('events/', views.events_view, name='events'),
    path('statistics/', views.dashboard_stats, name='dashboard_stats'),
    path("edit-dev/<int:pk>/", views.edit_dev, name="edit_dev"),
    path("edit-reg/<int:pk>/", views.edit_reg, name="edit_reg"),

]
