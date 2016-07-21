# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
	# URL pattern for the UserListView
    url(
        regex=r'^signup/$',
        view=views.SignupView.as_view(),
        name='portal-signup'
    ),
    url(
        regex=r'^signup-success/$',
        view=views.get_singup_success,
        name='portal-signup-success'
    ),
    url(
        regex=r'^signup-error/$',
        view=views.get_singup_error,
        name='portal-signup-error'
    ),
]