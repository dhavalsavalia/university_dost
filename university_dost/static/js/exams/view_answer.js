// Init Markdown-It
var md = markdownit().use(markdownitMathjax());

// This handles question_body_output
result_question = md.render($("#question_body").text());
$("div.question_body_output").html(result_question);

// This handles answer_output
result_answer = md.render($("#answer").text());
$("div.answer_output").html(result_answer);

// This handle explanation_output
result_explanation = md.render($("#explanation").text());
$("div.explanation_output").html(result_explanation);

// Select all the img tags in .answer_output and .explanation_output
// and addClass("img-fluid") to make them responsive
$(".answer_output, .explanation_output").find('*','img').addClass("img-fluid");


// Vote Vote Vote
// This handles upvote and stops page from refreshing
// why? because, duh? I wrote this shit in 2018
$('#upvote').submit(function(e){
    $.post('./vote/', $(this).serialize(), function(data){
        $('.vote_area').html(`<div class='alert alert-success' role='alert'>
                                    You vote has been registered! Thank you for making UniversityDost a better place to learn.
                                </div>`);
    });
    e.preventDefault();
});

$('#downvote').submit(function(e){
    $.post('./vote/', $(this).serialize(), function(data){
        $('.vote_area').html(`<div class='alert alert-success' role='alert'>
                                  You vote has been registered! Thank you for making UniversityDost a better place to learn.
                              </div>`);
    });
    e.preventDefault();
});

// This handles answer feedbacks
$('#answer_feedback').submit(function(e){
    $.post('./feedback/', $(this).serialize(), function(data){
        $('.modal-body').html(`<div class='alert alert-success' role='alert'>
                                  Thank you for your feedback! We will take appropriate soon.
                              </div>`);
        $('.modal-footer').html('<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>');
    });
    e.preventDefault();
});


