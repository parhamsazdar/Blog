$(document).ready(function () {

    $(".heading_sub").hover(
        function () {
            $(this).children('.collapse').collapse('show');
        }, function () {
            $(this).children('.collapse').collapse('hide');
        }
    );


    $('[name="main_category"]').click(function (event){
        let url="/cat_post/"+$(this).attr('id')
        event.preventDefault()

        window.location.replace(url)


    })




})


