from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^register/$', views.StudentRegistrationView.as_view(), name='student_registration'),
    url(r'^enroll-course/$', views.StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    url(r'^leave-course/$', views.StudentLeaveCourseView.as_view(), name='student_leave_course'),

    # Restore password
    url(r'^password-reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password-reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^password-reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),

    url(r'^courses/$', views.StudentCourseListView.as_view(), name='student_course_list'),
    url(r'^course/(?P<pk>\d+)/$', views.StudentCourseEnrolledView.as_view(), name='student_course_detail')
]
