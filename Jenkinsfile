pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building...'
        checkout(scm: scm, changelog: true, poll: true)
        bat(script: 'pip3 install jenkins_proj/src/', returnStdout: true, returnStatus: true)
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