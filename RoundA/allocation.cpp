#include <bits/stdc++.h>
using namespace std;
#include <math.h>  
#include <string.h>
#include <map>
#include <vector>



void Solve(int B,int t,vector<int> ent){
sort(ent.begin(),ent.end());
int cont=0;
int N=ent.size();
while(true){
if(cont>N-1){
break;
}
if(B-ent[cont]>=0){
B=B-ent[cont];
cont++;
}else{
break;
}

}

cout<<"Case #"<<t<<": "<<cont<<endl;
}





int main(){
int T;
cin>>T;
for(int t=0;t<T;t++){
int N,B;
cin>>N>>B;
vector <int> ent;
for(int j=0;j<N;j++){
int aux;
cin>>aux;
ent.push_back(aux);
}

Solve(B,t+1,ent);


}



return 0;
}
