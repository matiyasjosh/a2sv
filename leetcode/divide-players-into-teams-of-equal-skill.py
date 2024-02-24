class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill)-1
        c = 0
        f = skill[l]+skill[r]

        while l<r:
            if skill[l]+skill[r]!=f:
                return -1

            c+=skill[l]*skill[r]
            l+=1
            r-=1

        return c