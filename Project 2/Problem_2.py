import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    found_paths = []
    allpaths = os.listdir(path)
    for p in allpaths:
        if os.path.isdir(os.path.join(path, p)):
            found_paths += find_files(suffix, (path + "/" + p))
        if p.endswith(suffix):
            found_paths += [ (path + "/" + p) ]
    return found_paths

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print(find_files(".c", "./testdir")) # ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']
print(len(find_files(".c", "./testdir"))) # 4

# Test Case 2
print(find_files(".h", "./testdir")) # ['./testdir/subdir1/a.h', './testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h']
print(len(find_files(".h", "./testdir"))) # 4

# Test Case 3
print(find_files(".py", "./testdir")) # []
print(len(find_files(".py", "./testdir"))) # 0

# Test Case 4
# This returns the path for every file and directory in the given path
print(find_files("", "./testdir")) # ['./testdir/subdir1/a.c', './testdir/subdir1/a.h', './testdir/subdir1', './testdir/subdir2/.gitkeep', './testdir/subdir2', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir3/subsubdir1/b.h', './testdir/subdir3/subsubdir1', './testdir/subdir3', './testdir/subdir4/.gitkeep', './testdir/subdir4', './testdir/subdir5/a.c', './testdir/subdir5/a.h', './testdir/subdir5', './testdir/t1.c', './testdir/t1.h']
print(len(find_files("", "./testdir"))) # 16

#There should be four files that end in .c