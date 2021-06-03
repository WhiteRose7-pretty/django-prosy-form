from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    enable_nav_sidebar = False