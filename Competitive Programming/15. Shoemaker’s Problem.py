import functools

def job_cmp(a, b):
    # Custom comparison function for sorting jobs
    if a[0] * b[1] > b[0] * a[1]:
        return 1
    elif a[0] * b[1] == b[0] * a[1]:
        return 0
    else:
        return -1

num_tests = int(input("Enter the number of tests: "))  # Prompt for the number of tests

for i in range(num_tests):
    input()  # Ignore blank line
    num_jobs = int(input("Enter the number of jobs: "))  # Prompt for the number of jobs

    jobs = []
    for j in range(num_jobs):
        # Prompt for job characteristics
        T, S = [int(x) for x in input().split()]
        jobs.append((T, S, j + 1))

    jobs = sorted(jobs, key=functools.cmp_to_key(job_cmp), reverse=False)
    if i > 0:
        print()

    # Print the sorted job identifiers
    print(" ".join([str(j[2]) for j in jobs]))