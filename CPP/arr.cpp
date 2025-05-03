#include<iostream>
#include<bits/stdc++.h>
using namespace std;
template<class T>
class ArrayList
{
    T * p;
    int max_size,cur_pos,length;
    ofstream outf;


public:
    ArrayList(int x)
    {
        p=new T(x);
        max_size=x;
        length=0;
        cur_pos=2;
        outf.open("list_output.txt",std::fstream::out);

    }
    ArrayList()
    {
        p=new T;
        max_size=1;
    }

    int size()
    {
        return length;
    }
    void push(T item)
    {
        if(length==max_size)
        {
            max_size*=2;
            T* temp=new T(max_size);
            temp=p;
            delete [] p;
            p=new T(max_size);
            p=temp;
            delete [] temp;
        }
        for(int i=length-1; i>=cur_pos; i--)
        {
            p[i+1]=p[i];
        }
        length++;
        p[cur_pos]=item;
    }

    void pushBack(int item)
    {

        if(length==max_size)
        {
            max_size*=2;
            T* temp=new T(max_size);
            temp=p;
            delete[] p;
            p=new T(max_size);
            p=temp;
        }
        p[length++]=item;
    }
    T erase()
    {
        T temp=p[cur_pos];
        if(length*2==max_size)
        {
            max_size=max_size/2;
            T* temp=new T(max_size);
            temp=p;
            delete[] p;
            p=new T(max_size);
            p=temp;
        }
        for(T i=cur_pos; i<length-1; i++)
        {
            p[i]=p[i+1];
        }
        length--;
        return temp;

    }
    void setToBegin()
    {
        cur_pos=0;
    }
    void setToEnd()
    {
        cur_pos=length--;
    }
    void prev()
    {
        if(cur_pos!=0)
            cur_pos--;
    }
    void next()
    {
        if(cur_pos!=length-1)
            cur_pos++;
    }
    int currPos()
    {
        return cur_pos;

    }
    void setToPos(int pos)
    {
        cur_pos=pos;
    }
    T getValue()
    {
        return p[cur_pos];
    }
    int find(T item)
    {
        for(int i=0; i<length; i++)
        {
            if(p[i]==item)
            {
                outf<<p[i]<<"\n";
                return i;
            }
        }
        return -1;
    }
    int clear()
    {

        delete[] p;
        length=0;
        cur_pos=0;
    }
    void printf()
    {
        outf<<"<";
        for(int i=0; i<length; i++)
        {
            if(i==cur_pos)
                outf<<"| ";
            outf<<p[i]<<" ";
        }
        outf<<">\n";
    }
    void printff(int z=-1)
    {
        outf<<z<<"\n";
    }
    void printfT(T x)
    {
        outf<<x<<"\n";
    }
    void closef()
    {
        outf.close();
    }
    ~ArrayList(){
    delete [] p;
    }

};

