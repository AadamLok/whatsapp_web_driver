class presence_of_any_one_element_located(object):
  """
  An expectation for checking that an element from the 2 element passed in has present
  """
  def __init__(self, locator1, locator2):
    self.locator1 = locator1
    self.locator2 = locator2

  def __call__(self, driver):
    found_elem_1 = True
    found_elem_2 = True

    try:
        driver.find_element(*self.locator1)
    except:
        found_elem_1 = False
    
    try:
        driver.find_element(*self.locator2)
    except:
        found_elem_2 = False

    return found_elem_1 or found_elem_2

class element_has_some_text(object):
  """
  An expectation for checking that an element has some text loaded inside it
  """
  def __init__(self, locator):
    self.locator = locator

  def __call__(self, driver):
    element = driver.find_element(*self.locator)
    if element.text != "":
        return element
    else:
        return False