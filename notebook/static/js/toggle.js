document.getElementById('toggle-comment-form').addEventListener('click', function() {
    var form = document.getElementById('comment-form');
    if (form.style.display === 'none' || form.style.display === '') {
        form.style.display = 'block';
    } else {
        form.style.display = 'none';
    }
});
