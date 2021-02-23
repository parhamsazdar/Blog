$(document).ready(function () {

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    var $Result = $('#result_search')
    var $ResultItem = $('#result_item').remove()


    $('a#form_search').click(function (){
        $('form#form_search')[0].reset();
    })



    var ajaxFunction = function (data) {
        list = []
        $.ajax({
            headers: {'X-CSRFToken': csrftoken},
            type: "GET",
            url: "/api/post_all/",
            data: {search_word: data},
            success: function (resp) {
                console.log(resp)
                $Result.empty()
                if (resp) {
                    $Result.show()
                    for (post of resp) {
                        $$ResultItemCopy = $ResultItem.clone().attr('href','/post/'+post['id'])
                        $$ResultItemCopy.find('li').html(" عنوان: " + post['title'])
                        $Result.append($$ResultItemCopy)
                    }
                }

            }
        });

    }
    var $search = $('#search')


    $search.on('keyup paste', function () {
        if (this.value.length >= 1) {
            ajaxFunction(this.value);
        } else {
            $Result.empty()
        }

    });

});


