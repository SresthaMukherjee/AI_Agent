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

    // Function to add sender message
    eel.expose(senderText);
    function senderText(message) {
        var chatbox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatbox.innerHTML += `
                <div class="row justify-content-end mb-4">
                    <div class="width-size">${message}</div>
                </div>`;
            chatbox.scrollTop = chatbox.scrollHeight;
        }
    }

    // Function to add receiver message
    eel.expose(receiverText);
    function receiverText(message) {
        var chatbox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatbox.innerHTML += `
                <div class="row justify-content-start mb-4">
                    <div class="width-size">
                        <div class="receiver_message">${message}</div>
                    </div>
                </div>`;
            chatbox.scrollTop = chatbox.scrollHeight;
        }
    }

    // Hide loader and show FaceAuth
    eel.expose(hideLoader);
    function hideLoader() {
        $("#Loader").fadeOut();
        $("#FaceAuth").fadeIn();
    }

    // Hide Face auth and display Face Auth success animation
    eel.expose(hideFaceAuth);
    function hideFaceAuth() {
        $("#FaceAuth").fadeOut();
        $("#FaceAuthSuccess").fadeIn();
    }

    // Hide Face Auth success and display HelloGreet
    eel.expose(hideFaceAuthSuccess);
    function hideFaceAuthSuccess() {
        $("#FaceAuthSuccess").fadeOut();
        $("#HelloGreet").fadeIn();
    }

    // Hide Start Page and display blob
    eel.expose(hideStart);
    function hideStart() {
        $("#Start").fadeOut();

        setTimeout(function () {
            $("#Oval").addClass("animate__animated animate__zoomIn");
        }, 1000);

        setTimeout(function () {
            $("#Oval").fadeIn();
        }, 1000);
    }
});
