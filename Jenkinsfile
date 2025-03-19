pipeline {
    agent any

    stages {
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
