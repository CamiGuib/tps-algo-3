#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
#include <climits>
 
using namespace std;


/*
Idea: 
- Resuelvo con programacion dinamica bottom-up usando una matriz de memoizacion dp[i][ultB][ultN], donde i es el indice del numero que estamos mirando, ultB el indice del ultimo numero pintado de blanco
y ultN el indice del ultimo numero pintado de negro. El valor almacenado en dp[i][ultB][ultN] representa el minimo numero de numeros que quedan sin pintar para el estado i habiendo pintado como ultimo
numero blanco a ultN y como ultimo numero negro a ultN. 
- Para cada numero i considero 4 posibilidades: se lo puede pintar de blanco o negro; se lo puede pintar solo de blanco; se lo puede pintar solo de negro; o no se lo puede pintar ni de blanco ni de negro
- En cada caso, se actualiza el valor de dp[i][ultB][ultN] tomando el mínimo entre las opciones disponibles.
- El caso base es i = N
- El resultado es el minimo valor de dp[0]
*/ 
  
 
int borw(int N, vector<int> v) {
    
    // Creo una matriz de (N+1)x(N+1)x(N+1)
    vector<vector<vector<int>>> dp(N+1, vector<vector<int>>(N+1, vector<int>(N+1, numeric_limits<int>::max())));
 
    // Completo la matriz i = N (caso base)
    for (int ultB = 0; ultB <= N; ultB++) {
        for (int ultN = 0; ultN <= N; ultN++) {
            dp[N][ultB][ultN] = 0;
        }
    }
 
    // Completo el resto de las matrices
    for (int i = N-1; i >= 0; i--) {
        for (int ultB = 0; ultB <= i; ultB++) {
            for (int ultN = 0; ultN <= i; ultN++) {
                // Si es viable pintar de blanco y de negro
                if ((ultB == 0 || v[i] < v[ultB-1]) && (ultN == 0 || v[i] > v[ultN-1])) {
                    dp[i][ultB][ultN] = min({dp[i+1][i+1][ultN], dp[i+1][ultB][i+1], dp[i+1][ultB][ultN] + 1});
                }
 
                // Si es viable pintar de blanco pero no de negro
                if ((ultB == 0 || v[i] < v[ultB-1]) && !(ultN == 0 || v[i] > v[ultN-1])) {
                    dp[i][ultB][ultN] = min(dp[i+1][i+1][ultN], dp[i+1][ultB][ultN] + 1);
                }
 
                // Si no es viable pintar de blanco pero si de negro
                if (!(ultB == 0 || v[i] < v[ultB-1]) && (ultN == 0 || v[i] > v[ultN-1])) {
                    dp[i][ultB][ultN] = min(dp[i+1][ultB][i+1], dp[i+1][ultB][ultN] + 1);
                }
 
                // Si no es viable pintar de blanco ni de negro
                if (!(ultB == 0 || v[i] < v[ultB-1]) && !(ultN == 0 || v[i] > v[ultN-1])) {
                    dp[i][ultB][ultN] = dp[i+1][ultB][ultN] + 1;
                }
            }
        }
    }
    
    // Busco y entrego el minimo valor de la matriz dp[0]
    int fil = dp[0].size();
    int col = dp[0][0].size();
    int min = INT_MAX;
    for (int i = 0; i < fil; i++) {
        for (int j = 0; j < col; j++) {
            if (dp[0][i][j] < min) {
                min = dp[0][i][j];
            }
        }
    }
    
    return min;
}
 
 
 
int main() {
    
    // Leo los inputs e imprimo los outputs
    while (true) {
        int N;
        cin >> N;
        if (N == -1) {
            break;
        }
        vector<int> v(N);
        for (int i = 0; i < N; i++) {
            cin >> v[i];
        }
        cout << borw(N, v) << endl;    
    }
 
    return 0;
}
 
 
 
