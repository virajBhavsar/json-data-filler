from jsonmerge import merge
import json

class Merger:
    def getFiles(self,schema,data):
        with open(schema) as f:
            base = json.loads(f.read())

        with open(data) as f:
            head = json.loads(f.read())

        return [base,head]

    def refine(self,schema,data):
        a = []
        try:
            if(type(schema) == type(a)):
                schema = schema[0]
            else:
                pass
            for d in data:
                result = merge(schema,d)
                
                for i in result:
                    if(type(result[i]) == type(a)):
                        result[i] = self.refine(schema[i][0],result[i])
                a.append(result)
        except:
            print("sorry, but schema and data is not in propper format")
        return a
    
