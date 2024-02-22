class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[""]

        for p in path.split('/'):
            if p not in["",".",".."]:
                stack.append(p)
            elif len(stack)>1 and p == "..":
                stack.pop()

        p = '/'.join(stack)

        return p if len(stack)>1 else '/'