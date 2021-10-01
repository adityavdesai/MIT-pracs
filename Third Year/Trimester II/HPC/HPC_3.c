#include <stdio.h>
#include <omp.h>

int main(){

	unsigned long long int size;	// size of array to be sorted
	unsigned long long int temp;	// for swapping purpose
	printf("Enter size : ");
	scanf("%llu", &size);

	unsigned long long int arr_parallel[size];
	unsigned long long int arr_serial[size];
	// generate the array
	#pragma omp for
	for(unsigned long long int i=0; i<size; i++){
		arr_parallel[i] = size-i;
		arr_serial[i] = size-i;
	}

	double start = omp_get_wtime();	// record start time

	// use bubble sort parallely
	for(unsigned long long int i=0; i<size; i++){

		#pragma omp for
		for(unsigned long long int j=0; j<size-1; j+=2){	// compare even positioned elements
			if(arr_parallel[j]>arr_parallel[j+1]){
				// swap
				temp = arr_parallel[j];
				arr_parallel[j] = arr_parallel[j+1];
				arr_parallel[j+1] = temp;
			}
		}

		#pragma omp for
        for(unsigned long long int j=1; j<size-1; j+=2){        // compare odd positioned elements
                if(arr_parallel[j]>arr_parallel[j+1]){
					// swap
					temp = arr_parallel[j];
					arr_parallel[j] = arr_parallel[j+1];
					arr_parallel[j+1] = temp;
                }
        }

	}
	
	double end = omp_get_wtime();

    // print execution time
    printf("\nTime for parallel execution = %f\n", (end - start));

	start = omp_get_wtime();	//record start time

	// use bubble sort serially
	for(unsigned long long int i=0; i<size; i++){
		for(unsigned long long int j=0; j<size-i-1; j++){
			if(arr_parallel[j]>arr_parallel[j+1]){
				// swap
				temp = arr_parallel[j];
				arr_parallel[j] = arr_parallel[j+1];
				arr_parallel[j+1] = temp;
			}
		}
	}
	
	end = omp_get_wtime();

    // print execution time
    printf("\nTime for serial execution = %f\n", (end - start));

}
