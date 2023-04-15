//C:\Users\Vicky\Desktop\Repository\Concepts-of-CPP
//pg. no: 159

#include <iostream>
#include <cstring>

#include <conio.h>
//https://stackoverflow.com/questions/41407242/declaring-the-getch-function

using namespace std;

class employee
{
	private:
		
		char name[20];
		int age;
		float sal;
		
	public:
		
		employee()
		{
			cout<<endl<<"reached zero-argument contructor";
			strcpy(name, " ");
//			https://stackoverflow.com/questions/2220795/error-strcpy-was-not-declared-in-this-scope

			age=0;
			sal=0.0;
		}
		
		employee(char const *n, int a, float s)
		{
			cout<<endl<<"reached three-argument constructor"<<endl;
			strcpy(name, n);
			age=a;
			sal=s;
		}
		
//		https://stackoverflow.com/questions/59670/how-to-get-rid-of-deprecated-conversion-from-string-constant-to-char-warnin?rq=1
		void setdata(char const *n, int a, float s)
		{
			strcpy(name, n);
			age=a;
			sal=s;
		}
		
		void showdata()
		{
			cout<<endl<<name<<"\t"<<age<<"\t"<<sal;
		}
		
		~employee()
		{
			cout<<endl<<"reached destructor";
		}
};

int main()
{
	employee *p;
	p=new employee;
	p->setdata("sanjay", 23, 4500.50);
	
	employee *q;
	q=new employee("ajay", 24, 3400.50);
	
	p->showdata();
	q->showdata();
	cout<<endl;

	delete p;
	delete q;
	getch();
	return 0; 
}
