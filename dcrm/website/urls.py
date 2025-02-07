# copy from urls.py in dcrm/dcrm
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('records/<int:customer_id>', views.customer_record, name='record'),
    path('delete_record/<int:customer_id>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('edit_record/<int:customer_id>', views.edit_record, name='edit_record')

]
