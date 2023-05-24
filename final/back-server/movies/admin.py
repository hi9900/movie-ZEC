from django.contrib import admin
from .models import *

# # class PostAdmin(admin.ModelAdmin):
# #     list_display = '__all__' # : Admin 목록에 보여질 필드 목록
# #     list_display_links = '__all__' #  : 목록 내에서 링크로 지정할 필드 목록 (이를 지정하지 않으면, 첫번째 필드에만 링크가 적용)
# #     list_editable = '__all__' #  : 목록 상에서 수정할 필드 목록
# #     # list_per_page = '__all__' #  : 페이지 별로 보여질 최대 갯수 (디폴트 : 100)
# #     list_filter = '__all__' #  : 필터 옵션을 제공할 필드 목록
# #     actions = '__all__' #  : 목록에서 수행할 action 목록

# # Register your models here.
# @admin.register(Movie)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'original_language', 'original_title', 'overview', 'release_date', 'popularity', 'vote_count', 'vote_average', 'poster_path', 'backdrop_path', 'runtime')
#     list_display_links = ('id', 'title')
#     list_editable = ('overview',)  # Do not include 'id' in list_editable
#     list_filter = ('original_language', 'release_date')


admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Keyword)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(MovieList)