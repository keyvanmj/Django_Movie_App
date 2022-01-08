from itertools import chain


def merging_model(qs_1,qs_2):
    merge_query = list(chain(qs_1,qs_2))
    return merge_query