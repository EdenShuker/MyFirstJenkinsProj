pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building...'
        checkout(scm: scm, changelog: true, poll: true)
        bat 'python -c "print(\'hello\')"'
        bat(script: 'python --version', returnStdout: true)
        bat(script: 'pip --version', returnStdout: true, returnStatus: true)
        bat(script: 'dir', returnStatus: true, returnStdout: true)
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