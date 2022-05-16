$(document).ready(() => {
const signInBtn = document.querySelector('.signin-btn');
const signUpBtn = document.querySelector('.signup-btn');
const formBox = document.querySelector('.form-box');
const body = document.body;


signUpBtn.addEventListener('click', function(e){
    e.preventDefault();
    formBox.classList.add('active');
    body.classList.add('active')
});

signInBtn.addEventListener('click', function(e){
    e.preventDefault();
    formBox.classList.remove('active');
    body.classList.remove('active')
});

$("#btn_in").on('click', function(e) {
        e.preventDefault();
        const formData = {
            'email': $('#email_in').val(),
            'login': $('#login_in').val(),
            'password': $('#password_in').val()
        };
        $.ajax({
        type: 'post',
        url: '/authorization/registration',
        data: JSON.stringify(formData),
        contentType: "application/json; charset=utf-8",
        traditional: true,
        });

});
});
