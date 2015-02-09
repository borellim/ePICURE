import os, tempfile, subprocess

def pipe_test():
    """
    Simple function to test writing to named pipes from Python.
    """
    tmpdir = tempfile.mkdtemp(prefix='dakota_')
    #[inpipe_fd,inpipe_name] = tempfile.mkstemp(prefix='input_pipe', dir=tmpdir, text=True)
    filename = os.path.join(tmpdir, 'input_pipe')
    print "Trying to open FIFO: " + filename
    try:
        os.mkfifo(filename)
    except OSError, e:
        print "Failed to create FIFO: %s" % e
    else:
        fifo = open(filename, 'w') # ..buffering=0)
        # write stuff to fifo
        print >> fifo, "hello"
        trash = input() # wait
        fifo.close()
        os.remove(filename)
        os.rmdir(tmpdir)

def dakota_pipe_test():
    """
    Calls DAKOTA with a sample input file, passing it to DAKOTA
    via a named pipe. It makes a lot of assumptions, for example:
    - that 'rosen_multidir.in' is present in the current directory;
    - that the dakota binary is in the shell's $PATH;
    - that the MPI module can be loaded with 'module load mpi';
    and others.
    """
    input_filename = "rosen_multidim.in"
    output_filename = "rosen_multidim.out"

    input_file = open(input_filename,"r")
    input_text = input_file.read()
    input_file.close()

    tmpdir = tempfile.mkdtemp(prefix='dakota_')
    input_pipe = os.path.join(tmpdir, 'input_pipe')
    print "Trying to open FIFO: " + input_pipe
    try:
        os.mkfifo(input_pipe)
    except OSError, e:
        print "Failed to create FIFO: %s" % e
    else:
        dakota_process = subprocess.Popen('module load mpi; ' + \
                         ' dakota -i ' + input_pipe + ' -o ' + output_filename + ' -no_input_echo', shell=True)
        fifo = open(input_pipe, 'w', buffering=0)
        # write stuff to fifo
        print >> fifo, input_text
        fifo.close()
        print "Input file printed to Dakota. Waiting for completion..."
        dakota_process.wait()
        print "...Dakota completed. Deleting named pipe and temporary dir."
        os.remove(input_pipe)
        os.rmdir(tmpdir)

if __name__ == '__main__':
    dakota_pipe_test()
