import BBsort

def test_unsorted():
    # unsorted data with current data
	unsorted_list = [64,]
	assert BBsort.bubble_sort(unsorted_list) ==[]