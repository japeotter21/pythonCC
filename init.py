import cloudconvert

cloudconvert.default()

def createJob(): 
    cloudconvert.Job.create(payload={
    "tasks": {
        'import-my-file': {
            'operation': 'import/url',
            'url': 'https://my-url'
        },
        'convert-my-file': {
            'operation': 'convert',
            'input': 'import-my-file',
            'output_format': 'pdf',
            'some_other_option': 'value'
        },
        'export-my-file': {
            'operation': 'export/url',
            'input': 'convert-my-file'
        }
    }
})
    
def downloadFile():
    exported_url_task_id = "84e872fc-d823-4363-baab-eade2e05ee54"
    res = cloudconvert.Task.wait(id=exported_url_task_id)  # Wait for job completion
    file = res.get("result").get("files")[0]
    res = cloudconvert.download(filename=file['filename'], url=file['url'])
    print(res)

def uploadFile():
    job = cloudconvert.Job.create(payload={
        'tasks': {
            'upload-my-file': {
                'operation': 'import/upload'
            }
        }
    })

    upload_task_id = job['tasks'][0]['id']

    upload_task = cloudconvert.Task.find(id=upload_task_id)
    res = cloudconvert.Task.upload(file_name='path/to/sample.pdf', task=upload_task)

    res = cloudconvert.Task.find(id=upload_task_id)


# GET https://sync.api.cloudconvert.com/v2/jobs/{ID}
# job = cloudconvert.Job.wait(id=job['id'])