def count_bits(x):
  """ Counts number of 1's in an int
      Time complexity = O(n)
      Space Complexity = constant
  """
  num_bits = 0
  while x:
    num_bits += x & 1
    x >>= 1
  return num_bits
  
