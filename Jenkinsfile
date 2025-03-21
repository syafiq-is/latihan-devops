pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-app"
        IMAGE_VERSION = "latest"
        DOCKER_HUB_REPO = "suyafiku/latihan-devops"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Cloning Repository..."
                git branch: 'main', url: 'https://github.com/syafiq-is/latihan-devops.git' 
            }
        }
        
        stage('Install dependencies') {
            steps {
                echo "Installing Dependencies..."
                script {
                    sh 'python3 -m venv my-venv'
                    // change the Jenkins > Manage Jenkins > System > Shell, into /bin/bash
                    sh 'source my-venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        
        stage('Test') {
            steps {
                echo "Running Test..."
                sh 'source my-venv/bin/activate && pytest test_app.py'
            }
            post {
                success {
                    echo "All test passed"
                }
                failure {
                    echo "Test failed"
                }
            }
        }

        stage('Build') {
            steps {
                echo "Building App..."
                sh "docker build -t $IMAGE_NAME:$IMAGE_VERSION ."
            }
        }

        stage('Deploy to Docker Hub') {
            steps {
                echo "Deploying App to Docker Hub..."
                withCredentials([usernamePassword(credentialsId: 'DOCKER_HUB_CREDENTIALS', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "docker login -u $DOCKER_USER -p $DOCKER_PASS"
                    sh "docker tag $IMAGE_NAME:$IMAGE_VERSION $DOCKER_HUB_REPO:$IMAGE_VERSION"
                    sh "docker push $DOCKER_HUB_REPO:$IMAGE_VERSION"
                }
            }
        }
    }
}