/*

▒█░▒█ ░█▀▀█ ▒█▀▀█ ▒█▀▀█ ▒█░░▒█ 　 ▒█░▒█ ▒█▀▀▀█ ▒█░░░ ▀█▀ ▒█▀▀▄ ░█▀▀█ ▒█░░▒█ ▒█▀▀▀█ 
▒█▀▀█ ▒█▄▄█ ▒█▄▄█ ▒█▄▄█ ▒█▄▄▄█ 　 ▒█▀▀█ ▒█░░▒█ ▒█░░░ ▒█░ ▒█░▒█ ▒█▄▄█ ▒█▄▄▄█ ░▀▀▀▄▄ 
▒█░▒█ ▒█░▒█ ▒█░░░ ▒█░░░ ░░▒█░░ 　 ▒█░▒█ ▒█▄▄▄█ ▒█▄▄█ ▄█▄ ▒█▄▄▀ ▒█░▒█ ░░▒█░░ ▒█▄▄▄█ 

~ Made By Makan Dehizadeh
- ICS Class of 2016 - 2017 (SEM 1)

*/

// Music
import ddf.minim.*;
import ddf.minim.analysis.*;
import ddf.minim.effects.*;
import ddf.minim.signals.*;
import ddf.minim.spi.*;
import ddf.minim.ugens.*;
AudioPlayer player;
Minim minim;

// Main debugging and configs
float tick = 0;
boolean merryChristmas = true;
String textToWrite;

// Stars
float[] starX = new float[50];
float[] starY = new float[50];
boolean[] starColor = new boolean[50];

// Snow
int quantity = 100;
float [] xPosition = new float[quantity];
float [] yPosition = new float[quantity];
int [] flakeSize = new int[quantity];
int [] direction = new int[quantity];
int minFlakeSize = 1;
int maxFlakeSize = 5;

// Snowman
PImage img_hat;
PImage img_hair;
float hat_pos = 0;
boolean hat_up = true;

// Person
float eye_move_lr = random(443, 447);
float eye_move_ud = random(263, 267);
int count = 0;

// Moon
float inc_move = 0;
boolean g_right = true;

// Tree
float[] orn_color = new float[7];

