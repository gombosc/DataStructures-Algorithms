def binary_search(target, nums):
    """See if target appears in nums"""
    # We think of floor_index and ceiling_index as "walls" around
    # the possible positions of our target so by -1 below we mean
    # to start our wall "to the left" of the 0th index
    # (we *don't* mean "the last index")
    floor_index = -1
    ceiling_index = len(nums)

    # If there isn't at least 1 index between floor and ceiling,
    # we've run out of guesses and the number must not be present
    while floor_index + 1 < ceiling_index:
        # Find the index ~halfway between the floor and ceiling
        # We use integer division, so we'll never get a "half index"
        distance = ceiling_index - floor_index
        half_distance = distance // 2
        guess_index = floor_index + half_distance

        guess_value = nums[guess_index]
        if guess_value == target:
            print("Guess value is equal to: " + str(target))
            return True

        if guess_value > target:
            # Target is to the left, so move ceiling to the left
            ceiling_index = guess_index
            print("Guess value is bigger than: " + str(target) + " so we move ceiling to the left")
        else:
            # Target is to the right, so move floor to the right
            floor_index = guess_index
            print("Guess value is smaller than: " + str(target) + " so we move floor to the right")

    return False

    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, ];
    target = 11;
    print(target)
    binary_search(target, nums)
    # Start with the middle number: is it bigger or smaller than our target number? Since the list is sorted, this tells us if the target would be in the left half or the right half of our list.
    # We've effectively divided the problem in half. We can "rule out" the whole half of the list that we know doesn't contain the target number.
    # Repeat the same approach (of starting in the middle) on the new half-size problem. Then do it again and again, until we either find the number or "rule out" the whole set.
