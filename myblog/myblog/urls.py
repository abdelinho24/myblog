from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blog.views',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'index', name='index'),
    #url(r'^blog/view/(?P<slug>[^\.].html', 'view_post', name='view_blog_post'),
    url(r'^/about$', 'about', name='about'),
    url(r'^/contact$', 'contact', name='contact'),

    url(r'^admin/', include(admin.site.urls)),
)
