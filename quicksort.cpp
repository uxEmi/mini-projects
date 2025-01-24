#include <iostream>
#include <vector>
using namespace std;

int partition(vector<int>& v, int l, int h) {
    int pivot = v[l];
    int i = l;
    int j = h;

    while (i < j) {
        while (v[i] <= pivot) {
            i++;
        }
        while (v[j] > pivot) {
            j--;
        }
        if (i < j) {
            swap(v[i], v[j]);
        }
    }
    swap(v[l], v[j]);
    return j;
}

void quickSort(vector<int>& v, int l, int h) {
    if (l < h) {
        int pivotIndex = partition(v, l, h);
        quickSort(v, l, pivotIndex);
        quickSort(v, pivotIndex + 1, h);
    }
}

int main() {
    vector<int> v = {8, 4, 5, 2, 1};

    cout << "Original array: ";
    for (int num : v) {
        cout << num << " ";
    }
    cout << endl;

    quickSort(v, 0, v.size() - 1);

    cout << "Sorted array: ";
    for (int num : v) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
