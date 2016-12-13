//Functions for user authentication and register with AJAX

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

//This function register a new user.
function register(){
    var iName = $('#inputName').val()
    var iUsername = $('#inputUsername').val()
    var iPass = $('#inputPassword').val()
    if (iName == '' || iUsername == '' || iPass == '') {
        alert("Some fields are empty!");
    } else{
        $.ajax({
            url : "/register/",
            type : "POST",
            data : { 
                name : iName,
                username : iUsername,
                password : iPass,
                 },

            success : function(json) {
                if (json == true) {
                    parent.window.document.location.href = '';
                } else {
                    alert("Something went wrong. Try with other parameters...");
                }            
            },

            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
               alert("Something went wrong.")

            }
        }); 
    }   
}

//This function make autentication for the user
function login(){
    var iUsernameL = $('#inputUsernameL').val()
    var iPassL = $('#inputPasswordL').val()
    console.log(iUsernameL, iPassL)
    if (iUsernameL == '' || iPassL == '') {
        alert("Some fields are empty!");
    } else{
        $.ajax({
            url : "/login/",
            type : "POST",
            data : { 
                username : iUsernameL,
                password : iPassL,
                 },

            success : function(json) {
                if (json == true) {
                    parent.window.document.location.href = '';
                } else {
                    alert("Incorrect parameters...");
                }            
            },

            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
               alert("Something went wrong.")

            }
        }); 
    }   
}

//This function make logout for user.
function logout(){
    $.ajax({
        url : "/logout/",
        type : "GET",
        
        success : function(json) {
            if (json == true) {
                parent.window.document.location.href = '';
            } else {
                alert("Something went wrong....");
            }            
        },

        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
           alert("Something went wrong.")

        }
    }); 
       
}

//This function delete an account.
function delete_account(){
    $.ajax({
        url : "/delete/",
        type : "GET",
        
        success : function(json) {
            if (json == true) {
                parent.window.document.location.href = '';
            } else {
                alert("Something went wrong....");
            }            
        },

        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
           alert("Something went wrong.")

        }
    }); 
       
}

$("#slide_recently").slick();
$("#slide_all").slick();


//Standard of use CSRF with AJAX
function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    }); 

