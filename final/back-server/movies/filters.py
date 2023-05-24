from django.db.models import Q, Func, Value
import django_filters

from .models import Movie

class Replace(Func):
    function = 'REPLACE'

class MovieFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method="filter_search")

    class Meta:
        model = Movie
        fields = ["search"]

    def filter_search(self, queryset, name, value):
        # 공백 없이 검색어 처리
        compact_value = value.replace(" ", "")

        # 원본 제목에 대해서도 공백 없이 검색어 처리를 적용합니다.
        queryset = queryset.annotate(
            compact_title=Replace("title", Value(" "), Value("")),
            compact_original_title=Replace("original_title", Value(" "), Value(""))
        )

        return queryset.filter(
            Q(compact_title__icontains=compact_value) | Q(compact_original_title__icontains=compact_value)
        )
