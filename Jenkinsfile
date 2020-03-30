pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building...'
        sh 'll'
        checkout(scm: scm, changelog: true, poll: true)
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