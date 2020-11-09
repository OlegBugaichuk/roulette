$(document).ready(function () {
    for (i = 0; i < 5; i++) {
        $(".list li").clone().appendTo(".list");
    }
    $('.button').click(function () {
        $('.window').css({
            right: "0"
        })
        $('.list li').css({
            border: '4px solid transparent'
        })
        function selfRandom(min, max) {
            return Math.floor(Math.random() * (max - min + 1)) + min;
        }
        var x = selfRandom(20, 100);
        $('.window').animate({
            right: ((x*130)+(x*3-12)-119)
        }, 5000);
    });
});