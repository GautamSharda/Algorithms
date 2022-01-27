#O(n) time, O(n) space
def flatten_dictionary(dictionary):
  
  flat_dict = {}
  
  def looping(curr_dict, curr_string=''):
    for key in curr_dict:
      value = curr_dict[key]
      if key != '':
        if curr_string == '':
          flat_key = curr_string+key
        else:
          flat_key = curr_string+'.'+key
      else:
        flat_key = curr_string
      if type(value) != dict:
        flat_dict[flat_key] = value
      else:
        looping(value, flat_key)
  
  looping(dictionary)
  
  return flat_dict