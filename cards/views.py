from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, generics, permissions
from .models import Type, Genre, Card, Review
from .serializers import TypeSerializer, CardSerializer, GenreSerializer, ReviewSerializer, ReviewCreateSerializer
from author.permissions import IsAdminOrReadOnly, IsAuthorPermission
from .services import CardFilter, CustomSearchFilter
# Create your views here.


class TypeViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [IsAdminOrReadOnly, ]


class GenreViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly, ]


class CardViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    filter_backends = [DjangoFilterBackend, CustomSearchFilter]
    filterset_class = CardFilter
    search_fields = ['^title']
    lookup_field = 'id'


class ReviewViewSet(mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthorPermission, ]
    lookup_field = 'id'


class ReviewForCardAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Review.objects.all()
        print(self.request.query_params)
        cards_id = self.request.query_params.get('id')
        if cards_id:
            queryset = queryset.filter(cards__id__exact=cards_id)
        return queryset

    def get_serializer_class(self, *args, **kwargs):
        """Returns the appropriate serializer class based on the request method."""
        if self.request.method in permissions.SAFE_METHODS:
            return ReviewSerializer
        return ReviewCreateSerializer

    def perform_create(self, serializer, **kwargs):
        """Associates the created Review model object with the Card object with the provided id."""
        serializer.validated_data['cards'] = Card.objects.get(id=self.kwargs['id'])
        serializer.save()
