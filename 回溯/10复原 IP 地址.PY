# class Solution:
#     def restoreIpAddresses(self, s: str) -> List[str]:
#         result = []
#         self.trace(s,[],result,0)
#         fina_res = []
#         for res in result:
#             str = ''
#             for index in len(res):
#                 if index == 0:
#                     str = str + res[index]
#                 else:
#                     str = str+'.'+res[index]
#             fina_res.append(str)
#         return fina_res

#     def trace(self,s,path:List,result,startIndex):
#         if len(path)==4 and startIndex == len(s):
#             result.append(path[:])
#             return
#         for i in range(startIndex,len(s)):
#             str = s[startIndex:i+1]
#             if int(str)>=0 and int(str)<=255:
#                 path.append(str)
#                 self.trace(s,path,result,i+1)
#                 path.pop()
#             else:
#                 break


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.trace(s, [], 0, result)
        return list(map(lambda x: ".".join(x), result))
        # return [".".join(map(str, parts)) for parts in result]

    def trace(self, s, path, startIndex, result):

        if len(path) > 4:
            return
        if len(path) == 4 and startIndex >= len(s):
            result.append(path[:])
        for i in range(startIndex, len(s)):

            curS = s[startIndex : i + 1]
            if len(curS) > 1 and curS.startswith("0"):
                break
            if int(curS) >= 0 and int(curS) <= 255:
                path.append(curS)
                self.trace(s, path, i + 1, result)
                path.pop()
