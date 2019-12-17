def binarySearch(arr, item, low, high):
	if low > high:
		return -1
	mid = round((high+low)/2)
	print('(',high,'-',low,')/2=',mid)

	if arr[mid] == item:
		return mid
	elif arr[mid] < item:
		return binarySearch(arr, item, mid+1, high)
	else:
		return binarySearch(arr, item, low, mid-1)


input_list = [1,3,5,6,10,14,25,37,59]
# input_list.sort()
result = binarySearch(input_list, 25, 0, len(input_list)-1) # 3
if result < 0:
	print('Item is not in the list')
else:
	print('Your item is in index ',result)
