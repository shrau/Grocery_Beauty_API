class Calculator:
    
    def add(*args):
        for arg in args:
            return sum([*args])

        
    def subtract(*args):
        result=0
        for arg in args:
            result-=arg
        return result


