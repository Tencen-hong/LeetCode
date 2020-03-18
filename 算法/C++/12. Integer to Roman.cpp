class Solution {
public:
    string intToRoman(int num) {
        int digit = 0;// index to roman map
        string res = "";// to return
        string table[] = {"I", "V", "X", "L", "C", "D", "M"};// roman map
        while(num>0){
            if (num%10 > 0 ){
                if(num%10<4){// if digit_number is 1,2 or 3  , e.p III
                    for(int i=0;i<num%10;i++)
                        res = table[digit] + res;
                 }else if(num%10==4){ // digit_number = 4 need 2 characters ,e.p. IV
                    res = table[digit] + table[digit+1] + res;
                }else if(num%10<9){// digit_number < 9  , e.p. VII
                    for(int i=0;i<(num%10-5);i++)
                        res = table[digit] + res;
                    res = table[digit+1] + res;
                }else if(num%10==9){// digit_number=9 , e.p. IX
                    res = table[digit] + table[digit+2] + res;
                }
            }
            num /= 10;// num << 1 digit
            digit += 2;// idnex need + 2 index
        }
        
        return res;
    }
};