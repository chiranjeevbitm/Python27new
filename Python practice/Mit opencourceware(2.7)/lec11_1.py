class intSet(object):
    
    
    #An intSet is a set of integers
    def __init__(self):
        
        """Create an empty set of integers"""

        self.numBuckets = 47
        self.vals = []
        for i in range(self.numBuckets):
             self.vals.append([])
    def hashE(self, e):
       #Private function, should not be used outside of class
       return abs(e)%len(self.vals)
    def insert(self, e):
        
        """Assumes e is an integer and inserts e into self"""
        
        for i in self.vals[self.hashE(e)]:
            
            
            if i == e: return
        
            
         self.vals[self.hashE(e)].append(e)
    
         
    def member(self, e):
           """Assumes e is an integer
              Returns True if e is in self, and False otherwise"""
         return e in self.vals[self.hashE(e)]
    def __str__(self):
       """Returns a string representation of self"""
         elems = []
         for bucket in self.vals:
              for e in bucket: elems.append(e)
         elems.sort()
         result = ''
         for e in elems: result = result + str(e) + ','
         return '{' + result[:-1] + '}'

