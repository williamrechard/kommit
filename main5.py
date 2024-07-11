import random
import time
import git

file_name = "random_key_v3.r"
batch_size = 100  # Number of changes per commit

def create_and_commit_random_code(batch_code, batch_number, total_batches):
    with open(file_name, "a") as file:
        file.writelines(batch_code)
    
    repo = git.Repo(search_parent_directories=True)
    repo.index.add([file_name])
    repo.index.commit(f"Batch {batch_number}/{total_batches} commit")

    percentage = (batch_number / total_batches) * 100
    print(f"Progress: {percentage:.2f}% complete", end='\r')

num_commits = 500
start_time = time.time()

total_batches = num_commits // batch_size + (1 if num_commits % batch_size != 0 else 0)

for batch_number in range(total_batches):
    batch_code = [f"Random Code: {''.join(random.choice('0123456789ABCDEF') for _ in range(8))}\n" for _ in range(batch_size)]
    create_and_commit_random_code(batch_code, batch_number + 1, total_batches)

end_time = time.time()

print("Progress: 100.00% complete")
print(f"Total time taken for {num_commits} commits: {end_time - start_time} seconds")