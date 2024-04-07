#!/usr/bin/python

def search_replace(my_list, search, replace):
    def search_n_replace(i):
        return (i if i != search else replace)
    return list(map(search_n_replace, my_list))
