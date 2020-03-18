class Solution
{
  public:
    // Encodes a URL to a shortened URL.
    string encode(string longUrl)
    {
        for (int i = 0; i < longUrl.size(); i++)
        {
            longUrl[i] = longUrl[i] - 'a';
        }
        return longUrl;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl)
    {
        for (int i = 0; i < shortUrl.size(); i++)
        {
            shortUrl[i] = shortUrl[i] + 'a';
        }
        return shortUrl;
    }
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));