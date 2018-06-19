// This handles generation of CSRF token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});


// This grabs value of #university and call /get_courses/
// After that it will manipulate the DOM and create options for `course_select`
$('#university').change(function() {

    callAjax("/exams/get_courses/", {
            'ui': $(this).val()
        })
        .then(function(data) {
            var course_select = document.getElementById('course_select'),
                course_option = document.createDocumentFragment();

            // Remove previous options
            document.getElementById("course_select").options.length = 0;
            
            // Create defualt option which is disabled
            var default_option = document.createElement('option');
            default_option.selected = "true";
            default_option.disabled = "disabled";
            default_option.appendChild(document.createTextNode("Select Course"));
            course_option.appendChild(default_option);

            // Actual options from API
            for (i = 0; i < data.length; i++) {
                var option = document.createElement('option');
                option.value = data[i].id;
                option.appendChild(document.createTextNode(data[i].name));
                course_option.appendChild(option);
            }
            course_select.appendChild(course_option);
        })

});


// This grabs value of #course_select and call /get_subjects/
// After that it will manipulate the DOM and create options for `subject_select`
$('#course_select').change(function() {

    callAjax("/exams/get_subjects/", {
            'ci': $(this).val()
        })
        .then(function(data) {
            var subject_select = document.getElementById('subject_select'),
                subject_option = document.createDocumentFragment();

            // Remove previous options
            document.getElementById("subject_select").options.length = 0;

            // Create defualt option which is disabled
            var default_option = document.createElement('option');
            default_option.selected = "true";
            default_option.disabled = "disabled";
            default_option.appendChild(document.createTextNode("Select Subject"));
            subject_option.appendChild(default_option);

            // Actual options from API
            for (i = 0; i < data.length; i++) {
                var option = document.createElement('option');
                option.value = data[i].id;
                option.appendChild(document.createTextNode(data[i].name));
                subject_option.appendChild(option);
            }
            subject_select.appendChild(subject_option);
        })

});


// This grabs value of #subject_select and call /get_exams/
// After that it will manipulate the DOM and create options for `exams_select`
$('#subject_select').change(function() {

    callAjax("/exams/get_exams/", {
            'si': $(this).val()
        })
        .then(function(data) {
            var exams_select = document.getElementById('exams_select'),
                exam_option = document.createDocumentFragment();
            
            // Remove previous options
            document.getElementById("exams_select").options.length = 0;

            // Create defualt option which is disabled
            var default_option = document.createElement('option');
            default_option.selected = "true";
            default_option.disabled = "disabled";
            default_option.appendChild(document.createTextNode("Select Exam"));
            exam_option.appendChild(default_option);

            // Actual options from API
            for (i = 0; i < data.length; i++) {
                var option = document.createElement('option');
                option.value = data[i].id;
                var exam_name = data[i].month + "-" + data[i].year;
                option.appendChild(document.createTextNode(exam_name));
                exam_option.appendChild(option);
            }
            exams_select.appendChild(exam_option);
        })

});


// This simple function is my little pet who keeps everything clean
function callAjax(url, data) {
    return $.ajax({
        type: 'POST',
        url: url,
        data: data,
        "beforeSend": function(xhr, settings) {
            $.ajaxSettings.beforeSend(xhr, settings);
        },
    });
}


//jQuery time
var current_fs, next_fs, previous_fs; //fieldsets
var left, opacity, scale; //fieldset properties which we will animate
var animating; //flag to prevent quick multi-click glitches

$(".next").click(function() {
    if (animating) return false;
    animating = true;

    current_fs = $(this).parent();
    next_fs = $(this).parent().next();

    //activate next step on progressbar using the index of next_fs
    $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

    //show the next fieldset
    next_fs.show();
    //hide the current fieldset with style
    current_fs.animate({
        opacity: 0
    }, {
        step: function(now, mx) {
            //as the opacity of current_fs reduces to 0 - stored in "now"
            //1. scale current_fs down to 80%
            scale = 1 - (1 - now) * 0.2;
            //2. bring next_fs from the right(50%)
            left = (now * 50) + "%";
            //3. increase opacity of next_fs to 1 as it moves in
            opacity = 1 - now;
            current_fs.css({
                'transform': 'scale(' + scale + ')'
            });
            next_fs.css({
                'left': left,
                'opacity': opacity
            });
        },
        duration: 800,
        complete: function() {
            current_fs.hide();
            animating = false;
        },
        //this comes from the custom easing plugin
        easing: 'easeInOutBack'
    });
});

$(".previous").click(function() {
    if (animating) return false;
    animating = true;

    current_fs = $(this).parent();
    previous_fs = $(this).parent().prev();

    //de-activate current step on progressbar
    $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

    //show the previous fieldset
    previous_fs.show();
    //hide the current fieldset with style
    current_fs.animate({
        opacity: 0
    }, {
        step: function(now, mx) {
            //as the opacity of current_fs reduces to 0 - stored in "now"
            //1. scale previous_fs from 80% to 100%
            scale = 0.8 + (1 - now) * 0.2;
            //2. take current_fs to the right(50%) - from 0%
            left = ((1 - now) * 50) + "%";
            //3. increase opacity of previous_fs to 1 as it moves in
            opacity = 1 - now;
            current_fs.css({
                'left': left
            });
            previous_fs.css({
                'transform': 'scale(' + scale + ')',
                'opacity': opacity
            });
        },
        duration: 800,
        complete: function() {
            current_fs.hide();
            animating = false;
        },
        //this comes from the custom easing plugin
        easing: 'easeInOutBack'
    });
});
