// Favorites Button and Counter
// Uses jQuery AJAX
$('a[id=favorite]').on('click', function(event) {
    event.preventDefault();
    var button = $(this);

    $.ajax({
        url: '/like_motorcycle/',
        type: 'POST',
        data: { motorcycle_id: button.attr("data-id") },

        success: function(response) {
            // Toggle Favorites Button
            button.toggleClass("favorited");
            
            // Favorites Counter
            var counter = $('#favorites');
            counter_text = counter.html();
            if (response == 'add') {
                // Increment Favorites Counter
                if (counter_text == '') {
                    counter.html('(1)');
                } else {
                    counter_int = parseInt(counter_text.substring(1, counter_text.length-1));
                    counter_int++;
                    counter.html('(' + counter_int + ')');
                }                

            } else if (response == 'remove') {
                // Decrement Favorites Counter
                if (counter_text == '(1)' || counter_text == '') {
                    counter.html('');
                } else {
                    counter_int = parseInt(counter_text.substring(1, counter_text.length-1));
                    counter_int--;
                    counter.html('(' + counter_int + ')');
                }

            }
        }
    });
});

// You need these methods to add the CSRF token using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
