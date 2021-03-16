from django.urls import path

from .views import add_job, job_detail, apply_to_invest, edit_job

urlpatterns = [
    path('add/', add_job, name='add_job'),
    path('<int:job_id>/', job_detail, name='job_detail'),
    path('<int:job_id>/apply_to_invest/', apply_to_invest, name='apply_to_invest'),
    path('<int:job_id>/edit', edit_job, name='edit_job'),
]