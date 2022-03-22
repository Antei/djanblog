from django.urls import path
from . import views

app_name = 'blog'
#urlpatterns = [  
    # представление url шаблонов в удобном виде через функцию post_list
#    path('', views.post_list, name='post_list'), 
#    path('<int:year>/<int:month>/<int:day>/<slug:post>/',  
#	     views.post_detail, name='post_detail'),  
#]

urlpatterns = [  
    # №2 представление url шаблонов в удобном виде через класс PostListView
    path('', views.PostListView.as_view(), name='post_list'),  
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',  
	     views.post_detail, name='post_detail'),  
]