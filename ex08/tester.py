from ft_filter import ft_filter


def maior(num) -> bool:
    if num > 10:
        return True
    return False


nums = [20, 9, 8, 10, 12, 7, 6, 30]

maiores = ft_filter(maior, nums)
print(list(maiores))
print("\n")
print(ft_filter.__doc__)
print(filter.__doc__)
print("\n")
print(filter.__doc__ == ft_filter.__doc__)
