# I had a similar problem in reading a graph from a file. The processing included the computation
# of a 200 000x200 000 float matrix (one line at a time) that did not fit into memory.
# Trying to free the memory between computations using gc.collect() fixed the memory-related aspect
# of the problem but it resulted in performance issues: I don't know why but even though the amount of used
# memory remained constant, each new call to gc.collect() took some more time than the previous one.
# So quite quickly the garbage collecting took most of the computation time.
#
# To fix both the memory and performance issues I switched to the use of a multithreading trick
# I read once somewhere (I'm sorry, I cannot find the related post anymore).
# Before I was reading each line of the file in a big for loop, processing it,
# and running gc.collect() every once and a while to free memory space.
# Now I call a function that reads and processes a chunk of the file in a new thread.
# Once the thread ends, the memory is automatically freed without the strange performance issue.
#
# Practically it works like this:

from dask import delayed  # this module wraps the multithreading
def f(storage, index, chunk_size):  # the processing function
    # read the chunk of size chunk_size starting at index in the file
    # process it using data in storage if needed
    # append data needed for further computations  to storage
    return storage

partial_result = delayed([])  # put into the delayed() the constructor for your data structure
# I personally use "delayed(nx.Graph())" since I am creating a networkx Graph
chunk_size = 100  # ideally you want this as big as possible while still enabling the computations to fit in memory
for index in range(0, len(file), chunk_size):
    # we indicates to dask that we will want to apply f to the parameters partial_result, index, chunk_size
    partial_result = delayed(f)(partial_result, index, chunk_size)

    # no computations are done yet !
    # dask will spawn a thread to run f(partial_result, index, chunk_size) once we call partial_result.compute()
    # passing the previous "partial_result" variable in the parameters assures a chunk will only be processed after the previous one is done
    # it also allows you to use the results of the processing of the previous chunks in the file if needed

# this launches all the computations
result = partial_result.compute()

# one thread is spawned for each "delayed" one at a time to compute its result
# dask then closes the tread, which solves the memory freeing issue
# the strange performance issue with gc.collect() is also avoided