$(document).ready(function(){
    $('.addprooduct').on('click',function(e){
        e.preventDefault();
        // alert('test123');
        product_slug = $(this).attr('data-id');
            // alert(product_id)
        url = $(this).attr('data-url');
        // alert(url)
        $.ajax({
            type: 'GET',
            url: url,
            success: function(response){
                //  alert(response);
                console.log(response)
                $('#cartCounter').html(response.cartCount['items_in_cart']);
                $('#qnty').html(response.prodQnty);
            }
        })
    })
    // delete product from cart:
    $('.deleteprod').on('click',function(e){
        e.preventDefault();
        // alert('test123');
        product_slug = $(this).attr('data-id');
            // alert(product_id)
        url = $(this).attr('data-url');
        // alert(url)
        $.ajax({
            type: 'GET',
            url: url,
            success: function(response){
                //  alert(response);
                console.log(response)
                $('#cartCounter').html(response.cartCount['items_in_cart']);
                $('#qnty').html(response.prodQnty);
            }
        })
    })
});