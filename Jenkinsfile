pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/syafiq-is/latihan-devops.git' 
            }
        }
        
        stage('Install dependencies') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    // Activate virtual env and install dependencies
                    sh 'bash -c "source venv/bin/activate && pip install -r requirements.txt"'
                }
            }
        }
        
        stage('Test') {
            steps {
                sh 'pytest test_app.py'
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
                echo "Building app..."
                sh "docker build -t flask-app-prod ."
            }
            post {
                success {
                    echo "App built successfully"
                }
                failure {
                    echo "Failed to build app"
                }
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying app..."
            }
            post {
                success {
                    echo "App deployed successfully"
                }
                failure {
                    echo "Failed to deploy app"
                }
            }
        }
    }
}
