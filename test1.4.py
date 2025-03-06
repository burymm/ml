instructions = int(input())
# instructionsList = [
#     'add global a', 
#     'create foo global', 
#     'add foo b', 
#     'get foo a', 
#     'get foo c',
#     'create bar foo',
#     'add bar a',
#     'get bar a',
#     'get bar b'
#     ]

# instructionsList = [
#     'create first global',
# 'create second first',
# 'create third second',
# 'add first my_var',
# 'get third my_var'
#     ]


# instructionsList = [
# 'add global a',
# 'create foo1 global',
# 'create foo2 global',
# 'create bar1 foo1',
# 'create bar2 foo2',
# 'create new1 bar1',
# 'create new2 bar2',
# 'add global b',
# 'add foo1 a',
# 'add foo2 b',
# 'add bar1 a',
# 'add bar2 b',
# 'add new1 a',
# 'add new2 b',
# 'get new1 b'
#     ]

# instructionsList = [
# 'create foo global',
# 'create bar foo',
# 'add global a',
# 'add foo a',
# 'add bar c',
# 'get global c'
#     ]

# instructionsList = [
# 'create foo global',
# 'create bar foo',
# 'create barz bar',
# 'create bary barz',
# 'add bar b',
# 'create zoo bar',
# 'create zoo2 zoo',
# 'create zoo3 zoo2',
# 'add bary b',
# 'create doo zoo',
# 'get zoo b'
#     ]

obj = {
	'global': {
		'variables': [],
        'parent': 'None',
        'name': 'global'
	}
}

def findInScope(currObj, variable):
    if variable in currObj['variables']:
        return currObj['name']
    elif currObj['parent'] != 'None':
        return findInScope(getNamespaceData(currObj['parent']), variable)
    else:
        return 'None'

def getNamespaceData(namespace, currObj = obj):
    if namespace in currObj:
        return currObj[namespace]
    else:
        keys = list(currObj.keys())
        if keys:
            for key in keys:
                if key != 'variables' and key != 'parent' and key != 'name':
                    return getNamespaceData(namespace, currObj[key])
        else: 
            return None;
                

def add(currObj, namespace, variable):
    if namespace in currObj and type(currObj[namespace]['variables']) is list:
        currObj[namespace]['variables'].append(variable)
    else:
        keys = list(currObj.keys())
        for key in keys:
            if key != 'variables' and key != 'parent' and key != 'name':
                add(currObj[key], namespace, variable)
                #print(obj)
                return True
            
def get(currObj, namespace, variable):
    #print(getNamespaceData(namespace))
    if namespace in currObj and variable in currObj[namespace]['variables']:
        #print(namespace)
        return True
    else:
        keys = list(currObj.keys())
        for key in keys:
            if key != 'variables' and key != 'parent':
                if get(currObj[key], namespace, variable):
                    return True
    return False                
        
    

for i in range(instructions):
# for instuction in instructionsList:   
    command, namespace, variable = input().split()
    #print('autoinput', instuction)
    # command, namespace, variable = instuction.split()
    if command == 'add':
        add(obj, namespace, variable)
    if command == 'create':
        scopeData = getNamespaceData(variable)
        if scopeData:
            scopeData[namespace] = {'variables': [], 'parent': variable, 'name': namespace}
        #print(obj)
    if command == 'get':
        scopeData = getNamespaceData(namespace)
        if scopeData:
            print(findInScope(scopeData, variable))
        else:
            print('None')
    

