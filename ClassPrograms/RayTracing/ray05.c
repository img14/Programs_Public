#include <stdio.h>
#include <math.h>

#include <omp.h>

#define X 640
#define Y 480
#define S 5003
#define T 4

int rgb[Y][X][3];

typedef struct
{
   double x ;
   double y ;
   double z ;
} triple ;

triple e = { 0.50 , 0.50 , -1.00 } ; // the eye
triple g = { 0.00 , 1.25 , -0.50 } ; // the light

typedef struct
{
   double r;
   double g;
   double b;
}color;

typedef struct
{
   double r;
   triple c;
   color h;
}sphere;

typedef struct
{
   double t;
   int sph;
}storage;

double dotp( triple t , triple u )
{
   return t.x * u.x + t.y * u.y + t.z * u.z ;
}

void diff( triple* t , triple u , triple v ) 
{
   t->x = u.x - v.x ;
   t->y = u.y - v.y ;
   t->z = u.z - v.z ;
}
sphere s[S];
void init()
{
   s[0].c.x =      0.50 ;
   s[0].c.y = -20000.00 ;
   s[0].c.z =      0.50 ;
   s[0].r   =  20000.25 ;
   s[0].h.r =    205.0    ; 
   s[0].h.g =    133.0    ;
   s[0].h.b =     63.0    ;
   
   s[1].c.x =      1.00 ;
   s[1].c.y =      0.50 ;
   s[1].c.z =      1.00 ;
   s[1].r   =      0.25 ;
   s[1].h.r =      0.0    ;
   s[1].h.g =    255.0    ;
   s[1].h.b =      0.0   ;
   
   s[2].c.x =      0.00 ;
   s[2].c.y =      0.75 ;
   s[2].c.z =      1.25 ;
   s[2].r   =      0.50 ;
   s[2].h.r =    255.0    ; 
   s[2].h.g =      0.0    ;
   s[2].h.b =      0.0    ;
}

storage v[X][Y];

