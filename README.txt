python filecreate.py <no_of_files> <no_of_max_nodes_in_file>
e.g. filecreate.py 50 100
above command will create 50 files with maximum 100 nodes/vertices/links in the file

Use ir.sh to execute on Single Node Machine
Use ir-server.sh to execute on Cluster. First argument is input directory and second is the output directory.

output.txt has the output in format:
key[0]-source node
key[1]-target node
value[1]-source node
value[2]-target node
value[3]-distance between source and target
value[4]-hops between source and target
