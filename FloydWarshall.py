#FloydWarshall.py

import re, os, sys
from dumbo import main, opt
from math import log

##############HACK###############
#I could not find a way to pass params to runner
#I used -param option to pass nodecount
#It is always the first option
#nodecount is the number of nodes 

nodecount = int(sys.argv[2])
#################################

@opt( "addpath", "yes" )
def mapper1( key, value ):
    source = os.path.basename( key[0] ) 
    for target in value.split(' '):
        if target.endswith('.txt'):
             yield (source, target), (source, target, 1.0, '')

def reducer1( key, values ):
    yield key, list(values)[0]

def mapper2( key, value ):
    yield key[0], (value, 's')
    yield key[1], (value, 't')

def reducer2( key, values ):
    values = list( values )
    for sv in values:
        if sv[1]=='t':
            yield (sv[0][0], sv[0][1]), sv[0]
            for tv in values:
                if tv[1]=='s':
                    if sv[0][1]==tv[0][0] and sv[0][0]!=tv[0][1]:
                        yield (sv[0][0], tv[0][1]), (sv[0][0], tv[0][1], sv[0][2]+tv[0][2], sv[0][3]+key+'-'+tv[0][3])

def mapper3( key, value ):
    yield key, value

def reducer3( key, values ):
    values = list( values )
    minlen = float('inf')
    for value in values:
        if (minlen>value[2]):
            minlen = value[2]
            minvalue = value
    yield key, minvalue 

def runner( job ):
    job.additer( mapper1, reducer1 )
    for i in range(1, nodecount+1):
        job.additer( mapper2, reducer2 )
        job.additer( mapper3, reducer3 )

def starter( prog ):
    return

if __name__ == "__main__":
    main( runner, starter )
