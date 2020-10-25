function logEvent(string) {    
    console.log(string);
}

window.SpeechRecognition = window.SpeechRecognition        ||
                           window.webkitSpeechRecognition  ||
                           null;

if (!SpeechRecognition) {
   document.querySelector('.js-api-support').removeAttribute('hidden');
   document.querySelector('.js-api-info').setAttribute('hidden', '');
   [].forEach.call(document.querySelectorAll('form button'), function(button) {
      button.setAttribute('disabled', '');
   });
} else {
   var recognizer = new SpeechRecognition();
   var transcipt = document.getElementById('question');


document.getElementById('question').addEventListener('focus', function() {
   recognizer.stop();
   transcipt = document.getElementById('question');
   
});

document.getElementById('option1').addEventListener('focus', function() {
   recognizer.stop();
   transcipt = document.getElementById('option1');
});

document.getElementById('option2').addEventListener('focus', function() {
   recognizer.stop();
   transcipt = document.getElementById('option2');
});

document.getElementById('option3').addEventListener('focus', function() {
   recognizer.stop();
   transcipt = document.getElementById('option3');
});
document.getElementById('option4').addEventListener('focus', function() {
   recognizer.stop();
   transcipt = document.getElementById('option4');
});




   // Start recognising
   recognizer.addEventListener('result', function(event) {
      transcipt.textContent = '';

      for (var i = event.resultIndex; i < event.results.length; i++) {
         if (event.results[i].isFinal) {
            transcipt.textContent = event.results[i][0].transcript;
         } else {
            transcipt.textContent += event.results[i][0].transcript;
         }
      }
   });

   // Listen for errors
   recognizer.addEventListener('error', function(event) {
      logEvent('Recognition error: ' + event.message);
   });

   recognizer.addEventListener('end', function() {
      logEvent('Recognition ended');
   });

   document.getElementById('button-play').addEventListener('click', function() {
      transcipt.textContent = ''
      recognizer.lang = 'en-US';
      recognizer.interimResults = true

      try {
         recognizer.start();
         logEvent('Recognition started');
      } catch(ex) {
         logEvent('Recognition error: ' + ex.message);
      }
   });

   document.getElementById('button-stop').addEventListener('click', function() {
      recognizer.stop();
      logEvent('Recognition stopped');
   });


}
