const fileBtn = document.getElementById('files');
const customBtn = document.getElementById('custom_button');
const likesIcon = document.getElementById('likes_icon');

customBtn.addEventListener('click', function() {
    fileBtn.click();
});