def solution(diffs, times, limit):
    def get_total_time(level):
        time = 0
        for i in range(len(diffs)):
            if diffs[i] <= level:
                time += times[i]
            else:
                tmp = diffs[i] - level
                prev_time = times[i-1] if i > 0 else 0
                time += (times[i] + prev_time) * tmp + times[i]
        return time

    left,right = 1,max(diffs)
    answer = max(diffs)
    while left<=right:
        mid = (left+right)//2
        if get_total_time(mid)<=limit:
            answer = mid
            right = mid-1
        else:
            left = mid+1

    return answer
