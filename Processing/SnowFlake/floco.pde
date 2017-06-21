int numDivMax = 4;

float[] roda(float px, float py, float qx, float qy, float theta){
  float p2x = px - qx;
  float p2y = py - qy;
  float p3x = p2x*cos(theta)+p2y*sin(theta);
  float p3y = p2y*cos(theta)-p2x*sin(theta);
  p3x += qx;
  p3y += qy;
  return new float[] {p3x, p3y};
}

void draw() {

  float ax = 0 + width/4;
  float ay = width/1.55;
  float bx = width - width/4;
  float by = height/1.55;

 float[] e = roda(ax,ay,bx,by,-PI/3);
 float ex = e[0];
 float ey = e[1];
 
 
 magica(ax,ay,bx,by,0, true);
 magica(bx,by,ex,ey,0, true);
 magica(ex,ey,ax,ay,0, true);
}

void setup() {
  size(1000, 1000);
}

void magica(float ax, float ay, float bx, float by, float n, boolean pos){
   
  if(n==numDivMax){
     line(ax,ay,bx,by);
    }
    else {
       float cx = (2*ax/3) + bx/3;
       float cy = (2*ay/3) + by/3;

       float dx = (ax/3) + (2*bx)/3;
       float dy = (ay/3) + (2*by)/3;
         
       float e[];
       
        if(pos==true){
           e = roda(cx,cy,dx,dy,PI/3);
        } else{
           e = roda(cx,cy,dx,dy,-PI/3);
        }
      float ex = e[0];
      float ey = e[1];
     
      magica(ax,ay,cx,cy,n+1, pos);
      magica(cx,cy,ex,ey,n+1, pos);
      magica(ex,ey,dx,dy,n+1, pos);
      magica(dx,dy,bx,by,n+1, pos);

    }
}
