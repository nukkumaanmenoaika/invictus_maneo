
var modal = document.getElementById('myModal');
var btn = document.getElementById("myBTN");
var answ = document.getElementById("asnBTN");

btn.onclick = function(){
    modal.style.display = "block";
}

answ.onclick = function(){
    modal.style.display = "block";
    modal.style.display = "none";
    window.location.reload();
}

window.onclick = function(event){
    if (event.target == modal){
        modal.style.display = "none";
    }
}

const audio = document.getElementById('myAudio');
const playButton = document.getElementById('myBTN');

playButton.addEventListener('click', function() {
  if (audio.paused) {
    audio.play();
  } else {
    audio.pause();
  }
});
