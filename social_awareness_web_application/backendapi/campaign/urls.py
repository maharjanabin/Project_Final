from django.urls import path
from .views import CampaignPostListView, CampaignPostDetailView, CampaignPostFeaturedView, CampaignPostCategoryView

urlpatterns = [
    path('', CampaignPostListView.as_view()),
    path('featured', CampaignPostFeaturedView.as_view()),
    path('category', CampaignPostCategoryView.as_view()),
    path('<slug>', CampaignPostDetailView.as_view()),
]

