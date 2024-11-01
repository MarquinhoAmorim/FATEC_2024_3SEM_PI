from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'user'

urlpatterns = [
    
    # Index (root URL)
    path('', TemplateView.as_view(template_name='user/index.html'), name='index'),

    # Authentication & Registration
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('cadastro/', views.UserRegistrationView.as_view(), name='cadastro'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    # Dashboard & Profile Views
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard/conta/', views.DashboardContaView.as_view(), name='dashboardConta'),
    path('dashboard/mentorprofile/', views.MentorProfileListView.as_view(), name='mentorProfile'),
    path('dashboard/profile/<int:id>/', views.MentorProfileDetailView.as_view(), name='profile'),

    path('dashboard/chat/', views.DashboardChatView.as_view(), name='dashboardChat'),
    path('dashboard/agendamentosemanal/', views.AgendamentoSemanalView.as_view(), name='agendamentoSemanal'),
    path('dashboard/agendamentomensal/', views.AgendamentoMensalView.as_view(), name='agendamentoMensal'),
]
