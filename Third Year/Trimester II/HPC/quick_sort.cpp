#include <iostream>
#include <cstdlib>
#include <omp.h>

using namespace std;

//Partition function.
long int partition(long int arr[], long int low, long int high) {
	long int pivot = arr[high];	//Select the last element in the list as the pivot
	long int i = low - 1;
	long int temp;
	for (long int j = low; j < high; j++) {
		if (arr[j] < pivot) {
			i++;
			temp = arr[j];
			arr[j] = arr[i];
			arr[i] = temp;
		}
	}
	
	//Place the pivot at the proper position
	temp = arr[i+1];
	arr[i+1] = arr[high];
	arr[high] = temp;

	return i+1;
}

//Parallel quick sort
long int quicksort_parallel(long int arr[], long int low, long int high) {
	if (low < high) {
		long int mid = partition(arr, low, high);	//Partition the array into two subarrays using the partition function
		
		#pragma omp parallel sections 	//OpenMP directive
		{
			#pragma omp section 	//OpenMP directive
			{
				quicksort_parallel(arr, low, mid-1);	//Perform quicksort on the first subarray
			}
			#pragma omp section	//OpenMP directive
			{
				quicksort_parallel(arr, mid+1, high);	//Perform quicksort on the second subarray
			}
		}
	}
}

//Serial quick sort
long int quicksort_serial(long int arr[], long int low, long int high) {
	if (low < high) {
		long int mid = partition(arr, low, high);	//Partition the array into two subarrays using the partition function
		quicksort_serial(arr, low, mid-1);	//Perform quicksort on the first subarray
		quicksort_serial(arr, mid+1, high);	//Perform quicksort on the second subarray
	}
}

int main() {
	long int temp;
	long int n;
	
	cout << "Enter number of elements: ";
	cin >> n;
	long int arr[n];
	
	cout << "\nPopulating the array.\n";
	
	int choice_1;
	cout << "\nIs repetition allowed? (1/0): ";
	cin >> choice_1;
	
	int choice_2;
	cout << "\n1. Serial execution\n2. Parallel execution\nEnter choice: ";
	cin >> choice_2;
	long int t;
	
	int flag = 0;
	
	if(choice_1 == 1) {
		for(long int i = 0; i < n; i++) {
			arr[i] = (rand() % 1000000);	//Array is populated with random numbers in the range 0-999,999
		}
	}
	else {
		for(long int i = 0; i < n; i++) {
		        flag = 0;
			t = (rand() % 1000000);
			for (long int j = 0; j < i; j++) {	//This 'for' loop checks whether the current element has been included earlier, in order to avoid repetition 
				if (arr[j] == t) {
					flag = 1;
				}
			}
			if (flag == 0) {
        			arr[i] = t;
        		}
        		else {
        		        i--;
        		}
		}
	}
	
	double starttime = omp_get_wtime();	//Register the starting time for quick sort
	if (choice_2 == 1)
		quicksort_serial(arr, 0, n-1);		//Perform serial quick sort
	else if (choice_2 == 2)
		quicksort_parallel(arr, 0, n-1);	//Perform parallel quick sort	
	else
		cout << "Invalid choice.";
	double endtime = omp_get_wtime();	//Register the completion time for quick sort
	
	cout << "\nTime: " << (endtime - starttime);	//Calculate the running time for quick sort (difference between the completion time and starting time) and display it.
	
	return 0;
}
