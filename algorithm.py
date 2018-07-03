#二分查找
def binary_sort(alist,item):
    low = 0
    high = len(alist) - 1

    while low < high:
        mid = int((low + high)/2)
        guess = alist[mid]
        if guess == item:
            return mid
        elif guess < item:
            low += 1
        elif guess > item:
            high -= 1
        else:
            return None

#归并排序
def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        # 这个地方一定要有返回值，因为alist是被分解成的单一的元素
        return alist
    mid = n // 2

    # left 采用递归排序后形成的新序列
    left_li = merge_sort(alist[:mid])

    # right 采用递归排序后形成的新序列
    right_li = merge_sort(alist[mid:])

    # print(left_li,right_li)

    # 将两个子序列合并成一个序列
    # 左右指针
    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    # 此时还有最后一个元素没有加入到列表中，切片是没有越界的，它返回一个空列表
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result

#选择排序
def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def select_sort(arr):
    new_array = []
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        new_array.append(arr.pop(smallest))
    return new_array

#递归求和
def recursion_sum(arr):
    if arr == []:
        return 0
    return arr[0] + recursion_sum(arr[1:])

#递归求数组元素数
def recursion_count(arr):
    if arr == []:
        return 0
    return 1 + recursion_count(arr[1:])

#递归查找最大值
def find_max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    item = find_max(arr[1:])
    return arr[0] if arr[0] > item else item

#快速排序
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    st_num = arr[0]
    low = []
    high = []
    for i in arr[1:]:
        if i < st_num:
            low.append(i)
        else:
            high.append(i)
    return quick_sort(low) + [st_num] +quick_sort(high)

#迪克斯特拉算法
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] =None

processed = []

def update_parents():
    node = select_lowest_costs_node(costs)
    while node != None:
        neibor = graph[node]
        for i in neibor.keys():
            new_cost = costs[node]+graph[node][i]
            if costs[i] > new_cost:
                costs[i] = new_cost
                parents[i] = node
        processed.append(node)
        node = select_lowest_costs_node(costs)
    print(parents)

def select_lowest_costs_node(costs):
    num = infinity
    str1 = None
    for i in costs.keys():
        if costs[i] < num and i not in processed:
            num = costs[i]
            str1 = i
    return str1

#贪婪算法
def np_c():
    states_needed = set(["mt","wa","or","id","nv","ut","ca","az"])
    stations = {}
    stations["kone"] = set(["id","nv","ut"])
    stations["ktwo"] = set(["wa","id","mt"])
    stations["kthree"] = set(["or","nv","ca"])
    stations["kfour"] = set(["nv","ut"])
    stations["kfive"] = set(["ca","az"])
    final_stations = set()
    while states_needed:
        covered_states = set()
        for i,j in stations.items():
            print(i,j)
            cover = states_needed & j
            if len(cover) > len(covered_states):
                covered_states = cover
                final_stations.add(i)
                states_needed -= j
    print(final_stations)



if __name__ == '__main__':
    # li = [44,54,55,77,93,17,20,26,31]
    # sort_li = quick_sort(li)
    # print(sort_li)
    np_c()