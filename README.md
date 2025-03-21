## 🔍 Overview

This is a simple project to test CI/CD pipeline for a simple python flask project utilizing CI/CD tools Jenkins.

The project pipeline includes Cloning this Github Repository, Installing needed dependencies, Unit Testing, Building the image to Docker, and Deploying/Pushing the Image to Docker Hub.

## 📖 Instructions

1. Create a docker account and repository
2. Build/Run the docker-compose

```bash
docker-compose up -d
```

3. Go to http://localhost:8080 to access jenkins dashboard
4. Open the jenkins container logs to access the `initialAdminPassword` OR go to Jenkins container files, locate the `/var/jenkins_home/secrets/initialAdminPassword` for the password
5. Unlock Jenkins using the `initialAdminPassword`
6. Install `git` and `pipeline` plugins in Jenkins
7. Set the instance configuration into http://localhost:8080
8. Dashboard > Manage Jenkins > System > Shell, change it into `/bin/bash`
9. Dashboard > Manage Jenkins > Credential, click (global) and add your docker hub credentials, set the credential kind as Username with password, Scope: Global, ID: DOCKER_HUB_CREDENTIALS
10. Create a new pipeline, i used pipeline from SCM and add my Github Repository URL and set the Branch to Main,
11. [See my Jenkinsfile](https://github.com/syafiq-is/latihan-devops/blob/main/Jenkinsfile) (You could modify the environment variable such as DOCKER_HUB_REPO, IMAGE_NAME, and IMAGE_VERSION)
12. Create the pipeline
13. In the pipeline you just created run 'Build Now'
14. A new image will be created in your Docker and pushed to Docker Hub

## 💡 Final Thought

Jenkins is a interesting and fun way to automate Test, Build, and Deploy. Of course like every other thing it requires time and effort to learn a new thing especially applying them to a real world scenario which I exited to do if given the chance to do so.

I hope the thing i learn today will be used in the future.

Owner peace out ✌️
