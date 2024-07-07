from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.logins, name='login'),  #it is used for login 
    path("register/" ,views.register_account),   #it is used register
    path("logout/",views.user_logout),         #it is used for logout
    path("views/",views.view_flight),         #it is used to view all flights 
    path("my_booking/",views.my_bookings),       #it is used to view booking done by meeee
    path('add_flight/',views.book_flight),       #it is function to make booking     
    path("search/",views.search_flights)           #it is done to search flight related to time 
]