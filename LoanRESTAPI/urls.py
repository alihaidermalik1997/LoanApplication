"""LoanRESTAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import SignUpView, SignInView, ManageUserView
from application.views import LoanApplicationCreateView, LoanApplicationDetailView, ManageLoanApplicationView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/signup/', SignUpView.as_view(), name='signup'),
    path('api/user/signin/', SignInView.as_view(), name='signin'),
    path('api/loan-application/', LoanApplicationCreateView.as_view(), name='loan-application-create'),
    path('api/last-loan-application/', LoanApplicationDetailView.as_view(), name='loan-application-get'),
    path('api/loan-application/<int:id>/', ManageLoanApplicationView.as_view(), name='manage-loan-application'),
    path('api/manage_user/<int:id>/', ManageUserView.as_view(), name='manage-user'),
]
