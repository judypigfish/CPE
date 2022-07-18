#include <stdio.h>

int main(){
	while(1){
		int s;
		scanf("%d",&s);
		if (s==0)
			break;
		
		int now=0,m=1;
		while(now <= s){
			m++;
			now = m+m*(m-1)/2;
		}
		printf("%d %d\n",now-s,m);
	}
}
