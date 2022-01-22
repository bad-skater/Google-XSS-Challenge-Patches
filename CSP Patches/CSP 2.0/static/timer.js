// secondz= document.currentScript.getAttribute("one");
var secondz = document.getElementById('message').getAttribute('value');
console.log(secondz)
function startTimer(seconds) {
    seconds = parseInt(seconds) || 3;
    setTimeout(function() { 
      window.confirm("Time is up!");
      window.history.back();
    }, seconds * 1000);
  }

startTimer(secondz);