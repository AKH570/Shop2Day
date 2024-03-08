from django.shortcuts import render

# Create your views here.

def Reviews(request,id):
        comment=request.POST['comment']
        user=request.user
        activeAuction = Auction_listing.objects.get(pk=id)

        newComment = Comments(
            author = user,
            message = comment,
            auctionName=activeAuction
        )
        newComment.save()

        return HttpResponseRedirect(reverse(listingAuction,args=(id, )))