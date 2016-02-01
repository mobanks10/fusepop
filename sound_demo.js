
var notes = [60, 64, 67, 72];
var i = 0;

function setup() {
  osc = new p5.Oscillator('Triangle');
  osc.start();
  frameRate(1);
}

function draw() {
  var freq = midiToFreq(notes[i]);
  osc.freq(freq);
  i++;
  if (i >= notes.length){
    i = 0;
  }
}