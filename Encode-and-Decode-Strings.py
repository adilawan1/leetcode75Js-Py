class Solution:
    
    def encode(self, strs: List[str]) -> str:
        string=''
        for s in strs:
            string+=str(len(s))+'#'+s
        return string
    #   '5#Hello5#world'
    def decode(self, s: str) -> List[str]:
        i=0
        array=[]
        while i < len(s):
            j=i
            length=''
            print(f'index {i}')
            while s[j] != '#':
                length+=s[j]
                j+=1
            int_len=int(length) # 5
            skip_len=len(length)+1
            array.append(s[i+skip_len:j+int_len+1])
            i+=int_len+skip_len
        return array
