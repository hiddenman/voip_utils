from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import databrowse
from django.contrib.admin.views.decorators import staff_member_required
from rates.models import *

# The next two lines enable the admin and load each admin.py file:
from django.contrib import admin
admin.autodiscover()


databrowse.site.register(Country)
databrowse.site.register(Area)
databrowse.site.register(Operator)
databrowse.site.register(Rate)
databrowse.site.register(Target)

urlpatterns = patterns('',

                    (r'^$', 'voip_utils.rates.views.reports.redirect_to_admin'),
                    (r'^admin/rates_by_targets/$', 'voip_utils.rates.views.reports.rates_by_targets'),
                    (r'^admin/rates/rates_by_targets/$', 'voip_utils.rates.views.reports.rates_by_targets'),
                    (r'^admin/converter/$', 'voip_utils.rates.views.utilities.converter'),
                    (r'^admin/rates/converter/$', 'voip_utils.rates.views.utilities.converter'),
		    (r'^data/(.*)', staff_member_required(databrowse.site.root)),
		    (r'^admin/', include(admin.site.urls)),
                    )

