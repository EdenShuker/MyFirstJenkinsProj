pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    pip install -e src/
                    pip install -e test/
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}