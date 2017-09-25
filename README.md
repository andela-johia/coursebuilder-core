# Academy.AFRICA Courses

URL: https://courses.academy.africa

Academy.AFRICA's courses built on Google's Course builder. Learn more at https://academy.codeforafrica.org.

## Installation and Deployment

 - Create a google [cloud project](https://edu.google.com/openonline/course-builder/docs/1.11/set-up-course-builder/create-a-cloud-project.html)
 - Download and install [google-cloud-sdk](https://cloud.google.com/sdk/downloads)
 - Initialize the gcloud environment: `gcloud init`
 - Clone this repository from the terminal and navigate to the *"coursebuilder"* folder
 - Deploy the app following the [documentation](https://edu.google.com/openonline/course-builder/docs/1.11/set-up-course-builder/deploy-your-app.html)
 - [Visit your site](https://edu.google.com/openonline/course-builder/docs/1.11/set-up-course-builder/visit-your-site.html)

## Development


See the [documentation on development](https://edu.google.com/openonline/course-builder/docs/1.11/for-course-builder-developers/for-course-builder-developers.html). It is recommended to run the application with the google-cloud-sdk if you wish persist data during development (ensure that you have gcloud installed and the repository cloned before proceeding):
- Install the python app-engine `gcloud components install app-engine-python`
- Navigate to the root directory of the cloned repository on the terminal
- Start the application: `dev_appserver.py coursebuilder`

## Tests

- Set the course-builder environmental variable: `export COURSEBUILDER_RESOURCES=path/to/coursebuilder`

- Instructions for running the tests can be found in the file: *coursebuilder/tests/suite.py*

- Add required PYTHONPATH paths e.g: `export PYTHONPATH=$PYTHONPATH:path/to/coursebuilder`

- Run the tests as instructed in the script: *coursebuilder/tests/suite.py*

---

## License

Apache 2.0
