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
