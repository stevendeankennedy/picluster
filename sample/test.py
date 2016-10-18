from mpi4py import MPI
comm = MPI.COMM_WORLD
name=MPI.Get_processor_name()
print("Name:", name, "my rank:", comm.rank)
