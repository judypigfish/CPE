#include <iostream>
using namespace std;

int main(){
  while(1){
    int s;
    cin >> s;
    if (s==0)
      break;
    int now=0,m=1;
    while(now <= s){
      m++;
      now = m+m*(m-1)/2;
    }
    cout << now-s << " " << m << "\n";
  }
}
