#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

double f(double x)
{
	return (x*exp(x));
}

double f2(double x)
{
	return sin(x);
}

void fpRichardson(double h, int n){
	double ** D = new double * [n];
	for(int i=0;i<n;i++) D[i] = new double[n];

	//Line per line
	for(int i=0;i<n;i++){ //line
		cout<<h<<"  ";
		for(int j=0;j<=i;j++){ //column
			if(j==0) D[i][j]=(f(2.0+h)-f(2.0-h))/(2.0*h);
			if(j!=0) D[i][j]=(pow(4.0,j)*D[i][j-1]-D[i-1][j-1])/(pow(4.0,j)-1.0);
			cout<<setprecision(12)<<D[i][j]<<"  ";
		}
		h=h/2.0;
		cout<<endl;
	}
	cout<<"Exact= "<<setprecision(12)<<exp(2.0)+2.0*exp(2.0)<<endl;
}

void fppRichardson(double h, int n){
	double ** D = new double * [n];
	for(int i=0;i<n;i++) D[i] = new double[n];

	//Line per line
	for(int i=0;i<n;i++){ //line
		cout<<h<<"  ";
		for(int j=0;j<=i;j++){ //column
			if(j==0) D[i][j]=(f(2.0+h)-2.0*f(2.0)+f(2.0-h))/(h*h);
			if(j!=0) D[i][j]=(pow(4.0,j)*D[i][j-1]-D[i-1][j-1])/(pow(4.0,j)-1.0);
			cout<<setprecision(12)<<D[i][j]<<"  ";
		}
		h=h/2.0;
		cout<<endl;
	}
	cout<<"Exact= "<<setprecision(12)<<4.0*exp(2.0)<<endl;
}

double CalT(int m){
	double h,I,x;
	double PI=3.14159265358979323846;
	int N=2;
	N=pow(2,m);
	h=PI/(1.0*N);
	x=0.0;
	I=0.0;
	for(int i=0;i<=N;i++){
		if((i==0)||(i==N)){
			I=I+f2(x)/2.0;
		}
		else {
			I=I+f2(x);
		}
		x=x+h;
	}
	I=I*h;
	return I;
}

void Romberg(int mMax){
	double ** T = new double * [mMax+1];
	for(int i=0;i<=mMax;i++) T[i] = new double[mMax+1];

	//Line per line
	for(int m=2;m<=mMax;m++){ //line
		cout<<m<<"  ";
		for(int k=0;k<=m-2;k++){  //column
			if(k==0) T[m][k]=CalT(m);
			if(k!=0) T[m][k]=(pow(4.0,1.0*k)*T[m][k-1]-T[m-1][k-1])/(pow(4.0,1.0*k)-1.0);
			cout<<setprecision(13)<<T[m][k]<<"  ";
		}
		cout<<endl;
	}
}

int main(int argc, char** argv) {
	double h;
	int choice,n,mMax;

	do{
		cout<<"Menu: (1)f'(x) with Richardson ; (2)f''(x) with Richardson"<<endl;
		cout<<"Menu: (3)Romberg integration ; (4)Exit"<<endl;
		cin>>choice;
		switch(choice){
			case 1:
				cout<<"Enter h initial:"<<endl;
				cin>>h;
				cout<<"Enter number of step:"<<endl;
				cin>>n;
				fpRichardson(h,n);
				break;
			case 2:
				cout<<"Enter h initial:"<<endl;
				cin>>h;
				cout<<"Enter number of step:"<<endl;
				cin>>n;
				fppRichardson(h,n);
				break;
			case 3:
				cout<<"Enter mMax: "<<endl;
				cin>>mMax;
				Romberg(mMax);
				break;
			case 4:
				cout<<"Exit"<<endl;
				break;
			default:
				cout<<"Wrong choice"<<endl;
				break;
		}
	}while(choice!=4);

	return 0;
}