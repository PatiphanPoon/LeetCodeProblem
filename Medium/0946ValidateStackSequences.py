class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st2 = []
        pus_id, pop_id = 0, 0
        while pus_id < len(pushed):
            if pushed[pus_id] != popped[pop_id]:
                st2.append(pushed[pus_id])
            else:
                pop_id += 1
                while st2 and st2[-1] == popped[pop_id]:
                    pop_id += 1
                    st2.pop()
            pus_id += 1
        return not st2
