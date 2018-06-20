// Resizes height of #answer as needed
var answer_textarea = document.querySelector('#answer');
answer_textarea.addEventListener('keydown', autosize);

// Resizes height of #explanation as needed
var explanation_textarea = document.querySelector('#explanation');
explanation_textarea.addEventListener('keydown', autosize);


// Actual function that handles autosize
function autosize() {
    var el = this;
    setTimeout(function() {
        el.style.cssText = 'height:auto; padding:0';

        el.style.height = (25 + el.scrollHeight) + "px";
        el.style.height = (25 + el.scrollHeight) + "px";
        el.style.padding = "10px";
    }, 0);
};


// This function render Markdown-It text with MathJax for answer
(function() {

    var md = markdownit().use(markdownitMathjax());
    window.UpdateMath = function(TeX) {

        //set the MathOutput HTML
        document.getElementById("answer").innerHTML = TeX;
        result_answer = md.render($("#answer").text());
        $("div.output_answer").html(result_answer);

        //reprocess the MathOutput Element
        MathJax.Hub.Queue(["Typeset", MathJax.Hub, "preview3"]);

    }
})();


// This function render Markdown-It text with MathJax for explanation
(function() {

    var mdx = markdownit().use(markdownitMathjax());
    window.UpdateExplanation = function(TeX) {

        //set the MathOutput HTML
        document.getElementById("explanation").innerHTML = TeX;
        result_explanation = mdx.render($("#explanation").text());
        $("div.output_explanation").html(result_explanation);

        //reprocess the MathOutput Element
        MathJax.Hub.Queue(["Typeset", MathJax.Hub, "preview3"]);

    }
})();

$('#submit').click(function() {
    $('#question').submit();
});
