$(document).ready(function(){
    $('.add_product').on('click',function(e){
        e.preventDefault();
        // alert('test123');
        product_id = $(this).attr('data-id');
            // alert(product_id)
        url = $(this).attr('data-url');
        // alert(url)
        data = {
            product_id: product_id,
        }
        
        $.ajax({
            type: 'GET',
            url: url,
            data: data,
            success: function(response){
                // alert(response);
                console.log(response);
            }
        })
    })
});