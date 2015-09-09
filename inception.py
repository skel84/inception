from gomatic import GoCdConfigurator, HostRestClient, ExecTask
from github import Github, GithubException

github = Github()
user_whose_repos_are_scanned = github.get_user("teamoptimization")
for repo in user_whose_repos_are_scanned.get_repos():
    try:
        print "configuring", repo.name
        configurator = GoCdConfigurator(HostRestClient("go-server:8153"))

        pipeline = configurator\
            .ensure_pipeline_group("auto-created")\
            .ensure_pipeline(repo.name)\
            .set_git_url(repo.clone_url)
        job = pipeline\
            .ensure_initial_stage("bootstrap")\
            .ensure_job("configure-pipeline")
        bootstrap_file_url = "https://raw.githubusercontent.com/ivanmoore/inception/master/bootstrap.py"
        job.ensure_task(ExecTask(["bash", "-c", "curl -fSs " + bootstrap_file_url + " | python - " + repo.name]))

        configurator.save_updated_config()
    except GithubException:
        print 'ignoring', repo.name
