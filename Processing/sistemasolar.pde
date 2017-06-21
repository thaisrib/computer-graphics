float x,y,dx,dy;
int i = 0;

void setup(){ //CONFIGURAÇÃO DO PROGRAMA. RODA UMA VEZ NO INICIO
  size(500,500);
  frameRate(30);
}
void draw(){
background(0); //pintar fundo de branco
ellipseMode(CENTER);  // Set ellipseMode to CENTER
noStroke();

float xc = width/2;
float yc = height/2;
float xx = width/20;
float yy = height/20;
float xx1 = width/8;
float yy1 = height/8;
float xx2 = width/4;
float yy2 = height/4;
float r = width/3;
float r2 =width/8;

//sol
fill(#FEFF00);  // Set fill to gray
ellipse(xc,yc,xx2,yy2);  // (posição x, posição y, largura, altura)

//terra
float angTerra = TWO_PI/700; //500 FRAMES A CADA VOLTA
float theta = angTerra*i;
float x = r*cos(theta) + xc; //rotação em x a partir do sol
float y = r*sin(theta) + yc; //rotação em y a partir do sol (centro)
fill(#2500FF);  // Set fill to blue
ellipse(x, y , xx1, yy1); 

//lua
float angLua = TWO_PI/80; //80 FRAMES A CADA VOLTA (divide o circulo em 80 "fatias". Quando maior o número de frames, mais devagar irá se movimentar
float theta2 = angLua*i;
float x1 = r2*cos(theta2) + x; //rotação em x a partir da Terra
float y1 = r2*sin(theta2) + y; //rotação em y a partir da Terra
fill(255);  // Set fill to white
ellipse(x1, y1 , xx, yy); 
i++;
}