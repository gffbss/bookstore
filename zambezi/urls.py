from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zambezi.views.home', name='home'),
    # url(r'^zambezi/', include('zambezi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'store.views.home', name='home'),
    url(r'^books/$', 'store.views.books', name='books'),
    url(r'^books/view$', 'store.views.new_books', name='new_books'),



)
