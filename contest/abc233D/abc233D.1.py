N, K = map(int, input().split())
A = list(map(int, input().split()))


def count_subarrays_with_sum(arr, K):
    count = 0
    prefix_sum = 0
    prefix_sums = {0: 1}  # 累積和の初期値は0で、一度登場した累積和の値を保存する辞書

    for num in arr:
        prefix_sum += num

        # Kよりも大きな累積和の場合、何回か前の累積和を引くことで和がKになる可能性がある
        if prefix_sum - K in prefix_sums:
            count += prefix_sums[prefix_sum - K]

        # 累積和を辞書に追加
        prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1

    return count

result = count_subarrays_with_sum(A, K)
print(result)