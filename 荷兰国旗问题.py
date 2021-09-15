# 给定一个数组arr，和一个数num，请把小于num的数放在数组的左边，等于num的数放在数组的中间，大于num的数放在数组的右边
# 解题思路：（1）i < num时，i和小于区域的下一个数交换，小于区域往右扩1，i++
# （2）i=num时，i++
# （3）i > num时，i和大于区域的前一个数交换，大于区域往左扩1，i不变
# 当大于区域与i相遇，停止

def process(arr,num):
    xiao = -1
    da = len(arr)
    i = 0
    while i < da:
        if arr[i] < num:
            xiao +=1
            arr[i],arr[xiao]=arr[xiao],arr[i]
            i +=1
        elif arr[i] == num:
            i +=1
        else:
            da -= 1
            arr[i], arr[da] = arr[da], arr[i]
    return arr


print(process([3,5,6,3,4,5,2,4,6,7,3,6,8],5))