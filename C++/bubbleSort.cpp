#include <vector>
using namespace std;

vector<int> bubbleSort(vector<int> array) {
  int n = array.size();
  for(int i = 0; i < n; i++){
    for (int j = i; j < n; j++){
      if(array[i] > array[j]){
        swap(array[i], array[j]);
      }
    }
  }
  return array;
}
