#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>
#define N 10000

//Transformation function
float Exp(float x)
{
	return(-0.5*log(0.5*x));
}

int main(void)
{	
	int i;
	float x1[N],y[N],x2[N],x[N];
	
	srand(time(0));
	
	//generating random number between 0 and 1
	for (i=0; i<N; i++)
	{
		x1[i] = rand();
	}
	srand(1245);
	for (i=0; i<N; i++)
	{
		x2[i] = rand();
	}
	for (i = 0; i < N; i++)
	{
		if(x1[i] > x2[i])
		{
			x[i] = x2[i]/x1[i];
		}
		else if(x1[i] == 0 && x2[i] == 0)
		{
			x[i] = 1;
		}
		else
		{
			x[i] = x1[i]/x2[i];
		}
		y[i] = Exp(x[i]);
	}
	
	char fname[50];
	sprintf(fname,"q_4_data.txt");
	FILE *fp=fopen(fname,"w");
	
	for (i = 0; i<N ; i++)
	{
	fprintf(fp,"%f %f \n", x[i],y[i]);
	}
	fclose(fp);
}
