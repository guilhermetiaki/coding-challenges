#include <stdio.h>

int main(int argc, char const *argv[]){
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i){
		int n;
		scanf("%d", &n);

		int max_x = -1000, min_x = 1000, max_y = -1000, min_y = 1000;


		for (int j = 0; j < n; ++j){
			char type;
			scanf(" %c", &type);
			if (type == 'p'){
				int x, y;
				scanf("%d %d", &x, &y);
				if (x > max_x)
					max_x = x;
				if (x < min_x)
					min_x = x;
				if (y > max_y)
					max_y = y;
				if (y < min_y)
					min_y = y;
			}
			else if (type == 'c'){
				int x, y, r;
				scanf("%d %d %d", &x, &y, &r);
				if (x+r > max_x)
					max_x = x+r;
				if (x-r < min_x)
					min_x = x-r;
				if (y+r > max_y)
					max_y = y+r;
				if (y-r < min_y)
					min_y = y-r;

			}
			else{
				int x1, x2, y1, y2;
				scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
				if (x1 > max_x)
					max_x = x1;
				if (x1 < min_x)
					min_x = x1;
				if (y1 > max_y)
					max_y = y1;
				if (y1 < min_y)
					min_y = y1;
				if (x2 > max_x)
					max_x = x2;
				if (x2 < min_x)
					min_x = x2;
				if (y2 > max_y)
					max_y = y2;
				if (y2 < min_y)
					min_y = y2;
			}
		}
		printf("%d %d %d %d\n", min_x, min_y, max_x, max_y);
	}

	return 0;
}