
class CeasarSet(set):
  """A set object supporting a peek method for selecting an abritrary element."""

  def peek(self):
    """Select an arbritrary element from the set."""
    for x in self:
      return x
