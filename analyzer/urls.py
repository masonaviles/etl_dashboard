from django.urls import path
from .views import upload_view, result_view

app_name = 'analyzer'

urlpatterns = [
    path('', upload_view, name='upload'),
    path('results/<int:session_id>/', result_view, name='results'),
]
