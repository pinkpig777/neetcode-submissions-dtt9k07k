class Solution:

    def encode(self, strs: List[str]) -> str:
        # hello world
        encoded = ""
        for s in strs:
            length = str(len(s))
            encoded += length + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        l = 0
        r = 0
        res = []
        while r < len(s):
            while s[r] != "#":
                r += 1
            # r -> #
            length = int(s[l:r]) # 0, 1
            l = r + 1 # 2
            r = l + length # 7
            string = s[l:r]
            res.append(string)
            l = r
        return res