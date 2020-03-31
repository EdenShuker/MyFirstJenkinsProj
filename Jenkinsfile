pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        deleteDir()
        echo 'Building...'
        checkout(scm: scm, changelog: true, poll: true)
        bat 'python -m pip install virtualenv'
        bat(script: 'virtualenv env ', returnStatus: true, returnStdout: true)
        bat(script: 'call env/Scripts/activate.bat', returnStdout: true, returnStatus: true)
        bat 'pip install src/'
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