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
var csrftoken = getCookie('csrftoken');


// This grabs value of #university and call /get_courses/
// After that it will manipulate the DOM and create options for `course_select`
$('#university').change(function() {

    callAjax('../get_courses/', {
            'ui': $(this).val()
        })
        .then(function(data) {
            var course_select = document.getElementById('course_select'),
                course_option = document.createDocumentFragment();
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

    callAjax('../get_subjects/', {
            'ci': $(this).val()
        })
        .then(function(data) {
            var subject_select = document.getElementById('subject_select'),
                subject_option = document.createDocumentFragment();
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

    callAjax('../get_exams/', {
            'si': $(this).val()
        })
        .then(function(data) {
            console.log(data);
            var exams_select = document.getElementById('exams_select'),
                exam_option = document.createDocumentFragment();
            for (i = 0; i < data.length; i++) {
                var option = document.createElement('option');
                option.value = data[i].id;
                option.appendChild(document.createTextNode(data[i].name));
                exam_option.appendChild(option);
            }
            exams_select.appendChild(exam_option);
        })

});


// This simple function is my little pet who keeps everything clean
function callAjax(url, data) {
    return $.ajax({
        type: 'GET',
        url: url,
        data: data
    });
}