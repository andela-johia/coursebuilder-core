# CFA MOOC Project On-Boarding


## Intro
Welcome, the course-builder application's core was built by google and the documentation can be found here: https://edu.google.com/openonline/course-builder/docs/1.11/index.html

For installation, deployment and testing, refer the the README file at the root directory. Read the following sections as they will aid you during development:
- Meet Course Builder
- Set Up Course Builder
- Administer Site
- For Course Builder Developers

After installing the application locally, you may want to create some simple courses to test out the features you are working on. You also need the enable the 'explorer' feature to view the homepage on your local machine:
- Start the app and visit localhost:8080/ on your machine
- Go the dashboard, create a sample course and click the course
- go to: Settings -> Advanced site settings -> Course explorer (click edit) -> check 'value' box and save
- Visit localhost:8080/ again to view the homepage

---
### Folders
From the root directory, you will notice two folders: *coursebuilder/* and *frontend/*

#### coursebuilder/
The *coursebuilder/* folder contains the application itself, it's where you will be making most of your changes.

#### frontend/
The *frontend/* folder was setup during the initial stages of building the app's frontend and it contains a simple frontend development workflow. It was created because building the frontend directly on the app while the server is running is slow and inefficient. SASS is used to write the styles while gulp is used to convert the sass files to css, auto-prefix the css and direct the output to appropriate folders. The *scss/* folder contains styles for each page of the application written in SASS.

To use this workflow for a front-end task(ensure that you have NodeJs installed);
- Navigate to the *frontend/* folder in a terminal and run `npm install`
- Install gulp task runner if you don't have it already: `npm install -g gulp`
- Start the gulp task runner: `gulp`
- Now you can write your styles in SCSS format and it will be automatically converted to css

## Pages

The homepage and other pages like the tools page can be found in the directory: *coursebuilder/modules/explorer/_static/components/pages*

[PolymerJs](https://www.polymer-project.org/1.0/start/) version 1.2 was used in building these pages.

[Jinja2](http://jinja.pocoo.org/docs/2.9/) is the default templating langauge for the application and the folder *coursebuilder-core/coursebuilder/views/* contains templates for the course pages.

Most back-end functions of the applications are handled by well organized modules (e.g courses, explorer, oeditor e.t.c) found in the modules folder: *coursebuilder-core/coursebuilder/modules/*

Open the the *frontend/course-varaibles.txt* to view some variables available for the course templates, they might prove useful while working on the course page. These were generated in the courses.py file of the courses module: *coursebuilder-core/coursebuilder/modules/courses/courses.py*

## API

The application contains a GraphQL api which can be consumed from any page. For e.g the query:
` {
    allCourses {
      edges {
        node {id title}
      }
    }
  }` returns all courses available on the site with id and title. Learn more about graphQl here: http://graphql.org/

  The schema is documented in the file: `coursebuilder-core/coursebuilder/modules/gql/gql.py`

---

Hope you found this helpful. As you work on the project, feel free to document any information others might find helpful here, thanks.
