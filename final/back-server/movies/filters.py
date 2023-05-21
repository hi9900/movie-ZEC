from django.db.models import Q
import django_filters

from .models import Movie

class MovieFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method="filter_search")

    class Meta:
        model = Movie
        fields = ["search"]

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) #| Q(director__icontains=value) 
        )
