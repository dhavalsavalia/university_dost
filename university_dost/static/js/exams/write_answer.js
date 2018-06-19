var textarea = document.querySelector('textarea');


textarea.addEventListener('keydown', autosize);

function autosize() {
    var el = this;
    setTimeout(function() {
        el.style.cssText = 'height:auto; padding:0';

        el.style.height = (25 + el.scrollHeight) + "px";
        el.style.height = (25 + el.scrollHeight) + "px";
        el.style.padding = "10px";
    }, 0);
}

(function() {

    var md = markdownit().use(markdownitMathjax());
    window.UpdateMath = function(TeX) {

        //set the MathOutput HTML
        document.getElementById("answer").innerHTML = TeX;
        result = md.render($("#answer").text());
        $("div.output").html(result)

        //reprocess the MathOutput Element
        MathJax.Hub.Queue(["Typeset", MathJax.Hub, "preview3"]);

    }
})();

// Not working though
$.ready(function () {
    var ELEMENTS = document.getElementsByClassName('markdown-explanation');
    return Object.keys(ELEMENTS).map(function (key) {
        var explanation_element = ELEMENTS[key], explanation_element_editor = element.querySelector('.markdown-explanation-editor'), explanation_element_preview = element.querySelector('.markdown-explanation-preview');
        // Only add the new MarkdownX instance to fields that have no MarkdownX instance yet.
        if (!explanation_element.hasAttribute('data-markdownx-init')){
            return new MarkdownX(explanation_element, explanation_element_editor, explanation_element_preview);
            console.log("success");
        };
    });
});

(function() {

    var mdx = markdownit().use(markdownitMathjax());
    window.UpdateExplanation = function(TeX) {

        //set the MathOutput HTML
        document.getElementById("explanation").innerHTML = TeX;
        result_explanation = mdx.render($("#explanation").text());
        $("div.output_explanation").html(result_explanation)

        //reprocess the MathOutput Element
        MathJax.Hub.Queue(["Typeset", MathJax.Hub, "preview3"]);

    }
})();

$('#submit').click(function() {
    $('#question').submit();
});
