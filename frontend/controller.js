$(document).ready(function () {
    eel.expose(DisplayMessage);
    function DisplayMessage(message) {
      $(".siri-message li:first").text(message);
      $(".siri-message").textillate("start");
    }
    eel.expose(ShowHood)
    function ShowHood() {
        setTimeout(() => {
            $("#Oval").show();
            $("#SiriWave").hide();
        }, 500);
    }   
    // function ShowHood() {
    //     $("#Oval").attr("hidden", false);
    //     $("#SiriWave").attr("hidden", true);
    //   }
}); 