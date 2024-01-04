
$(document).ready(() => {
    const name = $('#name'),
        password = $('#password'),
        email = $('#email');

    $('#RegisterForm').submit((e) => {
        e.preventDefault();
        const csrftoken = $('input[name=csrfmiddlewaretoken]').val();
        const PostData = {
            name: name.val(),
            password: password.val(),
            email: email.val()
        }
        $.ajax({
            type: "POST",
            url: "/create-user/",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(PostData),
            headers: { "X-CSRFToken": csrftoken },
            success: function (result) {

                Swal.fire({
                    title: 'Respuesta ',
                    text: result.message,
                    confirmButtonText: '<a style="text-decoration: none; color:  white; font-size: 20px" href="/">Ok</a>',
                });
            }
        });
        return false;
    });

})