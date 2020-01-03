import re
#系统匹配库



# header 
# Helle Fancy Lee!
# Tips "以下题目均来源于LeetCode"
# LeetCode "简单算法题百斩"


# 1
# 小A 和 小B 在玩猜数字。小B 每次从 1, 2, 3 中随机选择一个，小A 每次也从 1, 2, 3 中选择一个猜。他们一共进行三次这个游戏，请返回 小A 猜对了几次？
# 输入的guess数组为 小A 每次的猜测，answer数组为 小B 每次的选择。guess和answer的长度都等于3。
def game(guess, answer) -> int:
	count = 0
	for v in range(3):
		if guess[v] == answer[v]:
			count = count + 1
	return count
# tips:
# 数组切片基础




# 2
# 给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
# J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。
def numJewelsInStones(J,S) -> int:
	count = 0
	lenStr = len(J)
	for x in range(lenStr):
		count_x = S.count(J[x])
		count += count_x
	return count 
# tips:
# python提供的count真是便捷




# 3
# 给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。
# 所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。
def defangIPaddr(address) -> str:
	return '[.]'.join(address.split('.'))
# tips:
# python数组字符串转化运用




# 4
# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
# 现有一个链表 -- head = [4,5,1,9]，它可以表示为:
# 4->5->1->9

def deleteNode(node):
	pass
# todo



# 5 
# 平面上有 n 个点，点的位置用整数坐标表示 points[i] = [xi, yi]。请你计算访问所有这些点需要的最小时间（以秒为单位）。
# 你可以按照下面的规则在平面上移动：
# 每一秒沿水平或者竖直方向移动一个单位长度，或者跨过对角线（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。
# 必须按照数组中出现的顺序来访问这些点。
def minTimeToVisitAllPoints(points) -> int:
	count = 0
	len_list = len(points)
	for x in range(len_list):
		if x + 1 >= len_list:
			pass
		else:
			x_len = abs(points[x + 1][0] - points[x][0])
			y_len = abs(points[x + 1][1] - points[x][1])
			if x_len > y_len:
				count += x_len
			else:
				count += y_len
	return count
# tips
# 这边可以用numpy库直接处理,切比雪夫向量算法
# 我的话直接实现切比雪夫向量,计算每步最少距离,X轴的差和Y轴的都差最大值就是两点之间最短距离




# 6
# 在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。
# 给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。
# 返回可以通过分割得到的平衡字符串的最大数量。
def balancedStringSplit(s) -> int:
	str_len = len(s)
	count = 0
	res = 0
	for x in range(str_len):
		if s[x] == "L":
			res+=1
		else:
			res-=1
		if res == 0:
			count+=1
	return count
# tips
# 最直观的办法就是用滑动窗口，上面解法我是看了网上的办法，思路十分新奇




# 7
# 给你一个字符串 S，
# 请你删去其中的所有元音字母（ 'a'，'e'，'i'，'o'，'u'）
# 并返回这个新字符串。
def removeVowels(S) -> str:
	List = ['a','e','i','o','u']
	for x in List:
		S = S.replace(x,'')
	return S	
# tips
# 简单的字符串操作




# 8
# 我们定制了一款特殊的力扣键盘，所有的键都排列在一行上。
# 我们可以按从左到右的顺序，用一个长度为 26 的字符串 keyboard （索引从 0 开始，到 25 结束）来表示该键盘的键位布局。
# 现在需要测试这个键盘是否能够有效工作，那么我们就需要个机械手来测试这个键盘。
# 最初的时候，机械手位于左边起第一个键（也就是索引为 0 的键）的上方。当机械手移动到某一字符所在的键位时，就会在终端上输出该字符。
# 机械手从索引 i 移动到索引 j 所需要的时间是 |i - j|。
# 当前测试需要你使用机械手输出指定的单词 word，请你编写一个函数来计算机械手输出该单词所需的时间。
def calculateTime(keyboard,word) -> int:
	word_site = []
	for x in word:
		word_site.append(keyboard.find(x))
	word_len = len(word_site)
	length = word_site[0]
	for v in range(word_len - 1):
		length += abs(word_site[v] - word_site[v+1])
	return length
# tips
# 先找出每个键的索引位置，然后两个位置差绝对值相加外加起始位置




# 9
# 给定两个列表 Aand B，并且 B 是 A 的变位（即 B 是由 A 中的元素随机排列后组成的新列表）。
# 我们希望找出一个从 A 到 B 的索引映射 P 。一个映射 P[i] = j 指的是列表 A 中的第 i 个元素出现于列表 B 中的第 j 个元素上。
# 列表 A 和 B 可能出现重复元素。如果有多于一种答案，输出任意一种。
def anagramMappings(A, B):
	ret_list = []
	for v in A:
		ret_list.append(B.index(v))
	return ret_list
# tips
# 简单列表索引应用




# 10
# 给定一个嵌套的整数列表，请返回该列表按深度加权后所有整数的总和。
# 每个元素要么是整数，要么是列表。同时，列表中元素同样也可以是整数或者是另一个列表。
def depthSum(nestedList) -> int:
	queue_list = []
	sum_list = 0
	for nest in nestedList:
    	queue_list.append([nest, 1])
    while queue_list:
        curr = queue_list.pop(0)
        if curr[0].isInteger():
            sum_list += curr[0].getInteger() * curr[1]
        else:
            for c in curr[0].getList():
                queue_list.append([c, curr[1] + 1])
    return sum_list
depthSum([[1,1],2,[1,1]])1




# 11
# 给你一个整数 n，请你返回 任意 一个由 n 个 各不相同 的整数组成的数组，并且这 n 个数相加和为 0 。
def sumZero(n) -> List[int]:
	return range(-n + 1, n, 2)
sumZero(5)