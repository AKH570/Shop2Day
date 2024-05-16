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
                    $('#cartCounter').html(response.cartCount['items_in_cart']); //cartCounter is id of cart in navber//
                    $('#qnty').html(response.prodQnty); //qnty is id of plus in productdetail page
                }
            }
        })
    })
    // decrease product from cart:
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
    // delete cart
    $('.delCart').on('click',function(e){
        e.preventDefault();
        // alert('test123');
        // return false; 
        cart_id = $(this).attr('data-id');
        url = $(this).attr('data-url');
        $.ajax({
            type: 'GET',
            url: url,
            success: function(response){
                console.log(response)
                if(response.status=='Failed'){
                    swal(response.message, "", "error")
                }
                else{
                    $('#cartCounter').html(response.cartCount['items_in_cart']);
                    swal(response.message,'', "success")
                    deleteCartItem(0, cart_id);
                    checkemptycart();
                    shophere();
                }
            }
        })
    })

    // delete cart without reloading page
    function deleteCartItem(itemQnty,cart_id){
        if(itemQnty <= 0){
            document.getElementById("cart_element-"+cart_id).remove()
        }       
    }
    // to show text when cart is empty
    function checkemptycart(){
        var cartcounter = document.getElementById('cartCounter').innerHTML
        if (cartcounter == 0){
            document.getElementById('empty-cart').style.display = 'block';
        }
    }
    function shophere(){
        var c_tcounter = document.getElementById('cartCounter').innerHTML
        if (c_tcounter == 0){
            document.getElementById('shop-here').style.display = 'block';
        }
    }
});