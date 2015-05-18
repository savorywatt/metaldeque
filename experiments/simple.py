import marshal

class Task(object):

    def __init__(self.function, args, kwargs, tag, task_name):

        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.tag = tag
        self.task_name = task_name
        self.complete = False

    @property
    def bytes(self):
        """Marshal Self"""

        return marshal.dumps(self)

    @classmethod
    def from_bytes(cls, data)
        """Build a Task from the bytes retrieved from disk"""

        return marshal.loads(data)


class Node(object):

    def __init__(self):
        self.prev = None
        self.next = None

class MetalDeque(object):


    def __init__(self, byte_capacity, max_task_size):

        self.byte_capacity = byte_capacity
        self.max_task_size = max_task_size
        self.item_capacity = item_capacity


    def put(self, task):
        """Puts a task into the queue by appending to the end"""
        pass

    def take(self, amount):
        """Will pull out the right amount of tasks"""
        pass
