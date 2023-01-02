from git import Repo
import time

PATH_OF_GIT_REPO = r'C:\schoolwerk\ehtroj'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def run(**args):
    def git_push():
        try:
            repo = Repo(PATH_OF_GIT_REPO)
            repo.git.add(update=True)
            repo.index.commit(COMMIT_MESSAGE)
            origin = repo.remote(name='origin')
            origin.push(force=True)
            print("pushed")
        except:
            print('Some error occured while pushing the code')    
    while True:
        time.sleep(90)
        git_push()