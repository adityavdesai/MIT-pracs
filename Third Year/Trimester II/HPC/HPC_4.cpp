#include<iostream>
#include<omp.h>
#include<vector>
using namespace std;
#define MAX 10

vector<int> populate() {
    vector<int> vec;
    for (int i=0 ; i<MAX ; i++) {
        vec.push_back(rand() % MAX);
    }
    return vec;
}

vector<int> serialAdd(vector<int> v1, vector<int> v2) {
    vector<int> sum;
    for (auto i=v1.begin(), j=v2.begin() ; i != v1.end() && j != v2.end() ; ++i, ++j)
        sum.push_back(*i + *j);
    return sum;     
}

/*
vector<int> parallelAdd(vector<int> v1, vector<int> v2) {
    vector<int> sum;
    #pragma omp parallel for
    for (auto i=v1.begin(), j=v2.begin() ; i != v1.end() && j != v2.end() ; ++i, ++j)
        sum.push_back(*i + *j);
    return sum;     
}
*/

int main() {
    vector<int> a, b;
    vector<int> serial_sum, parallel_sum;
    
    a = populate();
    b = populate();
    
    cout << "a:";
    for(auto i : a)
        cout << i << " ";
        
    cout << "\nb:";
    for(auto i : b)
        cout << i << " ";
    
    cout << "\nsum:";
    serial_sum = serialAdd(a, b);
    for(auto i : serial_sum)
        cout << i << " ";
        
    cout << "\nsum:";
    parallel_sum = parallelAdd(a, b);
    for(auto i : parallel_sum)
        cout << i << " ";
         
    return 0;
}
