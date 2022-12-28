from rest_framework.urls import path
from .views import TypeViewSet, GenreViewSet, CardViewSet, ReviewViewSet, ReviewForCardAPIView
urlpatterns = [
    path('type/', TypeViewSet.as_view({"get": "list"})),
    path('genre/', GenreViewSet.as_view({'get': 'list'})),
    path('manga/', CardViewSet.as_view({'get': 'list'})),
    path('manga/<int:id>/', CardViewSet.as_view({'get': 'retrieve'})),
    path('manga/<int:id>/reviews/', ReviewForCardAPIView.as_view()),
    path('reviews/<int:id>/', ReviewViewSet.as_view({'get': "retrieve",
                                                     "put": "update",
                                                     "patch": "partial_update",
                                                     "delete": "destroy"}))
]