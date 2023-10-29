from django.urls import path
from . import views

urlpatterns = [
    path("candidate_list/", views.candidate_list, name='candidate_list'),
    path("add_candidate/", views.add_candidate, name='add_candidate'),
    path("vote_index/", views.vote_index, name='vote_index'),
    path('<int:position_id>/', views.detail, name ='detail'),
	path('<int:position_id>/vote/', views.vote, name ='vote'),
]