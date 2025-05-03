/*from start we will find shortest paths to every forbidden node and also to the end
and will do the same considering start as end and end as start.then minimum will be
min of distance*/

#include <bits/stdc++.h>
using namespace std;
#define INF 1000000009
#define cin in

int main()
{
    int t = 1;
    ifstream in("in6.txt");
    ofstream out("out6.txt");

    while (t--)
    {
        int n, e, unavail, start, end;
        cin >> n >> e >> unavail >> start >> end;
        vector<pair<int, int>> adj[n + 1];

        if(t==2)
        {

        }

        for (int i = 0; i < e; i++)
        {
            int node1, node2, w;
            cin >> node1 >> node2 >> w;
            //cout<<node1<<" "<<node2<<" "<<w<<endl; 

            adj[node1].push_back({node2, w});
            adj[node2].push_back({node1, w});
        }

        vector<int> forbidden(n + 1);
        vector<int> distance(n + 1, INF);

        for (int i = 0; i < unavail; i++)
        {
            int x;
            cin >> x;
            forbidden[x] = 1;
        }

        priority_queue<pair<int, int>> pq;

        pq.push({0, start});
        distance[start]=0;

        vector<bool> processed(n + 1);

        while (!pq.empty())
        {
            int a = pq.top().second;
            pq.pop();

            if (processed[a])
                continue;
                
            processed[a] = true;

            if (forbidden[a] == 1)
                continue;

            for (auto u : adj[a])
            {
                int b = u.first;
                int w = u.second;
                if (distance[a] + w < distance[b])
                {
                    distance[b] = distance[a] + w;
                    pq.push({-distance[b], b});
                }
            }
        }

        priority_queue<pair<int, int>> pq2;
        pq2.push({0, end});

        vector<bool> processed2(n + 1);
        vector<int> distance2(n + 1, INF);

        distance2[end]=0;

        while (!pq2.empty())
        {
            int a = pq2.top().second;
            pq2.pop();

            if (processed2[a])
                continue;
            processed2[a] = true;

            if (forbidden[a] == 1)
                continue;

            for (auto u : adj[a])
            {
                int b = u.first;
                int w = u.second;
                if (distance2[a] + w < distance2[b])
                {
                    distance2[b] = distance2[a] + w;
                    pq2.push({-distance2[b], b});
                }
            }
        }

        int mn = distance[end];

        for (int i = 1; i < n + 1; i++)
        {
            mn = min(mn, distance[i] + distance2[i]);
        }

        if (mn >= INF)
           {

            cout << -1<<endl;
            out << -1<<endl;
           }

        else
            {cout << mn << endl;
            out << mn << endl;
            }

        
    }
}