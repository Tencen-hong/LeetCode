class Solution {
public:

    string simplifyName(string name) {
        string simplifyname;
        int at_pos = name.find("@");
        for (int i = 0; i < at_pos; i++) {
            if (name[i] == '.')
                continue;
            if (name[i] == '+')
                break;
            simplifyname += name[i];
        }
        simplifyname += name.substr(at_pos, name.size());
        return simplifyname;

    }
    int numUniqueEmails(vector<string>& emails) {
        set<string> differentAddress;
        for (int i = 0; i < emails.size(); i++) {
            string simplifyname = simplifyName(emails[i]);
            differentAddress.insert(simplifyname);
        }
        return differentAddress.size();
    }
};