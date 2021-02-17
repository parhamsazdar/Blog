$(document).ready(function () {

    $("#comment").submit(function (e) {
        e.preventDefault();
        var form = $(this);
        var url = form.attr('action');
        $textarea=$('#message')
        $.ajax({
            type: "POST",
            url: url,
            data: form.serialize(),
            success: function (resp) {
                console.log(resp);
                $('#alert .modal-body').html('نظر شما در انتظار تایید می باشد')
                $textarea.val('')
                $('#alert').modal('show')

            },
            error: function (xhr, ajaxOptions, thrownError){
                console.log(xhr)
                $('#alert .modal-body').html(xhr.responseJSON['text'][0])
                $('#alert').modal('show')

            }
        });
    });














})