#include<iostream>
#include<vector>

int main(){
    int N=0;
    std::cin >> N;
    std::vector<int> C(N, 0), P(N, 0), sum1(N, 0), sum2(N, 0);
    
    for(int i=0; i<N; i++){
        std::cin >> C[i] >> P[i];
    }

    //累積和
    for(int i=0; i<N; i++){
        if(i==0){
            sum1[i] = (C[i]==1 ? P[i]:0);
            sum2[i] = (C[i]==2 ? P[i]:0);
            //std::cout << sum1[i] << ",";
        }else{
            sum1[i] = sum1[i-1] + (C[i]==1 ? P[i]:0);
            sum2[i] = sum2[i-1] + (C[i]==2 ? P[i]:0);
            //std::cout << sum1[i] << ",,";
        }
    }

    int Q=0, A=0, B=0;
    std::cin >> Q;
    std::vector<int> L(Q, 0), R(Q, 0);

    for(int i=0; i<Q; i++){
        std::cin >> L[i] >> R[i];
    }

    for(int i=0; i<Q; i++){
        if(L[i]-2<0){
            A=sum1[R[i]-1];
            B=sum2[R[i]-1];
        }else{
            A=sum1[R[i]-1]-sum1[L[i]-2];
            B=sum2[R[i]-1]-sum2[L[i]-2];
        }
        std::cout << A << " " << B << "\n";
    }

    return 0;

}