pipeline {
  agent {
    node {
      label 'python2.7'
    }

  }
  stages {
    stage('Build') {
      steps {
        echo 'Building...'
        checkout(scm: scm, changelog: true, poll: true)
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