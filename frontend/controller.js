$(document).ready(function(){
    //Display Speak Message
    ele.expose(DisplayMessage);
    function DisplayMessage(message){
    $(".siri-message li:first").text(message);
    $(".siri-message").textillate("start");
    }
});