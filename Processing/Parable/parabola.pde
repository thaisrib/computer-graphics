float   x, xf, y, T, Ax, Ay, Bx, By, f;
float a = 1;
float b = 0;
float c = -1;

float dx = 0.01;

void setup(){
 x = -3;
 xf = 3;
 size(500,500);
 background(255);
}


float bask(float x){
   float h = a*pow(x,2) + b*x + c;
   return h;
}

void draw(){
line(width/2, height,width/2, 0);
line(width, height/2,0, height/2);
  
beginShape();
while(x<xf){
y = bask(x);
float xx = transX(x);
float yy = transY(y);
  vertex(xx,yy);
  x+=dx;
} 

endShape();

}

void function(){
float delta = pow(b,2) - 4*a*c;  

 if(delta > 0){
 float x1 = (-b + sqrt(delta))/2*a;
 float x2 = (-b - sqrt(delta))/2*a;
 }
 float xxc = -b/2*a;

}


float transX(float x){
 float xt = width/2 + (width*x)/6;
 return xt;

}

float transY(float y){
   float yt = height/2 - (height*y)/6; 
   return yt;
}
