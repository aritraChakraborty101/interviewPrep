#a tandem byciycle is a bicycle that has two sets of pedals and two sets of handlebars
#so that two riders can ride it at the same time
#you can also remove the second set of pedals and handlebars to ride it alone
#given the number of riders of the tandem bicycle and the speed of riders
#return the fastest speed that the tandem bicycle can travel
#the tandem bicycle is fastest when the fastest rider is pedaling
#and the slowest rider is not pedaling
#speed is represented as a positive integer
#you're given two arrays of positive integers
#one array is speeds of riders pedaling
#other array is speeds of riders not pedaling
#both arrays have same length
#and each index represents a rider
#write a function that returns the max possible speed of the tandem bicycle
#given the two arrays
#the number of riders is even
#and at least two riders
#and all riders have to be pedaling or none of them
#can be pedaling
#example:
#pedaling = [5, 5, 3, 9, 2]
#notPedaling = [3, 6, 7, 2, 1]
#output = 32



def forFast(redShirtSpeeds, blueShirtSpeeds):
    result = 0
    blueShirtSpeeds.sort()
    redShirtSpeeds.sort(reverse = True)
    for i in range(len(redShirtSpeeds)):
        result += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return result
    
def forSlow(redShirtSpeeds, blueShirtSpeeds):
    result = 0
    blueShirtSpeeds.sort()
    redShirtSpeeds.sort()
    for i in range(len(redShirtSpeeds)):
        result += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return result

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    if fastest:
        return forFast(redShirtSpeeds, blueShirtSpeeds)
    else:
        return forSlow(redShirtSpeeds, blueShirtSpeeds)
