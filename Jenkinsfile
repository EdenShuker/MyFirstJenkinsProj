pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building...'
        checkout(scm: scm, changelog: true, poll: true)
        bat(script: 'python -m pip install src/', returnStdout: true, returnStatus: true)
        bat(script: 'python -m pip install test/', returnStatus: true, returnStdout: true)
      }
    }

    stage('Test') {
      steps {
        echo 'Testing...'
        bat 'py.test test/jenkins_proj_test/ --junit-xml=test_results.xml'
        junit 'test_results.xml'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying...'
      }
    }

  }
}