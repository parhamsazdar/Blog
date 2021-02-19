$(document).ready(function () {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $form = $('#comment_edit').remove()
    $formcopy = $form.clone()
    UserId = $form.attr('id_user')

    function ForgetButton(button, parent, copyparent) {
        button.click(function () {
            parent.html(copyparent.html())
            var $EditButtonCopy=parent.find('#link_edit')
            $EditButtonCopy.click(HandleLinkEdit)

        })

    }

    function AjaxEditComment(e){

        e.preventDefault();
        var form = $(this);
        var url = "/api/edit_comment/"+$(this).attr('name');
        $textarea=$('#message')
        $.ajax({
            type: "PUT",
            headers: {'X-CSRFToken': csrftoken},
            url: url,
            data: form.serialize(),
            success: function (resp) {
                console.log(resp);
                $('#alert .modal-body').html(' ویرایش نظر شما در انتظار تایید می باشد')
                $textarea.val('')
                $('#alert').modal('show')
                form.closest('#comment_box').remove()

            },
            error: function (xhr, ajaxOptions, thrownError){
                console.log(xhr)
                $('#alert .modal-body').html(xhr.responseJSON['text'][0])
                $('#alert').modal('show')

            }
        });



    }
    function HandleLinkEdit(e) {
        e.preventDefault()
        var $BoxComment = $(this).closest('#comment_box')
        var $BoxCommentCopy = $BoxComment.clone()
        var copyformccopy = $formcopy.clone()
        $ForgetButton = copyformccopy.find('#forget')
        $BoxComment.html(copyformccopy)
        ForgetButton($ForgetButton, $BoxComment, $BoxCommentCopy)
        var RecordCommentEditButton=$BoxComment.find('#comment_edit')
        RecordCommentEditButton.attr('name',$BoxComment.attr('name'))
        RecordCommentEditButton.submit(AjaxEditComment)


    }

    var CommentBox = document.getElementsByClassName("comment_box");
    $.each(CommentBox, function (index, value) {
        $(value).find('#link_edit').click(HandleLinkEdit)

    })


})