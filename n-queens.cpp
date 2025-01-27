#include <iostream>
using namespace std;
int x[10],n;
void afis()
{
    int c=1;
    for(int i=1;i<=n;i++){
      for(int j=1;j<=n;j++)
         if(x[c]==j)
           cout<<'*'<<' ';
         else
           cout<<'-'<<' ';
     c++;
     cout<<endl;
    }
            
}
bool ok(int k)
{
    for(int i=1;i<k;i++)
       if(x[i]==x[k])
         return false;
    for(int i=1;i<k;i++)
       if(abs(x[i]-x[k])==abs(i-k))
         return false;
    return true;
}
bool solutie(int k)
{
    return k==n;
}
void back(int k)
{
    for(int i=1;i<=n;i++)
    {
        x[k]=i;
        if(ok(k))
        {
            if(solutie(k))
            {  
                afis();
                exit(0);   
            }
            else
              back(k+1);
        }
    }
}
int main()
{
    cin>>n;
    back(1);
    return 0;
}