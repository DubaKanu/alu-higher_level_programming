#!/usr/bin/python3
def search_replace(my_list, search, replace):
  """
  Replaces all occurrences of 'search' element with 'replace' element in a new list.

  Args:
      my_list: The initial list.
      search: The element to replace.
      replace: The new element.

  Returns:
      A new list with all occurrences of 'search' replaced by 'replace'.
  """

  new_list = []
  for item in my_list:
    if item == search:
      new_list.append(replace)
    else:
      new_list.append(item)
  return new_list
