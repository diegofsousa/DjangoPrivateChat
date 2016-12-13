//Chat room functions

setTimeout("get_new_massages()", 1);
setInterval("get_new_massages()", 2000);
setTimeout("verify_read()", 1);
setInterval("verify_read()", 2000);

var oldm = 0;

//When "enter" has pressed
$(document).keypress(function(e) {
    if(e.which == 13){
        if ($("#field").val() !== "" && $("#checkenter").is(':checked')) {
            send_message();
        }

    };
});


//This function show new messages without need reload the page.
function get_new_massages(){
    $.ajax({
        url : "newmessages/",
        type : "GET",

        success : function(json) {
            for (var i = 0; i < json.length; i++) {
                console.log(json[i][0])
                $('#newmessage').append("<p class='msg-receiver'>"+ json[i][0] +"</p>");
                $("#alertvisualized").html("");
                $("#information").html("");
                goToFinal();
            }
            read_messages();

        },

        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
            console.log('offline');

        }
    });

}

//This function read all messages received while the user are on page.
function read_messages(){
    $.ajax({
        url : "read/",
        type : "GET",

        success : function(json) {

        },
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
            console.log('offline');

        }
    });

}

//This function send the message what are in the field.
function send_message(){
    var campo = $("#field").val();
    if (campo !== ""){
        $.ajax({
            url : "send/",
            type : "POST",
            data : {
                id : campo,
                 },

            success : function(json) {
                if (json != false){
                    $('#newmessage').append("<div class='col-xs-12'><p class='msg-emitter pull-right' title="+ json[1] +">"+ json[0] +"</p></div>");
                    goToFinal();
                    $("#field").val('');
                    $("#alertvisualized").html("");
                    $("#information").html("");
                }
                else{
                    alert("Não foi possivel enviar mensagem")
                }
                

            },
            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
               alert("deu errado");

            }
        
        });
    }


}


//Function to go to the end the chat.
function goToFinal(){
    $(".nano").nanoScroller({ flash: true });
    $(".nano").nanoScroller({ scroll: 'bottom' });
}

//Function for when the user to search old messages.
$(".nano").bind("scrolltop", function(e){
    if (oldm == 0){
        $.ajax({
            url : "/allmessages/",
            type : "POST",
            data : { 
                id : b,
                 },
                 
            success : function(json) {
                $('#oldmessages').html("");
                for (var i = 0; i < json.length; i++) {                    
                    if (json[i][0] == 0) {
                        $('#oldmessages').append("<div class='col-xs-12'><p class='msg-emitter pull-right' data-toggle='tooltip' data-placement='left' title='"+ json[i][2] +"'>"+ json[i][1] +"</p></div>");
                    } else {
                        $('#oldmessages').append("<p class='msg-receiver' title='"+ json[i][2] +"'>"+ json[i][1] +"</p>");
                    }
                }
                oldm = 1;
                $('#oldmessages').append("<div id='newmessage'></div>");
                
            },
    
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }
});

//This function returns to user the moment what his message is vizualized
function verify_read() {
    console.log(b);
    $.ajax({

        url : "/verifyread/",
        type : "POST",
        data : { 
            id : b,
             },
             
        success : function(json) {
            if(json == true){
                $("#alertvisualized").html("<span class='glyphicon glyphicon-eye-open'></span> Visualized").addClass("pull-right txtvisualized");
            }else{
                $("#alertvisualized").html("");
            }
        },

        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
           

        }
    });
}

//This function delete all messages between participants.
function delete_chat(iduser) {
    console.log(iduser);
    $.ajax({
        url : "/deletechat/",
        type : "POST",
        data : { 
            id : iduser,
             },
             
        success : function(json) {
            if(json == true){
                parent.window.document.location.href = '';
            }else{
                alert("Erro ao excluir conversa!")
            }
        },

        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
           

        }
    });
}

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

$(".nano").nanoScroller({ scroll: 'bottom' });