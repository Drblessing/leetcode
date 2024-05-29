class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        Reverse the input string, removing pre/post/inbetween whitespace
        input: str
        output: str
        >>> reverseWords('a good      example!')
        >>> 'example! a good'
        '''
        
        # split the input string by whitespaces into list
        # join the reverse list with spaces
        return ' '.join(s.split()[::-1])