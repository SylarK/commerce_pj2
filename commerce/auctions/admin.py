from django.contrib import admin

from auctions.models import *

class viewAuction(admin.ModelAdmin):
    list_display = ('id','user', 'title', 'init', 'cat', 'status')

class viewResult(admin.ModelAdmin):
    list_display = ('id', 'user', 'toauction')

admin.site.register(User)
admin.site.register(Auction, viewAuction)
admin.site.register(Comment)
admin.site.register(Bid)
admin.site.register(WatchList)