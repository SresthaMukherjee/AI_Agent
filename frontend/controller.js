$(document).ready(function () {

    // Expose DisplayMessage function to Python
    eel.expose(DisplayMessage);
    function DisplayMessage(message) {
        $(".siri-message li:first").text(message);
        $(".siri-message").textillate("start"); // Animation trigger
    }

    // Expose ShowHood function to Python
    eel.expose(ShowHood);
    function ShowHood() {
        setTimeout(() => {
            $("#Oval").fadeIn();        // Smooth transition instead of .show()
            $("#SiriWave").fadeOut();   // Smooth transition instead of .hide()
        }, 500);
    }

    // Optional fallback using .attr for visibility control (commented version)
    /*
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }
    */
   eel.expose(senderText)
   function senderText(message){
    var chatbox = document.getElementById("chat-canvas-body");
    if(message.trim() !==""){
        chatbox.innerHTML += `<div class = "row justify-content-end mb-4">
        <div class = "width-size">${message}</div>
        </div>`;

        chatbox.scrollTop=chatbox.scrollHeight;
    }
   }

   eel.expose(receiverText)
   function receiverText(message){
    var chatbox = document.getElementById("chat-canvas-body");
    if(message.trim() !==""){
        chatbox.innerHTML += `<div class = "row justify-content-start mb-4">
        <div class = "width-size">
        <div class = "receiver_message">${message}</div>
        </div>`;

        chatbox.scrollTop=chatbox.scrollHeight;
    }
   }
});
