// add to cart
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
                console.log(response)
                if(response.status == 'login_required'){
                    swal(response.message, "", "info").then(function(){
                        window.location='/accounts/login';
                    })
                }else if(response.status == 'Failed'){
                    swal(response.message, "", "error")
                }
                else{
                    $('#cartCounter').html(response.cartCount['items_in_cart']);
                    $('#qnty').html(response.prodQnty);
                }
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
                console.log(response)
                if(response.status == 'login_required'){
                    swal(response.message, "", "info").then(function(){
                        window.location='/accounts/login';
                    })
                }else if(response.status=='Failed'){
                    swal(response.message, "", "error")
                }
                else{
                    $('#cartCounter').html(response.cartCount['items_in_cart']);
                    $('#qnty').html(response.prodQnty);}
            }
        })
    })
});