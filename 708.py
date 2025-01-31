
def remove(self, current=''):
  if current == '':
    current = self.tail
  if current.next:
    if current.next.next:
      current = current.next
      return self.remove(current)
    else:
      n = current.next.value
      current.next = None
      self.size -= 1
      return n
  elif current == self.tail:

    if current.value:
      n = current.value
      self.tail = None
      self.size -= 1
      return n
    else:
      return "Queue is already empty."
  else:
    raise ValueError("mind boggling coding error...")





























































