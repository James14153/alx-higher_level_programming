#!/usr/bin/python3

def find_peak(list_of_integers):
    """ Finds a peak in a list of integers """
    if not list_of_integers:
        return None

    def find_peak_util(arr, low, high):
        mid = low + (high - low) // 2
        if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
                (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid])):
            return arr[mid]
        if mid > 0 and arr[mid - 1] > arr[mid]:
            return find_peak_util(arr, low, mid - 1)
        return find_peak_util(arr, mid + 1, high)
    return find_peak_util(list_of_integers, 0, len(list_of_integers) - 1)
