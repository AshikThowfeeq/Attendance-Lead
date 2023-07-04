from django.urls import path
from .views import attendance_view,import_csv_to_database,update_database_from_csv,login_view,homepage

urlpatterns = [
    # Other URL patterns
    path('attendance/', attendance_view, name='attendance'),
    path('import-csv/', import_csv_to_database, name='import-csv'),
    path('update-database/',update_database_from_csv, name='update_database'),
    path('',login_view, name='login'),
    path('dashboard', homepage, name='dashboard'),
]
