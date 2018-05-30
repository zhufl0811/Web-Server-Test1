$(document).ready(function(){
    $("#query").click(function(){
        var name = $("#name").val();
        var price_min = $("#price_min").val();
        var price_max = $("#price_max").val();
        var rank = $("#rank").val();
        var pd = {"name":name, "price_min":price_min,"price_max":price_max,"rank":rank};
        $.ajax({
            type:"post",
            url:"/",
            data:pd,
            cache:false,
            success:function(data){
                window.location.href='/';
            },
            error:function(){
                alert("error!");
            },
        });
    });
});