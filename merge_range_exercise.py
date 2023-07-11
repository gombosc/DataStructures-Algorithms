meetings = ( (5,8), (2,3) )
sorted_meetings = ()

# Understanding the logic of the problem, we need to sort the meetings by start time, then merge the meetings that overlap.
def merge_ranges(meetings):
    if(meetings[0][1] >= meetings[1][i] and meetings[i][1] <= meetings[1][1]):
            sorted_meetings = (meetings[i][i], meetings[1][1])

    elif meetings[0][1] > meetings[1][1]:
            if(meetings[0][0] > meetings[1][0]):
                sorted_meetings = (meetings[1][0], meetings[0][1])
            else:
                sorted_meetings = (meetings[0])
    else: 
        return meetings
    return sorted_meetings

print(merge_ranges(meetings))


