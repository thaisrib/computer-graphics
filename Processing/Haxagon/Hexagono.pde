
void draw() {
  int n=6;
  float cx = width/2;
  float cy = height/2;
  float r = (width/2)* 0.9;
  float angulo = TWO_PI/n;
  beginShape();
  for(int i=0;i<n;i++){
    float t = i * angulo;
    float x = r * cos(t) + cx;
    float y = r * sin(t)+cy;
   vertex(x,y);
  }
  endShape(CLOSE);

}
