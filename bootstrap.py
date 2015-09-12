import sys
from gomatic import GoCdConfigurator, HostRestClient, ExecTask

configurator = GoCdConfigurator(HostRestClient('go-server:8153'))

pipeline_name = sys.argv[1]

pipeline = configurator\
    .ensure_pipeline_group('auto-created')\
    .find_pipeline(pipeline_name)

for stage in pipeline.stages()[1:]:
    pipeline.ensure_removal_of_stage(stage.name())

pipeline.ensure_stage('build').ensure_job('build')\
    .ensure_task(ExecTask('echo build'))

environments = open('environments.txt').readlines()
for environment in environments:
    if environment:
        pipeline\
            .ensure_stage('deploy-to-' + environment)\
            .ensure_job('deploy')\
            .ensure_task(ExecTask('echo deploy to ' + environment))

configurator.save_updated_config()
