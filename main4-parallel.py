import time
import git

def create_empty_commit(commit_number, total_commits):
    repo = git.Repo(search_parent_directories=True)
    repo.git.commit(allow_empty=True, message=f"Empty commit {commit_number}")

    percentage = (commit_number / total_commits) * 100
    print(f"Progress: {percentage:.2f}% complete", end='\r')

num_commits = 10000
start_time = time.time()

for i in range(num_commits):
    create_empty_commit(i + 1, num_commits)
    time.sleep(0.1)  # Small delay to ensure the repository state is correctly updated

end_time = time.time()

print("Progress: 100.00% complete")
print(f"Total time taken for {num_commits} commits: {end_time - start_time} seconds")
