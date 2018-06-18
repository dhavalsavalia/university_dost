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

$('#submit').click(function() {
    $('#question').submit();
});
