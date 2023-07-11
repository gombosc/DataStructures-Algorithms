# Solution to Greedy Algorithm Problem: Merge Range
meetings = ( (0, 1), (10, 12), (9, 10), (4,8), (3, 5) )

def merge_ranges(meetings):
    # Sort by start time
    sorted_meetings = sorted(meetings)
    print(f'Sorted meetings: {sorted_meetings}')

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]
    print(f'Merged meetings at start: {merged_meetings}')

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        print(f'Current meeting start: {current_meeting_start}')
        print(f'Current meeting end: {current_meeting_end}')

        # Check if the current meeting overlaps with the last merged meeting
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]
        print(f'Last merged meeting start: {last_merged_meeting_start}')
        print(f'Last merged meeting end: {last_merged_meeting_end}')

        # If the current meeting overlaps with the last merged meeting, use the later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            print(f'Overlap detected')
            # Replace the last merged meeting with the updated one
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))
            print(f'Merged meetings: {merged_meetings}')

        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))
            print(f'Merged meetings: {merged_meetings}')
        return merged_meetings

merge_ranges(meetings)