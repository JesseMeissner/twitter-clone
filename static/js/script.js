const fileBtn = document.getElementById('files');
const customBtn = document.getElementById('custom_button');
const likesIcon = document.getElementById('likes_icon');
const menuBtn = document.getElementById('menu_icon');

customBtn.addEventListener('click', function() {
    fileBtn.click();
});

$(function() {
    $('.js-menu-icon').click(function() {
        $(this).next().toggle();
    })
})