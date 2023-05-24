import django_filters
from django.db.models import Q, Func, Value
from django.db.models.functions import Replace

from .models import Movie


class MovieFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method="filter_search")
    
    director = django_filters.CharFilter(field_name="director__name", lookup_expr='icontains')
    actor = django_filters.CharFilter(field_name="characters__actor__name", lookup_expr='icontains')
    character = django_filters.CharFilter(field_name="characters__character", lookup_expr='icontains')
    genre = django_filters.CharFilter(field_name="genres__name", lookup_expr='icontains')


    class Meta:
        model = Movie
        fields = ["search", "director", "actor", "character", "genre"]

    def filter_search(self, queryset, name, value):
        # 공백 없이 입력 처리
        compact_value = value.replace(" ", "")

        # 원본 제목에 대해서도 공백 없이 
        queryset = queryset.annotate(
            compact_title=Replace("title", Value(" "), Value("")),
            compact_original_title=Replace("original_title", Value(" "), Value(""))
        )

        return queryset.filter(
            Q(compact_title__icontains=compact_value) | Q(compact_original_title__icontains=compact_value)
        )
