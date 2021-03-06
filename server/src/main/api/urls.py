from django.conf.urls import re_path, include, url
from .views import (WorkshopListAPIView, EventListAPIView, 
                    WorkshopDetailAPIView, EventDetailAPIView, MemberListAPIView,
                    UserRegisterAPIView, UserLoginAPIView, UserEmailVerificationView,
                    ClassRoomView, ClassCourseView, ContactUsAPIView, LatestWorkshopListAPIView,
                     UserEnrollmentView, ForgotPassword,ResetPassword, WorkshopEnrollmentView)
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = [
    url(r'^events/$', EventListAPIView.as_view(), name='events'),
    url(r'^workshops/$', WorkshopListAPIView.as_view(), name='workshops'),
    url(r'^workshops/detail/(?P<name>\w+)/$', WorkshopDetailAPIView.as_view(), name='workshops-details'),
    url(r'^workshops/latest/$', LatestWorkshopListAPIView.as_view(), name='current-workshops'),
    url(r'^workshops/enrollments/$', WorkshopEnrollmentView.as_view(), name='enroll-workshops'),
    url(r'^events/detail/(?P<pk>[0-9]+)/$', EventDetailAPIView.as_view(), name='event-details'),
    url(r'^members/$', MemberListAPIView.as_view(), name='members'),
    url(r'^auth/register/$', UserRegisterAPIView.as_view(), name='user-register'),
    url(r'^auth/login/$', UserLoginAPIView.as_view(), name='user-register'),
    url(r'^auth/verify/$',  verify_jwt_token, name='token-verify'),
    url(r'^auth/activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        UserEmailVerificationView.as_view(), name='email-activation'),
    url(r'^auth/password/forgot/$', ForgotPassword.as_view(), name='forgot-password'),
    url(r'^auth/password/reset/$', ResetPassword.as_view(), name='reset-password'),
    url(r'^user/classroom/$', ClassRoomView.as_view(), name='user-classroom'),
    url(r'^user/enroll/$', UserEnrollmentView.as_view(), name='user-enrollment'),
    url(r'^user/classroom/(?P<workshopid>[0-9]+)/$', ClassCourseView.as_view(), name='class-course'),
    url(r'^contact/$', ContactUsAPIView.as_view(), name="contact-us"),

]