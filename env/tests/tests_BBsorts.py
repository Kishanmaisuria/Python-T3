import BBRead

def test_unsorted():
    # unsorted data with current data
	unsorted_list = [64,]
	assert BBRead.BBsort(unsorted_list) ==[]