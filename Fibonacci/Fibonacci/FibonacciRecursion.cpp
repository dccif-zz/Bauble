#include<iostream>
#include<time.h>
using namespace std;

//int Fibonacci(int n) {
//	if (n == 1 || n == 2) {
//		return 1;
//	}
//	else
//	{
//		return Fibonacci(n - 2) + Fibonacci(n - 1);
//	}
//}

//int fiboTail(int n, int a, int b)
//{
//	if (n == 1) return a;
//	if (n == 2) return b;
//	return fiboTail(n - 1, b, a + b);
//}


enum { gnFib = 99 };
int gFib[gnFib];

int fib(int n)    // Take an n value
{
	if (n < 0 || n >= gnFib) return 0;
	int &fn = gFib[n];
	if (!fn) {
		if (n == 0 || n == 1) fn = 1;
		else fn = fib(n - 1) + fib(n - 2);
	}
	return fn;
}

int main() {
	int n;
	int res;
	double timeuse;
	clock_t tStart = clock();
	while (true)
	{
		cin >> n;
		//res = Fibonacci(n);
		res = fib(n);
		timeuse = (double)(clock() - tStart);
		cout << res << " time: " << timeuse << endl;
	}
}