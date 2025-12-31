#include <bits/stdc++.h>
#define lli long long
#define plli pair<lli,lli>
using namespace std;



vector<plli> merge(vector<plli> &left,vector<plli> &right)
{
    vector<plli> res;


    //lli ind=left.size()+right.size();

    lli lind=0;
    lli rind=0;
    while(lind<left.size() && rind<right.size())
    {
        if(left[lind].second==right[rind].second)
        {
            if(left[lind].first<right[rind].first)
            {
                res.push_back(left[lind]);
                lind++;
            }

            else
            {

                res.push_back(right[rind]);
                rind++;
            }
        }

        else if(left[lind].second<right[rind].second)
        {
            res.push_back(left[lind]);
            lind++;
        }

        

        else
        {
            res.push_back(right[rind]);
            rind++;

        }

    }
    while(lind<left.size())
    {
        
        res.push_back(left[lind]);
        lind++;
        

    }
    while(rind<right.size())
    {
       
        res.push_back(right[rind]);
        rind++;
        

    }

    return res;


}


vector<plli> mergeSort(vector<pair<lli,lli>> &p,lli first,lli last)
{
    if(first==last)
    {
        
         vector<plli> res;
         res.push_back(p[first]);

         return res;

    }

    lli mid=(first+last)/2;

    vector<plli> left;
    left=mergeSort(p,first,mid);

    vector<plli> right;
    right=mergeSort(p,mid+1,last);

    vector<plli> res;
    res=merge(left,right);

    return res;
   

}



int main()
{
    lli n;
    cin>>n;

    vector<pair<lli,lli>> timestamp;

    for(lli j=0;j<n;j++)
    {
        lli x,y;

        cin>>x>>y;

        timestamp.push_back({x,y});

    }
    //sort(timestamp.begin(),timestamp.end(),comp);

    timestamp=mergeSort(timestamp,0,n-1);


    lli last=0;
    vector<pair<int,int>> ans;

    for(lli j=0;j<n;j++)
    {
        if(timestamp[j].first>=last)
        {
            last=timestamp[j].second;
            ans.push_back(timestamp[j]);
        }
    }

    cout<<ans.size()<<"\n";

    for(lli j=0;j<ans.size();j++)
    {
        cout<<ans[j].first<<" "<<ans[j].second<<"\n";
    }
}