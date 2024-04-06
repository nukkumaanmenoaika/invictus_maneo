var modal = document.getElementById('myModal');
var btn = document.getElementById("myBTN");
var answ = document.getElementById("asnBTN");

btn.onclick = function(){
    modal.style.display = "block";
}

window.onclick = function(event){
    if (event.target == modal){
        modal.style.display = "none";
    }
}

var audio = document.getElementById('myAudio');
var playButton = document.getElementById('myBTN');

playButton.addEventListener('click', function() {
  if (audio.paused) {
    audio.play();
  } else {
    audio.pause();
  }
});

var label1 = document.getElementById('answer');
var label2 = document.getElementById('wrongAnswer1');
var label3 = document.getElementById('wrongAnswer2');

var score = document.getElementById('score')

var rightAnswer = label1.innerHTML;

let answersArr = [label1.innerHTML, label2.innerHTML, label3.innerHTML]

function shuffleArray(array) {
  for (var i = array.length - 1; i > 0; i--) {  
      var j = Math.floor(Math.random() * (i + 1));
                 
      var temp = array[i];
      array[i] = array[j];
      array[j] = temp;
  }
     
  return array;
}

answersArr = shuffleArray(answersArr)

label1.innerHTML = answersArr[0];
label2.innerHTML = answersArr[1];
label3.innerHTML = answersArr[2];

var input1 = document.getElementById('input1');
var input2 = document.getElementById('input2');
var input3 = document.getElementById('input3');

answ.onclick = function(){
  if(input1.checked){
    if(label1.innerHTML == rightAnswer){
      alert('Правильно')
      score.innerHTML = 10
    }
    else{
      alert('Неправильно')
      return
    }
  }

  if(input2.checked){
    if(label2.innerHTML == rightAnswer){
      alert('Правильно')
      score.innerHTML = 10
    }
    else{
      alert('Неправильно')
      return
    }
  }

  if(input3.checked){
    if(label3.innerHTML == rightAnswer){
      alert('Правильно')
      score.innerHTML = 10
    }
    else{
      alert('Неправильно')
      return
    }
  }

  modal.style.display = "block";
  modal.style.display = "none";
  window.location.reload();
}