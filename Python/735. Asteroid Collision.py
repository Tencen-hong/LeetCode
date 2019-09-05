class Solution:
    '''
    由于小于0的小行星往左移动，大于0的小行星往右移动，所以只有在左边的小行星往右移动，而右边的小行星往左移动的情况下，两者才可能发生相撞而爆炸。因此，我们定义一个堆栈，当且仅当栈顶元素大于0，并且当前元素小于0的时候，两者就会相撞，所以我们计算相撞后哪个小行星爆炸了：如果是栈顶的爆炸了，那么需要出栈，并且循环检查当前小行星还会不会和新的栈顶元素相撞；如果是当前小行星爆炸了，则不用做什么；如果是两个小行星同时爆炸了，则需要出栈，并且跳出循环检测。
    '''

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids:
            return []

        st = []
        for i in range(len(asteroids)):
            value = asteroids[i]
            while st and st[-1] > 0 and value < 0:
                sign = st[-1] + value
                if sign == 0:
                    value = 0
                elif sign > 0:
                    value = st[-1]
                st.pop()

            if value != 0:
                st.append(value)

        return st
