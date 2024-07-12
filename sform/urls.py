from django.urls import path
from .views import student_create_view,location_create_view,college_create_view,fetch_bank_details,bank_create_view,student_detail_view,login_view,logout_view,welcome_page,full_detail_view,add_other_details_view

urlpatterns = [
    path('', welcome_page, name='welcome_page'),
    path('create/', student_create_view, name='student_create'),
    path('student/<int:student_id>/', student_detail_view, name='student_detail'),
    path('location/', location_create_view, name='location_create'),
    path('college/', college_create_view, name='college_create'),
    path('bank/', bank_create_view, name='bank_create'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('student/<int:student_id>/full_detail/', full_detail_view, name='full_detail'),
    path('add_other_details/', add_other_details_view, name='add_other_details'),
    path('fetch-bank-details/', fetch_bank_details, name='fetch_bank_details'),
    
]