int main(void)
{
   int tid, nthreads, jj, total;
   int count[T];
   omp_set_num_threads(T);
  
   for(jj=0;jj<T;jj++)
   {
      count[jj]=0;
   }  
   int y , x ;

   FILE* fout ;
   for( y = 0 ; y < Y ; y++ )
   {
      for( x = 0 ; x < X ; x++)
      {
         rgb[y][x][0] = 0.0;
         rgb[y][x][1] = 0.0;
         rgb[y][x][2] = 0.0;
      }
   }
   init();
   //fscanf
   FILE* fIn;
   fIn = fopen("helix.txt","r");
   int co;
   for(co = 3; co<S; co++)
   {
      double xx;
      double yy;
      double zz;
      double rr;
      fscanf(fIn, "%lf %lf %lf %lf", &xx, &yy, &zz, &rr);
      s[co].c.x =      xx ;
      s[co].c.y =      yy ;
      s[co].c.z =      zz ;
      s[co].r   =      rr ;
      s[co].h.r =      0.0  ; 
      s[co].h.g =      0.0  ;
      s[co].h.b =    255.0  ;

   }
   int i;
   int j;
   int k;

   
   #pragma omp parallel for private(tid)
   for(j = 0; j<Y; j++)
   {
      #pragma omp parallel for private(tid)
      for(i = 0; i<X; i++)
      {
         double min = 99999999999;
          int minSphere = -1;
          double shade = .45;

         double x = ((double)i - ((double)(X) - (double)(Y))/2.0)/(double)Y;
         double y = (1 - (j/((double)Y)));

         double z = 0.0;
         triple r;
         r.x = x - e.x;
         r.y = y - e.y;
         r.z = z - e.z;
         double mag = sqrt(r.x*r.x + r.y*r.y +r.z*r.z);
         r.x = r.x/mag;
         r.y = r.y/mag;
         r.z = r.z/mag;
         #pragma omp parallel for private(tid)
         for(k = 0; k < S; k++)
         {
            double a = 1.0;
            double b = (2*r.x *(e.x - s[k].c.x) + 2*r.y *(e.y - s[k].c.y) + 2*r.z *(e.z - s[k].c.z));
            double c = (pow(e.x, 2) + pow(e.y, 2) + pow(e.z, 2) + pow(s[k].c.x, 2) + pow(s[k].c.y, 2) + pow(s[k].c.z, 2) - 2*(s[k].c.x*e.x + s[k].c.y*e.y + s[k].c.z*e.z) - pow(s[k].r, 2));
            
            double dis = (b*b - 4*a*c);
            
            if(dis < 0)
            {
               v[j][i].t = 99999999999;
               v[j][i].sph = -1;
            } 
            else
            {
               double f1 = (-1*b + sqrt(b*b - 4*a*c))/(2*a);
               double g1 = (-1*b - sqrt(b*b - 4*a*c))/(2*a);

               if(f1 > 0 && g1 > 0)
               {
                  if(f1 < g1)
                  {
                     if(f1 < min)
                     {
                        min = f1;
                        minSphere = k;
                     }
                  }
                  else
                  {
                     if(g1 < min)
                     {
                        min = g1;
                        minSphere = k;
                     }
                  }
               }
            }
         
         }
            v[j][i].t = min;
            v[j][i].sph = minSphere;
                   triple pos;
            pos.x = r.x*v[j][i].t + e.x;
            pos.y = r.y*v[j][i].t + e.y;
            pos.z = r.z*v[j][i].t + e.z;


            triple l;
            l.x = pos.x - g.x;
            l.y = pos.y - g.y;
            l.z = pos.z - g.z;
            mag = sqrt(l.x*l.x + l.y*l.y + l.z*l.z);
            l.x = l.x/mag;
            l.y = l.y/mag;
            l.z = l.z/mag;
         #pragma omp parallel for private(tid)
         for(k = 0; k < S; k++)
         {
            if(k != minSphere)
            {
     

            double a2 = 1.0;
            double b2 = (2*l.x *(pos.x - s[k].c.x) + 2*l.y *(pos.y - s[k].c.y) + 2*l.z *(pos.z - s[k].c.z));
            double c2 = (pow(pos.x, 2) + pow(pos.y, 2) + pow(pos.z, 2) + pow(s[k].c.x, 2) + pow(s[k].c.y, 2) + pow(s[k].c.z, 2) - 2*(s[k].c.x*pos.x + s[k].c.y*pos.y + s[k].c.z*pos.z) - pow(s[k].r, 2));
            
            double dis2 = (b2*b2 - 4*a2*c2);
            
            if(dis2 >= 0)
            {
               double t1 = (-1*b2 + sqrt(b2*b2 - 4*a2*c2))/(2*a2);
               double t2 = (-1*b2 - sqrt(b2*b2 - 4*a2*c2))/(2*a2);
               if(t1 <= 0 || t2 <= 0)
               {
                  shade = .4;
               }

            }

            
            
         }

         }
         triple n;
         n.x = (pos.x - s[minSphere].c.x)/(s[minSphere].r);
         n.y = (pos.y - s[minSphere].c.y)/(s[minSphere].r);
         n.z = (pos.z - s[minSphere].c.z)/(s[minSphere].r);

         if(shade == .45)
         {
            shade -= (.4 * dotp(l,n));
         }
         if(v[j][i].sph != -1)
         {
            rgb[j][i][0] = s[v[j][i].sph].h.r * shade;
            rgb[j][i][1] = s[v[j][i].sph].h.g * shade;
            rgb[j][i][2] = s[v[j][i].sph].h.b * shade;
         }
      }
   }

   fout = fopen( "spheres05.ppm" , "w" ) ;

   fprintf( fout , "P3\n" ) ;
   fprintf( fout , "%d %d\n" , X, Y ) ;
   fprintf( fout , "255\n" ) ;

   for( y = 0 ; y < Y ; y++ )
   {
      for( x = 0 ; x < X ; x++)
      {
         fprintf( fout , "%d %d %d " ,
          rgb[y][x][0] , rgb[y][x][1] , rgb[y][x][2] ) ;
      }
      fprintf(fout, "\n");
   }
   fclose( fout ) ;

   return 0 ;
}