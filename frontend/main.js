$(document).ready(function () {

    eel.init()()
    $(".text").textillate({
      loop: true,
      speed: 1500,
      sync: true,
      in: {
        effect: "bounceIn",
      },
      out: {
        effect: "bounceOut",
      },
    });
    $(document).ready(function () {
    // Ensure eel is defined before calling
    if (typeof eel !== "undefined" && eel.init) {
        eel.init();
    }

    $(".text").textillate({
        loop: true,
        minDisplayTime: 2000,
        initialDelay: 500,
        in: {
            effect: "bounceIn",
            delayScale: 1.5,
            delay: 50,
        },
        out: {
            effect: "bounceOut",
            delayScale: 1.5,
            delay: 50,
        },
    });
});

  
    $(".siri-message").textillate({
      loop: true,
      sync: true,
      in: {
        effect: "fadeInUp",
        sync: true,
      },
      out: {
        effect: "fadeOutUp",
        sync: true,
      },
    });
  
    // var siriWave = new SiriWave({
    //   container: document.getElementById("siri-container"),
    //   width: 940,
    //   style: "ios9",
    //   amplitude: "1",
    //   speed: "0.30",
    //   height: 200,
    //   autostart: true,
    //   waveColor: "#ff0000",
    //   waveOffset: 0,
    //   rippleEffect: true,
    //   rippleColor: "#ffffff",
    // });
   
    var siriWave = new SiriWave({
      container: document.getElementById("siri-container"),
      width: 940,
      height: 200,
      style: "ios9",
      amplitude: 1,  // Removed quotes
      speed: 0.30,    // Removed quotes
      autostart: true,
      waveColor: "#ff0000"
  });
    $("#MicBtn").click(function () {
      eel.play_assistant_sound();
      $("#Oval").attr("hidden", true);
      $("#SiriWave").attr("hidden", false);
  
      eel.takeAllCommands()();
    });
  
    function doc_keyUp(e) {
      // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time
  
      if (e.key === "j" && e.metaKey) {
        eel.play_assistant_sound();
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.takeAllCommands()();
      }
    }
    document.addEventListener("keyup", doc_keyUp, false);
  
    function PlayAssistant(message) {
      if (message != "") {
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.takeAllCommands(message);
        $("#chatbox").val("");
        $("#MicBtn").attr("hidden", false);
        $("#SendBtn").attr("hidden", true);
      } else {
        console.log("Empty message, nothing sent."); // Log if the message is empty
      }
    }
  
    function ShowHideButton(message) {
      if (message.length == 0) {
        $("#MicBtn").attr("hidden", false);
        $("#SendBtn").attr("hidden", true);
      } else {
        $("#MicBtn").attr("hidden", true);
        $("#SendBtn").attr("hidden", false);
      }
    }
  
    $("#chatbox").keyup(function () {
      let message = $("#chatbox").val();
      console.log("Current chatbox input: ", message); // Log input value for debugging
      ShowHideButton(message);
    });
  
    $("#SendBtn").click(function () {
      let message = $("#chatbox").val();
      PlayAssistant(message);
    });
  
    $("#chatbox").keypress(function (e) {
      key = e.which;
      if (key == 13) {
        let message = $("#chatbox").val();
        PlayAssistant(message);
      }
    });
  });
