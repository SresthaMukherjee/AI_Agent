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
});
