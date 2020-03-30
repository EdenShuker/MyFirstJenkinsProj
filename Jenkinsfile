pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                checkout csm
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