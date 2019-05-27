class Goal:
    def __init__(self, posize):
        self._posize = posize

    # With this two functions below you can call the goals index from the class
    # Example goal_object[i] gives posize[i]

    def __getitem__(self, key):
        return self._posize[key]

    def __setitem__(self, key,key2):
        self._posize[key] = self._posize[key2]