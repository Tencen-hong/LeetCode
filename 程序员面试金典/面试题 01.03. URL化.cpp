
class Solution {
public:
    string replaceSpaces(string S, int length) {
        string new_S;
        for(int i = 0;i<length;i++){
            if(S[i]==' '){
                new_S += "%20";
            }else{
                new_S += S[i];
            }
        }
        return new_S;
    }
};