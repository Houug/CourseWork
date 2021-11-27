$(window).resize(function () {
    if (($(window).width() !== 900) && ($(window).height() !== 500)) {
        window.resizeTo(900, 500);
    }
});