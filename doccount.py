import os
from dumbo import main, opt

@opt( "addpath", "yes" )
def mapper0( key, value ):
    yield "N", key[0]

def reducer0( key, values ):
    yield len(set( values )), ""

def runner( job ):
    job.additer( mapper0, reducer0 )

def starter( prog ):
    return

if __name__ == "__main__":
    main( runner, starter )
