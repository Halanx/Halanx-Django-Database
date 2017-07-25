#include <bits/stdc++.h>
using namespace std;

vector<vector<int> >adj;
vector<bool> vis;
vector<int> color;
enum COLOR {WHITE, GREY, BLACK};
int n;

//-------------------------------------
void bfs_util(int u){
	queue<int> Q;
	Q.push(u);
	vis[u] = true;

	while(!Q.empty()){
		u = Q.front();
		cout<<u<<" ";
		Q.pop();
		for(auto &v:adj[u]){
			if(!vis[v]){
				vis[v] = true;
				Q.push(v);
			}
		}
	}
}


void bfs(){
	vis.resize(n,0);
	for(int u=0;u<n;u++){
		if(!vis[u]){
			bfs_util(u);
		}
	}

}

//-------------------------------------

void dfs_util(int u){
	cout<<u<<" ";
	for(auto &v:adj[u]){
		if(!vis[v]){
			vis[v] = true;
			dfs_util(v);
		}
	}
}


void dfs(){
	vis.resize(n,0);

	for(int u=0;u<n;u++){
		if(!vis[u]){
			cout<<endl;
			vis[u] = true;
			dfs_util(u);
		}
	}
}

//-------------------------------------


bool has_cycle_util(int u){
	color[u] = GREY;
	for(auto &v:adj[u]){

		if(color[v] == GREY)
			return true;

		if(color[v] == WHITE and has_cycle_util(v))
			return true;
	}
	color[u] = BLACK;
	return false;
}



bool has_cycle(){
	color.resize(n,WHITE);

	for(int u=0;u<n;u++){
		if(color[u] == WHITE){
			if(has_cycle_util(u))
				return true;
		}
	}

	return false;
}

//-------------------------------------

void topological_sort_util(int u, stack<int> &S){

	for(auto &v:adj[u]){
		if(!vis[v]){
			vis[v] = true;
			topological_sort_util(v,S);
		}
	}
	S.push(u);
}


void topological_sort(){
	stack<int> S;
	vis.resize(n,0);

	for(int u=0;u<n;u++){
		if(!vis[u]){
			vis[u] = true;
			topological_sort_util(u,S);
		}
	}

	while(!S.empty()){
		cout<<S.top()<<" ";
		S.pop();
	}
}

//-------------------------------------

int main(){
	n = 6;
	adj.resize(n);
	adj[5].push_back(2);
	adj[5].push_back(0);
	adj[4].push_back(0);
	adj[4].push_back(1);
	adj[2].push_back(3);
	adj[3].push_back(1);

	topological_sort();
}