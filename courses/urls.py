from django.urls import re_path, include
from . import views

urlpatterns = [
    re_path(r'^my-courses/$', views.ManageCourseListView.as_view(), name='manage_course_list'),
    re_path(r'^create/$', views.CourseCreateView.as_view(), name='course_create'),
    re_path(r'^(?P<pk>\d+)/edit/$', views.CourseUpdateView.as_view(), name='course_edit'),
    re_path(r'^(?P<pk>\d+)/delete/$', views.CourseDeleteView.as_view(), name='course_delete'),

    re_path(r'^$', views.CourseListView.as_view(), name='course_list'),
    re_path(r'^subject/(?P<subject>[\w-]+)/$', views.CourseListView.as_view(), name='course_list_subject'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.CourseDetailView.as_view(), name='course_detail'),

    re_path(r'^api/', include(('courses.api.urls', 'api'), namespace='api')),
]
