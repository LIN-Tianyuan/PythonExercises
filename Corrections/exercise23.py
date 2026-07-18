"""
Leetcode 70: Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45

Français:
Vous montez un escalier. Il faut n marches pour atteindre le sommet.

À chaque fois, vous pouvez monter soit 1, soit 2 marches.
De combien de façons différentes pouvez-vous monter jusqu'au sommet ?

中文：
你正在爬楼梯。需要走 n 级台阶才能到达顶端。
每次你可以选择走 1 级或 2 级台阶。你有多少种不同的方式可以爬到顶端？
"""
def climb_stairs(self, n: int) -> int:
    """
    题目意思:
    你要爬到第 n 阶楼梯。
    每次只能爬：1 阶 2 阶 问一共有多少种不同的爬法。

    例如 n = 3：
    1 + 1 + 1
    1 + 2
    2 + 1

    所以答案是 3。

    先找规律

    假设现在要到达第 n 阶。

    最后一步只有两种可能：

    从第 n - 1 阶爬 1 阶上来
    从第 n - 2 阶爬 2 阶上来

    因此：

    爬到第 n 阶的方法数
    = 爬到第 n-1 阶的方法数
    + 爬到第 n-2 阶的方法数

    也就是：

    dp[n] = dp[n - 1] + dp[n - 2]

    初始情况：

    dp[1] = 1
    dp[2] = 2

    会发现它和斐波那契数列非常像：

    n = 1 → 1
    n = 2 → 2
    n = 3 → 3
    n = 4 → 5
    n = 5 → 8
    :param self:
    :param n:
    :return:
    """
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]