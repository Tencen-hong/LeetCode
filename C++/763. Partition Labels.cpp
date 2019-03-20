class Solution {
public:
    vector<int> partitionLabels(string S) {
        vector<int> ans;
        int start_pos=0;
        int end_pos=0;
        map<char,int> mmap;//每个字符最后一次出现的位置
        for(int i=0;i<S.size();i++){
            mmap[S[i]]=i;
        }
        int i=0;
        while(start_pos<S.size()){
            end_pos = mmap[S[start_pos]];
            bool flag=true;
            for(i=start_pos;i<=end_pos;i++){//某段区间内的字符在后方再次出现，扩展区间
                if(mmap[S[i]]>end_pos){
                    end_pos =  mmap[S[i]];
                    start_pos = i;°
                    flag=false;
                    break;
                }
            }
            if(flag==true){
                start_pos = end_pos + 1;
                ans.push_back(end_pos+1);//字符都限在某段区间内，分割
            }
      
        }
        for(int i=ans.size()-1;i>=1;i--){
            ans[i] = ans[i]-ans[i-1];
        }
        return ans;
    }
};