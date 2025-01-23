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
       }while(v[i]<=v[l] && i<=h);
       do
       {
         j--;
       }while(v[j]>v[l] && j>=0);
       if(i<j)
         swap(v[i],v[j]);
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
    vector<int> v={8,4,5,2,1};
    quicksort(v,0,v.size()-1);
    for(auto i:v)
       cout<<i<<' ';
    return 0;
}