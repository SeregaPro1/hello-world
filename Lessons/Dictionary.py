# dicitonary = A changeable, inordered collentinon of unique key: value pairs
#                Fast because they use hashing, allow us to access a value quikly

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}

capitals.update({'Germany':'Berlin'}) # add need key and value
capitals.update({'USA':'Las Vegas'}) # update need key
capitals.pop('China') # delete neew items
# capitals.clear() # delete all key


# print(capitals['Germany'])# show need item in key
# print(capitals.get('Germany')) # show need item in key
# print(capitals.keys()) # show keys
# print(capitals.values()) # show values
# print(capitals.items()) # show items

for key,value in capitals.items():
    print(key, value)
