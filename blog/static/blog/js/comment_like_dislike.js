$(document).ready(function () {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    var $LikeCounter = $('#like_counter_comment')
    var $DislkeCounter = $('#dislike_counter_comment')
    var $LikeLink = $('#comment_like')
    var $DisLikelink = $('#comment_dislike')
    $LikeLink.click(function (e) {

        console.log($LikeLink)
        e.preventDefault();
        var url = $(this).attr('href');
        $.ajax({
            headers: {'X-CSRFToken': csrftoken},
            url: url,
            type: "PUT",
            data: {
                like: $('#user_pk').attr('value'),
            },
            success: function (resp) {

                console.log(resp)
                $('#alert .modal-body').html(resp['result'])
                $('#alert').modal('show')
                if (resp['status'] == 200) {
                    $LikeCounter.html(parseInt($LikeCounter.html()) + 1);
                    $LikeLink.css('color', 'red')
                } else if (resp['status'] == 201) {
                    $LikeCounter.html(parseInt($LikeCounter.html()) + 1);
                    $LikeLink.css('color', 'red')
                    $DislkeCounter.html(parseInt($DislkeCounter.html()) - 1);
                    $DisLikelink.css('color', '#99abb4')
                } else if (resp['status'] == 202) {
                    $LikeCounter.html(parseInt($LikeCounter.html()) - 1)
                    $LikeLink.css('color', '#99abb4')
                }
            },
            error: function (xhr, ajaxOptions, thrownError) {
                console.log(xhr)
                $('#alert .modal-body').html('we have server error')
                $('#alert').modal('show')
            }


        })


    })


    $DisLikelink.click(function (e) {
        e.preventDefault();
        var url = $(this).attr('href');
        $.ajax({
            headers: {'X-CSRFToken': csrftoken},
            url: url,
            type: "PUT",
            data: {
                dislike: $('#user_pk').attr('value'),
            },
            success: function (resp) {

                console.log(resp)
                $('#alert .modal-body').html(resp['result'])
                $('#alert').modal('show')
                if (resp['status'] == 200) {
                    $DislkeCounter.html(parseInt($DislkeCounter.html()) + 1);
                    $DisLikelink.css('color', 'red')
                } else if (resp['status'] == 201) {
                    $DislkeCounter.html(parseInt($DislkeCounter.html()) + 1);
                    $DisLikelink.css('color', 'red')
                    $LikeCounter.html(parseInt($LikeCounter.html()) - 1);
                    $LikeLink.css('color', '#99abb4')
                } else if (resp['status'] == 202) {
                    $DislkeCounter.html(parseInt($DislkeCounter.html()) - 1)
                    $DisLikelink.css('color', '#99abb4')
                }
            },
            error: function (xhr, ajaxOptions, thrownError) {
                console.log(xhr)
                $('#alert .modal-body').html('we have server error')
                $('#alert').modal('show')
            }


        })


    })


})