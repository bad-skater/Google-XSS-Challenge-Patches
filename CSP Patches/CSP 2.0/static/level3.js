// var x = document.getElementsByClassName("tab");
var y = document.getElementById('tab1');
var z = document.getElementById('tab2');
var q = document.getElementById('tab3');

function checkk(){
    chooseTab('1')
}

function checkx(){
    chooseTab('2')
}

function checky(){
    chooseTab('3')
}

y.addEventListener('click',checkk,false)
z.addEventListener('click',checkx,false)
q.addEventListener('click',checky,false)

// function check(){
//     console.log(x.activeElement)
// }
// [0].id
// numComments = x.length;
// for (var i = 0; i < numComments; i++) {
//     x[i].addEventListener('click', check, false);
//   }

// console.log(document.activeElement.id)

function chooseTab(num) {
    // Dynamically load the appropriate image.
    var html = "Image " + parseInt(num) + "<br>";
    html += "<img src='/static/logos/cloud" + num + ".jpg' />";
    $('#tabContent').html(html);

    window.location.hash = num;

    // Select the current tab
    var tabs = document.querySelectorAll('.tab');
    for (var i = 0; i < tabs.length; i++) {
      if (tabs[i].id == "tab" + parseInt(num)) {
        tabs[i].className = "tab active";
        } else {
        tabs[i].className = "tab";
      }
    }

    // Tell parent we've changed the tab
    top.postMessage(self.location.toString(), "*");
  }

window.onload = function() { 
    chooseTab(unescape(self.location.hash.substr(1)) || "1");
}

  // Extra code so that we can communicate with the parent page
window.addEventListener("message", function(event){
    if (event.source == parent) {
        chooseTab(unescape(self.location.hash.substr(1)));
    }
}, false);
