"""My project"""

version = 'v1'  # production version

deps={'sum': '1.0',
      'product': '1.0'}


def task_sum():
    for i in [1, 2]:
        infile = 'rawdata{:d}.txt'.format(i)
        outfile = 'sum{:d}.txt'.format(i)
        yield {'action': 'sum {} {}'.format(infile, outfile),
               'deps': ['sum'],
               'inputs': [infile],
               'outputs': [outfile]}

        
def task_multiply():
    infiles = ['sum{:d}.txt' for i in [1, 2]]
    outfile = 'result.txt'
    return {'action': 'multiply {} {}'.format(' '.join(infiles), outfile),
            'deps': ['multiply'],
            'inputs': infiles,
            'outputs': [outfile]}
