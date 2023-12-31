
$(document).ready(function () {
    const password = $('#password'),
        email = $('#email');

    $('#LoginForm').submit((e) => {
        e.preventDefault();
        const csrftoken = $('input[name=csrfmiddlewaretoken]').val();
        const PostData = {
            password: password.val(),
            email: email.val()
        }

        $.ajax({
            type: "POST",
            url: "/login_user/",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(PostData),
            headers: { "X-CSRFToken": csrftoken },
            success: function (result) {
                if(result.message !='Credenciales incorrectas'){
                    Swal.fire({
                        title: 'Respuesta ',
                        text: result.message,
                        confirmButtonText: '<a style="text-decoration: none; color:  white; font-size: 20px" href="/delete-history/">Ok</a>',
                    });
                }else{
                    Swal.fire({
                        title: 'Respuesta ',
                        text: result.mensaje,
                        confirmButtonText: '<a style="text-decoration: none; color:  white; font-size: 20px">Ok</a>',
                    });
                
                }
            }
        });
        return false;
    });

})