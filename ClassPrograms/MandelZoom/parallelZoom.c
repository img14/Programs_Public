#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <GL/glut.h>
#include "mpi.h"

#define N     600

int t[N][N];

double scale = 4.0;
double cX = 0.0;
double cY = 0.0;
double max = 500.0;

int        rank   ;
int        size   ;
MPI_Status status ;
int        tag = 0;

int test(double a, double b, int mz)
{
   double e = 0.0;
   double c = 0.0;
   double d = 0.0;
   int it = 0;
   while(it < mz)
   {
      if(c*c + d*d > 4.0)
      {
         break;
      }
      e = c*c - d*d + a;
      d = 2*c*d + b;
      c = e; 
      it++;
   }
   if(it < mz)
   {
      return 1;
   }
   return 0;
}
void displayfunc()
{

   glClear(GL_COLOR_BUFFER_BIT);
   glColor3f(0.0, 0.0, 0.0);
   glBegin(GL_POINTS);
   int g,h; 
   for(g = 0; g<N; g++)
   {
      for(h = 0; h<N; h++)
      {
         if(t[g][h] == 0)
         {
            glVertex2f(g,h);
         }      
      }
   }
   glEnd();
   glutSwapBuffers();
}
void reshapefunc(int wscr,int hscr)
{
   glViewport(0,0,(GLsizei)N,(GLsizei)N);
   glMatrixMode(GL_PROJECTION);
   glLoadIdentity();
   gluOrtho2D(0.0,1.0*N,0.0,1.0*N);
   glMatrixMode(GL_MODELVIEW);
}
void testBoard()
{
   int        j  ;
   int row = 0;
   double results1[N+5];
   if(rank == 0)
   {      
      results1[1] = scale;
      results1[2] = cX;
      results1[3] = cY;
      results1[4] = max;
   
      for( j = 1 ; j < size ; j++ )
      {
         results1[0] = (double)row;
         MPI_Send(results1 , N+5 , MPI_DOUBLE , j , tag , MPI_COMM_WORLD ) ;
         row++;
      }
      while(row < N) 
      {
         MPI_Recv(results1, N+5 , MPI_DOUBLE , MPI_ANY_SOURCE , tag , MPI_COMM_WORLD , &status ) ;
         int w;
         for(w = 0; w<N; w++)
         {
            t[(int)(results1[0])][w] = results1[w+5]; 
         }
         results1[0] = (double)row;
         results1[1] = scale;
         results1[2] = cX;
         results1[3] = cY;
         results1[4] = max;
         j = status.MPI_SOURCE ;
         MPI_Send(results1 , N+5 , MPI_DOUBLE , j , tag , MPI_COMM_WORLD ) ;
         row++;
      }
      int h;
      int w;
      for(h = 0; h<(size-1); h++)
      {
         MPI_Recv(results1, N+5, MPI_DOUBLE, MPI_ANY_SOURCE, tag, MPI_COMM_WORLD, &status);
         for(w = 0; w<N; w++)
         {
            t[(int)(results1[0])][w] = results1[w+5]; 
         }
      }
   }
}

void mousefunc(int button,int state,int xscr,int yscr)
{
   double sFactor = 4.0;
   if(button==GLUT_LEFT_BUTTON)
   {
      if(state==GLUT_DOWN)
      {
         cX += (xscr - (N/2.))/N * scale; 
         cY += ((N/2.) - yscr)/N * scale;
         scale = scale/sFactor;
         max*=1.6;
         testBoard();
         glutPostRedisplay();
      }
   }
}
int main(int argc,char* argv[])
{  
   MPI_Init(      &argc          , &argv ) ;
   MPI_Comm_size( MPI_COMM_WORLD , &size ) ; 
   MPI_Comm_rank( MPI_COMM_WORLD , &rank ) ; 
   
   int        k , j  ;
   int row = 0;
   double results[N+5];
   
   if(rank == 0)
   {
      glutInit(&argc,argv);
      glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
      glutInitWindowSize(N,N);
      glutInitWindowPosition(100,50);
      glutCreateWindow("");
      glClearColor(1.0,1.0,1.0,0.0);
      testBoard();
      glutDisplayFunc(displayfunc);
      glutMouseFunc(mousefunc);
      glutReshapeFunc(reshapefunc);
      glutMainLoop();
   }
   else
   {
      double cx;
      double cy;
      double sc;
      double m;
      while(1)
      {
         MPI_Recv(results , N+5 , MPI_DOUBLE , 0 , tag , MPI_COMM_WORLD , &status ) ;
         row = results[0];
         sc = results[1];
         cx = results[2];
         cy = results[3];
         m = results[4];
         int q = 0;
         double c;
         double d = cx + (row - (N/2.))/N * sc;
         for(c = cy - sc/2.0; c < cy + sc/2.0; c += (sc/N))
         {
            results[q+4] = test(d, c, m);
            q++;
         }
         MPI_Send(results , N+5 , MPI_DOUBLE , 0 , tag , MPI_COMM_WORLD ) ;
      }
   }
   MPI_Finalize();
   return 0;
}