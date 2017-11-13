from django.conf.urls import url



from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^student_list/$', views.student_list, name='student_list'),
    url(r'^group_list/$', views.group_list, name='group_list'),
    url(r'^exam_list/$', views.exam_list, name='exam_list'),

    url(r'^add_student/$', views.add_student, name='add_student'),
    url(r'^edit_student/(?P<student_id>\d+)/$', views.edit_student, name='edit_student'),
    url(r'^delete_student/(?P<student_id>\d+)/$', views.delete_student, name='delete_student'),

    url(r'^add_group/$', views.add_group, name='add_group'),
    url(r'^edit_group/(?P<group_id>\d+)/$', views.edit_group, name='edit_group'),

    url(r'^add_exam/$', views.add_exam, name='add_exam'),
    url(r'^edit_exam/(?P<exam_id>\d+)/$', views.edit_exam, name='edit_exam'),
    url(r'^delete_exam/(?P<exam_id>\d+)/$', views.delete_exam, name='delete_exam'),

    url(r'^contact_admin/$', views.contact_admin, name='contact_admin'),

    url(r'^journal/$', views.journal, name='journal'),




]
