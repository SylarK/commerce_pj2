from django.contrib import admin

from auctions.models import *

admin.site.register(User)
admin.site.register(Auction)
admin.site.register(Comment)
admin.site.register(Bid)
admin.site.register(WatchList)