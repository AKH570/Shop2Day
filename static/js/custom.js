$(document).ready(function(){
    $('.addprooduct').on('click',function(e){
        e.preventDefault();
        // alert('test123');
        product_slug = $(this).attr('data-id');
            // alert(product_id)
        url = $(this).attr('data-url');
        // alert(url)
        data = {
            product_slug: product_slug,
        }
        $.ajax({
            type: 'GET',
            url: url,
            data: data,
            success: function(response){
                //  alert(response);
                console.log(response)
                $('#cartCounter').html(response.cartCount['items_in_cart']);
                $('#qnty').html(response.prodQnty);
            }
        })
    })
    // to load the cartqty in product details pages:
    // $('.productQty').each
});