// Myself
void setup() {
  // Start console post message
  println("Makan's Christmas Scene - Dev Version");
  println("-------------------------------------");
  
  // Main intro text
  size(800, 500); // size
  background(#000000);
  textSize(25);
  text("Made by", 320, 240);
  textSize(50);
  text("Makan Dehizadeh", 175, 300);
  
  // Stars positions
  for (int i = 0; i < 25; i++) {
    starX[i] = random(0, 800);
    starY[i] = random(0, 500);
  }
  
  // Snowman images
  img_hat = loadImage("hat.png");
  img_hair = loadImage("hair.png");
  
  // Snow
  frameRate(30);
  noStroke();
  smooth();
  for(int i = 0; i < quantity; i++) {
    flakeSize[i] = round(random(minFlakeSize, maxFlakeSize));
    xPosition[i] = random(0, width);
    yPosition[i] = random(0, height);
    direction[i] = round(random(0, 1));
  }
  
  colorMode(HSB); // set hsb color for fade
  
  for (int i = 0; i < 7; i++)
    orn_color[i] = random(0, 255); // Loops 7 ornaments.
  
  minim = new Minim(this);
  player = minim.loadFile("song.mp3", 2048);
  player.play();
}

// Myself
void draw() {
  background(#000958);
  tick++;
  
  // draw all functions
  stars();
  moon();
  snow();
  snow_man();
  house();
  tree();
  right_mount();
  left_mount();
  draw_text();
  
  // Check if mouse pressed for text change
  if (mousePressed) {
    println("[DEBUG] Mouse Pressed."); // show print text on console
    if (merryChristmas) // check for true/false
      merryChristmas = false;
    else
      merryChristmas = true;
  }
  
  if (tick == 1)
    println("[PROGRAM] Final drawing complete..");
}

// Myself
void tree() {
  // Door
  fill(#582701);
  rect(710, 325, 20, 50);
  
  // Roof
  fill(#029000);
  triangle(670, 340, 770, 340, 720, 270);
  triangle(680, 310, 760, 310, 720, 250);
  triangle(690, 280, 750, 280, 720, 230);
  
  // Star
  fill(#FFEA00);
  pushMatrix();
  translate(720, 230);
  rotate(frameCount / -100.0);
  star_on_tree_(0, 0, 7.5*0.667, 17.5*0.667, 5); 
  popMatrix();
  
  for (int i = 0; i < 7; i++) { // for statement loop 7.
    if (orn_color[i] >= 255) orn_color[i] = 0; else orn_color[i]++;
    fill(orn_color[i], 255, 255);
    
    if (i == 0)
      ellipse(740, 330, 10, 10);
    else if (i == 1)
      ellipse(695, 330, 10, 10);
    else if (i == 2)
      ellipse(700, 300, 10, 10);
    else if (i == 3)
      ellipse(740, 300, 10, 10);
    else if (i == 4)
      ellipse(720, 320, 10, 10);
    else if (i == 5)
      ellipse(720, 290, 10, 10);
    else
      ellipse(715, 260, 10, 10);
  }
}

// Myself
void draw_text() {
  // Changes text based on mouseclick
  if (merryChristmas) 
    textToWrite = "Merry Christmas";
  else
    textToWrite = "Happy New Year";
   
  // Bottom text
  fill(#000000);
  textFont(createFont("font.ttf", 82));
  text(textToWrite, 330, 450);
  
  // FPS counter
  textFont(createFont("font2.ttf", 20));
  text(round(frameRate) + " FPS", 735, 500);
}

// Myself
void house() {
  // Body and roof
  fill(#6C5000);
  rect(400, 210, 225, 150);
  triangle(400, 210, 625, 210, 512.5, 100);
  
  // door
  fill(#461C00);
  rect(525, 260, 60, 100);
  rect(425, 240, 60, 60);
  
  // person
  fill(#DE9462);
  rect(448, 270, 15, 30); // neck
  ellipse(455, 270, 40, 40); // head
  
  fill(#FFFFFF);
  ellipse(445, 265, 8, 8); //eyes
  ellipse(462, 265, 8, 8);
  
  fill(#000000);
  ellipse(443 + (mouseX / 200), 264 + (mouseY / 200), 4, 4); // pupils
  ellipse(460 + (mouseX / 200), 264 + (mouseY / 200), 4, 4);
  
  fill(#BC0000);
  arc(455, 275, 20, 20, 0, PI, CHORD);
  image(img_hair, 427, 240, width/14, height/14);
}

// Myself
void left_mount() {
  // main drawing functions
  fill(#B7B7B7);
  stroke(#000000);
  strokeWeight(2);
  
  // main triangle
  triangle(-100, 500, 200, 500, 50, 200);
  
  // top triangle
  strokeWeight(0);
  fill(#FFFFFF);
  triangle(0, 300, 100, 300, 50, 200);
}

// Myself
void right_mount() {
  // setting colors and stroke
  fill(#FFFFFF);
  stroke(#000000);
  strokeWeight(2);
  
  ellipse(500, 500, 1000, 300); // main drawing
}
 
// Myself
void stars() {
  strokeWeight(0); // weight of the stroke
  
  for (int i = 0; i < 50; i++) { // 50 stars
    if (tick % 25 == 0) {
      if (starColor[i]) // change star color
        starColor[i] = false;
      else
        starColor[i] = true;
    }
    
    // Star color.
    if (starColor[i])
      fill(#FCF000);
    else
      fill(#C1B202);
    
    // Draw star.
    float a = random(4, 6);
    ellipse(starX[i], starY[i], a, a);
  }
}

// Myself
void moon() {
  fill(#A0A0A0);
  ellipse(10 + inc_move, 10, 200, 200);
  
  if (g_right) {
    inc_move++;
    if (inc_move >= 800)
      g_right = false;
  } else {
    if (inc_move <= 0)
      g_right = true;
    inc_move--;
  }
  
  fill(#747474); // movement of the moon and rings.
  ellipse(10 + inc_move, 10, 20, 20);
  ellipse(75 + inc_move, 25, 20, 20);
  ellipse(50 + inc_move, 60, 20, 20);
  ellipse(-40 + inc_move, 60, 20, 20);
  ellipse(-35 + inc_move, 20, 20, 20);
  ellipse(5 + inc_move, 70, 20, 20);
}

// Myself
void snow_man() {
  fill(#FFFFFF);
  strokeWeight(0);
  
  // Main snowballs.
  ellipse(300, 340, 75, 75);
  ellipse(300, 290, 60, 60);
  ellipse(300, 250, 50, 50);
  
  // Eyes
  fill(#000000);
  ellipse(312, 245, 7, 7);
  ellipse(288, 245, 7, 7);
  
  // Buttons
  ellipse(300, 285, 7, 7);
  ellipse(300, 300, 7, 7);
  ellipse(300, 330, 7, 7);
  ellipse(300, 350, 7, 7);
  
  // Scarf
  fill(#FF0000);
  rect(268, 264, 60, 15);
  
  // Move hat based on current value.
  if (hat_up) {
    hat_pos++;
    if (hat_pos > 20)
      hat_up = false;
  } else {
    hat_pos--;
    if (hat_pos == 0)
      hat_up = true;
  }
  
  // Hand
  strokeWeight(5);
  line(330, 280, 360, 240);
  line(360, 240, 330, 230 - hat_pos);
  strokeWeight(0);
  
  // Nose and hat.
  fill(#FCA500);
  triangle(298, 260, 298, 250, 320, 255);
  image(img_hat, 266, 201 - hat_pos, width/12, height/12);
}

// http://solemone.de/demos/snow-effect-processing/
void snow() {
  strokeWeight(0);
  fill(#FFFFFF);
  for(int i = 0; i < xPosition.length; i++) {
    ellipse(xPosition[i], yPosition[i], flakeSize[i], flakeSize[i]);
    if(direction[i] == 0)
      xPosition[i] += map(flakeSize[i], minFlakeSize, maxFlakeSize, .1, .5);
    else
      xPosition[i] -= map(flakeSize[i], minFlakeSize, maxFlakeSize, .1, .5);
    yPosition[i] += flakeSize[i] + direction[i]; 
    if(xPosition[i] > width + flakeSize[i] || xPosition[i] < -flakeSize[i] || yPosition[i] > height + flakeSize[i]) {
      xPosition[i] = random(0, width);
      yPosition[i] = -flakeSize[i];
    }
  }
}

// https://processing.org/examples/star.html
void star_on_tree_(float x, float y, float radius1, float radius2, int npoints) {
  float angle = TWO_PI / npoints;
  float halfAngle = angle/2.0;
  beginShape();
  for (float a = 0; a < TWO_PI; a += angle) {
    float sx = x + cos(a) * radius2;
    float sy = y + sin(a) * radius2;
    vertex(sx, sy);
    sx = x + cos(a+halfAngle) * radius1;
    sy = y + sin(a+halfAngle) * radius1;
    vertex(sx, sy);
  }
  endShape(CLOSE);
}