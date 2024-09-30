def cast(ancestor : object, class_of_descendent : type) -> object:
    descendent = class_of_descendent()
    descendent.__dict__ = ancestor.__dict__
    return descendent