#include <iostream>
#include <vector>
using namespace std;
int partition(vector<int>& v,int l,int h)
{
   int i=l,j=h;
   while(i<j)
   {
       do
       {
        i++;
       }while(v[i]<=v[l]);
       do
       {
         j--;
       }while(v[j]>v[l]);
       if(i<j)
         swap(v[j],v[i]);
   }
   swap(v[l],v[j]);
   return j;
}
void quicksort(vector<int>& v,int l,int h)
{
    if(l<h)
    {
        int j=partition(v,l,h);
        quicksort(v,l,j);
        quicksort(v,j+1,h);
    }
}
int main()
{
    vector<int> v={1,4,2,3,9,8,7};
    quicksort(v,0,v.size()-1);
    for(auto i:v)
       cout<<i<<' ';
    return 0;
}